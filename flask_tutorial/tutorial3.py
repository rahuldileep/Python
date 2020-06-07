#!/usr/bin/env python3

from flask import Flask, redirect, url_for, render_template
import pygal

app = Flask(__name__)


@app.route('/NDRexample/')
def pygalexample():
	try:
		graph = pygal.Line()
		graph.title = 'NDR values for different features.'
		graph.x_labels = ['r61x','r65x','r71x','r70x']
		graph.add('IPv4', [138, 141, 139, 138])
		graph.add('IPv6', [177, 176, 176, 178])
		graph.add('v4_QoS',  [232,  233, 230, 231])
		graph.add('v4_ACL',  [205, 203, 206, 204])
		graph_data = graph.render_data_uri()
		return render_template("graphing.html", graph_data = graph_data)
	except Exception as e:
		return(str(e))

if __name__ == "__main__":
	app.run()