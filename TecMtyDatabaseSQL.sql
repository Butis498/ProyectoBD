DROP DATABASE TecMtyDatabase;

CREATE DATABASE TecMtyDatabase;


USE TecMtyDatabase;


CREATE TABLE Departamento
(
	ID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	numOficina INT,
	telefono VARCHAR(30),
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
	departamentoID INT NOT NULL,
	nombre VARCHAR(50) NOT NULL,
	hrsSemanal INT,
	planSemestre INT,
	descripcion VARCHAR(200),
	PRIMARY KEY(ID),
	FOREIGN KEY(departamentoID) REFERENCES Departamento(ID)
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
	telefono VARCHAR(30),
	nomina INT not null UNIQUE,
	departamentoID INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(departamentoID) REFERENCES Departamento(ID)
);


CREATE TABLE Grupo
(
	GrupoID int not null ,
	cursoID int not null,
	semestre VARCHAR(20) NOT NULL,
	año INT NOT NULL,
	rECOA INT null,
	profeMatricula VARCHAR(15) not null,
	PRIMARY KEY (GrupoID),
	FOREIGN key (cursoID) REFERENCES Curso(ID),
	FOREIGN KEY (profeMatricula) REFERENCES Profesores(matricula)
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
	telefono VARCHAR(30),
	celular VARCHAR(30),
	carreraID INT NOT NULL,
	PRIMARY KEY(matricula),
	FOREIGN KEY(carreraID) REFERENCES Carrera(ID)
);


