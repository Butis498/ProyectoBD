import pymysql
import sys


class Database:

    def __init__(self):
        # host = "127.0.0.1"
        host = "localhost"
        user = "root"
        password = "3261098Butis2000"
        db = "TecMtyDatabase"
        port = 3306

        self.con = pymysql.connect(host=host,
                                   user=user,
                                   password=password,
                                   db=db,
                                   port=port,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_members(self):
        query = '''
                SELECT * 
                FROM Alumno
                '''
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_datos(self):
        query = '''
                SELECT p.nomina , p.fName , c.nombre
                FROM Profesores p , Curso c, CursoPorProfesor cpp
                WHERE p.matricula = cpp.matriculaProfesor AND c.ID = cpp.cursoID
                '''
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_resultados(self):
        query = '''
                SELECT g.rECOA , c.ID , c.nombre , g.GrupoID , g.semestre , g.año
                FROM Grupo g, Profesores p, Curso c , CursoPorProfesor cpp
                WHERE g.cursoID = c.ID AND cpp.matriculaProfesor = p.matricula
                GROUP by c.ID,g.rECOA  , c.nombre , g.GrupoID , g.semestre , g.año;
                '''
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_horas(self):
        query = '''
                SELECT p.nomina , p.fName , h.dia , h.hora
                FROM Profesores p , HorasLibresProfesores h
                WHERE p.matricula = h.profesorMatricula
                '''
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_profesores(self):
        query = '''
                SELECT * 
                FROM Profesores
                '''
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_cur(self):
        query = '''
                SELECT c.nombre
                FROM Curso c, Alumno a , CursoPorAlumno ca
                WHERE c.ID = ca.cursoID AND ca.matriculaAlumno = a.matricula 
                '''
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_dep(self):
        query = '''
                SELECT * 
                FROM Departamento
                '''
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_member(self, member_no, member_name):

        query = '''
                SELECT *
                FROM Alumno
                '''
        if member_no != '':
            query += 'WHERE matricula = \'{}\''.format(member_no)
            if member_name != '':
                query += 'AND fName = \'{}\''.format(member_name)
        elif member_name != '':
            query += 'WHERE fName = \'{}\''.format(member_name)

        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_profesor(self, member_no, member_name):

        query = '''
                SELECT *
                FROM Profesores
                '''
        if member_no != '':
            query += 'WHERE nomina = {}'.format(member_no)
            if member_name != '':
                query += 'AND fName = \'{}\''.format(member_name)
        elif member_name != '':
            query += 'WHERE fName = \'{}\''.format(member_name)

        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_cursos(self, matricula):

        query = '''
                SELECT c.nombre
                FROM Curso c, Alumno a , CursoPorAlumno ca
                WHERE c.ID = ca.cursoID AND ca.matriculaAlumno = a.matricula 
                '''
        if matricula != '':
            query += 'AND a.matricula = \'{}\''.format(matricula)

        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_dato(self, nomina):

        query = '''
                SELECT p.nomina , p.fName , c.nombre
                FROM Profesores p , Curso c, CursoPorProfesor cpp
                WHERE p.matricula = cpp.matriculaProfesor AND c.ID = cpp.cursoID
                '''
        if nomina != '':
            query += 'AND p.nomina = {}'.format(nomina)

        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_resultado(self, nomina):

        query = '''
                SELECT g.rECOA , c.ID , c.nombre , g.GrupoID , g.semestre ,g.año
                FROM Grupo g, Profesores p, Curso c , CursoPorProfesor cpp 
                WHERE g.cursoID = c.ID AND  p.matricula = g.profeMatricula AND p.matricula = cpp.matriculaProfesor
                '''
        if nomina != '':
            query += 'AND p.nomina = {}'.format(nomina)

        query += '''
                 GROUP by c.ID , c.nombre , g.GrupoID , g.semestre ,g.año
                 '''

        self.cur.execute(query)
        result = self.cur.fetchall()


        return result

    def list_hora(self, nomina):

        query = '''
                SELECT p.nomina , p.fName , h.dia , h.hora
                FROM Profesores p , HorasLibresProfesores h
                WHERE p.matricula = h.profesorMatricula
                '''
        if nomina != '':
            query += 'AND p.nomina = {}'.format(nomina)

        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_deps(self, dep_num, dep_name):
        query = '''
                SELECT *
                FROM Departamento
                '''
        if dep_num != '':
            query += 'WHERE ID = {}'.format(dep_num)
            if dep_name != '':
                query += 'AND nombre = \'{}\''.format(dep_name)
        elif dep_name != '':
            query += 'WHERE nombre = \'{}\''.format(dep_name)

        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def insert_member(self, fName, lName, matricula, sex, DOB, curp, telefono, celular, carreraID, direccion):

        query = '''
                INSERT INTO Alumno (fName, lName, matricula, sex, DOB,curp,telefono,celular,carreraID, direccion)
                VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', \'{}\')
                '''.format(fName, lName, matricula, sex, DOB, curp, telefono, celular, carreraID, direccion)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def insert_profesor(self, fName, lName, matricula, sex, DOB, curp, telefono, nomina,  departamentoID, direccion ):

        query = '''
                INSERT INTO Profesores (fName, lName, matricula, sex, DOB,curp,telefono,nomina,departamentoID, direccion )
                VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', \'{}\' )
                '''.format(fName, lName, matricula, sex, DOB, curp, telefono, nomina, departamentoID, direccion )
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def insert_departamento(self, ID, nombre, numOficina, telefono):
        query = '''
                INSERT INTO Departamento (ID , nombre , numOficina , telefono)
                VALUES ('{}', '{}', '{}', '{}')
                '''.format(ID, nombre, numOficina, telefono)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def delete_member(self, member_no):

        query = '''
                DELETE FROM Alumno
                WHERE matricula = \'{}\'
                '''.format(member_no)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def delete_profesor(self, member_no):

        query = '''
                DELETE FROM Profesores
                WHERE matricula = \'{}\'
                '''.format(member_no)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def delete_dep(self, dep_id):
        query = '''
                DELETE FROM Departamento
                WHERE ID = {}
                '''.format(dep_id)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()
