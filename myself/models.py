from django.db import models

class Skilltype(models.Model):
    skilltitle = models.CharField(max_length=50)
    skilldesc = models.CharField(max_length=500)

    def __str__(self):
        return self.skilltitle + ','+self.skilldesc

class Skills(models.Model):
    skilltype = models.ForeignKey(Skilltype, on_delete=models.CASCADE);
    skillname = models.CharField(max_length=50)

    def __str__(self):
        return self.skillname
