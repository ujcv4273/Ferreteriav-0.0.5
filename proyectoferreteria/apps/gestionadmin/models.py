from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models.functions import Concat
import datetime
from django.core.paginator import Paginator
import logging
import logging.config  # needed when logging_config doesn't start with logging.config
from copy import copy
from django.db import models

from django.core import mail
from django.core.mail import get_connection
from django.core.management.color import color_style
from django.utils.module_loading import import_string
from django.views.debug import ExceptionReporter

# para signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from django.conf import settings
now= datetime.datetime.now()
# Create your models here.
from django.core.exceptions import ValidationError


"""Validaciones"""
def validar_mayor_a_tres(value):
    if value<3:
        raise ValidationError('Número debe ser mayor que 2')

def validarquenoseacero(value):
    if(value)<1:
         raise ValidationError('Número debe ser mayor que 1')
    if(value)>200000:
         raise ValidationError('Número no debe ser mayor que 200,000')

def validarsueldo(value):
    if value<1000:
        raise ValidationError('Sueldo inválido debe ser mayor a 999')
    if value>200000:
        raise ValidationError('Sueldo inválido debe ser menor a 200000')

def validarhora(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if(lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·" ):
             raise ValidationError('Solo se permite ingresar números')
        n=n+1
    
    if lista[2]!=":":
        raise ValidationError('Hora inválida el formato es por ejemplo: 12:45')
    if not (len(value)) > 4:
        raise ValidationError('Hora incorrecta el formato es por ejemplo: 12:45')
    if lista[0]=="3" or lista[0]=="4" or lista[0]=="5" or lista[0]=="6" or lista[0]=="7" or lista[0]=="8" or lista[0]=="9":
        raise ValidationError('Hora incorrecta el formato es por ejemplo: 12:45')
    if lista[3]=="6" or lista[3]=="7" or lista[3]=="8" or lista[3]=="9":
        raise ValidationError('Hora incorrecta el formato es por ejemplo: 12:45')
    if (lista[0]=="2" and lista[1]=="4") or (lista[0]=="2" and lista[1]=="5") or (lista[0]=="2" and lista[1]=="6") or (lista[0]=="2" and lista[1]=="7") or (lista[0]=="2" and lista[1]=="8") or (lista[0]=="2" and lista[1]=="9"):
        raise ValidationError('Hora incorrecta el formato es por ejemplo: 12:45')

def validarnombre(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if(lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·"or lista[n]=="'"or lista[n]==";"or lista[n]=="'" or lista[n]=="\\" or lista[n]=="+" or lista[n]=="-"or lista[n]=="¡" ):
             raise ValidationError('Nombre incorrecto, solo se permite ingresar letras')
        n=n+1
    
    
    if (len(lista))<3:
        raise ValidationError('El texto es inválido debe ser mayor a 3 caracteres, digite de nuevo')
    
    if lista[0]=="a" and lista [1]=="b" and lista[2]=="c":
        raise ValidationError('El texto debe ser válido digite de nuevo')


    lista=[]
    vocal=["a","e","i","o","u","á","é","í","ó","ú"]
    cont=0
    for i in vocal:
        for j in value:
            if(i==j):
                cont+=1
    if(cont<1):
     raise ValidationError('El texto es inválido, digite de nuevo')   
    
def validardireccion(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if(lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]=="" or lista[n]=="#" or lista[n]=="$" or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·" ):
            raise ValidationError('Nombre incorrecto, solo se permite ingresar letras')
        n=n+1
    
    if(len(lista)<30):
        raise ValidationError('La dirección debe contener al menos 30 caracteres')
    if lista[0]=="a" and lista [1]=="b" and lista[2]=="c":
        raise ValidationError('La dirección debe ser válida digite de nuevo debe contener al menos 1 vocal')

    if lista[0]=="." or lista[0]==",":
       raise ValidationError('La dirección no puede contener un punto al inicio')
    
    lista=[]
    vocal=["a","e","i","o","u","á","é","í","ó","ú"]
    cont=0
    for i in vocal:
        for j in value:
            if(i==j):
                cont+=1
    if(cont<1):
     raise ValidationError('El texto es inválido, debe contener vocales digite de nuevo')   
def validarnumero(value):
    numeros=[]
    n=0
    for indice in value:
        numeros.append(indice)
        if(numeros[n]!="0" and numeros[n]!="1" and numeros[n]!="2" and numeros[n]!="3" and numeros[n]!="4" and numeros[n]!="5" and numeros[n]!="6" and numeros[n]!="7" and numeros[n]!="8" and numeros[n]!="9"):
            raise ValidationError('El número no puede contener letras')
        n=n+1
        
    if ((numeros[0]=="0") or (numeros[0]=="1") or (numeros[0]=="4") or (numeros[0]=="5") or (numeros[0]=="6")):
        raise ValidationError('El número no es válido, intente de nuevo')
    if(len(numeros))<8:
        raise ValidationError('El número debe contener al menos 8 dígitos, intente de nuevo')
    if("-" in numeros or ("." in numeros)):
        raise ValidationError('El número debe contener al menos 8 dígitos, ejemplo 99234567')

def validartamaño(value):
    if  value<1:
        raise ValidationError('El número no puede ser menor a 0')
    if  value>999999999:
        raise ValidationError('El número no puede ser mayor a 9 dígitos')

def validarnegativos(value):
    if value<=0:
        raise ValidationError('El número no puede ser menor que 0')
    if value>1000000000:
        raise ValidationError('El número no puede ser superior a 1000000000')

def validarcorreoexistenteProveedor(value):
    listaE = Proveedor.objects.all()
    for data in listaE:
        if(data.Correo_Proveedor==value):
            raise ValidationError('El correo ya existe')

def validarcorreoexistenteCliente(value):
    listaE = Cliente.objects.all()
    for data in listaE:
        if(data.Correo_Cliente==value):
            raise ValidationError('El correo ya existe')

def validartiempogarantia(value):
    if value<0:
        raise ValidationError('El número no puede ser menor que 0')
    if value>24:
        raise ValidationError('El número no puede ser superior a 24')

def validarCAIySAR(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if(lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·"or lista[n]=="<"or lista[n]==">"or lista[n]=="|"or lista[n]=="&" ):
             raise ValidationError('Número incorrecto, solo se permite ingresar numeros, letras y guiones')
        n=n+1

def validarsar(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if(lista[n]=="a" or lista[n]=="b" or lista[n]=="c" or lista[n]=="d" or lista[n]=="e" or lista[n]=="f" or lista[n]=="g" or lista[n]=="h" or lista[n]=="i" or lista[n]=="j" or lista[n]=="k" or lista[n]=="l" or lista[n]=="m" or lista[n]=="n" or lista[n]=="o" or lista[n]=="p" or lista[n]=="q" or lista[n]=="r" or lista[n]=="s" or lista[n]=="t" or lista[n]=="u" or lista[n]=="v" or lista[n]=="w" or lista[n]=="x" or lista[n]=="y" or lista[n]=="z" or lista[n]=="A" or lista[n]=="B" or lista[n]=="C" or lista[n]=="D" or lista[n]=="E" or lista[n]=="F" or lista[n]=="G" or lista[n]=="H" or lista[n]=="I" or lista[n]=="J" or lista[n]=="K" or lista[n]=="L" or lista[n]=="M" or lista[n]=="N" or lista[n]=="O" or lista[n]=="P" or lista[n]=="Q" or lista[n]=="R" or lista[n]=="S" or lista[n]=="T" or lista[n]=="U" or lista[n]=="V" or lista[n]=="W" or lista[n]=="X" or lista[n]=="Y" or lista[n]=="Z"  ):
            raise ValidationError ('Solo se pueden ingresar números')
        n=n+1
def validaridentidad(value):
    lista=[]
    n=0
    for indice in value:
        lista.append(indice)
        if  (lista[n]=='-' or lista[n]=="a" or lista[n]=="b" or lista[n]=="c" or lista[n]=="d" or lista[n]=="e" or lista[n]=="f" or lista[n]=="g" or lista[n]=="h" or lista[n]=="i" or lista[n]=="j" or lista[n]=="k" or lista[n]=="l" or lista[n]=="m" or lista[n]=="n" or lista[n]=="o" or lista[n]=="p" or lista[n]=="q" or lista[n]=="r" or lista[n]=="s" or lista[n]=="t" or lista[n]=="u" or lista[n]=="v" or lista[n]=="w" or lista[n]=="x" or lista[n]=="y" or lista[n]=="z" or lista[n]=="A" or lista[n]=="B" or lista[n]=="C" or lista[n]=="D" or lista[n]=="E" or lista[n]=="F" or lista[n]=="G" or lista[n]=="H" or lista[n]=="I" or lista[n]=="J" or lista[n]=="K" or lista[n]=="L" or lista[n]=="M" or lista[n]=="N" or lista[n]=="O" or lista[n]=="P" or lista[n]=="Q" or lista[n]=="R" or lista[n]=="S" or lista[n]=="T" or lista[n]=="U" or lista[n]=="V" or lista[n]=="W" or lista[n]=="X" or lista[n]=="Y" or lista[n]=="Z" or lista[n]=="@" or lista[n]=="º" or lista[n]=="!" or lista[n]==""or lista[n]=="#"or lista[n]=="$"or lista[n]=="~"or lista[n]=="%" or lista[n]=="&" or lista[n]=="¬" or lista[n]=="/" or lista[n]=="("or lista[n]==")" or lista[n]=="=" or lista[n]=="?" or lista[n]=="¿" or lista[n]=="^" or lista[n]=="" or lista[n]=="Ç" or lista[n]=="¨" or lista[n]==";"or lista[n]==":" or lista[n]=="_" or lista[n]=="["or lista[n]=="]"or lista[n]=="{"or lista[n]=="}"or lista[n]=="·"or lista[n]=="<"or lista[n]==">"or lista[n]=="|"or lista[n]=="&"):
            raise ValidationError ('Solo se pueden ingresar números')
        n=n+1
    if (lista[0]=="2" or lista[0]=="3" or lista[0]=="4" or lista[0]=="5" or lista[0]=="6" or lista[0]=="7" or lista[0]=="8" or lista[0]=="9"):
        raise ValidationError ('La identidad debe comenzar con 0 ó 1')
    if (lista[0]=="1" and lista[1]=="9"):
        raise ValidationError ('La identidad no puese pasar de 19')
    if (lista[4]=="0" or lista[4]=="3" or lista[4]=="4" or lista[4]=="5" or lista[4]=="6" or lista[4]=="7" or lista[4]=="8" or lista[4]=="9"):
        raise ValidationError ('El año no puedo ser mayor de 2002')
    if (lista[5]=="1" or lista[5]=="2" or lista[5]=="3" or lista[5]=="4" or lista[5]=="5" or lista[5]=="6" or lista[5]=="7" or lista[5]=="8" ):
        raise ValidationError ('El año no puede ser menor de 1920')
    if (lista[4]=="1" and lista[5]=="9"):
        if (lista[6]=="0" or lista[6]=="1" ):
            raise ValidationError ('El año no puedo ser menor de 1920')
    if  (lista[4]=="2" and lista[5]=="0"):
        if (lista[6]=="1" or lista[6]=="2" or lista[6]=="3" or lista[6]=="4" or lista[6]=="5" or lista[6]=="6" or lista[6]=="7"  or lista[6]=="8" or lista[6]=="9" ):
            raise ValidationError ('El año maximo debera ser 2002')
    if  (lista[4]=="2" and lista[5]=="0" and lista[6]=="0" ):
        if (lista[7]=="3" or lista[7]=="4" or lista[7]=="5" or lista[7]=="6" or lista[7]=="7" or lista[7]=="8" or lista[7]=="9"):
            raise ValidationError ('El año maximo debera ser 2002')

    if(len(lista)<13):
        raise ValidationError('La identidad debe contener 13 números')

def validate_decimals(value):
       try:
           return round(float(value), 2)
       except:
           raise ValidationError(
               _('%(value) no es un numero entero es un decimal'),
               params={'value': value},
           )    

"""Clases"""


class Marca (models.Model):
    idMarca=models.AutoField(verbose_name='Id', primary_key=True, validators=[validartamaño])
    nombreMarca= models.CharField(verbose_name='Descripción', max_length=30, unique=True, validators=[validarnombre])
    def __str__(self):
        return '{}'.format(self.nombreMarca)


    
    
"""1.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
2.-Se agrego el models.Autofield para que sea autoincremental"""
class Categoria (models.Model):
    Id_Categoria=models.AutoField(verbose_name='Id', primary_key=True, validators=[validartamaño])
    Descripcion_Categoria=models.CharField(verbose_name='Descripción',unique=True ,max_length=30,validators=[validarnombre])

    def __str__(self):
        return '{}'.format(self.Descripcion_Categoria)
    

"""5.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
6.-Se agrego el models.Autofield para que sea autoincremental"""
class Proveedor (models.Model):
    Id_Proveedor = models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Nombre_Proveedor=models.CharField(verbose_name='Nombre',max_length=35,unique=True, validators=[validarnombre])
    Correo_Proveedor=models.EmailField(verbose_name='Correo',max_length=30,null=True,blank=True,unique=True)
    Direccion_Proveedor=models.TextField(verbose_name='Dirección',max_length=100, validators=[validardireccion])
    Telefono_Proveedor=models.CharField(verbose_name='Teléfono',max_length=8, validators=[validarnumero])
     
    def __str__(self):
        return '{}'.format(str(self.Id_Proveedor)+" "+self.Nombre_Proveedor)
    class Meta:
        verbose_name_plural="Proveedores"
"""3.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
4.-Se agrego el models.Autofield para que sea autoincremental"""
class Garantia (models.Model):
    Id_Garantia = models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Descripcion_Garantia=models.TextField(verbose_name='Descripción',max_length=50,unique=True,validators=[validarnombre])
    Tiempo_Garantia_Mes=models.IntegerField(verbose_name='Tiempo garantía por mes', validators=[validartiempogarantia])

    def __str__(self):
        return '{}'.format(self.Descripcion_Garantia)

"""7.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
8.-Se agrego el models.Autofield para que sea autoincremental"""
class FormaPago(models.Model):
    Id_Forma_Pago=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Descripcion_Forma_Pago=models.TextField(verbose_name='  Descripcion',max_length=30,unique=True,validators=[validarnombre])
    def __str__(self):
        return '{}'.format(str(self.Id_Forma_Pago)+" "+self.Descripcion_Forma_Pago)

"""10.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
11.-Se agrego el models.Autofield para que sea autoincremental
26.- no se aplicaron los cambios anteriores porque explotaba"""
class MetodoPago(models.Model):
    idMetodoPago=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    descripcionMetodoPago=models.TextField(verbose_name='Descripción',max_length=30,unique=True, validators=[validarnombre])
    def __str__(self):
        return '{}'.format(str(self.idMetodoPago)+" "+self.descripcionMetodoPago)

"""12.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
13.-Se agrego el models.Autofield para que sea autoincremental"""
class Cliente(models.Model):
    Id_Cliente=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Identidad=models.CharField(verbose_name='Identidad', max_length=13, validators=[validaridentidad], unique=True)
    Nombre_Cliente=models.CharField(verbose_name='Nombre',max_length=30, validators=[validarnombre])
    Correo_Cliente=models.EmailField(verbose_name='Correo',max_length=30,null=True,blank=True,unique=True)
    Direccion_Cliente=models.TextField(verbose_name='Dirección',max_length=100, validators=[validardireccion])
    Telefono_Cliente=models.CharField(verbose_name='Teléfono',max_length=8, validators=[validarnumero], unique=True)
    
    def __str__(self):
        return '{}'.format(self.Nombre_Cliente)
    

"""14.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
15.-Se agrego el models.Autofield para que sea autoincremental"""
class TurnoEmpleado(models.Model):
    MAT='Matutino'
    VESP='Vespertino'
    NOC='Nocturno'
    MIX='Mixto'
    ESP='Especial'
    TURNO = [
        (MAT,'Matutino'),
        (VESP,'Vespertino'),
        (NOC,'Nocturno'),
        (MIX,'Mixto'),
        (ESP,'Especial')
    ]
    Id_Turno=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Turno=models.CharField(verbose_name='Turno',max_length=30,unique=True,choices=TURNO, default=MAT, validators=[validarnombre])
    Hora_de_Entrada=models.CharField(verbose_name='Hora entrada',max_length=5,default='17:40', validators=[validarhora])
    Hora_de_Salida=models.CharField(verbose_name='Hora salida',max_length=5,default='23:40', validators=[validarhora])
    def __str__(self):
        return '{}'.format(str(self.Id_Turno)+" "+self.Turno)


"""9.-Se valido que el IHSS y el RAP no fueran numeros negativos"""
"""16.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
17.-Se agrego el models.Autofield para que sea autoincremental
18.-Se elimino el sueldo base de la impresion porque creaba un error que hay que resolver"""
class Planilla(models.Model):
    Id_Planilla=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Sueldo_Base=models.DecimalField(verbose_name='Sueldo Base', max_digits=10, decimal_places=2, validators=[validarnegativos])
    IHSS=models.DecimalField(verbose_name='IHSS',max_digits=10, decimal_places=2,validators=[validarnegativos])
    RAP=models.DecimalField(verbose_name='RAP',max_digits=10, decimal_places=2,validators=[validarnegativos])

    def __str__(self):
        return '{}'.format(str(self.Id_Planilla)+" "+str(self.Sueldo_Base))

"""18.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
19.-Se agrego el models.Autofield para que sea autoincremental"""
class Empleado(models.Model):
    Id_Empleado=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Id_Turno=models.ForeignKey(TurnoEmpleado, verbose_name='Turno', null=False, blank=False, on_delete=models.PROTECT)
    Id_Planilla=models.ForeignKey(Planilla, verbose_name='Planilla', null=False, blank=False, on_delete=models.PROTECT)
    Nombre_Empleado=models.CharField(verbose_name='Nombre',max_length=30,validators=[validarnombre])
    Direccion_Empleado=models.TextField(verbose_name='Dirección',max_length=100, validators=[validardireccion])
    Telefono_Empleado=models.CharField(verbose_name='Teléfono',max_length=8, validators=[validarnumero])
    def __str__(self):
        return '{}'.format(self.Nombre_Empleado)


"""20.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
21.-Se agrego el models.Autofield para que sea autoincremental"""
class Producto(models.Model):
    Id_Producto=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Nombre_Producto=models.CharField(verbose_name='Nombre',max_length=40,unique=True, validators=[validarnombre])
    Precio_Venta=models.FloatField(verbose_name='Precio Venta',validators=[validarquenoseacero])
    Precio_Compra=models.FloatField(verbose_name='Precio Compra',validators=[validarquenoseacero])
    Id_Marca=models.ForeignKey(Marca,verbose_name='Marca', null=False, blank=False, on_delete=models.PROTECT)
    Id_Categoria=models.ForeignKey(Categoria, verbose_name='Categoría', null=False, blank=False, on_delete=models.PROTECT)
    Id_Garantia=models.ForeignKey(Garantia,verbose_name='Garantía', null=False, blank=False, on_delete=models.PROTECT)
    Existencia=models.IntegerField(verbose_name='Existencia',validators=[validarquenoseacero])
    Existencia_Minima=models.IntegerField(verbose_name='Existencia Mínima',validators=[validar_mayor_a_tres])
    estado=models.BooleanField(default=True)
    def __str__(self):
        return '{}'.format(self.Nombre_Producto)

"""22.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
23.-Se agrego el models.Autofield para que sea autoincremental"""
class Factura(models.Model):
    Id_Factura=models.AutoField(verbose_name='Id de factura',primary_key=True, validators=[validartamaño])
    Id_Empleado=models.ForeignKey(User, verbose_name='Empleado', null=False, blank=False, on_delete=models.PROTECT)
    Id_Cliente=models.ForeignKey(Cliente, verbose_name='Cliente', null=True, blank=True, on_delete=models.PROTECT)
    Id_MetodoPago=models.ForeignKey(MetodoPago, verbose_name='Método de pago',null=False, blank=False, on_delete=models.PROTECT)
    Id_FormaPago=models.ForeignKey(FormaPago, verbose_name='Forma de Pago',null=False, blank=False, on_delete=models.PROTECT)
    Numero_Sar=models.CharField(verbose_name='Número de la SAR',max_length=15, default='004-340-34523', validators=[validarCAIySAR, validarsar])
    #Para presentarse no puede ser ManyToManyField
    Id_producto=models.ManyToManyField(Producto, verbose_name='Producto')
    Fecha=models.DateTimeField(auto_now_add=True)
    Codigo_CAI=models.CharField(max_length=36, verbose_name='Código CAI',  default='114-560-345KJ')
    ISV18=models.FloatField(validators=[validarnegativos], verbose_name='ISV al 18%')
    ISV15=models.FloatField(validators=[validarnegativos], verbose_name='ISV al 15%')
    Total_Factura=models.FloatField(validators=[validarnegativos],verbose_name='Total')
    def __str__(self):
        return '{}'.format(str(self.Id_Factura)+" "+str(self.Id_Empleado))


class ComprasEnc(models.Model):

    no_factura=models.CharField(max_length=100, default='056-052-68753')
    fecha_factura=models.DateField(null=True,blank=True, default='2020-07-18')
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    estado=models.BooleanField(default=True)

    cliente=models.ForeignKey(Cliente,on_delete=models.PROTECT)
    def __str__(self):
        return '{}'.format(self.no_factura)

    def save(self):
        self.total = self.sub_total + self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"

class ComprasDet(models.Model):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.PROTECT)
    producto=models.ForeignKey(Producto,on_delete=models.PROTECT)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = (self.sub_total) + float(self.descuento)
        super(ComprasDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Compras"
        verbose_name="Detalle Compra"


 
"""24.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
25.-Se agrego el models.Autofield para que sea autoincremental"""
#class FacturaDetalle(models.Model):
#    Id_Factura_Detalle = models.AutoField(primary_key=True, validators=[validartamaño])
#    Id_Factura = models.OneToOneField(Factura, on_delete=models.PROTECT)
#    Id_Producto=models.ForeignKey(Producto, null=False, blank=False, on_delete=models.PROTECT)
#    Cantidad = models.IntegerField(validators=[validarquenoseacero])
#
#    def __str__(self):
#        return '{}'.format(" "+str(self.Id_Factura_Detalle)+" "+""+str(self.Id_Factura))

@receiver(post_delete, sender=ComprasDet)
def detalle_compra_borrar(sender,instance, **kwargs):
    id_producto = instance.producto.Id_Producto
    id_compra = instance.compra.id

    enc = ComprasEnc.objects.filter(pk=id_compra).first()
    if enc:
        sub_total = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('sub_total'))
        descuento = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        enc.sub_total=sub_total['sub_total__sum']
        enc.descuento=descuento['descuento__sum']
        enc.save()
    
    prod=Producto.objects.filter(Id_Producto=id_producto).first()
    if prod:
        cantidad = int(prod.Existencia) + int(instance.cantidad)
        prod.Existencia = cantidad
        prod.save()


@receiver(post_save, sender=ComprasDet)
def detalle_compra_guardar(sender,instance,**kwargs):
    id_producto = instance.producto.Id_Producto

    prod=Producto.objects.filter(Id_Producto=id_producto).first()
    if prod:
        cantidad = int(prod.Existencia) - int(instance.cantidad)
        prod.Existencia = cantidad
        prod.save()









    
    



