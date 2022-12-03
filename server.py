from flask import Flask, render_template, url_for, redirect
from cupcakes import return_csv_list, find_cupcakes, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cupcakes = return_csv_list("cupcakedisplay.csv"))

@app.route("/order")
def order():
    return render_template("order.html", orders = return_csv_list("orders.csv"))

@app.route("/cupcakes")
def cupcakes():
    return render_template("cupcake.html")

@app.route("/individual_cupcake")
def individual_cupcake():
    return render_template("individual_cupcake.html")

@app.route('/add-cupcake/<name>')
def add_cupcake(name):
    cupcake = find_cupcakes("cupcakedisplay.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Cupcake not found."

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4545, host = "localhost")