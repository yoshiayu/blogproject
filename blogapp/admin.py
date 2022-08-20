from django.contrib import admin
# modelsからBlogPstクラスをインポート
from .models import BlogPost

# Django管理サイトにBlogPostを登録
admin.site.register(BlogPost)
