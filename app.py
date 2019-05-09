from flask import Flask, render_template, request, redirect, url_for
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
            DOB = request.form["DOB"]
            curp = request.form["curp"]
            telefono = request.form["telefono"]
            celular = request.form["celular"]
            carreraID = request.form["carreraID"]
            direccion = request.form["direccion"]
            _db.insert_member(fName, lName, matricula, sex, DOB,
                              curp, telefono, celular, carreraID, direccion)
            print('Alumno agregado', file=sys.stdout)

            membs = _db.list_members()
            print('Listing all members from normal query', file=sys.stdout)
            return membs

        else:
            if request.method == "GET":
                member_no = request.values.get('matricula', '')
                member_name = request.values.get('memberName', '')
                membs = _db.list_member(member_no, member_name)

                return membs

    res = db_query()

    return render_template('students.html', result=res, content_type='application/json')


@app.route('/curso_por_alumno', methods=["GET", "POST"])
def curso_por_alumno():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            cursos = _db.list_cur()
            return cursos
        else:
            if request.method == "GET":
                matricula = request.values.get('matricula','')
                cursos = _db.list_cursos(matricula)
                return cursos
    res = db_query()

    return render_template('curso_por_alumno.html', result=res, content_type='application/json')


@app.route('/info_por_nomina', methods=["GET", "POST"])
def info_por_nomina():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            datos = _db.list_datos()
            return datos
        else:
            if request.method == "GET":
                nomina = request.values.get('nomina','')
                datos = _db.list_dato(nomina)
                return datos
    res = db_query()

    return render_template('info_por_nomina.html', result=res, content_type='application/json')


@app.route('/horas_por_nomina', methods=["GET", "POST"])
def horas_por_nomina():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            datos = _db.list_horas()
            return datos
        else:
            if request.method == "GET":
                nomina = request.values.get('nomina','')
                datos = _db.list_hora(nomina)
                return datos
    res = db_query()

    return render_template('horas_por_nomina.html', result=res, content_type='application/json')


@app.route("/ecoa", methods=["GET", "POST"])
def ecoa():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            datos = _db.list_resultados()
            return datos
        else:
            if request.method == "GET":
                nomina = request.values.get('nomina','')
                datos = _db.list_resultado(nomina)
                return datos
    res = db_query()

    return render_template('ecoa.html', result=res, content_type='application/json')


@app.route('/profesores', methods=["GET", "POST"])
def profesores():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            fName = request.form["fName"]
            lName = request.form["lName"]
            matricula = request.form["matricula"]
            sex = request.form["sex"]
            DOB = request.form["DOB"]
            curp = request.form["curp"]
            telefono = request.form["telefono"]
            nomina = request.form["nomina"]
            departamentoID = request.form["departamentoID"]
            direccion = request.form["direccion"]
            _db.insert_profesor(fName, lName, matricula, sex, DOB,
                                curp, telefono, nomina, departamentoID, direccion )

            membs = _db.list_profesores() 
            return membs

        else:
            if request.method == "GET":
                member_no = request.values.get('nominas', '')
                member_name = request.values.get('memberNames', '')
                membs = _db.list_profesor(member_no, member_name)

                return membs

    res = db_query()

    return render_template('profesores.html', result=res, content_type='application/json')


@app.route('/departamento', methods=["GET", "POST"])
def departamento():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            DepID = request.form["DepID"]
            nombre = request.form["nombre"]
            numOficina = request.form["numOficina"]
            telefono = request.form["telefono"]

            _db.insert_departamento(DepID, nombre, numOficina, telefono)

            deps = _db.list_dep()
            return deps

        else:
            if request.method == "GET":
                dep_num = request.values.get('DepsID', '')
                dep_name = request.values.get('depName', '')
                deps = _db.list_deps(dep_num, dep_name)

                return deps

    res = db_query()

    return render_template('departamento.html', result=res, content_type='application/json')


@app.route('/del_members', methods=["POST"])
def del_members():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                member_no = request.form["matriculadel"]
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
                member_no = request.form["matriculadel"]
                _db.delete_profesor(member_no)
        membs = _db.list_profesores()
        return membs

    res = db_query()

    return render_template('profesores.html', result=res, content_type='application/json')


@app.route('/del_dep', methods=["POST"])
def del_dep():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                dep_id = request.form["DelID"]
                _db.delete_dep(dep_id)
        dep = _db.list_dep()
        print('Listing all members from normal query', file=sys.stdout)
        return dep

    res = db_query()

    return render_template('departamento.html', result=res, content_type='application/json')
