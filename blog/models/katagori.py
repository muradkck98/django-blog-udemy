from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='isim',unique=True) #uniqlik sayesinde ikitane aynı isim varsa murat-kocak murat-kocak2 otomatik ekler

    class Meta: #tablonun sqlite içindeki adı
        db_table = 'kategori'
        verbose_name_plural = 'Kategoriler'
        verbose_name ='kategori'

    def __str__(self): #object leri stringolarak
        return self.isim
