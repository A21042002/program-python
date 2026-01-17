from flask import Flask, request, render_template, redirect
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',
password='',database='empdb')
app = Flask(__name__)
@app.route("/")
def home():
     cur = conn.cursor()
     cur.execute("SELECT * FROM `emp_all_info`")
     rows = cur.fetchall()
     cur.close()
     return render_template("insert.html",rows=rows)
@app.route("/insert",methods=['GET','POST'])
def insert():
    try:
        name = request.form['name']
        desig = request.form['desig']
        cur = conn.cursor()
        sql = "INSERT INTO `emp_info`( `name`, `desig`) VALUES (%s,%s)"
        cur.execute(sql,(name,desig))
        conn.commit()
        cur.close()
        return redirect("/")
    except Exception as e:
        return (str(e))
    
@app.route("/up/<eno>")
def up(eno):
     cur = conn.cursor()
     cur.execute("SELECT * FROM `emp_info` where emp_info.eno=%s",(eno,))
     rows = cur.fetchall()
     cur.close()
     return render_template("update.html",rows=rows)


@app.route("/update",methods=['GET','POST'])
def update():
    try:
        eno =  request.form['eno']
        name = request.form['name']
        desig = request.form['desig']
        cur = conn.cursor()
        sql = "UPDATE `emp_info` SET `name`=%s,`desig`=%s WHERE emp_info.eno=%s"
        cur.execute(sql,(name,desig,eno))
        conn.commit()
        cur.close()
        return redirect("/")
    except Exception as e:
        return (str(e))

if __name__ == '__main__':
    app.run(debug=True)