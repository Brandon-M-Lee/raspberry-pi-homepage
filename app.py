from flask import Flask, render_template
from route import result
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result')
def result_page():
    return result.result_get()