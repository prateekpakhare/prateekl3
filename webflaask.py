from flask import Flask, render_template, url_for,request, redirect
import requests
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
#    print(url_for('static', filename='air.ico'))
    return render_template('/index2.html')

@app.route('/<username>')
def hello_world2(username=None):
    print(url_for('static', filename='air.ico'))
    return render_template('/index.html',name=username)

@app.route('/components.html')
def hello_world1():
    return render_template('/components.html')

@app.route('/thankyou.html')
def hello_thanks():
    return render_template('/thankyou.html')


@app.route('/blog/2020/new')
def hello_world3():
    return 'this is 2020 new and a new llog'

def write_to_csv(data):
    with open('data.csv', mode='a', newline='') as db:
        name=data["name"]
        email=data["email"]
        message=data["message"]
        csvwriter=csv.writer(db, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        data=request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'there was an error'
