##trying to encrypt this and send it to you...
##just gonna do it with thunderbird

##[nick@loopytunes /]$ sudo gpg -r Nichalous James Gibbons --encrypt /blackport/MK_n

from bottle import run, route, static_file, abort, error, response
import subprocess

#@ host bluelabs route blackport/MK_n
#-insert python for request for credentials
#-call for asana user and pass

"""
def signin(user, password):
	if signin() == "nick@blue-labs.org, BlackBuddyGreyGod1!":
		route "blackport/MK_n/nick"
	elif signin() == david@blue-labs.org:
		route "blackport/MK_n/david"
	else:
		return "you are not athorized accsess" 
def entry(nick, david)
	if "route blackport/MK_n/nick":
		print ("Hey Welcome to my page!!")
		print ("<img> source = /batrang")
"""
@error(404)
def ok(response):
	return static_file("error404.html", root = "/blackport")


@route("/ps")
def ps():
	data = subprocess.check_output(['ps','aux'])
	return data 

@route("/<path:re:.*>", method = "ANY")
def DIF(path):
	if not path in ("", "cube.jpg", "page2.html", "batarang.jpg", "index.html"):
		abort(404, "filenotfound")

	if path == "":
		path = "index.html"

	return static_file (path, root = "/blackport")
	

run(host = "localhost", port = 8080, debug = True) 

