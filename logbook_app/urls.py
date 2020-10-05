from django.urls import path
from logbook_app import views
from django.contrib.auth import views as auth_views
from logbook_app.forms import LoginForm

app_name = 'logbook_app'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html', form_class=LoginForm), name='login'),
    path('logout-page/', auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    
    path('home-page/', views.home, name='home'),

    path('add-page/', views.add_logbook, name='add_logbook'),
    path('view-page/', views.view_logbook, name='view_logbook'),
    path('view-page/<id>/', views.edit_logbook, name='edit_logbook'),
    path('view-page/<id>/delete', views.delete_logbook, name='delete_logbook'),

    path('add-infopage/', views.add_info, name='add_info'),
    path('view-infopage/', views.view_info, name='view_info'),
    path('view-infopage/<id>/', views.edit_info, name='edit_info'),
    path('view-infopage/<id>/delete', views.delete_info, name='delete_info'),

]