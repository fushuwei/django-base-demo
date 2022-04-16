"""django_base_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.views.static import serve

urlpatterns = [
    # templates路由
    url(r'^templates/(?P<path>.*)$', serve, {"document_root": 'templates'}),

    # 配置静态资源路由
    url(r'^static/(?P<path>.*)$', serve, {'document_root': 'static'}),

    # 管理端页面路由
    url('admin/', admin.site.urls),

    # 自定义模块路由
    url('demo/', include('django_base_demo.apps.demo.urls')),
]
