from django.contrib import admin
from .models import PremiumSubscription, Transaction

@admin.register(PremiumSubscription)
class PremiumSubscriptionAdmin(admin.ModelAdmin):

    PremiumSubscription._meta.verbose_name = "Đăng ký Premium"
    PremiumSubscription._meta.verbose_name_plural = "Đăng ký Premium"

    list_display = ('user_vi', 'is_active_vi', 'subscription_start_vi', 'subscription_end_vi', 'days_left_vi')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'user__email')

    def user_vi(self, obj):
        return obj.user
    user_vi.short_description = "Người dùng"
    user_vi.admin_order_field = 'user'   # ← gắn field gốc để sort + màu xanh

    def is_active_vi(self, obj):
        return "Có" if obj.is_active else "Không"
    is_active_vi.short_description = "Đang hoạt động"
    is_active_vi.admin_order_field = 'is_active'

    def subscription_start_vi(self, obj):
        return obj.subscription_start
    subscription_start_vi.short_description = "Ngày bắt đầu"
    subscription_start_vi.admin_order_field = 'subscription_start'

    def subscription_end_vi(self, obj):
        return obj.subscription_end
    subscription_end_vi.short_description = "Ngày kết thúc"
    subscription_end_vi.admin_order_field = 'subscription_end'

    def days_left_vi(self, obj):
        return obj.days_left
    days_left_vi.short_description = "Số ngày còn lại"
    # days_left có thể là property -> nếu muốn sort thì cần annotate trong queryset


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    Transaction._meta.verbose_name = "Giao dịch"
    Transaction._meta.verbose_name_plural = "Giao dịch"

    list_display = ('order_id_vi', 'user_vi', 'amount_vi', 'months_vi', 'status_vi', 'created_at_vi')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username', 'user__email')

    def order_id_vi(self, obj):
        return obj.order_id
    order_id_vi.short_description = "Mã đơn hàng"
    order_id_vi.admin_order_field = 'order_id'

    def user_vi(self, obj):
        return obj.user
    user_vi.short_description = "Người dùng"
    user_vi.admin_order_field = 'user'

    def amount_vi(self, obj):
        return obj.amount
    amount_vi.short_description = "Số tiền"
    amount_vi.admin_order_field = 'amount'

    def months_vi(self, obj):
        return obj.months
    months_vi.short_description = "Số tháng"
    months_vi.admin_order_field = 'months'

    def status_vi(self, obj):
        return obj.status
    status_vi.short_description = "Trạng thái"
    status_vi.admin_order_field = 'status'

    def created_at_vi(self, obj):
        return obj.created_at
    created_at_vi.short_description = "Ngày tạo"
    created_at_vi.admin_order_field = 'created_at'

