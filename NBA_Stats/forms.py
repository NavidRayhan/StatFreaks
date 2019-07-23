from django import forms

class Player_Lookup(forms.Form):
	player_searched = forms.CharField(label="Name", max_length=50)
