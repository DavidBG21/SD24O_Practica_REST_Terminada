/*TABLA DE alumnos*/
DROP TABLE IF EXISTS app.alumnos CASCADE;
CREATE TABLE app.alumnos(
	id SERIAL PRIMARY KEY, 
	nombre VARCHAR(100),	
	edad INTEGER,
    domicilio VARCHAR(100),
	carrera VARCHAR(100),
    trimestre VARCHAR(100),
	email VARCHAR(100) UNIQUE,
	password VARCHAR(100),	
	fecha_registro TIMESTAMP WITH TIME ZONE
);

INSERT INTO app.alumnos(nombre, edad, domicilio, carrera, trimestre, email,password, fecha_registro) VALUES('Rosa Gonzáles',36, 'Av. 102, 53','Ingeniería en Computación','24-O', 'rgonzalez@email.com','1234','2024-08-31T15:20:30+08:00');
INSERT INTO app.alumnos(nombre, edad, domicilio, carrera, trimestre, email,password, fecha_registro) VALUES('Irene Rojas',38, 'Calle 33, 10','Ingeniería en Computación', '24-I', 'irojas@email.com','1234','2024-08-31T15:20:30+08:00');
INSERT INTO app.alumnos(nombre, edad, domicilio, carrera, trimestre, email,password, fecha_registro) VALUES('Israel Ortíz',8, 'Av. Reforma, 122','Licenciatura en Matemáticas Aplicadas', '24-O', 'iortiz@email.com','1234','2024-08-31T15:20:30+08:00');
INSERT INTO app.alumnos(nombre, edad, domicilio, carrera, trimestre, email,password, fecha_registro) VALUES('Ximena Ramírez',10, 'Av. Constituyentes, 41','Licenciatura en Matemáticas Aplicadas','24-I', 'xramirez@email.com','1234','2024-08-31T15:20:30+08:00');

/*TABLA de calificaciones*/
DROP TABLE IF EXISTS app.calificaciones CASCADE;
CREATE TABLE app.calificaciones(
	id SERIAL PRIMARY KEY, 
	id_alumno INTEGER,
	uea VARCHAR(100),	
	calificacion VARCHAR(100),
	FOREIGN KEY(id_alumno) REFERENCES app.alumnos(id)	
);

INSERT INTO app.calificaciones(id_alumno,uea,calificacion) VALUES(1,'POO','B');
INSERT INTO app.calificaciones(id_alumno,uea,calificacion) VALUES(1,'Sistemas Distribuidos','B');
INSERT INTO app.calificaciones(id_alumno,uea,calificacion) VALUES(2,'POO','MB');
INSERT INTO app.calificaciones(id_alumno,uea,calificacion) VALUES(3,'Sistemas Distribuidos','MB');
INSERT INTO app.calificaciones(id_alumno,uea,calificacion) VALUES(4,'Programación Web','B');


/* tabla de fotos*/
DROP TABLE IF EXISTS app.fotos CASCADE;
CREATE TABLE app.fotos(
	id SERIAL PRIMARY KEY, 
    id_alumno INTEGER,
	titulo VARCHAR(100),
	descripcion VARCHAR(100),
	ruta VARCHAR,		
    FOREIGN KEY(id_alumno) REFERENCES app.alumnos(id)	
);
INSERT INTO app.fotos(id_alumno,titulo,descripcion,ruta) VALUES(1,'titulo 1','descripción 1','/home/servidor/fotos/sfd235fg.jpg');
INSERT INTO app.fotos(id_alumno,titulo,descripcion,ruta) VALUES(2,'titulo 2','descripción 2','/home/servidor/fotos/tsdfw23f.jpg');
INSERT INTO app.fotos(id_alumno,titulo,descripcion,ruta) VALUES(2,'titulo 3','descripción 3','/home/servidor/fotos/terwe324.jpg');
INSERT INTO app.fotos(id_alumno,titulo,descripcion,ruta) VALUES(3,'titulo 4','descripción 4','/home/servidor/fotos/sfw23425.jpg');
INSERT INTO app.fotos(id_alumno,titulo,descripcion,ruta) VALUES(4,'titulo 5','descripción 5','/home/servidor/fotos/2345sdr2.jpg');

