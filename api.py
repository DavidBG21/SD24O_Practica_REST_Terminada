from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones

# creación del servidor
app = FastAPI()

#definición de la base del alumno
class UsuarioBase(BaseModel):
    nombre:Optional[str]=None
    edad:int
    domicilio:str    
    
alumnos = [{
    "id": 0,
    "nombre": "Homero Simpson",
    "edad": 40,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 1,
    "nombre": "Marge Simpson",
    "edad": 38,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 2,
    "nombre": "Lisa Simpson",
    "edad": 8,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 3,
    "nombre": "Bart Simpson",
    "edad": 10,
    "domicilio": "Av. Simpre Viva"
}]

#   --- GET INICIAL --- #
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }
    return respuesta

"""
@app.get("/alumnos/{id}/calificaciones/{id_calificacion}")
def calificaciones_usuario_por_id(id: int, id_calificacion: int):
    print("buscando calificacion con id:", id_calificacion, " del alumno con id:", id)
    # simulamos la consulta
    calificacion = {
        "id_calificacion": 787,
        "uea": "WEB Dinamico",
        "calificacion": "MB"
    }
    return calificacion
"""
############## TODAS LAS CONSULTAS DE LA PRACTICA ##############

@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def fotos_por_id_alum(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones del alumno ", id)
    return repo.calificaciones_por_id_alumno(sesion, id)

@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alum(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos del alumno ", id)
    return repo.fotos_por_id_alumno(sesion, id)

@app.get("/fotos/{id}")
def foto_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando foto por id")
    return repo.foto_por_id(sesion,id)

@app.get("/calificaciones/{id}")
def calificacion_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando calificacion por id")
    return repo.calificacion_por_id(sesion, id)

@app.delete("/fotos/{id}")
def borrar_foto(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_foto_por_id(sesion,id) #REHUSANDO EL MÉTODO
    return {"foto_borrada", "ok"}

@app.delete("/calificaciones/{id}")
def borrar_calificacion(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificacion_por_id(sesion,id)
    return {"calificcion_borrada", "ok"}

@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    return {"calificaciones_de_alumno_borradas", "ok"}

@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion,id)
    return {"fotos_de_alumno_borradas", "ok"}

@app.delete("/alumnos/{id}")
def borrar_usuario(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    repo.borrar_fotos_por_id_alumno(sesion,id)
    repo.borra_alumno_por_id(sesion,id)
    return {"usuario_borrado", "ok"}

"""
######### REVISAR CON CUIDADO ##################################################
@app.post("/alumnos")
def guardar_usuario(alumno:UsuarioBase, parametro1:str):
    print("alumno a guardar:", alumno, ", parametro1:", parametro1)
    #simulamos guardado en la base.
    
    usr_nuevo = {}
    usr_nuevo["id"] = len(alumnos)
    usr_nuevo["nombre"] = alumno.nombre
    usr_nuevo["edad"] = alumno.edad
    usr_nuevo["domicilio"] = alumno.domicilio

    alumnos.append(alumno)

    return usr_nuevo

@app.put("/alumno/{id}")
def actualizar_usuario(id:int, alumno:UsuarioBase):
    #simulamos consulta
    usr_act = alumnos[id]
    #simulamos la actualización
    usr_act["nombre"] = alumno.nombre
    usr_act["edad"] = alumno.edad
    usr_act["domicilio"] = alumno.domicilio    

    return usr_act
    

################################################################################

## Peticiones de calificaciones
# "/calificaciones?id_alumno={id_usr}&calificacion={calif}"
@app.get("/calificaciones")
def lista_compras(id_alumno:int,calificacion:str,sesion:Session=Depends(generador_sesion)):
    print("/calificaciones?id_alumno={id_usr}&calificacion={calif}")
    return repo.devuelve_calificaciones_por_alumno_calificacion(sesion,id_alumno,calificacion)

@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todas las fotos")
    return repo.devuelve_fotos(sesion)

@app.post("/fotos")
async def guardar_foto(titulo:str=Form(None), descripcion:str=Form(...), foto:UploadFile=File(...)):
    print("titulo:", titulo)
    print("descripcion:", descripcion)

    home_usuario=os.path.expanduser("~")
    nombre_archivo=uuid.uuid4().hex  #generamos nombre único en formato hexadecimal
    extension = os.path.splitext(foto.filename)[1]
    ruta_imagen=f'{home_usuario}/fotos-ejemplo/{nombre_archivo}{extension}'
    print("guardando imagen en ruta:", ruta_imagen)

    with open(ruta_imagen,"wb") as imagen:
        contenido = await foto.read() #read funciona de manera asyncrona
        imagen.write(contenido)

    return {"titulo":titulo, "descripcion":descripcion, "foto":foto.filename}
"""