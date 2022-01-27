from django.contrib import admin
from blog.models import KategoriModel
from blog.models.yazi import YazilarModel

# Register your models here.

admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslık','icerik')
    list_display = (
        'baslik', 'olusturulma_tarihi', 'duzenleme_tarihi'
    )

admin.site.register(YazilarModel, YazilarAdmin)
