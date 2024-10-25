from flask import Flask,render_templates
import smtplib

app=Flask(__name__)

#route() decorators
@app.route('/')
def home():
    return render_templates('index.html')

if __name__=='__main__':
    app.run(debug=True)
