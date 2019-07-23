from django.urls import path

from . import views 

app_name = 'NBA_Stats'

urlpatterns = [
	path('', views.index, name="index"),
	path('<str:player_name>/', views.single_player, name='single')]
	
	#path('<str:player_searched>/', views.player_search, name='player_search'),
	#path('?q=<str:query>/', views.single_player, name='single_player')]