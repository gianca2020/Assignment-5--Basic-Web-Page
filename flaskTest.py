from flask import Flask
from flask_mailman import Mail, EmailMessage

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config["MAIL_SERVER"] = "smtp.fastmail.com"
    app.config["MAIL_PORT"] = "465"
    app.config["MAIL_USERNAME"] = "napoliee@fastmail.com"
    app.config["MAIL_PASSWORD"] = "9jq5zzypelx8qrx2"
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    mail.init_app(app)

    @app.route("/")
    def index():
        msg = EmailMessage(
            "here is the title",
            "This is my test with frameworks :)",
            "napoliee@fastmail.com",
            ["napoliee@fastmail.com"]
        )
        msg.send()
        return "sent email..."

    return app
