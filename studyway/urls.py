"""studyway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from core.views import register_teacher,list_teacher,update_teacher,register_student
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView as loginTeacher
from django.contrib.auth.views import LogoutView as logoutTeacher
urlpatterns = [
    path('', register_teacher,name="register-teacher"),
    path('teacher-page', list_teacher,name="teacher-page"),
    path('teacher-update/<str:id>',update_teacher,name="teacher-update"),
    path('login-teacher/', loginTeacher.as_view(),name="login"),
    path('logout-teacher/', logoutTeacher.as_view(),name="logout"),
    path('register-student',register_student,name="register-student"),
    path('admin/', admin.site.urls),
   
   ] 
urlpatterns+=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
