from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<name>")
def user_page(name):
    return render_template("user.html", username=name)

@app.route("/")
def index():
    return """
    <h1>Flask User App</h1>
    <p>次の形式でアクセスしてください：</p>
    <ul>
      <li><a href="/user/hiro">/user/hiro</a></li>
      <li><a href="/user/あなたの名前">/user/あなたの名前</a></li>
    </ul>
    """

@app.route("/user/")
def user_root():
    return """
    <h2>ユーザー名が指定されていません</h2>
    <p>次のように URL にユーザー名を追加してください：</p>
    <ul>
      <li><a href="/user/hiro">/user/hiro</a></li>
    </ul>
    """
 
