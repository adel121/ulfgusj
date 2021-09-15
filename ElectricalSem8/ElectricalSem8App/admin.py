from django.contrib import admin
from .models import Course,Video,Document,VisitCount,News,Student,Group, Viewer, Schedule
# Register your models here.

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Document)
admin.site.register(VisitCount)
admin.site.register(News)
admin.site.register(Schedule)
#hek b3ml register. ktir direct w basita


class StudentAdmin(admin.ModelAdmin):
    list_display = ("Name", "Discipline", "Gmail", "Email","LinuxGroup" )


admin.site.register(Student, StudentAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ("Names", "Week", "Method", "Description" )
admin.site.register(Group, GroupAdmin)

class ViewerAdmin(admin.ModelAdmin):
	list_display = ("Username", "Password","Name","datamate","Schedule","data1","data2","data3","data4","biomate","bio1")
admin.site.register(Viewer,ViewerAdmin)