CREATE TABLE CursoPorAlumno
(
	ID int NOT NULL
	AUTO_INCREMENT,
	cursoID int not null,
	matriculaAlumno VARCHAR
	(9) NULL,
		FOREIGN key
	(matriculaAlumno) REFERENCES Alumno
	(matricula),
		PRIMARY key
	(ID),
		FOREIGN key
	(cursoID) REFERENCES Curso
	(ID)
);





	CREATE TABLE HorasLibresProfesores
	(
		ID int NOT NULL
		AUTO_INCREMENT,
	dia char
		(1) NOT NULL,
	hora INT NOT NULL,
	profesorMatricula VARCHAR
		(9) NOT NULL ,
	PRIMARY KEY
		(ID),
	FOREIGN key
		(profesorMatricula) REFERENCES Profesores
		(matricula) 
	
);

		CREATE TABLE CursoPorProfesor
		(
			matriculaProfesor VARCHAR(9) not null,
			cursoID int not null,
			ID int NOT NULL
			AUTO_INCREMENT,
	PRIMARY key
			(ID),
	FOREIGN key
			(cursoID) REFERENCES Curso
			(ID),
	FOREIGN Key
			(matriculaProfesor) REFERENCES Profesores
			(matricula)
 

);



			INSERT INTO Departamento
			VALUES
				(1, 'Ingeniería', 101, '81-1234-5678');

			INSERT INTO Departamento
				(ID, nombre, numOficina, telefono)
			VALUES
				(2, 'Ciencias Sociales', 101, '81-1234-1234');

			INSERT INTO Departamento
				(ID, nombre, numOficina, telefono)
			VALUES
				(3, 'Economía', 101, '81-1234-1111');

			INSERT INTO Carrera
				(ID, departamentoID, nombre)
			VALUES
				(101, 1, 'ITC');

			INSERT INTO Carrera
				(ID, departamentoID, nombre)
			VALUES
				(102, 1, 'Mecatronica');

			INSERT INTO Carrera
				(ID, departamentoID, nombre)
			VALUES
				(301, 3, 'LIN');
			INSERT INTO Curso
				(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion)
			VALUES
				(1, 1, 'Matematicas para Ingeniería', 6, 3, 'Este curso es de mates para ingenieros en tercer semestre y dura 6 horas semanales.');

			INSERT INTO Curso
				(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion)
			VALUES
				(2, 1, 'Física para Ingeniería', 8, 2, 'Este curso es de mates para ingenieros en segundo semestre y dura 8 horas semanales.');

			INSERT INTO Curso
				(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion)
			VALUES
				(3, 3, 'Matematicas para Licenciados', 4, 1, 'Este curso es de mates para ingenieros en primer semestre y dura 4 horas semanales.');
	INSERT INTO Profesores
				(matricula, curp, fName, lName, sex, DOB, direccion, telefono, nomina, departamentoID )
			VALUES
				('L0012345', 'CACX485820', 'Esteban', 'Dido', 'M', '1990-7-04', 'x dirección', '81-1234-1234', 1234, 1 );

			INSERT INTO Profesores
				(matricula, curp, fName, lName, sex, DOB, direccion, telefono, nomina, departamentoID)
			VALUES
				('L0067890', 'YOLO485820', 'Marco', 'Farias', 'M', '1996-3-01', 'x dirección', '81-1234-1234', 4321, 2 );

			INSERT INTO Profesores
				(matricula, curp, fName, lName, sex, DOB, direccion, telefono, nomina, departamentoID )
			VALUES
				('L0055345', 'WOWO485820', 'Elba', 'Nanero', 'F', '1980-7-25', 'x dirección', '81-1234-1234', 6234, 3 );

			INSERT INTO Grupo
				(GrupoID, cursoID, semestre, año, rECOA , profeMatricula)
			VALUES
				(1, 1, 'Fall', 2016, 90 , 'L0055345');

			INSERT INTO Grupo
				(GrupoID, cursoID, semestre, año, rECOA , profeMatricula)
			VALUES
				(2, 1, 'Spring', 2017, 80, 'L0012345' );

			INSERT INTO Grupo
				(GrupoID, cursoID, semestre, año, rECOA , profeMatricula )
			VALUES
				(3, 1, 'Summer', 2017, 95 , 'L0067890');

		

			INSERT INTO Alumno
				(matricula, curp, fName, lName, sex, DOB, direccion, telefono, celular, carreraID)
			VALUES
				('A01553456', 'XOXO485820', 'Juanito', 'Banana', 'M', '1999-7-25', 'x dirección', '81-1234-1234', '6234', 301);

			INSERT INTO Alumno
				(matricula, curp, fName, lName, sex, DOB, direccion, telefono, celular, carreraID)
			VALUES
				('A02553456', 'XOXC485820', 'Maria', 'Rosado', 'F', '1998-7-25', 'x dirección', '81-1234-1234', '6234', 101);

			INSERT INTO Alumno
				(matricula, curp, fName, lName, sex, DOB, direccion, telefono, celular, carreraID)
			VALUES
				('A05553456', 'XOOL485820', 'Humberto', 'Rateira', 'M', '1997-7-25', 'x dirección', '81-1234-1234', '6234', 101);

			INSERT INTO CursoPorAlumno
				(ID, cursoID, matriculaAlumno)
			VALUES
				(1, 1, 'A01553456');

			INSERT INTO CursoPorAlumno
				(ID, cursoID, matriculaAlumno)
			VALUES
				(2, 2, 'A01553456');

			INSERT INTO CursoPorAlumno
				(ID, cursoID, matriculaAlumno)
			VALUES
				(3, 3, 'A05553456');

			INSERT INTO HorasLibresProfesores
				(dia, hora, profesorMatricula)
			VALUES
				('L', 16, 'L0012345');

			INSERT INTO HorasLibresProfesores
				(dia, hora, profesorMatricula)
			VALUES
				('M', 12, 'L0012345');

			INSERT INTO HorasLibresProfesores
				(dia, hora, profesorMatricula)
			VALUES
				('X', 10, 'L0012345');

			INSERT INTO CursoPorProfesor
				(matriculaProfesor, cursoID)
			VALUES
				('L0012345', 1);

			INSERT INTO CursoPorProfesor
				(matriculaProfesor, cursoID)
			VALUES
				('L0067890', 2);

			INSERT INTO CursoPorProfesor
				(matriculaProfesor, cursoID)
			VALUES
				('L0055345', 3);




