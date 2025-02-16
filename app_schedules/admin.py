from django.contrib import admin

from app_schedules.models import Schedule, Appointment


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'word_card', 'date', 'time', 'status')
    list_filter = ('user', 'word_card', 'date', 'time', 'status')
    search_fields = ('user__email', 'word_card__word', 'date', 'time')
    ordering = ('-id',)
    fields = ('user', 'word_card', 'date', 'time', 'status')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'appointment_date', 'appointment_time', 'purpose', 'location', 'status', 'confirmation_status')
    list_filter = ('user', 'appointment_date', 'appointment_time', 'purpose', 'location', 'status', 'confirmation_status')
    search_fields = ('user__email', 'appointment_date', 'appointment_time', 'purpose', 'location', 'status')
    ordering = ('-id',)
    fields = ('user', 'appointment_date', 'appointment_time', 'purpose', 'location', 'status', 'confirmation_status')


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Appointment, AppointmentAdmin)
