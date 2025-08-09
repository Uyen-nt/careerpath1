from django.contrib import admin
from .models import PremiumSubscription, Transaction
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse
from django.utils.html import format_html
from .views import send_payment_confirmation_email

@admin.register(PremiumSubscription)
class PremiumSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'trial_start', 'trial_end', 'subscription_start', 'subscription_end', 'days_left')
    list_filter = ('is_active', 'has_used_trial')
    search_fields = ('user__username', 'user__email')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'amount', 'months', 'status', 'created_at', 'action_link')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username', 'user__email')
    actions = ['mark_as_completed']

    def action_link(self, obj):
        if obj.status == 'pending':
            url = reverse('premium:confirm_payment', args=[obj.id])
            return format_html('<a href="{}" class="button">Xác nhận</a>', url)
        return '-'
    action_link.short_description = 'Hành động'

    def mark_as_completed(self, request, queryset):
        for transaction in queryset.filter(status='pending'):
            subscription, _ = PremiumSubscription.objects.get_or_create(user=transaction.user)
            subscription.activate_subscription(months=transaction.months)
            transaction.status = 'completed'
            transaction.save()
            send_payment_confirmation_email(transaction.user, transaction.months, transaction.amount)
            messages.success(request, f"Đã xác nhận giao dịch {transaction.order_id} và kích hoạt Premium cho {transaction.user.username}.")
    mark_as_completed.short_description = "Xác nhận giao dịch và kích hoạt Premium"