"""
URL configuration for alem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from stock_manage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('add_items/',views.add_items,name="add_items"),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/',views.stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    path('profile/', views.profile, name="profile"),
    path('stock_list/', views.stock_list, name="stock_list"),
    path('notification/', views.notification, name='notification'),
    path('history_list_all/', views.history_list_all, name='history_list_all'),
    path('add_to_history/<str:cat>/<str:usern>/<int:iss>/<int:rec>/<int:fs>/<str:targa>/<int:purch_quan>/<str:sales_quan>/<str:sales_price>/<str:purch_price>/<int:onhand>', views.add_to_history, name="add_to_history"),
    path('stock_list_all', views.stock_list_all, name='stock_list_all'),
    path('stock_list_user/<str:pk>', views.stock_list_user, name='stock_list_user'),
    path('accounts/', include('registration.backends.default.urls')),
]
