from django.urls import path
from . import views
app_name = 'Utilisateur'
urlpatterns = [
   path('', views.home, name='home'), 
   path('pulv', views.List_Puvl, name='list_pulv'), 
   path('engrais/', views.engrais, name='engrais'),
   path('MatIr', views.List_MatIr, name='list_matir'), 
   path('product/', views.product_view, name='product_page'),
   path('profil/', views.Profil_view, name='profil_page'),
   path('login/', views.login_view, name='login_page'),
   path('register/', views.register_view, name='register_page'),
   
]
