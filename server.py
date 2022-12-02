from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/cupcakes")
def cupcakes():
    return render_template("cupcakes.html")

@app.route("/individual_cupcake")
def individual_cupcake():
    return render_template("individual_cupcake.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4545, host = "localhost")