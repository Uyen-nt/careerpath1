from django.contrib import admin
from .models import PremiumSubscription, Transaction

@admin.register(PremiumSubscription)
class PremiumSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'trial_start', 'trial_end', 'subscription_start', 'subscription_end', 'days_left')
    list_filter = ('is_active', 'has_used_trial')
    search_fields = ('user__username', 'user__email')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'amount', 'months', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username', 'user__email')
