from django.contrib import admin
from blog.models import (
    KategoriModel, YazilarModel, YorumModel, IletisimModel
)

# Register your models here.
admin.site.register(KategoriModel)

@admin.register(YazilarModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik')
    list_display = (
        'baslik', 'olusturulma_tarihi', 'duzenleme_tarihi'
    )

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'olusturulma_tarihi','duzenleme_tarihi')
    search_fields = ('yazan__username',)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email', 'olusturulma_tarihi')
    search_fields = ('email',)
