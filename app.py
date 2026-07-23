from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "inventory-secret-key"


@app.route("/")
def home():
    return """
    <h1>Inventory Management System</h1>
    <h3>Welcome Rishika 👋</h3>
    <p>Your project setup is successful.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)