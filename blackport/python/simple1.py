
##pushing test file to request completion of bottle.py acl conf

"""from bottle import route, run, template

@route('/titania/<name>')
def index(name):
	return template('<b> WAKE ME UP {{name}}</b.!', name=name)

	run(host='localhost, port=8080')
"""
#initial pages for simple assignment 1
from bottle import Bottle, route, run, static_file, abort, error, response
import subprocess

app = Bottle()

@app.route('/blackport/<pagename>')
def blackport():
	if pagename == route('/blackport/wiekie'):
		print("hey alex! hi CINDY! was up DJ")
	elif pagename == route('/blackport/LGT'):
		print("Was up Light Fam!!!")
		print("<img> source = /desktop/buinessss/sunflower.jpg")
		return

run(app, host='localhost', port=8080, debug=True)
###################################################################
