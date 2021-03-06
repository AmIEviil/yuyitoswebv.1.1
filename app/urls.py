from django.urls import path
from .views import filtrar_palabra_clave,eliminar_producto,restar_producto,limpiar_carrito,agregar_producto, registro,bancos,pagowebpay, visualizar_prod,webpay,catalogo,delivery,home,vista_prod,carritodecompras,fiado,mediosdepago,productos,quienessomos          


urlpatterns = [
    path('', home, name="home"),
    path('vista_prod/<id>/', vista_prod, name="vista_prod"),
    path('visualizar_prod/<id>/', visualizar_prod, name="visualizar_prod"),
    path('carritodecompras/', carritodecompras, name="carritodecompras"),
    path('fiado/', fiado, name="fiado"),
    path('mediosdepago/', mediosdepago, name="mediosdepago"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('delivery/', delivery, name="delivery"),
    path('catalogo/', catalogo, name="catalogo"),
    path('webpay/', webpay, name="Webpay"),
    path('pagowebpay/',pagowebpay, name="Pagowebpay"),
    path('bancos/',bancos, name="Bancos"),
    path('registro/',registro, name="registro"),
    path('agregar/<int:id_producto>/', agregar_producto, name="Add"),
    path('eliminar/<int:id_producto>/', eliminar_producto, name="Del"),
    path('restar/<int:id_producto>/', restar_producto, name="Res"),
    path('limpiar/', limpiar_carrito, name="Era"),
    path('filtro_pc/',filtrar_palabra_clave, name="filtroPC"),
]
