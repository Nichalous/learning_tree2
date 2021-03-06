
###################################################################

##Less than simple assignment 2
##make sure no one can get to a nonexisiting extension route of blackport

from bottle import Bottle, route, run, static_file, abort, error, response, request, hook
import subprocess

##add error403.html
@error(403)
def ediquite(response):
	return static_file("error403.html", root = "/home/nick/projects/blackport")


##add error404.html
@error(404)
def adiquite(response):
	return static_file("error404.html", root ="/home/nick/projects/blackport")

	##include existing possible files so if a case arrises where a file not existing, you get directed to my 404.html

@hook('before_request')
def start_session():
	request.src = request.environ.get('REMOTE_ADDR')

@route("lsof.thang")
def lsofdatthang:
	data = subprocess.check_out(["ps, aux"])
	ws = [()]


@route("/<path:re:.*>", method = "ANY")
def future(path):
	##allow only certain addresses accsess

	if not request.src in ('127.0.0.1', '10.255.0.67', '10.255.0.69', '10.255.0.70'):
		abort(403, "getthouhence!")

	if path == '':
		path = 'index.html'
##printcheck
	if not path in ("cube.jpg", "page2.html", "batarang.jpg", "index.html", "sunflower.jpg"):
		abort(404, "filenotfound")

	if path == "":
		path = "index.html"

	return static_file (path, root = "/home/nick/projects/blackport")

run(host = "10.255.0.67", port = 1069, debug = True)
