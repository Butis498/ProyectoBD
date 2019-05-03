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
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_profesores(self):
        query = '''
                SELECT * 
                FROM Profesores
                '''
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result


    def list_dep(self):
        query = '''
                SELECT * 
                FROM Departamento
                '''
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_member(self, member_no, member_name):
        member_name = ("'"+ member_name + "'")

        query = '''
                SELECT *
                FROM Alumno
                '''
        if member_no != '':
            query += 'WHERE matricula = {}'.format(member_no)
            if member_name != '':
                query += 'AND fName = \'{}\''.format(member_name)
        elif member_name != '':
            query += 'WHERE fName = \'{}\''.format(member_name)

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result


    def list_profesor(self, member_no, member_name):
        member_name = ("'"+ member_name + "'")

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

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result

    def list_deps(self, dep_num, dep_name):
        dep_name = ("'"+ dep_name + "'")
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

        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        result = self.cur.fetchall()

        return result


    def insert_member(self, fName, lName, matricula, sex, dob, curp, telefono, celular, carreraID, direccion):
        direccion = ("'"+ direccion + "'")
        query = '''
                INSERT INTO Alumno (fName, lName, matricula, sex, dob,curp,telefono,celular,carreraID, direccion)
                VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}')
                '''.format(fName, lName, matricula, sex, dob, curp, telefono, celular, carreraID, direccion)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def insert_profesor(self, fName, lName, matricula, sex, dob, curp, telefono,nomina, celular, carreraID, direccion):
        direccion = ("'"+ direccion + "'")

        query = '''
                INSERT INTO Profesores (fName, lName, matricula, sex, dob,curp,telefono,nomina,celular,carreraID, direccion)
                VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}')
                '''.format(fName, lName, matricula, sex, dob, curp, telefono,nomina, celular, carreraID, direccion)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def insert_departamento(self, ID , nombre , numOficina , telefono):
        query = '''
                INSERT INTO Departamento (ID , nombre , numOficina , telefono)
                VALUES ('{}', '{}', '{}', '{}')
                '''.format(ID , nombre , numOficina , telefono)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()


    def delete_member(self, member_no):

        member_no = ("'"+  member_no +"'")
        query = '''
                DELETE FROM Alumno
                WHERE matricula = {}
                '''.format(member_no)
        print('Query: {}'.format(query), file=sys.stdout)
        self.cur.execute(query)
        self.con.commit()

    def delete_profesor(self, member_no):
        
        query = '''
                DELETE FROM Profesores
                WHERE matricula = {}
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


