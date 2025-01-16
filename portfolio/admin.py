from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Portfolio

class PortfolioPostAdmin(SummernoteModelAdmin):  
    prepopulated_fields= {'slug':('title',)}
    list_display = ('id', 'title', 'slug', 'tag')
    list_display_links = ('title','slug')
    summernote_fields = ('content',)

    class Meta:
        model = Portfolio


admin.site.register(Portfolio, PortfolioPostAdmin)