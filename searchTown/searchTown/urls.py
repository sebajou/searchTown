"""searchTown URL Configuration

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
from django.urls import path, re_path
from searchTownApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('town/', views.IndexView.as_view(), name='index'),
    path('town/show/<str:pk>/', views.show, name='detail'),
    path('town/edit/<str:pk>/', views.edit, name='edit'),
    # path('town/create/', views.create, name='edit'),
    path('town/delete/<str:pk>/', views.delete, name='delete'),
    path('town_search/?search=', views.TownsAPIView.as_view(), name='search'),
    path('town/town_results_list/', views.search_from_endpoint, name='search_from_endpoint'),
    # path('town/search_results/', views.search_results, name='search_results'),
]
