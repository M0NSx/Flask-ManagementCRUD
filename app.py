from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template('index.html', datas=data)

@app.route("/add_user", methods= ["POST", "GET"])
def add_user():
    if request.method == "POST":
        Name = request.form["Name"]
        Age = request.form["Age"]
        City = request.form["City"]
        Street = request.form["Street"]
        Number = request.form["Number"]
        Email = request.form["Email"]
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO users (Name,Age,City,Street,Number,Email) values (?,?,?,?,?,?)", (Name, Age, City, Street, Number, Email))
        con.commit()
        flash("Data registered", "success")
        return redirect(url_for('index'))
    return render_template("add_user.html")

@app.route("/edit_user/<string:id>", methods= ["POST", "GET"])
def edit_user(id):
    if request.method == "POST":
        Name = request.form["Name"]
        Age = request.form["Age"]
        City = request.form["City"]
        Street = request.form["Street"]
        Number = request.form["Number"]
        Email = request.form["Email"]
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("UPDATE users SET Name=?, Age=?, City=?, Street=?, Number=?, Email=? WHERE ID=?", (Name, Age, City, Street, Number, Email, id))
        con.commit()
        flash("Data updated", "success")
        return redirect(url_for('index'))
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('select * from users where ID=?', (id,))
    data = cur.fetchone()
    return render_template('edit_user.html', datas=data)

@app.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute('delete from users where ID=?', (id,))
    con.commit()
    flash("Data deleted", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = "admin123"
    app.run(debug=True)
