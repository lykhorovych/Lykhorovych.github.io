from django.db import models
from datetime import time


# Create your models here.
class Tonometr(models.Model):
    sys = models.IntegerField(default=0)
    dys = models.IntegerField(default=0)
    puls = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sys}/{self.dys} pyls{self.puls} --{self.date}"

    @property
    def get_tusk(self):
        return f"{self.sys} / {self.dys}"

    @property
    def get_puls(self):
        return f"{self.puls}"

    def get_date(self):
        return self.date.strftime("%d %m %Y %H:%M:%S")
