from flask import Flask, render_template, request
import dataExtract
import pandas as pd

#print("HelloWorld")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Login.html')

@app.route('/send', methods=['POST'])
def send():

    if request.method=='POST':
        form = request.form
        username = form.get("username")
        password = form.get("password")
        
        passwordData, emailData = dataExtract.getUser(username)
        #print(passwordData)

        if passwordData == password :
            return render_template('username.html', username = username, email = emailData)   
        else:
            return render_template('Login.html')

    #return render_template('Login.html')

if __name__ == "__main__":
    app.run(debug = True)