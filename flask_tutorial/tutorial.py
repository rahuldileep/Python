#!/usr/bin/env python3

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!! Welcome to <h1>FLASK WORLD</h1>"

@app.route("/<name>")
def user(name):
	return f"Hello {name}!!!"

@app.route("/admin/")
def admin():
	return redirect(url_for("user",name="Admin"))

if __name__ == "__main__":
    app.run()

