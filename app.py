from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("land.html")

@app.route("/choose")
def choose():
    return render_template("choose.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/ordernow")
def ordernow():
    city = request.args.get("city" , None)
    db = sqlite3.connect("Data Base/BabySitter.db")
    cr = db.cursor()
    cr.execute(f""" SELECT id , Name , City , Prise , Images FROM Nany WHERE city LIKE '%{city}%' """)
    result = cr.fetchall()
    db.close()
    return render_template("ordernow.html" , data = result)

@app.route("/accept/<int:id>")
def accept(id):
    db = sqlite3.connect("Data Base/BabySitter.db")
    cr = db.cursor()
    cr.execute(f""" SELECT * FROM Nany WHERE id = {id} """)
    result = cr.fetchall()
    db.close()
    return render_template("accept.html" , data = result[0])



if __name__ == "__main__":
    app.run(debug=True ,port=9000)