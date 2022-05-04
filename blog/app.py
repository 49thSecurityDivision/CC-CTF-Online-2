#!/usr/bin/python3
from flask import Flask, session, redirect, url_for, request, render_template
from flask_session import Session

app = Flask(__name__)
app.secret_key = b'0xvrvik'

SESSION_TYPE = 'memcached'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('admin'))
    else:
        return render_template('index.html')

@app.route('/admin')
def admin():
    if 'username' not in session:
        return redirect(url_for('index'))
    else:
        return render_template('admin.html', username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print('Here')
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Incorrect username or password'
        else:
            session['username'] = 'admin'
            return redirect(url_for('admin'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)