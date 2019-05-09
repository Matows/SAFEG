#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import memcache as mc
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    global db
    if request.method == 'GET':
        dIO = db.get("doorIsOpen")
        graph = db.get("graph")
        # Have to init DataManager first
        days = [day for day, _ in graph]
        values = [value for _, value in graph]
        return render_template("index.html", doorIsOpen=bool(dIO), days=days, values=values)
    elif request.method == 'POST':
        if request.form["door"] == "close":
            db.set("door", "close")
        elif request.form["door"] == "open":
            db.set("door", "open")

def run():
    try:
        global db
        db = mc.Client(['127.0.0.1:11211'])
        app.run(debug=True)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()
