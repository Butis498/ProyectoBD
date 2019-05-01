DROP DATABASE TecMtyDatabase

CREATE DATABASE TecMtyDatabase

USE TecMtyDatabase

CREATE TABLE Departamento
(
	ID				INT NOT NULL,
	nombre			VARCHAR(50) NOT NULL,
	numOficina		INT,
	telefono		INT,
	PRIMARY KEY(ID)
)


CREATE TABLE Carrera
(
	ID				INT NOT NULL,
	departamentoID	INT NOT NULL,
	nombre			VARCHAR(50) NOT NULL,
	PRIMARY KEY(ID),
	FOREIGN KEY(departamentoID) REFERENCES Departamento(ID)
)

CREATE TABLE Curso
(
	ID				INT NOT NULL,
	carreraID		INT NOT NULL,
	nombre			VARCHAR(50) NOT NULL,
	hrsSemanal		INT,
	planSemestre	INT,
	descripcion		VARCHAR(200),
	PRIMARY KEY(ID),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)
)

--Creamos esta tabla para unir a las tablas de Carrera y Curso
--CREATE TABLE CursosPorCarrera
--(



--)

CREATE TABLE Grupo /*weak entity*/
(
	ID numeric PRIMARY KEY REFERENCES Curso(ID) ON DELETE CASCADE,
   	semestre			INT NOT NULL,
   	año					INT NOT NULL,
   	rECOA				INT,
   	numGrupo			INT NOT NULL
)


CREATE TABLE Alumno
(
	--matricula        INT IDENTITY(1,1), --uses the IDENTITY keyword to perform an auto-increment feature. In the example above, the starting value for IDENTITY is 1, and it will increment by 1 for each new record.
	matricula       VARCHAR(15) NOT NULL,
	curp			VARCHAR(20) NOT NULL UNIQUE,
	fName           VARCHAR(15) NOT NULL,
	lName           VARCHAR(15) NOT NULL,
	sex             CHAR(1),
	DOB             DATETIME,
	direccion       VARCHAR(100),
	telefono		INT,
	celular			INT,
	carreraID		INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)
)


CREATE TABLE Profesores
(
	matricula       VARCHAR(15) NOT NULL,
	curp			VARCHAR(20) NOT NULL UNIQUE,
	fName           VARCHAR(15) NOT NULL,
	lName           VARCHAR(15) NOT NULL,
	sex             CHAR(1),
	DOB             DATETIME,
	direccion       VARCHAR(100),
	telefono		INT,
	nomina			INT,
	celular			INT,
	carreraID		INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)


)

CREATE TABLE HorasLibresProfesores
(
	ID INT IDENTITY(1,1) PRIMARY KEY, /* SQL Server uses the IDENTITY keyword to perform an auto-increment feature, IDENTITY is 1, and it will increment by 1 for each new record. MySQL uses the AUTO_INCREMENT keyword to perform an auto-increment feature. */
  	dia nvarchar(1) NOT NULL,
	hora INT NOT NULL,
  	profesorMatricula INT NOT NULL REFERENCES Profesores(matricula) ON DELETE CASCADE /* A foreign key with cascade delete means that if a record in the parent table is deleted, then the corresponding records in the child table will automatically be deleted.*/
)
/*

CREATE TABLE Grupo
(



)
*/
