from django.contrib import admin
from sorl.thumbnail import get_thumbnail

from .models import Producto, Proveedor, Marca, Categoria
from .actions import export_as_excel


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'nombre', 'descripcion', 'marca', 'categoria','existencia', 'precioCompra', 'precioVenta', 'precioPorMayor', 'proveedor', 'imagen_producto')
    list_filter = ('categoria', 'marca', 'proveedor',)
    search_fields = ('nombre', 'descripcion', 'marca__nombre', 'categoria__nombre')
    list_editable = ('existencia', 'precioCompra', 'precioVenta', 'precioPorMayor')
    actions = (export_as_excel, )
    # raw_id_fields = ('nombre', )

    def imagen_producto(self, obj):
    	# print obj.imagen.url -- get_thumbnail(obj.cover, '50x50').url
    	return '<img src="%s" />' % get_thumbnail(obj.imagen, '50x50').url

    imagen_producto.allow_tags = True


admin.site.register(Producto, ProductoAdmin)

admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Categoria)



# class AlbumAdmin(admin.ModelAdmin):
#     list_display = ('title', 'artist', 'imagen_album',)
#     list_filter = ('artist',)
#     search_fields = ('title', )
#     list_editable = ('artist',)

#     def imagen_album(self, obj):
#         # print get_thumbnail(obj.cover, '50x50').url
#         return '<img src="%s" />' % obj.cover.url

#     imagen_album.allow_tags = True