from flask import Flask, render_template, url_for 


app = Flask(__name__)
app.secret_key = "hello"

@app.route("/login")


def login():
    return render_template("")


app.route("/home")


def home():
    return render_template("")



if __name__ == "__main__":
    app.run(debug=True)