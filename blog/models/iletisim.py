import email 
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class IletisimModel(models.Model):
    email = models.EmailField(max_length = 250)
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "iletişim"
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'
        
  
    def __str__(self):
        return self.email