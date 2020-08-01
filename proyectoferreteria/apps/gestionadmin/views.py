from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
import datetime
from django.db.models import Sum
from django.views import generic
from proyectoferreteria.apps.gestionadmin.models import Marca, Categoria, Proveedor, Producto, Factura, ComprasEnc,ComprasDet, Cliente
from proyectoferreteria.apps.gestionadmin.formularios.marca_form import MarcaForm
from proyectoferreteria.apps.gestionadmin.formularios.categoria_form import CategoriaForm
from proyectoferreteria.apps.gestionadmin.formularios.proveedor_form import ProveedorForm
from proyectoferreteria.apps.gestionadmin.formularios.producto_form import ProductoForm
from proyectoferreteria.apps.gestionadmin.formularios.factura_form import FacturaForm
from proyectoferreteria.apps.gestionadmin.formularios.compras_enc_form import ComprasEncForm
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io



def probando(request):
    listaE = Producto.objects.all()
    contexto = {'lista': listaE}
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 50, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')




def dash_index(request):
    return render(request,'gestionadmin/dashboard.html')



def vista_principal(request):
    return render(request,'base/baseprincipal.html')


######### Marca ###########
def marca_index(request):
    listaE = Marca.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexmarca.html', contexto)

    
def marca_nueva(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Marca_index')
    else:
        form = MarcaForm()
    return render(request, 'gestionadmin/formmarca.html', {'form':form})

def marca_edit(request, id_exp):
    exp = Marca.objects.get(idMarca=id_exp)
    if request.method == 'GET':
        
        form = MarcaForm(instance=exp)

    else:
        form = MarcaForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Marca_index') 
    return render(request, 'gestionadmin/formmarca.html', {'form':form})

def marca_delete(request, id_exp):
    exp = Marca.objects.get(idMarca=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Marca_index') 
    return render(request, 'gestionadmin/formmarca.html', {'form':exp})    

######### Categoría ###########
def categoria_index(request):
    listaE = Categoria.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexcategoria.html', contexto)

    
def categoria_nueva(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Categoria_index') 
    else:
        form = CategoriaForm()
    return render(request, 'gestionadmin/formcategoria.html', {'form':form})

def categoria_edit(request, id_exp):
    exp = Categoria.objects.get(Id_Categoria=id_exp)
    if request.method == 'GET':
        
        form = CategoriaForm(instance=exp)
    else:
        form = CategoriaForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Categoria_index') 
    return render(request, 'gestionadmin/formcategoria.html', {'form':form})

def categoria_delete(request, id_exp):
    exp = Categoria.objects.get(Id_Categoria=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Categoria_index') 
    return render(request, 'gestionadmin/formcategoria.html', {'form':exp})    


######### FACTURA ###########
def factura_index(request):
    listaE = Factura.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexfactura.html', contexto)

    
def factura_nueva(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            
            form.save()
        return redirect('Factura_index') 
    else:
        form = FacturaForm()
    return render(request, 'gestionadmin/formfactura.html', {'form':form})

def factura_edit(request, id_exp):
    exp = Factura.objects.get(Id_Factura=id_exp)
    if request.method == 'GET':
        
        form = FacturaForm(instance=exp)
    else:
        form = FacturaForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Factura_index') 
    return render(request, 'gestionadmin/formfactura.html', {'form':form})

def factura_delete(request, id_exp):
    exp = Factura.objects.get(Id_Factura=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Factura_index') 
    return render(request, 'gestionadmin/formfactura.html', {'form':exp})    




######### Proveedor ###########
def proveedor_index(request):
    listaE = Proveedor.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexproveedor.html', contexto)

    
def proveedor_nueva(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Proveedor_index') 
    else:
        form = ProveedorForm()
    return render(request, 'gestionadmin/formproveedor.html', {'form':form})

def proveedor_edit(request, id_exp):
    exp = Proveedor.objects.get(Id_Proveedor=id_exp)
    if request.method == 'GET':
        
        form = ProveedorForm(instance=exp)
    else:
        form = ProveedorForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('Proveedor_index')
        else:
            return render(request, 'gestionadmin/formproveedor.html', {'form':form}) 
    return render(request, 'gestionadmin/formproveedor.html', {'form':form})

def proveedor_delete(request, id_exp):
    exp = Proveedor.objects.get(Id_Proveedor=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Proveedor_index') 
    return render(request, 'gestionadmin/formproveedor.html', {'form':exp})    


######### Producto ###########
def producto_index(request):
    listaE = Producto.objects.all()
    contexto = {'lista': listaE}
    return render(request, 'gestionadmin/indexproducto.html', contexto)

    
def producto_nueva(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Producto_index') 
    else:
        form = ProductoForm()
    return render(request, 'gestionadmin/formproducto.html', {'form':form})

def producto_edit(request, id_exp):
    exp = Producto.objects.get(Id_Producto=id_exp)
    if request.method == 'GET':
        
        form = ProductoForm(instance=exp)
    else:
        form = ProductoForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('Producto_index') 
    return render(request, 'gestionadmin/formproducto.html', {'form':form})

def producto_delete(request, id_exp):
    exp = Producto.objects.get(Id_Producto=id_exp)
    if request.method == 'POST':
        exp.delete()
        return redirect('Producto_index') 
    return render(request, 'gestionadmin/formproducto.html', {'form':exp}) 

############################################################################
class ComprasView(generic.ListView):
    model = ComprasEnc
    template_name = "gestionadmin/index_compras.html"
    context_object_name = "obj"

def compras(request,compra_id=None):
    template_name="gestionadmin/compras.html"
    prod=Producto.objects.filter(estado=True)
    form_compras={}
    contexto={}

    if request.method=='GET':
        form_compras=ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e = {
                'cliente': enc.cliente,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total':enc.total
            }
            form_compras = ComprasEncForm(e)
        else:
            det=None
        
        contexto={'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_compras}

    if request.method=='POST':
        observacion = request.POST.get("observacion")
        no_factura = request.POST.get("no_factura")
        fecha_factura = request.POST.get("fecha_factura")
        cliente = request.POST.get("cliente")
        sub_total = 0
        descuento = 0
        total = 0

        if not compra_id:
            clie=Cliente.objects.get(Id_Cliente=cliente)

            enc = ComprasEnc(
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                cliente=clie,

            )
            if enc:
                enc.save()
                compra_id=enc.id
        else:
            enc=ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                enc.observacion = observacion
                enc.no_factura=no_factura
                enc.fecha_factura=fecha_factura
                enc.save()

        if not compra_id:
            return redirect("compras_list")
        
        producto = request.POST.get("id_id_producto")
        cantidad = request.POST.get("id_cantidad_detalle")
        precio = request.POST.get("id_precio_detalle")
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        descuento_detalle  = request.POST.get("id_descuento_detalle")
        total_detalle  = request.POST.get("id_total_detalle")

        prod = Producto.objects.get(Id_Producto=producto)

        det = ComprasDet(
            compra=enc,
            producto=prod,
            cantidad=cantidad,
            precio_prv=precio,
            descuento=descuento_detalle,
            costo=0,
        )

        if det:
            det.save()

            sub_total=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento=descuento["descuento__sum"]
            enc.save()

        return redirect("compras_edit",compra_id=compra_id)



    return render(request, template_name, contexto)

class CompraDetDelete(generic.DeleteView):
    model = ComprasDet
    template_name = "gestionadmin/compras_det_del.html"
    context_object_name = 'obj'
    
    def get_success_url(self):
          compra_id=self.kwargs['compra_id']
          return reverse_lazy('compras_edit', kwargs={'compra_id': compra_id})

          import logging
def some_view(request):
    logging.error('something')