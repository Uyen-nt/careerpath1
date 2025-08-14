from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.urls import reverse

from quiz_highschool.models import QuizHighschool
from quiz_university.models import QuizUniversity

from premium.models import PremiumSubscription


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)  # Tự động đăng nhập sau khi đăng ký
            return redirect('home')  # Thay 'home' bằng tên URL bạn muốn
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect dựa theo quyền
            if user.is_staff:
                return redirect(reverse('admin:index'))
            return redirect('home')
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không chính xác.")
    else:
        form = CustomAuthenticationForm()

    # Form reset mật khẩu
    password_reset_form = PasswordResetForm()

    return render(request, 'login.html', {
        'form': form,
        'password_reset_form': password_reset_form
    })

@require_POST # Chỉ cho phép phương thức POST
def ajax_password_reset_view(request):
    # Kiểm tra xem có phải là request AJAX không (tùy chọn nhưng là good practice)
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax:
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Tùy chỉnh các tham số để gửi email
            # Quan trọng: cần có `request=request` để Django có thể tạo link tuyệt đối
            form.save(
                request=request,
                from_email=None, # Sử dụng DEFAULT_FROM_EMAIL trong settings.py
                email_template_name='registration/password_reset_email.txt',  # fallback plain text
                subject_template_name='registration/password_reset_subject.txt',
                html_email_template_name='registration/password_reset_email.html',  # ✅ gửi email HTML
            )

            return JsonResponse({'status': 'success', 'message': 'Vui lòng kiểm tra email để đặt lại mật khẩu.'})
        else:
            # Trả về lỗi nếu form không hợp lệ
            return JsonResponse({'status': 'error', 'errors': form.errors.get_json_data()}, status=400)
    
    # Nếu không phải AJAX, trả về lỗi
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

    def form_valid(self, form):
        form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'message': 'Mật khẩu đã được thay đổi thành công!'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # ✅ Gửi về một dictionary chứa TẤT CẢ các lỗi
            # JavaScript sẽ tự xử lý việc hiển thị
            return JsonResponse({
                'status': 'error', 
                'errors': form.errors.get_json_data()
            }, status=400)
            
        return super().form_invalid(form)

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    # Lịch sử định hướng ngành học (Highschool)
    quiz_history_highschool = QuizHighschool.objects.filter(user=request.user).order_by('-created_at')
    
    # Lịch sử định hướng ngành nghề (University)
    quiz_history_university = QuizUniversity.objects.filter(user=request.user).order_by('-updated_at')

    return render(request, 'profile.html', {
        'user': request.user,
        'quiz_history_highschool': quiz_history_highschool,
        'quiz_history_university': quiz_history_university,
    })



