"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf.urls import url, include
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView
from organization.views import OrgView
from django.views.static import serve
from .settings import MEDIA_ROOT

import xadmin

urlpatterns = [
    url('xadmin', xadmin.site.urls),
    url('index/', TemplateView.as_view(template_name='index.html'), name="index"),
    url('login/', LoginView.as_view(), name="login"),
    url('register/', RegisterView.as_view(), name='register'),
    url('captcha/', include('captcha.urls')),

    url('org/', include('organization.urls', namespace="org")),

    # 课程相关
    url('course/', include('courses.urls', namespace="course")),



    url('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]
