from django.contrib import admin
from st.models import students
from st.models import teachers
class stAdmin(admin.ModelAdmin):
    list_display=('name','roll','cgpa','advisor','username','password','sem','cgpa1','cgpa2','cgpa3','cgpa4','cgpa5','cgpa6','cgpa7','cgpa8')
    
admin.site.register(students,stAdmin)
# Register your models here.
class ttAdmin(admin.ModelAdmin):
    list_display=('user_name','teachers_id','fullname','password','department')
    
admin.site.register(teachers,ttAdmin)