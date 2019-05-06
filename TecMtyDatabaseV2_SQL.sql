DROP DATABASE TecMtyDatabase

CREATE DATABASE TecMtyDatabase

USE TecMtyDatabase

CREATE TABLE Departamento
(
	ID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	numOficina INT,
	telefono VARCHAR(30),
	PRIMARY KEY(ID)
)


CREATE TABLE Carrera
(
	ID INT NOT NULL,
	departamentoID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	PRIMARY KEY(ID),
	FOREIGN KEY(departamentoID) REFERENCES Departamento(ID)
)

CREATE TABLE Curso
(
	ID INT NOT NULL,
	departamentoID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	hrsSemanal INT,
	planSemestre INT,
	descripcion VARCHAR(200),
	PRIMARY KEY(ID),
	FOREIGN KEY(departamentoID) REFERENCES Departamento(ID),
)



CREATE TABLE Grupo
(
	ID INT PRIMARY KEY REFERENCES Curso(ID) ON DELETE CASCADE,
	semestre INT NOT NULL,
	año INT NOT NULL,
	rECOA INT,
	numGrupo INT NOT NULL
)


CREATE TABLE Alumno
(
	matricula VARCHAR(15) NOT NULL,
	curp VARCHAR(20) NOT NULL UNIQUE,
	fName VARCHAR(15) NOT NULL,
	lName VARCHAR(15) NOT NULL,
	sex CHAR(1),
	DOB DATETIME,
	direccion VARCHAR(100),
	telefono VARCHAR(30),
	celular VARCHAR(30),
	carreraID INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)
)


CREATE TABLE CursoPorAlumno
(
	ID int IDENTITY(1,1) NOT NULL, --AUTO_INCREMENT,
	cursoID int not null,
	matriculaAlumno VARCHAR(15) NULL,
		FOREIGN key (matriculaAlumno) REFERENCES Alumno(matricula),
		PRIMARY key (ID),
		FOREIGN key (cursoID) REFERENCES Curso(ID)
)

CREATE TABLE Profesores
(
	matricula VARCHAR(15) NOT NULL,
	curp VARCHAR(20) NOT NULL UNIQUE,
	fName VARCHAR(15) NOT NULL,
	lName VARCHAR(15) NOT NULL,
	sex CHAR(1),
	DOB DATETIME,
	direccion VARCHAR(100),
	telefono VARCHAR(30),
	nomina INT,
	celular VARCHAR(30),
	carreraID INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)


)

CREATE TABLE HorasLibresProfesores
(
	ID  int IDENTITY(1,1) NOT NULL, --AUTO_INCREMENT,
	dia char(1) NOT NULL,
	hora INT NOT NULL,
	profesorMatricula VARCHAR(15) NOT NULL REFERENCES Profesores(matricula) ON DELETE CASCADE,
	PRIMARY KEY (ID)
)


INSERT INTO Departamento VALUES (1, 'Ingeniería', 101, '81-1234-5678')

INSERT INTO Departamento(ID, nombre, numOficina, telefono) VALUES (2, 'Ciencias Sociales', 101, '81-1234-1234')

INSERT INTO Departamento(ID, nombre, numOficina, telefono) VALUES (3, 'Economía', 101, '81-1234-1111')

INSERT INTO Carrera(ID, departamentoID, nombre) VALUES (101, 1, 'ITC')

INSERT INTO Carrera(ID, departamentoID, nombre) VALUES (102, 1, 'Mecatronica')

INSERT INTO Carrera(ID, departamentoID, nombre) VALUES (301, 3, 'LIN')

INSERT INTO Curso(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion) VALUES (1, 1, 'Matematicas para Ingeniería', 6, 3, 'Este curso es de mates para ingenieros en tercer semestre y dura 6 horas semanales.')

INSERT INTO Curso(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion) VALUES (2, 1, 'Física para Ingeniería', 8, 2, 'Este curso es de mates para ingenieros en segundo semestre y dura 8 horas semanales.')

INSERT INTO Curso(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion) VALUES (3, 3, 'Matematicas para Licenciados', 4, 1, 'Este curso es de mates para ingenieros en primer semestre y dura 4 horas semanales.')


