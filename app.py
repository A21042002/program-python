from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

conn = mysql.connector.connect(host="localhost",user="root",passwd="",database="empdb")

app = Flask(__name__)
with open("config.json","r") as c:
    params = json.load(c)["params"]
    # this will run local uri
    if ["local_uri"]==True:
        app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]
db = SQLAlchemy(app)


class EMP_INFO(db.Model):
    eno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    desig = db.Column(db.String(5), nullable=False)


@app.route("/")
def p1():
    return render_template("index.html",params=params)


@app.route("/tableshow")
def p2():
    rows = EMP_INFO.query.all()
    return render_template("tableshow.html", rows=rows,params=params)


@app.route("/insert", methods=['GET', 'POST'])
def p3():
    if request.method == "POST":
        name = request.form.get('name')
        desig = request.form.get('desig')
        entry = EMP_INFO(name=name, desig=desig)
        db.session.add(entry)
        db.session.commit()
    return render_template("insert.html",params=params)

if __name__ == "__main__":
    app.run(debug=True)
