
from django.contrib import admin
from django.urls import path

from first.views import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    # path('about/', about_page),
]
