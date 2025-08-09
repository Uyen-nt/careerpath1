from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PremiumSubscription, Transaction
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()

def send_payment_confirmation_email(user, months, amount):
    subject = 'Xác Nhận Thanh Toán Premium - CareerPath'
    context = {
        'user': user,
        'months': months,
        'amount': amount,
        'end_date': timezone.now() + timezone.timedelta(days=30 * months),
    }
    message = render_to_string('email_payment_confirmation.html', context)
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=message,
    )

@login_required
def premium_home(request):
    user = request.user
    subscription, _ = PremiumSubscription.objects.get_or_create(user=user)
    subscription.check_status()

    now = timezone.now()
    trial_expired = False
    trial_active = False
    subscription_active = False
    days_left = 0

    if subscription.trial_start:
        if subscription.trial_end > now and not subscription.subscription_start:
            trial_active = True
            days_left = (subscription.trial_end - now).days
        elif subscription.trial_end <= now and not subscription.subscription_start:
            trial_expired = True

    if subscription.subscription_start and subscription.subscription_end > now:
        subscription_active = True
        days_left = (subscription.subscription_end - now).days

    context = {
        "subscription": subscription,
        "trial_active": trial_active,
        "trial_expired": trial_expired,
        "subscription_active": subscription_active,
        "days_left": days_left,
        "has_used_trial": subscription.has_used_trial,
    }
    return render(request, 'premium.html', context)

@login_required
def start_trial(request):
    user = request.user
    subscription, _ = PremiumSubscription.objects.get_or_create(user=user)
    if subscription.has_used_trial:
        return redirect('premium:renew_premium')
    if not subscription.is_active:
        subscription.start_trial()
    return render(request, 'trial_success.html')

@login_required
def renew_premium(request):
    user = request.user
    subscription, _ = PremiumSubscription.objects.get_or_create(user=user)
    subscription.check_status()

    if request.method == "POST":
        months = int(request.POST.get('months', 1))
        amount = {1: 49000, 3: 139000, 6: 219000}.get(months, 49000)
        order_id = f"{user.id}-{timezone.now().strftime('%Y%m%d%H%M%S')}"

        context = {
            'amount': amount,
            'months': months,
            'user': user,
            'order_id': order_id,
        }
        return render(request, 'premium_payment_qr.html', context)

    return render(request, 'renew_premium.html', {"user": user})

@login_required
def initiate_payment(request):
    if request.method == "POST":
        user = request.user
        months = int(request.POST.get('months', 1))
        amount = {1: 49000, 3: 139000, 6: 219000}.get(months, 49000)
        order_id = f"{user.id}-{timezone.now().strftime('%Y%m%d%H%M%S')}"

        # Tạo giao dịch
        Transaction.objects.create(
            user=user,
            order_id=order_id,
            amount=amount,
            months=months,
            status='pending'
        )

        return JsonResponse({
            'status': 'success',
            'qr_code_url': '/static/images/qr_payment.png',
            'order_id': order_id,
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@staff_member_required
def confirm_payment(request, transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id, status='pending')
        subscription, _ = PremiumSubscription.objects.get_or_create(user=transaction.user)
        
        subscription.activate_subscription(months=transaction.months)
        transaction.status = 'completed'
        transaction.save()
        send_payment_confirmation_email(transaction.user, transaction.months, transaction.amount)
        
        return redirect('premium:payment_success', user_id=transaction.user.id, months=transaction.months)
    except Transaction.DoesNotExist:
        return render(request, 'payment_error.html', {'error': 'Giao dịch không tồn tại hoặc đã được xác nhận.'})

@login_required
def payment_success(request, user_id, months):
    user = request.user
    try:
        target_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return render(request, 'payment_error.html', {'error': 'Người dùng không tồn tại.'})
    
    if not (user.is_staff or user.id == user_id):
        return render(request, 'payment_error.html', {'error': 'Bạn không có quyền truy cập trang này.'})
    
    return render(request, 'payment_success.html', {'user': target_user, 'months': months})

def premium_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        subscription = PremiumSubscription.objects.filter(user=request.user).first()
        if not subscription or not subscription.check_status():
            return redirect('premium:renew_premium')
        return view_func(request, *args, **kwargs)
    return wrapper