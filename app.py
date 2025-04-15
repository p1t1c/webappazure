from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask on Azure Web App 👋 update "

if __name__ == "__main__":
    app.run()
