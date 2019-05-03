from flask import Flask, render_template, request , redirect , url_for
import logging
import sys

import db 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# example!
@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():

    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')


@app.route('/students', methods=["GET", "POST"])
def students():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            fName = request.form["fName"]
            lName = request.form["lName"]
            matricula = request.form["matricula"]
            sex = request.form["sex"]
            dob = request.form["dob"]
            curp = request.form["curp"]
            telefono = request.form["telefono"]
            celular = request.form["celular"]
            carreraID = request.form["carreraID"]
            direccion = request.form["direccion"]
            _db.insert_member(fName, lName, matricula, sex, dob,curp,telefono,celular,carreraID, direccion)
            print('Alumno agregado', file=sys.stdout)

            membs = _db.list_members()
            print('Listing all members from normal query', file=sys.stdout)
            return membs

        else:
            if request.method == "GET":
                member_no = request.values.get('matricula', '')
                member_name = request.values.get('memberName', '')
                membs = _db.list_member(member_no, member_name)
                print('Listing member given info' + member_no + ' ' + member_name, file=sys.stdout)
                return membs

    res = db_query()

    return render_template('students.html', result=res, content_type='application/json')


@app.route('/curso_por_alumno' , methods=["GET", "POST"])
def curso_por_alumno():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            cursos = _db.list_cur() 
            return cursos
        else:
            if request.method == "GET":
                print('Antes')
                matricula = request.values.get('matricula', '')
                cursos = _db.list_cursos(matricula)
                return cursos
    res = db_query()

    return render_template('curso_por_alumno.html', result=res, content_type='application/json')



                




@app.route('/profesores', methods=["GET", "POST"])
def profesores():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            fName = request.form["fName"]
            lName = request.form["lName"]
            matricula = request.form["matricula"]
            sex = request.form["sex"]
            dob = request.form["dob"]
            curp = request.form["curp"]
            telefono = request.form["telefono"]
            nomina = request.form["nomina"]
            celular = request.form["celular"]
            carreraID = request.form["carreraID"]
            direccion = request.form["direccion"]
            _db.insert_profesor(fName, lName, matricula, sex, dob,curp,telefono,nomina,celular,carreraID, direccion)
            print('Profesor agregado', file=sys.stdout)

            membs = _db.list_profesores()
            print('Listing all members from normal query', file=sys.stdout)
            return membs

        else:
            if request.method == "GET":
                member_no = request.values.get('nomina', '')
                member_name = request.values.get('memberName', '')
                membs = _db.list_profesor(member_no, member_name)
                print('Listing member given info' + member_no + ' ' + member_name, file=sys.stdout)
                return membs

    res = db_query()

    return render_template('profesores.html', result=res, content_type='application/json')




@app.route('/departamento', methods=["GET", "POST"])
def departamento():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            ID = request.form["ID"]
            nombre = request.form["nombre"]
            numOficina = request.form["numOficina"]
            telefono = request.form["telefono"]
            
            _db.insert_departamento(ID , nombre , numOficina , telefono )
            print('departamento agregado', file=sys.stdout)

            deps = _db.list_dep()
            print('Listing all members from normal query', file=sys.stdout)
            return deps

        else:
            if request.method == "GET":
                dep_num = request.values.get('ID', '')
                dep_name = request.values.get('depName', '')
                deps = _db.list_deps(dep_num, dep_name)
                print('Listing member given info' + dep_num + ' ' + dep_name, file=sys.stdout)
                return deps

    res = db_query()

    return render_template('departamento.html', result=res, content_type='application/json')



@app.route('/del_members', methods=["POST"])
def del_members():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                member_no = request.form["matricula"]
                _db.delete_member(member_no)
        membs = _db.list_members()
        print('Listing all members from normal query', file=sys.stdout)
        return membs

    res = db_query()

    return render_template('students.html', result=res, content_type='application/json')



@app.route('/del_profesor', methods=["POST"])
def del_profesor():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                member_no = request.form["matricula"]
                _db.delete_profesor(member_no)
        membs = _db.list_profesores()
        print('Listing all members from normal query', file=sys.stdout)
        return membs

    res = db_query()

    return render_template('profesores.html', result=res, content_type='application/json')





@app.route('/del_dep', methods=["POST"])
def del_dep():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                dep_id = request.form["ID"]
                _db.delete_dep(dep_id)
        dep = _db.list_dep()
        print('Listing all members from normal query', file=sys.stdout)
        return dep

    res = db_query()

    return render_template('departamento.html', result=res, content_type='application/json')



