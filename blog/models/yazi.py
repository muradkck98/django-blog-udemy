from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstracModel

class YazilarModel(DateAbstracModel):
    resim = models.ImageField(upload_to='yazı_resimleri')
    baslik = models.CharField(max_length=50) #baslik alanı
    icerik = RichTextField() #içerik alanı
    slug = AutoSlugField(populate_from = 'baslik',unique=True) #yazıların slug ı
    Kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi') #bir yazı birden fazla kategori ile eslesebilir
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name = 'yazilar') 

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'

    def __str__(self):
        return self.baslik



