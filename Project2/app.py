from flask import Flask, request, url_for, redirect, render_template, flash
import sqlite3 as sql

app = Flask(__name__)

app.route('/')
app.route('/index')
