'''
    Created by Sachin Shah
    Copywrite 2019
'''

from flask import request, redirect, session, url_for, send_from_directory, Flask

import os
 

STATIC_FOLDER = './static/'
app = Flask(__name__, static_folder=STATIC_FOLDER)


@app.route('/kernel')
def start():
    return send_from_directory(app.static_folder,'kernels.html')

@app.route('/kmeans')
def kmeans():
    return send_from_directory(app.static_folder,'kmeans.html')

@app.route('/img-flower')
def flower():
    return send_from_directory(app.static_folder,'flower.jpeg')

@app.route('/img-minerals')
def mineral():
    return send_from_directory(app.static_folder,'mineral.jpeg')


@app.route('/style')
def style():
	return send_from_directory(app.static_folder,'style.css')

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)