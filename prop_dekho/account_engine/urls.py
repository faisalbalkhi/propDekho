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
    path('pg-Coliving/',views.pg_Coliving, name='pg_Coliving'),
    path('rent/',views.rent, name='rent'),
    path('dashboard-myprofile/', views.dashboard_mypropfile, name='dashboard_mypropfile'),
    path('plot/',views.plot, name='plot'),
    path('commercial/',views.commercial, name='commercial'),
    path('property/',views.property, name='property'),
    path('pgDetails/',views.pgDetails, name='pgDetails'),
    path('rent-All-Listing/',views.rent_All_Listing, name='rent_All_Listing'),
    path('sell-All-Listing/',views.sell_All_Listing, name='sell_All_Listing'),

]
