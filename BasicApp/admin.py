from django.contrib import admin
from BasicApp.models import Topic, ActiveRecord, Webpage


admin.site.register(ActiveRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
