# La clase base de las clases modelos
# los modelos o clases modelo son las clases que mapean a las tablas
from orm.config import BaseClass
# Importar de SQLALchemy los tipos de datos que usan las columnas de las tablas
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
# Para que calcular la hora actual
import datetime

# Por convención las clases tienen nombres en singular y comienzan con mayúsculas
class Alumno(BaseClass):
    __tablename__="alumnos" # Nombre de la tabla en la BD
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column("email",String(100))
    password=Column(String(100))
    fecha_registro=Column(DateTime(timezone=True),default=datetime.datetime.now)

class Calificacion(BaseClass):
    __tablename__="calificaciones"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    uea=Column(String(100))
    calificacion=Column(String(100))

class Foto(BaseClass):
    __tablename__="fotos"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(50))