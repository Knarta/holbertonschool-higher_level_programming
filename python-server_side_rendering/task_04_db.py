#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filepath} not found")
        return []

def read_csv(filepath):
    try:
        products = []
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        print(f"File {filepath} not found")
        return []

def fetch_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        products = cursor.fetchall()
        conn.close()
        return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = fetch_from_sqlite()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)