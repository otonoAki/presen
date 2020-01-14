from django.db import models

class Userinfo(models.Model):

    oauth_token = models.CharField(primary_key=True,max_length=100)
    followes = models.IntegerField()
    friends_rs_count = models.IntegerField()
    favourites_count = models.IntegerField()
    screen_name = models.CharField(max_length=100,null=True)