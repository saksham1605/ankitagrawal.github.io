from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from email.mime.text import MIMEText
import smtplib
import requests
import string
import random

app=Flask(__name__)
app.secret_key='Hello'



@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        data=request.form["Message"]
        name=request.form["name"]
        em=request.form["email"]
        send_email(em,name,data)
        return render_template("index.html")
    else:
        return render_template("index.html")



def send_email(email,name,data):
    from_email="sakshamweb0@gmail.com"
    from_password="Saksham@16"

    to_email="shakti.agarg@gmail.com"
    subject="New Message"
    message="You have new message from  Name<strong> %s</strong> <br>Message: <strong> %s</strong><br>Email: <strong> %s</strong>:"%(name,data,email)
    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)



if __name__=="__main__":
    app.run(debug=True)
