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


@app.route('/members', methods=["GET", "POST"])
def members():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            fName = request.form["fName"]
            lName = request.form["lName"]
            sex = request.form["sex"]
            dob = request.form["dob"]
            address = request.form["address"]
            _db.insert_member(fName, lName, sex, dob, address)
            print('Member inserted', file=sys.stdout)

            membs = _db.list_members()
            print('Listing all members from normal query', file=sys.stdout)
            return membs

        else:
            if request.method == "GET":
                member_no = request.values.get('memberNo', '')
                member_name = request.values.get('memberName', '')
                membs = _db.list_member(member_no, member_name)
                print('Listing member given info' + member_no + ' ' + member_name, file=sys.stdout)
                return membs

    res = db_query()

    return render_template('members.html', result=res, content_type='application/json')

@app.route('/del_members', methods=["POST"])
def del_members():
    def db_query():
        _db = db.Database()
        if request.method == "POST":
            if len(request.form) != 0:
                member_no = request.form["memberNo"]
                _db.delete_member(member_no)
        membs = _db.list_members()
        print('Listing all members from normal query', file=sys.stdout)
        return membs

    res = db_query()

    return render_template('members.html', result=res, content_type='application/json')

@app.route('/spmembers')
def sp_members():
    def db_query():
        _db = db.Database()
        membs = _db.SP_list_members()
        print('Listing all members from a Stored Prodecure', file=sys.stdout)

        return membs

    res = db_query()

    return render_template('members.html', result=res, content_type='application/json')


@app.route('/top_and_bottom')
def top_and_bottom():
    def db_query():
        _db = db.Database()
        top_n_bot = _db.top_and_bottom_clients()
        print('Listing top and bottom members depending on their number of rentals', file=sys.stdout)

        return top_n_bot

    res = db_query()

    return render_template('top_and_bottom_clients.html', result=res, content_type='application/json')
