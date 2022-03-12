from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/admin')
def about():
    return 'Nothing in directory trust me.'

@app.route('/robot.txt')
def robot():
    return 'Congrat!!! you have found SensitiveData'