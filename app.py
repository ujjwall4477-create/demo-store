from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "demo_secret_key"

# Product Data
PRODUCTS = {
    "phone": {"name": "Phone", "price": 10000, "img": "phone.jpg"},
    "laptop": {"name": "Laptop", "price": 50000, "img": "laptop.jpg"},
    "headphones": {"name": "Headphones", "price": 2000, "img": "headphones.jpg"},
}

# Home Page
@app.route("/")
def home():
    cart_count = len(session.get("cart", []))
    return render_template("home.html", cart_count=cart_count)

# Products Page
@app.route("/products")
def products():
    cart_count = len(session.get("cart", []))
    return render_template("products.html", products=PRODUCTS, cart_count=cart_count)

# Catalog Page
@app.route("/catalog")
def catalog():
    cart_count = len(session.get("cart", []))
    return render_template("catalog.html", cart_count=cart_count)

# About Page
@app.route("/about")
def about():
    cart_count = len(session.get("cart", []))
    return render_template("about.html", cart_count=cart_count)

# Contact Page
@app.route("/contact")
def contact():
    cart_count = len(session.get("cart", []))
    return render_template("contact.html", cart_count=cart_count)

# Add to Cart
@app.route("/add/<pid>")
def add(pid):
    cart = session.get("cart", [])
    cart.append(pid)
    session["cart"] = cart
    return redirect(url_for("products"))

# Cart Page
@app.route("/cart")
def cart():
    cart_ids = session.get("cart", [])
    items = []
    total = 0

    for cid in cart_ids:
        product = PRODUCTS[cid]
        items.append(product)
        total += product["price"]

    cart_count = len(cart_ids)

    return render_template(
        "cart.html",
        items=items,
        total=total,
        cart_count=cart_count
    )

# Payment Page
@app.route("/payment")
def payment():
    cart_count = len(session.get("cart", []))
    return render_template("payment.html", cart_count=cart_count)

# Clear Cart
@app.route("/clear")
def clear():
    session["cart"] = []
    return redirect(url_for("products"))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

