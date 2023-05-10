from django.contrib import admin
from st.models import students
class stAdmin(admin.ModelAdmin):
    list_display=('name','roll','cgpa','advisor','uid')
    
admin.site.register(students,stAdmin)
# Register your models here.
