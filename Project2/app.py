from flask import Flask, request, url_for, redirect, render_template, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    con = sql.connect('database2.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from giveaways")
    data = cur.fetchall()
    return render_template('index.html', datas=data)

@app.route('/add_giveaway', methods=["POST", "GET"])
def add_giveaway():
    if request.method == "POST":
        GiveAwayName = request.form["GiveAwayName"]
        Type = request.form["Type"]
        Reward = request.form["Reward"]
        Entries = request.form["Entries"]
        MaxWinners = request.form["MaxWinners"]
        InitialDate = request.form["InitialDate"]
        Duration = request.form["Duration"]

        con = sql.connect('database2.db')
        cur = con.cursor()
        cur.execute('INSERT INTO giveaways (GiveAway Name, Type, Reward, Entries, Max winners, Initial Date, Duration) values (?,?,?,?,?,?,?)', (GiveAwayName, Type, Reward, Entries, MaxWinners, InitialDate, Duration))
        con.commit()
        flash('GiveAway added', 'success')
        return redirect(url_for('index'))
    return render_template('add_giveaway.html')

@app.route('/edit_giveaway/<string:id>', methods=["POST", "GET"])
def edit_giveaway(id):
    if request.method == "POST":
        GiveAwayName = request.form["GiveAwayName"]
        Type = request.form["Type"]
        Reward = request.form["Reward"]
        Entries = request.form["Entries"]
        MaxWinners = request.form["MaxWinners"]
        InitialDate = request.form["InitialDate"]
        Duration = request.form["Duration"]

        con = sql.connect('database2.db')
        cur = con.cursor()
        cur.execute('UPDATE giveaways SET GiveAwayName=?, Type=?, Reward=?, Entries=?, MaxWinners=?, InitialDate=?, Duration=? where id=?', (GiveAwayName, Type, Reward, Entries, MaxWinners, InitialDate, Duration, id))
        con.commit()
        flash('GiveAway updated', 'success')
        return redirect(url_for('index'))
    return render_template('edit_giveaway.html')

@app.route('/delete_giveaway/<string:id>', methods=["GET"])
def delete_giveaway(id):
    con = sql.connect('database2.db')
    cur = con.cursor()
    cur.execute('DELETE FROM giveaways where id=?', (id,))
    con.commit()
    flash('GiveAway deleted', 'success')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = "admin123"
    app.run(debug=True)
