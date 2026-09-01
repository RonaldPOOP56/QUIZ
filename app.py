from flask import Flask, render_template, request, redirect, url_for
import os
import json

workdir = os.getcwd()
staticdir = os.path.join(workdir, 'static')
print(workdir, staticdir)

app = Flask(__name__, static_folder=staticdir, static_url_path='/static')

@app.route('/')
def index():
    return render_template('user.html')

@app.route('/staff')
def staff():
    return render_template('/portals/portals.html')

@app.route('/staff/create')
def create_quiz():
    return render_template('/portals/create.html')



if __name__ == '__main__':
    app.run(debug=True)