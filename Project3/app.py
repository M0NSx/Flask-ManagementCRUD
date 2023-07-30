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
