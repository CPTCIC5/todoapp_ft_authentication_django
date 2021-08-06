from django.contrib import admin
from .models import Contact, Todo
# Register your models here.
admin.site.site_header='TODO ADMIN'
admin.site.site_title='WELCOME ADMIN'
admin.site.index_title='ADD A TODO'

admin.site.register(Todo)
admin.site.register(Contact)


