from flask import Flask, redirect, request, render_template, flash, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    con = sql.connect('database3.db')
    con.row_factory = sql.Row
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
        con.commit()
        flash("Product added", "success")
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/edit_product/<string:id>', methods=["POST", "GET"])
def edit_product(id):
    if request.method == "POST":

        ProductName = request.form["ProductName"]
        Type = request.form["Type"]
        Brand = request.form["Brand"]
        Price = request.form["Price"]
        MadeIn = request.form["MadeIn"]

        con = sql.connect('database3.db')
        cur = con.cursor()
        cur.execute('UPDATE products SET ProductName=?, Type=?, Brand=?, Price=?, MadeIn=? where ID=?', (ProductName, Type, Brand, Price, MadeIn, id))
        con.commit()
        flash("Product updated", "success")
        return redirect(url_for('index'))
    con = sql.connect('database3.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('select * from products where ID=?', (id,))
    data = cur.fetchone()
    return render_template('edit_product.html', datas=data)

@app.route('/delete_product/<string:id>', methods=["GET"])
def delete_product(id):
    con = sql.connect('database3.db')
    cur = con.cursor()
    cur.execute('DELETE from products where ID=?', (id,))
    con.commit()
    flash("Product deleted", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = "admin123"
    app.run(debug=True)
