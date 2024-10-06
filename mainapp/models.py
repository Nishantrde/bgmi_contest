from django.db import models

class Team(models.Model):
    team_name = models.CharField(default="", max_length=100)
    member_1 = models.CharField(default="", max_length=100)
    member_2 = models.CharField(default="", max_length=100)
    member_3 = models.CharField(default="", max_length=100)
    member_4 = models.CharField(default="", max_length=100)
    ph_no = models.CharField(default="", max_length=100)

    def __str__(self):
        return self.team_name
