from django.contrib import admin

from app_payments.models import PaymentMethod, Subscription


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'card_holder_name', 'card_expiry_date', 'created_at')
    list_filter = ('user', 'card_expiry_date')
    search_fields = ('user__email', 'card_holder_name', 'card_expiry_date')
    ordering = ('-id',)
    fields = ('user', 'card_holder_name', 'payment_token', 'card_expiry_date', 'billing_address', 'created_at', 'updated_at')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan_name', 'plan_price', 'start_date', 'end_date', 'auto_renew', 'status', 'created_at')
    list_filter = ('user', 'plan_name', 'start_date', 'end_date', 'auto_renew', 'status')
    search_fields = ('user__email', 'plan_name', 'start_date', 'end_date')
    ordering = ('-id',)
    fields = ('user', 'payment_method', 'plan_name', 'plan_price', 'start_date', 'end_date', 'auto_renew', 'status', 'created_at', 'updated_at')


admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(Subscription, SubscriptionAdmin)