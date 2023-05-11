from django.contrib import admin
from tt.models import teachers

class ttAdmin(admin.ModelAdmin):
    list_display=('user_name','teachers_id','fullname','password','department')
    
admin.site.register(teachers,ttAdmin)
# Register here.
