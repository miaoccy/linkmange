from django.contrib import admin
from link.models import prolink,links




# Register your models here.
class ProAdmin (admin.ModelAdmin):
    list_display = ["cpname","linknum","create_time"]
    search_fields = ["cpname"]



class LinkAdmin (admin.ModelAdmin):
    list_display = ["prolink","linkname","link","linkhj","create_time"]
    search_fields = ["prolink__cpname","linkname","linkhj"]
    list_filter = ["linkhj"]


admin.site.register(prolink,ProAdmin) 
admin.site.register(links,LinkAdmin)