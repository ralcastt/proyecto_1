from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader




def saludar(request):
    return HttpResponse("hola mundo!") 

def segundaVista(request):
    return HttpResponse("<h1> Segunda Vista! </h1>")

def saludo_con_nombre(request, nombre):
    documento=f"<h1> hola {nombre}</h1>"
    return HttpResponse()    


def calcula_anio_nacimiento(request, edad):
    anio_actual= datetime.datetime.today().year
    anio_nacimiento=anio_actual-int(edad)
    return HttpResponse(f"Usted nacio en el anio {anio_nacimiento}")    



#def probandoHtml(request):

        #diccionario={"nombre":"Rafael" ,"apellido":"Castillo", "edad": 34,"lista_de_notas":[1,9,5,4,7,8,2] }

        #archivo= open(r"D:\Curso de Python\tercera entrega\proyecto1\plantillas\template1.html")
        #contenido= archivo.read()
        #archivo.close()
        #template= Template(contenido)
        #contexto= Context(diccionario)
        #documento= template.render(contexto)
        #return HttpResponse(documento)


def probandoHtml(request):
    diccionario= {"nombre":"Rafael" ,"apellido":"Castillo", "edad": 34,"lista_de_notas":[1,9,5,4,7,8,2] }
    template= loader.get_template("template1.html")   
    documento= template.render(diccionario)
    return HttpResponse(documento)     

        
