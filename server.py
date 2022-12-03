from flask import Flask, render_template, url_for, redirect
from cupcakes import return_csv_list, find_cupcakes, add_cupcake_dictionary
import csv

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

@app.route("/secret")
def secret():
    return render_template("secret.html")

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

@app.route('/delete-order/<index>')
def delete_order(index):
    try:
        index = int(index)
        orders_file = "orders.csv"
        orders = return_csv_list(orders_file)
        assert index >= 0
        assert index < len(orders)

        orders.pop(index)
        with open(orders_file, "w", newline="\n") as csvfile:
            fieldnames= ["type", "name", "cake", "price", "filling", "frosting", "sprinkles"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for order in orders:
                writer.writerow(order)

    except AssertionError:
        pass
    return redirect(url_for("order"))

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 4545, host = "localhost")