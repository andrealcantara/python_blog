from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'category', 'approved']
    search_fields = ['title','sub_title','category']

    def get_queryset(self, request):
        return Post.objects.filter(approved=True)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'content']

admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)