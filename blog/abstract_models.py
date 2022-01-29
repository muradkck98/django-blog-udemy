from django.db import models

class DateAbstracModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True) #yazılar tablomuzda kayır olusturduğumuzda otomatik tarih dolacak
    duzenleme_tarihi = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True