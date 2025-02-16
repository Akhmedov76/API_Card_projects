from django.contrib import admin

from app_tests.models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'questions', 'answers')
    list_filter = ('team',)
    search_fields = ('questions', 'answers')
    ordering = ('-id',)
    fields = ('team', 'questions', 'answers')

admin.site.register(Test, TestAdmin)
