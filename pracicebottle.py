
###################################################################

##Less than simple assignment 2
##make sure no one can get to a nonexisiting extension route of blackport

from bottle import Bottle, route, run, static_file, abort, error, response
import subprocess

##add error404.html
@error(404)
	def adiquite(response):
			return static_file("error404.html", root ="/blackport")

		##include existing possible files so if a case arrises where a file not existing, you get directed to my 404.html

@route("/<path:re:.*>", method = "ANY")
	def furture(path):
		if not path in ("", "cube.jpg", "page2.html", "batarang.jpg", "index.html", "sunflower.jpg"):
				abort(404, "filenotfound")

		if path == "":
				path = "index.html"

			return static_file (path, root = "/blackport")

##add error403.html
@error(403)
	def ediquite(response):
			return static_file("error403.html", root = "/blackport)

		##allow only certain addresses accsess

		if not path in(127.0.0.1, 10.255.0.67, 10.255.0.69, 10.255.0.70., int('') 
			abort(403, "getthouhence!")

		if path == int(''):
				path = "index2.html"

##run on host 192.168.0.4

run(host = 192.168.0.4, port = 69, debug = True)