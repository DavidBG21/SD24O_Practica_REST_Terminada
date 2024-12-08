import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ------------ Peticiones de la práctica ---------------------

# GET '/alumnos'
# select * from app.alumnos
def devuelve_alumnos(sesion:Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

# GET '/alumnos/{id}'
# select * from app.alumnos where id = id_alumno
def alumno_por_id(sesion:Session,id_alumno:int):
    print("select * from app.alumnos where id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()

# GET '/fotos'
# select * from app.fotos
def devuelve_fotos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

# GET '/fotos/{id}'
# select * from app.fotos where id = id_foto
def foto_por_id(sesion:Session,id_foto:int):
    print("select * from fotos where id = id_foto")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

# GET '/alumnos/{id}/fotos'
# select * from app.fotos where id_alumno=id
def fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.fotos where id_alumno=", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all() 

# GET '/calificaciones'
# select * from app.calificaciones
def devuelve_calificaciones(sesion:Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

# GET '/calificaciones/{id}'
# select * from app.calificaciones where id = id_calificacion
def calificacion_por_id(sesion:Session,id_calificacion:int):
    print("select * from calificaciones where id = id_calificacion")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first()

# select * from app.calificaciones where id_alumno=id
def calificaciones_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.calificaciones where id_alumno=", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).all() 

# DELETE '/alumnos/{id}'
# delete from app.alumnos where id=id_alumno
def borra_alumno_por_id(sesion:Session,id_alumno:int):
    print("delete from app.alumnos where id=", id_alumno)
    #1.- select para ver si existe el alumno a borrar
    usr = alumno_por_id(sesion, id_alumno)
    #2.- Borramos
    if usr is not None:
        #Borramos alumno
        sesion.delete(usr)
        #Confirmar los cambios
        sesion.commit()
        #print(f"SIMULANDO QUE SE BORRÓ EL ALUMNO CON ID {id_alumno}")
    respuesta = {
        "mensaje": "alumno eliminado"
    }
    return respuesta

# DELETE '/alumnos/{id}/calificaciones'
# delete from app.calificaciones where id_alumno=id
def borrar_calificaciones_por_id_alumno(sesion:Session,id_alumno:int):
    print("delete from app.calificaciones where id_alumno=",id_alumno)
    calif_alu = calificaciones_por_id_alumno(sesion, id_alumno)
    if calif_alu is not None:
        for calificacion_alumno in calif_alu:
            sesion.delete(calificacion_alumno)
            #print(f"SIMULANDO QUE SE BORRÓ LA CALIFICACIÓN CON ID {id_alumno}")
        sesion.commit()
        #print(f"SIMULANDO QUE SE BORRARON TODAS LAS CALIFICACIONES DEL ALUMNO")

# DELETE '/alumnos/{id}/fotos'
# delete from app.fotos where id_alumno=id
def borrar_fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("delete from app.fotos where id_alumno=",id_alumno)
    fotos_alu = fotos_por_id_alumno(sesion, id_alumno)
    if fotos_alu is not None:
        for foto_alumno in fotos_alu:
            sesion.delete(foto_alumno)
            #print(f"SIMULANDO QUE SE BORRÓ LA FOTO CON ID {id_alumno}")
        sesion.commit()
        #print(f"SIMULANDO QUE SE BORRARON TODAS LAS FOTOS DEL ALUMNO")

# NO ESPECIFICA QUE SE IMPLEMENTE ESTAS CONSULTAS, PERO SE TIENEN QUE ATENDER LAS SIGUIENTES TAMBIÉN...
# Y DEBIDO A QUE SON DE ID ÚNICO, SE PUEDEN BORRAR SIN NECESIDAD DE ITERAR

# DELETE '/fotos/{id}'
# delete from app.fotos where id=id_foto
def borrar_foto_por_id(sesion:Session,id_foto:int):
    print("delete from app.fotos where id=", id_foto)
    usr = foto_por_id(sesion, id_foto)
    if usr is not None:
        sesion.delete(usr)
        sesion.commit()
        #print("FOTO CON ID UNICO BORRADO\n\n")
    respuesta = {
        "mensaje": "foto eliminada"
    }
    return respuesta

# DELETE '/calificaciones/{id}'
# delete from app.calificaciones where id=id_calif
def borrar_calificacion_por_id(sesion:Session,id_calif:int):
    print("delete from app.calificaciones where id=", id_calif)
    usr = calificacion_por_id(sesion, id_calif)
    if usr is not None:
        sesion.delete(usr)
        sesion.commit()
        #print("CALIFICAION CON ID UNICO BORRADA\n\n")
    respuesta = {
        "mensaje": "calificaion eliminada"
    }
    return respuesta

# GET '/calificaciones?id_alumno={id_alum}&calificacion={calif}'
# select * from app.calificaciones where id_alumno=id_alum and calificacion>=calif
#def devuelve_calificaciones_por_alumno_calificacion(sesion:Session, id_alum:int, calif:str):
#    print("select * from app.calificaciones where id_alumno=id_alum and calificacion=calif")
#    return sesion.query(modelos.Calificacion).filter(and_(modelos.Calificacion.id_alumno==id_alum, modelos.Calificacion.calificacion==calif)).all()