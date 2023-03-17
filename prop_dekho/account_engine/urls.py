from django.urls import path
from account_engine import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('dashboard-add-listing/', views.dashboard_add_listing, name='dashboard_add_listing'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('agent-list/', views.agent_list, name='agent_list'),
    path('dashboard-agent/', views.dashboard_agent, name='dashboard_agent'),
    path('dashboard-myprofile/', views.dashboard_mypropfile, name='dashboard_mypropfile'),

]
