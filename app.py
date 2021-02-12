from flask import Flask, render_template, request
from schedule_task import get_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/sent',methods=['POST'])
def send_email():
    if request.method == 'POST':
        email = request.form['email']
        ticker = request.form['ticker']
        get_email(email, ticker)
        
    #return render_template("sent_signal.html",email=email)    


if __name__ == "__main__":
    app.run(debug=True)