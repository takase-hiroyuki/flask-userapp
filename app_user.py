from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<name>")
def user_page(name):
    return render_template("user.html", username=name)
