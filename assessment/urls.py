"""LIM URL Configuration

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

from django.urls import path
from .views import index, Signup, Login, profile,Newassessment,Demographics,Thirdpage
urlpatterns = [
    path('', index, name='home'),
    path('login', Login.as_view()),
    path('signup', Signup.as_view()),
    path('profile', profile),
    path('newassessment',Newassessment.as_view()),
    path('demographics',Demographics.as_view()),
    path('thirdpage',Thirdpage.as_view())
]