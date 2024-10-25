from flask import Flask,render_myweb
import smtplib

app=Flask(__name__)

#route() decorators
@app.route('/')
def home():
    return render_myweb('index.html')

if __name__=='__main__':
    app.run(debug=True)
