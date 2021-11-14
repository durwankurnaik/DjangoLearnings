from django.db import models


# Create your models here.


class TimeTable(models.Model):
    match_no = models.IntegerField(default=0)
    venue = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    home_team = models.CharField(max_length=100)
    opp_team = models.CharField(max_length=100)

    def __str__(self):
        return 'Match number ' + str(self.match_no)


class Register(models.Model):
    user = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    dob = models.DateField()

    def __str__(self):
        return self.user + ', ' + self.name


class Player(models.Model):
    player_num = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    team_name = models.CharField(max_length=50)
    player_type = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class PointsTable(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    tie = models.IntegerField(default=0)

    def __str__(self):
        return 'Rank ' + str(self.rank)
