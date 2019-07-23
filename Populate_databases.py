import os, sys
sys.path.append('/Navsite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Navsite.settings'
import django
django.setup()
from NBA_Stats.models import Basic_Stats, Advanced_Stats, Single_Season


import sqlite3
import xlrd

#scripts to populate the databases

def update_Basic_Stats():
	loc = "NBA_Stats/Basic_Stats_2000s.xlsx"
	book = xlrd.open_workbook(loc)
	for sheet in range(0,20):
		a = book.sheet_by_index(sheet) #2019
		for i in range(1,a.nrows):	
			try:
				player = Basic_Stats(Year=a.name,
				    Name = a.row_values(i)[1].split('\\')[0].replace('*',""),
				    Points=a.row_values(i)[27],
				    Assists=a.row_values(i)[22],
				    Rebounds=a.row_values(i)[21],
				    Age = a.row_values(i)[3],
				    Games= a.row_values(i)[4],
				    Minutes=a.row_values(i)[5],
				    Field_Goals_attempted=a.row_values(i)[7],
				    Field_Goal_percentage=a.row_values(i)[8],
				    ThreeP_attempted=a.row_values(i)[10],
				    ThreeP_percentage=a.row_values(i)[11],
				    Eff_FGP= a.row_values(i)[15],
				    Free_throws = a.row_values(i)[16],
				    Free_throw_percentage = a.row_values(i)[18],
				    Offensive_rebounds = a.row_values(i)[19],
				    Steals = a.row_values(i)[23],
				    Blocks =a.row_values(i)[24],
				    Turnovers = a.row_values(i)[25],
				    Fouls = a.row_values(i)[26]
				    )
				player.save()
			except:
				pass

def update_Advanced_Stats():
	loc = "NBA_Stats/Advanced_Stats_2000s.xlsx"
	book = xlrd.open_workbook(loc)
	for sheet in range(0,20):
		a = book.sheet_by_index(sheet) #2019
		for i in range(1,a.nrows):	
			try:
				player = Advanced_Stats(Year=a.name,
				    Name = a.row_values(i)[1].split('\\')[0].replace('*',""),
				    PER=a.row_values(i)[2],
				    True_shooting=a.row_values(i)[3],
				    ThreeP_attempt_rate = a.row_values(i)[4],
				    Rebound_perc=a.row_values(i)[8],
				    Offensive_rebound_perc= a.row_values(i)[6],
				    Defensive_rebound_perc=a.row_values(i)[7],
				    Assist_perc=a.row_values(i)[9],
				    Steal_perc=a.row_values(i)[10],
				    Block_perc=a.row_values(i)[11],
				    Turnover_perc=a.row_values(i)[12],
				    Usage= a.row_values(i)[13],
				    Offensive_winshares_per48 = a.row_values(i)[14]/48,
				    Defensive_winshares_per48 = a.row_values(i)[15]/48,
				    Offensive_BPM = a.row_values(i)[18],
				    Defensive_BMP = a.row_values(i)[19],
				    Value_over_replacement_player =a.row_values(i)[21]
				    )
				player.save()
			except:
				continue

def update_Single_Season():
	for i in Basic_Stats.objects.all():
		for j in Advanced_Stats.objects.all():
			if i.Name+str(i.Year) == j.Name +str(j.Year):
				player_item = Single_Season(Basic_Stats = i, Advanced_Stats = j)
				player_item.save()


#update_Basic_Stats()
#update_Advanced_Stats()
#update_Single_Season()
