from django.db import models
from datetime import datetime as dt
from django.utils import timezone
from django.conf import settings
from django.utils.timezone import activate
activate(settings.TIME_ZONE)

# Create your models here.
"""
class Period(models.Model):
    inicial = models.DateTimeField(auto_now_add=True)
    fim = models.DateTimeField()
    valid_period = models.BooleanField(default=False)

    class Meta:
        ordering =["-fim","-valid_period"]

    def val_period(self):
        if(self.inicial< dt.now()< self.fim):
            self.valid_period=True
        return self.valid_period

    def __str__(self):
        return self.fim.strftime('%d-%m-%y')
"""

class Dinar(models.Model):
    name = models.CharField(max_length=200)
    inicial = models.DateTimeField(auto_now=True)
    fim = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Dinar"
        verbose_name_plural = "Dinares"
        ordering =["-fim"]

"""
    def save(self, *args, **kwargs):
        today=dt.now()
        if self.inicial >= today:
            if((self.fim > self.inicial) and self.fim-self.inicial>1):
                super(Dinar,self).save(*args,**kwargs)
"""



class Item(models.Model):
    name   = models.CharField(max_length=200)
    nombre = models.PositiveIntegerField(default=1)
    price  = models.DecimalField(max_digits=10, decimal_places=4)
    date   = models.DateTimeField(auto_now_add=True)
    #add_time = models.TimeField(auto_now_add=True)
    isException = models.BooleanField(default=False)
    dinar = models.ForeignKey(Dinar)
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name
