#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Erreur lors de la lecture du JSON: {e}")
        return []

def read_csv():
    try:
        products = []
        with open("products.csv", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception as e:
        print(f"Erreur lors de la lecture du CSV: {e}")
        return []

@app.route('/')
def index():
    return redirect(url_for('products', source='json'))

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id:
        products = [p for p in products if p["id"] == product_id]

    if product_id and not products:
        return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


