from flask import render_template
from bible import app


@app.route('/index', methods=['GET'])
def index():

    return render_template("index.html")
