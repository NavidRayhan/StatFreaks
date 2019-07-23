from django.shortcuts import render, render_to_response, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Basic_Stats, Single_Season, Advanced_Stats
from django.db import connection as conn 
from django.db.models import Avg,Value, When,Q
from .forms import Player_Lookup
import random
import sqlite3

#random player appears as the default value in the nav bar	

def index(request):
	template = loader.get_template("NBA_Stats/index.html")
	context = {
        'Random_Player': Single_Season.objects.all()[random.randint(0,7000)].Basic_Stats.Name
    }
	return HttpResponse(template.render(context, request))

def single_player(request, player_name):
	#try:
	Most_Recent_Season= Basic_Stats.objects.raw("""SELECT * from 
	NBA_Stats_basic_stats WHERE Name=%s COLLATE NOCASE
		order by Year desc limit 1""",[player_name])[0]

	Best_Season = Basic_Stats.objects.raw("""SELECT * from 
	NBA_Stats_basic_stats WHERE Name=%s COLLATE NOCASE
		order by Points desc limit 1""",[player_name])[0]
		#except:
	
		
		#template = loader.get_template("NBA_Stats/player_not_found.html") 
	#	return HttpResponse(template.render(
	#		{'player': player_name.replace('%'," "),
	#		'Random_Player': Single_Season.objects.all()[random.randint(0,7000)].Basic_Stats.Name},
	#		request))
		
	#Pass every season that this player has played		
	Career_Averages_Basic = Basic_Stats.objects.aggregate(
		Points = Avg('Points', filter=Q(Name__iexact=player_name)),
		Assists = Avg('Assists', filter=Q(Name__iexact=player_name)),
		Rebounds = Avg('Rebounds', filter=Q(Name__iexact=player_name)),
		Games = Avg('Games', filter=Q(Name__iexact=player_name)),
		Minutes = Avg('Minutes', filter=Q(Name__iexact=player_name)),
		Field_Goals_attempted = Avg('Field_Goals_attempted', filter=Q(Name__iexact=player_name)),
		Field_Goal_percentage = Avg('Field_Goal_percentage', filter=Q(Name__iexact=player_name)),
		ThreeP_attempted = Avg('ThreeP_attempted', filter=Q(Name__iexact=player_name)),
		ThreeP_percentage = Avg('ThreeP_percentage', filter=Q(Name__iexact=player_name)),
		Offensive_rebounds = Avg('Offensive_rebounds', filter=Q(Name__iexact=player_name)),
		Eff_FGP = Avg('Eff_FGP', filter=Q(Name__iexact=player_name)),
		Free_throws = Avg('Free_throws', filter=Q(Name__iexact=player_name)),
		Free_throw_percentage = Avg('Free_throw_percentage', filter=Q(Name__iexact=player_name)),
		Steals = Avg('Steals', filter=Q(Name__iexact=player_name)),
		Blocks= Avg('Blocks', filter=Q(Name__iexact=player_name)),
		Turnovers = Avg('Turnovers', filter=Q(Name__iexact=player_name)),
		Fouls = Avg('Fouls', filter=Q(Name__iexact=player_name)),
		)
	for key in Career_Averages_Basic:
		if key not in ["Free_throw_percentage", "ThreeP_percentage"]:
			Career_Averages_Basic[key] = round(Career_Averages_Basic[key],1)
		else:
			Career_Averages_Basic[key] = round(Career_Averages_Basic[key],3)
	def get_ranks(Season):
		Rank = {
			'Points' : Basic_Stats.objects.filter(Points__gt=Season.Points).filter(Year=Season.Year).count()+1,
			'Assists' : Basic_Stats.objects.filter(Assists__gt=Season.Assists).filter(Year=Season.Year).count()+1,
			'Rebounds' : Basic_Stats.objects.filter(Rebounds__gt=Season.Rebounds).filter(Year=Season.Year).count()+1,
			'Games' : Basic_Stats.objects.filter(Games__gt=Season.Games).filter(Year=Season.Year).count()+1,
			'Minutes' : Basic_Stats.objects.filter(Minutes__gt=Season.Minutes).filter(Year=Season.Year).count()+1,
			'Field_Goals_attempted' : Basic_Stats.objects.filter(Field_Goals_attempted__gt=Season.Field_Goals_attempted).filter(Year=Season.Year).count()+1,
			'Field_Goal_percentage' : Basic_Stats.objects.filter(Field_Goal_percentage__gt=Season.Field_Goal_percentage).filter(Year=Season.Year).count()+1,
			'ThreeP_attempted' : Basic_Stats.objects.filter(ThreeP_attempted__gt=Season.ThreeP_attempted).filter(Year=Season.Year).count()+1,
			'ThreeP_percentage' : Basic_Stats.objects.filter(ThreeP_percentage__gt=Season.ThreeP_percentage).filter(Year=Season.Year).count()+1,
			'Offensive_rebounds' : Basic_Stats.objects.filter(Offensive_rebounds__gt=Season.Offensive_rebounds).filter(Year=Season.Year).count()+1,
			'Eff_FGP' : Basic_Stats.objects.filter(Eff_FGP__gt=Season.Eff_FGP).filter(Year=Season.Year).count()+1,
			'Free_throws' : Basic_Stats.objects.filter(Free_throws__gt=Season.Free_throws).filter(Year=Season.Year).count()+1,
			'Free_throw_percentage' : Basic_Stats.objects.filter(Free_throw_percentage__gt=Season.Free_throw_percentage).filter(Year=Season.Year).count()+1,
			'Steals' : Basic_Stats.objects.filter(Steals__gt=Season.Steals).filter(Year=Season.Year).count()+1,
			'Blocks': Basic_Stats.objects.filter(Blocks__gt=Season.Blocks).filter(Year=Season.Year).count()+1,
			'Turnovers' : Basic_Stats.objects.filter(Turnovers__gt=Season.Turnovers).filter(Year=Season.Year).count()+1,
			'Fouls' : Basic_Stats.objects.filter(Fouls__gt=Season.Fouls).filter(Year=Season.Year).count()+1
		}
		
		return Rank

	Recent_Rank = get_ranks(Most_Recent_Season)
	Best_Rank = get_ranks(Best_Season)
	#Career_Averages_Advanced=

	context = {
		'Most_Recent_Season': Most_Recent_Season,
		'Recent_Rank':Recent_Rank,
		'Best_Rank': Best_Rank,
		'Best_Season' : Best_Season,
		'Career_Averages_Basic' : Career_Averages_Basic,
		'Random_Player': Single_Season.objects.all()[random.randint(0,7000)].Basic_Stats.Name
	}	
	template = loader.get_template("NBA_Stats/single_player.html") 
	return HttpResponse(template.render(context, request))

