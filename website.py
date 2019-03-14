#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import memcache
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    dIO = mc.get("doorIsOpen")
    graph = mc.get("graph")
    days = [day for day, _ in graph]
    values = [value for _, value in graph]
    return render_template("index.html", doorIsOpen=bool(dIO), days=days, values=values)


if __name__ == "__main__":
    mc = memcache.Client(['127.0.0.1:11211'])
    app.run(debug=True)
