from django.db import models

# Create your models here.
class Football(models.Model):
	match_datetime = models.DateTimeField()
	country = models.CharField(max_length=100)
	league = models.CharField(max_length=100)
	home_team = models.CharField(max_length=100)
	away_team = models.CharField(max_length=100)
	home_odds = models.DecimalField(max_digits = 5,decimal_places = 2)
	draw_odds = models.DecimalField(max_digits = 5,decimal_places = 2)
	away_odds = models.DecimalField(max_digits = 5,decimal_places = 2)
	predicted_home_score = models.DecimalField(max_digits = 5,decimal_places = 2)
	predicted_away_score = models.DecimalField(max_digits = 5,decimal_places = 2)
	total_predicted_score = models.DecimalField(max_digits = 5,decimal_places = 2)
	csv = models.FileField(upload_to='media/csv/')

	def __str__(self):
		return self.country