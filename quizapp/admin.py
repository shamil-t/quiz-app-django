from django.contrib import admin
from .models import User_Model,Quiz_Model,Quiz_result
# Register your models here.


admin.site.register(User_Model)
admin.site.register(Quiz_Model)
admin.site.register(Quiz_result)
