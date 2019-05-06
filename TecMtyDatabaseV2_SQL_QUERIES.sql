USE TecMtyDatabase

SELECT *
FROM Departamento

SELECT *
FROM Carrera


INSERT INTO Departamento VALUES (1, 'Ingeniería', 101, '81-1234-5678');

INSERT INTO Departamento(ID, nombre, numOficina, telefono) VALUES (2, 'Ciencias Sociales', 101, '81-1234-1234');

INSERT INTO Departamento(ID, nombre, numOficina, telefono) VALUES (3, 'Economía', 101, '81-1234-1111');

INSERT INTO Carrera(ID, departamentoID, nombre) VALUES (101, 1, 'ITC');

INSERT INTO Carrera(ID, departamentoID, nombre) VALUES (102, 1, 'Mecatronica');

INSERT INTO Carrera(ID, departamentoID, nombre) VALUES (301, 3, 'LIN');

INSERT INTO Curso(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion) VALUES (1, 1, 'Matematicas para Ingeniería', 6, 3, 'Este curso es de mates para ingenieros en tercer semestre y dura 6 horas semanales.');

INSERT INTO Curso(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion) VALUES (2, 1, 'Física para Ingeniería', 8, 2, 'Este curso es de mates para ingenieros en segundo semestre y dura 8 horas semanales.');

INSERT INTO Curso(ID, departamentoID, nombre, hrsSemanal, planSemestre, descripcion) VALUES (3, 3, 'Matematicas para Licenciados', 4, 1, 'Este curso es de mates para ingenieros en primer semestre y dura 4 horas semanales.');
