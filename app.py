from datetime import datetime
from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_there(name=None):
    return render_template(
        'hello_there.html',
        name=name,
        datetime=datetime.now()
    )
