"""
URL configuration for apples project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings              # 17,18 - импорты для медиафайлов
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from store.views import MainCategory, GetAllProductsByCategories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainCategory.as_view(), name='home'),
    path('all_categories/<str:categories_name>/', GetAllProductsByCategories.as_view(), name='all_categories'),
    path('user/', include('user.urls')),  # перенаправление
    path('basket/', include('basket.urls')),
]
# скрипт для изображений медиафайлов

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)