from flask import *
import mysql.connector
app = Flask(__name__)
dictionary = {}
app.secret_key = "abc"
@app.route("/")
def user():
    return render_template("index1.html")
@app.route("/login",methods=["POST","GET"])
def login():
    if "LOG" in session:
        return redirect(url_for("view"))
    return render_template("index.html")
@app.route("/details",methods=["POST","GET"])
def details():
    if request.method == "POST":
        name = request.form["Name"]
        passwd = request.form["Pass"]
        email = request.form["Email"]
        dictionary.update(request.form)
        session["LOG"] = "Value"
        if not name or not passwd or not email:
            return redirect(url_for("login"))
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="bro")
        try:
            mycursor =  mydb.cursor()
            mycursor.execute("INSERT INTO emp_values VALUES (%s,%s,%s)",(name,passwd,email))
            mydb.commit()
        except:
            mydb.rollback()
        mydb.close()
    return "<h1 align ='center'> SUCCESSFULLy  LOGGED IN  </h1> "
@app.route("/logout",methods = ["POST","GET"] ) 
def logout():
    if "LOG" not in session:
        return redirect(url_for("login"))
    session.pop("LOG")
    return redirect(url_for("user"))
@app.route("/view",methods =["POST","GET"]) 
def view():
    if "LOG" not in session:
        return redirect(url_for("login"))
    return render_template("index2.html",dictionary = dictionary)
if __name__ == '__main__':
    app.run(debug = True)

           
            