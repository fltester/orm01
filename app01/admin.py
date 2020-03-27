from django.contrib import admin

# Register your models here.
from app01 import models
#注册数据到admin
#创建admin用户，createsuperuser
admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)
admin.site.register(models.Book1)
admin.site.register(models.Publish)