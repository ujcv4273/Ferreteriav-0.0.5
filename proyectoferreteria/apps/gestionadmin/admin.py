from django.contrib import admin
from django.db import models
from proyectoferreteria.apps.gestionadmin.models import FormaPago, MetodoPago, Garantia, Marca, Categoria, Proveedor,Cliente, Planilla, Empleado, Producto, Factura, TurnoEmpleado, ComprasDet,ComprasEnc
from django.core.paginator import Paginator
# Register your models here.
##@admin.register(Factura)
from django.contrib import admin
from django.http import HttpResponse
import csv


from django.http import FileResponse
from reportlab.pdfgen import canvas
import io

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import time

from import_export import resources
from import_export.admin import ImportExportModelAdmin


import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.utils import timezone
from django_xhtml2pdf.utils import generate_pdf
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

from reportlab.platypus import Paragraph, Table

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View

def link_callback(self, request, queryset,uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL      # Typically /static/
        sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL       # Typically /static/media/
        mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
                raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path

class MarcaResource (resources.ModelResource):
    class Meta:
        model= Marca

class MarcaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('idMarca','nombreMarca')
    resource_class = MarcaResource


    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'


    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfmarca.html'
        today = timezone.now()

        marcas = Marca.objects.all()
        context = {
            'obj': marcas,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'


admin.site.register(Marca, MarcaAdmin)


class ClienteAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Cliente','Identidad','Nombre_Cliente','Correo_Cliente','Direccion_Cliente','Telefono_Cliente')
    ##list_filter = ('Nombre_Cliente','Id_Cliente')
    ##list_display_links = ('Id_Cliente', 'Correo_Cliente')
    search_fields = ('Nombre_Cliente','Id_Cliente')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfcliente.html'
        today = timezone.now()

        clientes = Cliente.objects.all()
        context = {
            'obj': clientes,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'
admin.site.register(Cliente, ClienteAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display =('Id_Categoria','Descripcion_Categoria')
    search_fields =('Id_Categoria','Descripcion_Categoria')
    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfcategoria.html'
        today = timezone.now()

        categorias = Categoria.objects.all()
        context = {
            'obj': categorias,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'

admin.site.register(Categoria,CategoriaAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Proveedor','Nombre_Proveedor','Correo_Proveedor','Direccion_Proveedor','Telefono_Proveedor')
    search_fields = ('Id_Proveedor','Nombre_Proveedor','Correo_Proveedor','Direccion_Proveedor','Telefono_Proveedor')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'


    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfproveedor.html'
        today = timezone.now()

        proveedores = Proveedor.objects.all()
        context = {
            'obj': proveedores,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'

admin.site.register(Proveedor,ProveedorAdmin)

class GarantiaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Garantia','Descripcion_Garantia','Tiempo_Garantia_Mes')
    search_fields = ('Id_Garantia','Descripcion_Garantia','Tiempo_Garantia_Mes')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfgarantia.html'
        today = timezone.now()

        garantias = Garantia.objects.all()
        context = {
            'obj': garantias,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'


admin.site.register(Garantia,GarantiaAdmin) 
    

class FormaPagoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Forma_Pago','Descripcion_Forma_Pago')
    search_fields= ('Id_Forma_Pago','Descripcion_Forma_Pago')
    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'


    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfformapago.html'
        today = timezone.now()

        formapagos = FormaPago.objects.all()
        context = {
            'obj': formapagos,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'
admin.site.register(FormaPago,FormaPagoAdmin)

class MetodoPagoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('idMetodoPago','descripcionMetodoPago')
    search_fields= ('idMetodoPago','descripcionMetodoPago')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfmetodopago.html'
        today = timezone.now()

        metodopagos = MetodoPago.objects.all()
        context = {
            'obj': metodopagos,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'

admin.site.register(MetodoPago, MetodoPagoAdmin)

class PlanillaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Planilla','Sueldo_Base','IHSS','RAP')
    search_fields = ('Id_Planilla','Sueldo_Base','IHSS','RAP')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfplanilla.html'
        today = timezone.now()

        planillas = Planilla.objects.all()
        context = {
            'obj': planillas,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'

admin.site.register(Planilla,PlanillaAdmin)


class EmpleadoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Empleado','Nombre_Empleado','Id_Turno','Id_Planilla','Direccion_Empleado','Telefono_Empleado')
    search_fields = ('Id_Empleado','Id_Turno','Id_Planilla','Nombre_Empleado','Direccion_Empleado','Telefono_Empleado')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfempleado.html'
        today = timezone.now()

        empleados = Empleado.objects.all()
        context = {
            'obj': empleados,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'

admin.site.register(Empleado,EmpleadoAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Producto','Nombre_Producto','Precio_Venta','Precio_Compra','Id_Marca','Id_Categoria','Id_Garantia','Existencia','Existencia_Minima')
    search_fields = ('Id_Producto','Nombre_Producto')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfproducto.html'
        today = timezone.now()

        productos = Producto.objects.all()
        context = {
            'obj': productos,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'
admin.site.register(Producto,ProductoAdmin)


class TurnoEmpleadoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Turno','Turno','Hora_de_Entrada','Hora_de_Salida')
    search_fields = ('Id_Turno','Turno','Hora_de_Entrada','Hora_de_Salida')

    actions = (
        'export_as_csv','imprimir_pdf',
    )
 
    def export_as_csv(self, request, queryset):
        """ Export CSV action """
        # En meta almacenamos el nombre del archivo
        meta = self.model._meta
        # Guardamos una lista con los nombres de los campos
        field_names = [field.name for field in meta.fields]
 
        # Creamos una HttpResponse para enviar el archivo CSV
        response = HttpResponse(content_type='text/csv')
        # Indicamos el nombre del archivo (meta)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        # Creamos un objeto csv que va a escribir en nuestro HttpResponse
        writer = csv.writer(response)
 
        # El metodo writerow escribe secuencialmente los elementos de la lista que recibe
        # por parametro en las columas del csv y realiza un salto de linea
        writer.writerow(field_names)
        # En queryset tenemos almacenados los objetos que seleccionamos, recorremos la lista
        # para escribir sus elementos en el csv.
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
 
        # Devolvemos el objeto HttpResponse
        return response
    # Le ponemos un nombre bonito.
    export_as_csv.short_description = 'Exportar a Excel'

    def imprimir_pdf(self, request, queryset):
        template_path = 'gestionadmin/pdfturnoempleado.html'
        today = timezone.now()

        turnoempleados = TurnoEmpleado.objects.all()
        context = {
            'obj': turnoempleados,
            'today': today,
            'request': request
            }
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte de marcas.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funy view
        if pisaStatus.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    imprimir_pdf.short_description = 'Exportar a pdf'
admin.site.register(TurnoEmpleado,TurnoEmpleadoAdmin)

#class FacturaAdmin(admin.ModelAdmin):
#    list_per_page = 10
#    list_display = ('Id_Factura','Id_Empleado','Id_Cliente','Id_MetodoPago','Id_FormaPago','Numero_Sar','Codigo_CAI','ISV18','ISV15','Total_Factura')
#    search_fields = ('Id_Factura','Total_Factura')
#admin.site.register(Factura, FacturaAdmin)





