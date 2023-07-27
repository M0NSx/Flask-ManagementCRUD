from flask import Flask, request, url_for, redirect, render_template, flash
import sqlite3 as sql

app = Flask(__name__)

app.route('/')
app.route('/index')
def index():
    con = sql.connect('database2.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from giveaways")
    data = cur.fetchall()
    return render_template('index.html', datas=data)
