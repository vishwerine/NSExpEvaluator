from django.db import models

# Create your models here.

class Article(models.Model):
	img_loc = models.CharField(max_length=200)
	caption = models.CharField(max_length=200)
	hypothesis = models.CharField(max_length=200)
	nhypothesis = models.CharField(max_length=200)


