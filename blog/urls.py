"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from blogpost.views import Index, PostView, AddPost, ModifyPost, DeletePost, LoginView, LogoutView
#app_name = "blog"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name = 'Index'),
    path('post<int:p_id>/', PostView),
    path('add/', AddPost.as_view(), name = 'Add'),
    path('post<pk>/modify/', ModifyPost.as_view(), name = 'Modify'),
    path('post<pk>/delete/', DeletePost.as_view(), name = 'Delete'),
    path('login/', LoginView, name = 'Login'),
    path('logout/', LogoutView, name = 'Logout'),
]
