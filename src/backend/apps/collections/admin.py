from django.contrib import admin

from apps.collections.models import Collect, Payment, Reason


class CollectAdmin(admin.ModelAdmin):
    pass


class ReasonAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Collect, CollectAdmin)
admin.site.register(Reason, ReasonAdmin)
admin.site.register(Payment, PaymentAdmin)
