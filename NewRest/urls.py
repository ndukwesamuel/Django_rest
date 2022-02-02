"""NewRest URL Configuration

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
from django.urls import path
from DataApp.views import( home, API_NAME,
     PostView, PostDetail, PostCreate,PostDelete, PostUpdate
)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name="home"),
    path('API_NAME/', API_NAME, name="API"),
    path('', PostView.as_view(), name="simple"),
    path('create/', PostCreate.as_view(), name="create"),

    path('list/<pk>/', PostDetail.as_view(), name="details"),
    path('delete/<pk>/', PostDelete.as_view(), name="Delete"),
    path('update/<pk>/', PostUpdate.as_view(), name="Delete"),







]
