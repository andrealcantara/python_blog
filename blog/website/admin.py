from django.contrib import admin
from .models import Post, Contact
from django.forms import ModelForm, CharField,TextInput


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'category', 'approved']
    search_fields = ['title', 'sub_title', 'category']

    def get_queryset(self, request):
        return Post.objects.filter(approved=True)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'content']

    def get_form(self, request, obj=None):
        form = super(admin.EventAdmin, self).get_form(request, obj=None)
        id = CharField(width=CharField(attrs={'size':30,'max_length':50}))
        form.base_fields['id'] = id;

admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)