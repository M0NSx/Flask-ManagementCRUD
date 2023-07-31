from flask import Flask, redirect, request, render_template, flash, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    con = sql.connect('database3.db')
    sql.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('select * from products')
    data = cur.fetchall()
    return render_template('index.html', datas=data)

@app.route('/add_product', methods=["POST", "GET"])
def add_product():
    if request.method == "POST":

        ProductName = request.form["ProductName"]
        Type = request.form["Type"]
        Brand = request.form["Brand"]
        Price = request.form["Price"]
        MadeIn = request.form["MadeIn"]

        con = sql.connect('database3.db')
        cur = con.cursor()
        cur.execute('INSERT INTO products (ProductName, Type, Brand, Price, MadeIn) values (?,?,?,?,?)', (ProductName, Type, Brand, Price, MadeIn))
        cur.commit()
        flash("Product added", "success")
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/edit_product/<string:id>', methods=["POST", "GET"])
def edit_product(id):
