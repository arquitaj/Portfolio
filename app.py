from flask import Flask, render_template, url_for, request
from flask_mail import Mail, Message


my_email = "arquitaj.python@gmail.com"
password = "xcsa xqwz vlow hfth"

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = my_email
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route('/', methods =["GET", "POST"])
@app.route('/home', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("full-name")
        email = request.form.get("email")
        content = request.form.get("message")

        message = Message(
            subject = name + ' is sending you a message via your Portfolio',
            recipients = [my_email],
            sender = (name, email)
        )
        message.html = content + " <b><br><b><br>Sender Information:<br>Name : "+name+"<br>Email: "+email
        mail.send(message)

        return 'Message sent'
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)