from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"


@app.route("/")
def home():
    return "<h1>Hello, world!</h1>"


def main():
    app.run(port=80, host="0.0.0.0")


if __name__ == '__main__':
    main()
