from django.contrib import admin
from .models import CustomUser, Course, Enrollment, Feedback, File

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Feedback)
admin.site.register(File)