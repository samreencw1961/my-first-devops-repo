from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from AWS CodeDeploy - Version 2!</h1>
    <h2>Deployment Successful</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)