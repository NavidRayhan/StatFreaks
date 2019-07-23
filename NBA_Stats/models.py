from django.db import models

# Basic stats for one season for one player 
class Basic_Stats(models.Model):
	
	Name = models.CharField(max_length=60, default=None)
	Year = models.IntegerField(default=None)
	Points = models.FloatField(default=None)
	Assists = models.FloatField(default=None)
	Rebounds = models.FloatField(default=None)
	Age = models.IntegerField(default=None)
	Games = models.IntegerField(default=None)
	Minutes = models.FloatField(default=None)
	Field_Goals_attempted = models.FloatField(default=None)
	Field_Goal_percentage = models.FloatField(default=None)
	ThreeP_attempted = models.FloatField(default=None)
	ThreeP_percentage = models.FloatField(default=None) 
	Offensive_rebounds = models.FloatField(default=None)
	Eff_FGP = models.FloatField(default=None)
	Free_throws = models.FloatField(default=None)
	Free_throw_percentage = models.FloatField(default=None)
	Steals = models.FloatField(default=None)
	Blocks = models.FloatField(default=None)
	Turnovers = models.FloatField(default=None)
	Fouls = models.FloatField(default=None)

	def __str__(self):
		return "{0} {1}, Basic Stats".format(self.Name,self.Year)
	
#advanced stats for one season for one player
class Advanced_Stats(models.Model):
	Name = models.CharField(max_length=60, default=None)
	Year = models.IntegerField(default=None)
	PER = models.FloatField(default=None)
	True_shooting = models.FloatField(default=None)
	ThreeP_attempt_rate = models.FloatField(default=None)
	Rebound_perc = models.FloatField(default=None)
	Offensive_rebound_perc = models.FloatField(default=None)
	Defensive_rebound_perc = models.FloatField(default=None)
	Assist_perc = models.FloatField(default=None)
	Steal_perc = models.FloatField(default=None)
	Block_perc = models.FloatField(default=None)
	Turnover_perc = models.FloatField(default=None)
	Usage = models.FloatField(default=None)
	Offensive_winshares_per48 = models.FloatField(default=None)
	Defensive_winshares_per48 = models.FloatField(default=None)
	Offensive_BPM = models.FloatField(default=None)
	Defensive_BMP = models.FloatField(default=None)
	Value_over_replacement_player = models.FloatField(default=None)

	def __str__(self):
		return "{0} {1}, Advanced Stats".format(self.Name,self.Year)

#Awards that the player earned this season
class Awards(models.Model):
	Name = models.CharField(max_length=60, default=None)
	Year = models.IntegerField(default=None)
	All_Star = models.BooleanField(default=None)
	All_NBA = models.IntegerField(blank=True)
	All_NBA_defense = models.IntegerField(blank=True)
	MVP = models.BooleanField(default=False)
	DPOY = models.BooleanField(default=False)
	MIP = models.BooleanField(default=False)
	All_Rookie = models.IntegerField(blank=True)
	Champion = models.BooleanField(default=False)

#stores every season for every player 
class Single_Season(models.Model):
	Basic_Stats = models.ForeignKey(Basic_Stats, on_delete=models.CASCADE, default=None)
	Advanced_Stats = models.ForeignKey(Advanced_Stats, on_delete = models.CASCADE, default=None)
	#Awards = models.ForeignKey(Awards, on_delete = models.CASCADE, default=None, blank=True)
	def __str__(self):
		return "{0}, {1}".format(self.Basic_Stats.Name, self.Basic_Stats.Year)
