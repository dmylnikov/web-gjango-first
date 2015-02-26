from django.contrib import admin
from myapp.models import Post

#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','header','date']
#    fields = []

admin.site.register(Post, PostAdmin)
