from django.contrib import admin
from .models import *

# Register your models here.

class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Number', 'Email', 'Message')
admin.site.register(contactus,contactusAdmin)


class signupAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'password', 'image', 'address')
admin.site.register(signup,signupAdmin)


class feedbackusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'image', 'feedback')
admin.site.register(feedbackus,feedbackusAdmin)


class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'Npic')
admin.site.register(category,categoryAdmin)

class ourblogAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Image','Data','Date')
admin.site.register(ourblog,ourblogAdmin)

class mynewsAdmin(admin.ModelAdmin):
    list_display = ('id','newstitle','newsdec','newsimage','newscategory','newsdate','newsreporter')
admin.site.register(mynews,mynewsAdmin)

class signup_reporterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'password', 'image', 'address')
admin.site.register(signup_reporter,signup_reporterAdmin)