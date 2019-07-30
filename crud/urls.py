
from django.contrib import admin
from django.urls import path, include
import classcrud.views
import classcrud.urls
import viewcrud.views
import viewcrud.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',viewcrud.views.welcome, name = 'welcome'),
    path('funccrud/', include(viewcrud.urls)),
    path('classcrud', include(classcrud.urls)),
]
