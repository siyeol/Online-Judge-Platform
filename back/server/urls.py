"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('code_efficiency/', include('apps.code_efficiency.urls')),
    # path('code_explain/', include('apps.code_explain.urls')),
    # path('code_readability/', include('apps.code_readability.urls')),
    # path('copy_detect/', include('apps.copy_detect.urls')),
    path('code_submit/', include('apps.code_submit.urls')),
    path('code_run/', include('apps.code_run.urls')),
    path('lecture/', include('apps.db.urls'))
]
