from django.db import models


# Create your models here.


class Register(models.Model):
    user = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return self.user


class Player(models.Model):
    player_num = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    team_name = models.CharField(max_length=50)
    player_type = models.CharField(max_length=25)
    description = models.CharField(max_length=500, default="")
    image = models.ImageField()

    def __str__(self):
        return self.name


class TeamInfo(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    played = models.IntegerField()
    won = models.IntegerField()
    loss = models.IntegerField()
    tie = models.IntegerField()
    description = models.CharField(max_length=500, default="")
    image = models.ImageField()

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
        return str(self.rank) + ', ' + str(self.name)


class TopRaider(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return str(self.rank) + ', ' + str(self.name)


class TopDefender(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return str(self.rank) + ', ' + str(self.name)
