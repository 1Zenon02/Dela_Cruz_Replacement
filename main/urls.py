from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views  # import views from the main app itself
from .views import ProjectDetailView, manager_login

urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request_quote/', views.request_quote, name='request_quote'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('manager/register/', views.manager_register, name='manager_register'),
    path('manager/login/', views.manager_login, name='manager_login'),
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/projects/<str:status>/', views.project_list, name='project_list'),
    path('manager/project/<int:pk>/update/', views.project_update, name='project_update'),
    path('manager/update-material/<int:material_id>/', views.update_material, name='update_material'),
    path('manager/elements/', views.list_project_elements, name='list_project_elements'),
    path('manager/materials/', views.list_materials, name='list_materials'),
    path('manager/elements/add/', views.add_project_element, name='add_project_element'),
    path('manager/elements/<int:pk>/edit/', views.edit_project_element, name='edit_project_element'),
    path('manager/elements/<int:pk>/delete/', views.delete_project_element, name='delete_project_element'),
    path('manager/materials/add/', views.add_material, name='add_material'),
    path('manager/materials/<int:pk>/edit/', views.edit_material, name='edit_material'),
    path('manager/materials/<int:pk>/delete/', views.delete_material, name='delete_material'),


    path('manager/logout/', views.manager_logout, name='manager_logout'),
    path('logout/', views.logout_view, name='logout'),






]