@login_required
def delete_account_view(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')
    return render(request, 'delete_account_confirm.html')


@login_required
@require_POST
def ajax_update_avatar(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Sử dụng một form đơn giản chỉ chứa trường avatar
        # Chúng ta có thể tạo một form mới hoặc tái sử dụng CustomUserChangeForm
        # Ở đây, ta sẽ truy cập trực tiếp để đơn giản hóa
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        
        # Chỉ kiểm tra và lưu trường avatar
        if 'avatar' in request.FILES:
            request.user.avatar = request.FILES['avatar']
            request.user.save(update_fields=['avatar'])
            
            # Trả về đường dẫn của ảnh mới để JS cập nhật giao diện
            return JsonResponse({'status': 'success', 'new_avatar_url': request.user.avatar.url})

        # Nếu không có file nào được gửi
        return JsonResponse({'status': 'error', 'message': 'Không có file nào được chọn.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Yêu cầu không hợp lệ.'}, status=400)


@login_required
def ajax_update_profile(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        user = request.user
        
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        # [THAY ĐỔI 1]: Lấy username từ form
        username = request.POST.get('username', '').strip()

        # --- Validation ---
        if not first_name or not last_name:
            return JsonResponse({'status': 'error', 'message': 'Họ và Tên không được để trống.'})

        # [THAY ĐỔI 2]: Thêm validation cho username
        if not username:
            return JsonResponse({'status': 'error', 'message': 'Tên người dùng không được để trống.'})

        # Chỉ kiểm tra nếu tên người dùng có sự thay đổi
        if username != user.username:
            # Kiểm tra xem tên người dùng mới đã tồn tại chưa
            if request.user._meta.model.objects.filter(username=username).exists():
                 return JsonResponse({'status': 'error', 'message': 'Tên người dùng này đã tồn tại. Vui lòng chọn tên khác.'})

        # Kiểm tra định dạng email
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'status': 'error', 'message': 'Địa chỉ email không hợp lệ.'})

        # Kiểm tra email đã tồn tại chưa (trừ email của chính user này)
        if request.user._meta.model.objects.filter(email=email).exclude(pk=user.pk).exists():
             return JsonResponse({'status': 'error', 'message': 'Địa chỉ email này đã được sử dụng.'})

        # --- Cập nhật thông tin ---
        try:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username # Thêm dòng cập nhật username
            
            # Chạy validation đầy đủ của model (ví dụ: kiểm tra ký tự không hợp lệ trong username)
            user.full_clean()
            user.save()
        except ValidationError as e:
            # Bắt lỗi từ full_clean()
            # Django thường trả về lỗi dưới dạng dictionary, ta lấy lỗi đầu tiên
            error_message = list(e.message_dict.values())[0][0]
            return JsonResponse({'status': 'error', 'message': f'Dữ liệu không hợp lệ: {error_message}'})


        # [THAY ĐỔI 3]: Trả về username mới trong JSON
        return JsonResponse({
            'status': 'success',
            'message': 'Cập nhật thành công!',
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def ajax_delete_account(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        user = request.user
        
        # Kiểm tra xem tên người dùng nhập vào có khớp không
        # confirmation = request.POST.get('confirmation_text', '')
        # if confirmation != user.username:
        #     return JsonResponse({
        #         'status': 'error',
        #         'message': 'Tên người dùng xác nhận không chính xác.'
        #     }, status=400)

        # Đăng xuất người dùng trước khi xóa
        logout(request)
        
        # [THAY ĐỔI QUAN TRỌNG]: Xóa vĩnh viễn tài khoản khỏi database
        user.delete()

        return JsonResponse({
            'status': 'success',
            'message': 'Tài khoản của bạn đã được xóa vĩnh viễn.',
            'redirect_url': reverse('home') 
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

# @login_required
# def edit_profile_view(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('users:profile')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     return render(request, 'edit_profile.html', {'form': form})
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Q


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
# ĐÚNG:
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import CustomUser

# ---------- QUẢN LÝ SUPERUSER ----------
@user_passes_test(lambda u: u.is_superuser)
def manage_superusers_view(request):
    superusers = CustomUser.objects.filter(is_superuser=True).order_by("-date_joined")
    candidates = CustomUser.objects.filter(is_superuser=False).order_by("-date_joined")[:10]
    return render(request, "control_manage_superusers.html", {
        "superusers": superusers,
        "candidates": candidates,
    })

@staff_member_required
@require_POST
def promote_to_superuser(request, user_id):
    u = get_object_or_404(CustomUser, pk=user_id)
    u.is_superuser = True
    u.is_staff = True  # cần để vào /admin/
    u.save(update_fields=["is_superuser", "is_staff"])
    messages.success(request, f"Đã nâng {u.username} thành superuser.")
    return redirect("users:manage_superusers")

@staff_member_required
@require_POST
def revoke_superuser(request, user_id):
    u = get_object_or_404(CustomUser, pk=user_id)
    u.is_superuser = False
    # tuỳ chính sách của bạn: có thể vẫn giữ is_staff nếu muốn
    u.is_staff = False
    u.save(update_fields=["is_superuser", "is_staff"])
    messages.success(request, f"Đã hạ quyền superuser của {u.username}.")
    return redirect("users:manage_superusers")


# ---------- QUẢN LÝ USER THƯỜNG ----------
@staff_member_required
def manage_users_view(request):
    qs = CustomUser.objects.filter(is_staff=False).order_by('-date_joined')
    q = request.GET.get('q', '').strip()
    premium = request.GET.get('premium')
    active = request.GET.get('active')

    if q:
        qs = qs.filter(Q(username__icontains=q) | Q(email__icontains=q))
    if premium in ('1', '0'):
        qs = qs.filter(is_premium=(premium == '1'))
    if active in ('1', '0'):
        qs = qs.filter(is_active=(active == '1'))

    return render(request, 'control_manage_users.html', {
        'users_list': qs, 'q': q, 'premium': premium, 'active': active
    })


@staff_member_required
@require_POST
def toggle_active(request, user_id):
    u = get_object_or_404(CustomUser, pk=user_id, is_staff=False)
    u.is_active = not u.is_active
    u.save(update_fields=['is_active'])
    messages.success(request, f'Đã {"mở" if u.is_active else "khóa"} {u.username}.')
    return redirect('users:manage_users')

@staff_member_required
@require_POST
def set_premium(request, user_id):
    u = get_object_or_404(CustomUser, pk=user_id, is_staff=False)
    days = int(request.POST.get('days', '30'))
    u.is_premium = True
    u.premium_expiry = timezone.now() + timedelta(days=days)
    u.save(update_fields=['is_premium', 'premium_expiry'])

    # ✅ Cập nhật/khởi tạo subscription tương ứng
    sub, _ = PremiumSubscription.objects.get_or_create(user=u)
    if sub.subscription_start is None:
        sub.subscription_start = timezone.now()
    sub.subscription_end = u.premium_expiry
    sub.is_active = True
    sub.save(update_fields=['subscription_start', 'subscription_end', 'is_active'])

    messages.success(request, f'Đã set premium cho {u.username} {days} ngày.')
    return redirect('users:manage_users')

@staff_member_required
@require_POST
def remove_premium(request, user_id):
    u = get_object_or_404(CustomUser, pk=user_id, is_staff=False)
    u.is_premium = False
    u.premium_expiry = None
    u.save(update_fields=['is_premium', 'premium_expiry'])

    # ✅ Đồng bộ subscription nếu có
    from premium.models import PremiumSubscription
    sub = PremiumSubscription.objects.filter(user=u).first()
    if sub:
        sub.is_active = False
        sub.subscription_end = None
        sub.save(update_fields=['is_active', 'subscription_end'])

    messages.success(request, f'Đã gỡ premium của {u.username}.')
    return redirect('users:manage_users')

