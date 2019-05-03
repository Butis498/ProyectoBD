
USE TecMtyDatabase;

CREATE TABLE Departamento
(
	ID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	numOficina INT,
	telefono INT,
	PRIMARY KEY(ID)
);


CREATE TABLE Carrera
(
	ID INT NOT NULL,
	departamentoID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	PRIMARY KEY(ID),
	FOREIGN KEY(departamentoID) REFERENCES Departamento(ID)
);

CREATE TABLE Curso
(
	ID INT NOT NULL,
	carreraID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	hrsSemanal INT,
	planSemestre INT,
	descripcion VARCHAR(200),
	PRIMARY KEY(ID),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID),
);



CREATE TABLE Grupo
(
	ID numeric PRIMARY KEY REFERENCES Curso(ID) ON DELETE CASCADE,
	semestre INT NOT NULL,
	año INT NOT NULL,
	rECOA INT,
	numGrupo INT NOT NULL
);


CREATE TABLE Alumno
(
	matricula VARCHAR(15) NOT NULL,
	curp VARCHAR(20) NOT NULL UNIQUE,
	fName VARCHAR(15) NOT NULL,
	lName VARCHAR(15) NOT NULL,
	sex CHAR(1),
	DOB DATETIME,
	direccion VARCHAR(100),
	telefono INT,
	celular INT,
	carreraID INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)
);


CREATE TABLE CursoPorAlumno
(
	ID int NOT NULL AUTO_INCREMENT,
	cursoID int not null,
	matriculaAlumno VARCHAR(9) NULL,
		FOREIGN key (matriculaAlumno) REFERENCES Alumno(matricula),
		PRIMARY key (ID),
		FOREIGN key (cursoID) REFERENCES Curso(ID)
);

CREATE TABLE Profesores
(
	matricula VARCHAR(15) NOT NULL,
	curp VARCHAR(20) NOT NULL UNIQUE,
	fName VARCHAR(15) NOT NULL,
	lName VARCHAR(15) NOT NULL,
	sex CHAR(1),
	DOB DATETIME,
	direccion VARCHAR(100),
	telefono INT,
	nomina INT,
	celular INT,
	carreraID INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)


);

CREATE TABLE HorasLibresProfesores
(
	ID  int NOT NULL AUTO_INCREMENT,
	dia char(1) NOT NULL,
	hora INT NOT NULL,
	profesorMatricula INT NOT NULL REFERENCES Profesores(matricula) ON DELETE CASCADE,
	PRIMARY KEY (ID)
);

