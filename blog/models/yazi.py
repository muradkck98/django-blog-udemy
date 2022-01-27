from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class YazilarModel(models.Model):
    resim = models.ImageField(upload_to='yazı_resimleri')
    baslik = models.CharField(max_length=50) #baslik alanı
    icerik = RichTextField() #içerik alanı
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True) #yazılar tablomuzda kayır olusturduğumuzda otomatik tarih dolacak
    duzenleme_tarihi = models.DateTimeField(auto_now=True) 
    slug = AutoSlugField(populate_from = 'baslik',unique=True) #yazıların slug ı
    Kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi') #bir yazı birden fazla kategori ile eslesebilir
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'yazilar') 

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.baslik
