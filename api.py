from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones
import orm.esquemas as esquemas

# creación del servidor
app = FastAPI()

############## TODAS LAS CONSULTAS DE LA PRACTICA ##############

# GET '/alumnos'
# Cada print indica que tipo de acción atiende
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificacion_por_id_alum(id:int,sesion:Session=Depends(generador_sesion)):
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
    print("Borrando foto por id")
    repo.borrar_foto_por_id(sesion,id)
    return {"foto_borrada", "ok"}

@app.delete("/calificaciones/{id}")
def borrar_calificacion(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando calificacion por id")
    repo.borrar_calificacion_por_id(sesion,id)
    return {"calificcion_borrada", "ok"}

@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando calificaciones por id de alumno")
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    return {"calificaciones_de_alumno_borradas", "ok"}

@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando fotos por id de alumno")
    repo.borrar_fotos_por_id_alumno(sesion,id)
    return {"fotos_de_alumno_borradas", "ok"}

@app.delete("/alumnos/{id}")
def borrar_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Borrando alumno por id, junto a sus tablas relacionadas")
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    repo.borrar_fotos_por_id_alumno(sesion,id)
    repo.borra_alumno_por_id(sesion,id)
    return {"alumno_borrado", "ok"}


######################## PRACTICA PARTE 2 ########################

@app.post("/alumnos")
def guardar_alumno(alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    print("Insertando alumno")
    return repo.guardar_alumno(sesion,alumno)

@app.put("/alumnos/{id}")
def actualizar_alumno(id:int,info_alumno:esquemas.AlumnoBase,sesion:Session=Depends(generador_sesion)):
    print("Actualizando datos de alumno")
    return repo.actualiza_alumno(sesion,id,info_alumno)

@app.post("/alumnos/{id}/calificaciones")
def guardar_calificacion_alumno(id_alumno:int,calificacion:esquemas.CalificacionBase, sesion:Session=Depends(generador_sesion)):
    print("Insertando calificacion de alumno")
    return repo.guardar_calificacion_alumno(sesion,id_alumno,calificacion)

@app.put("/calificaciones/{id}")
def actualizar_calificacion(id:int,info_calif:esquemas.CalificacionBase,sesion:Session=Depends(generador_sesion)):
    print("Actualizando calificaciones de alumno")
    return repo.actualizar_calificacion(sesion,id,info_calif)

@app.post("/alumnos/{id}/fotos")
def guardar_foto_alumno(id_alumno:int,foto:esquemas.FotoBase, sesion:Session=Depends(generador_sesion)):
    print("Insertando foto de alumno")
    return repo.guardar_foto_alumno(sesion,id_alumno,foto)

@app.put("/fotos/{id}")
def actualizar_foto(id_foto:int,info_calif:esquemas.FotoBase,sesion:Session=Depends(generador_sesion)):
    print("Actualizando foto")
    return repo.actualizar_foto(sesion,id_foto,info_calif)