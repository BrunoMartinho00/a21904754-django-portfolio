#  hello/urls.py

from django.urls import path
from . import views


app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aboutme/', views.aboutme_page_view, name='aboutme'),
    path('projects/', views.projects_page_view, name='projects'),
    path('contacts/', views.contacts_page_view, name='contacts'),
    path('scripts/', views.scripts_page_view, name='scripts'),
    path('login/', views.login_page_view, name='login'),
    path('logout/', views.logout_page_view, name='logout'),
    path('new-formacao/', views.new_formacao_page_view, name='new_formacao'),
    path('edit-formacao/<int:formacao_id>/', views.edit_formacao_page_view, name='edit_formacao'),
    path('remove-formacao/<int:formacao_id>/', views.remove_formacao_page_view, name='remove_formacao'),
    path('new-participacao/', views.new_participacao_page_view, name='new_participacao'),
    path('edit-participacao/<int:participacao_id>/', views.edit_participacao_page_view, name='edit_participacao'),
    path('remove-participacao/<int:participacao_id>/', views.remove_participacao_page_view, name='remove_participacao'),
    path('new-interesse/', views.new_interesse_page_view, name='new_interesse'),
    path('edit-interesse/<int:interesse_id>/', views.edit_interesse_page_view, name='edit_interesse'),
    path('remove-interesse/<int:interesse_id>/', views.remove_interesse_page_view, name='remove_interesse'),
]