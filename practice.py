
###################################################################

##Less than simple assignment 2
##make sure no one can get to a nonexisiting extension route of blackport

from bottle import Bottle, route, run, static_file, abort, error, response, request, hook
import subprocess, string

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
	if not request.src in ('127.0.0.1', '10.255.0.67', '10.255.0.69', '10.255.0.70'):
		abort(403, "getthouhence!")

@route('/lsofdatthang')
def lsofdatthang():
	# run the "ps aux" command to get all processes
	data = subprocess.check_output(['ps','aux'])

	# change the byte encoded data to a string; b'asdf' => 'asdf'
	data = data.decode()

	# split that one long string into one string per line we got from ps aux
	data = data.split('\n')

	# now use enumerate() around the list of data[] to give us a line number+line...
	# IF that line has the word 'prey' in it, and store the generated list in a
	# new variable called ws
	ws = [(n,x) for n,x in enumerate(data) if 'prey' in x]

	# prepare our data for the HTML template
	webfoo = []
	for row,line in ws:
		webfoo.append('<tr>')
		webfoo.append('  <td>{}</td><td>{}</td>'.format(row,line))
		webfoo.append('</tr>')

	# concatenate this into one string
	pgmdata = '\n'.join(webfoo)

	# build a web page of this data
	html = '''
	<!DOCTYPE html>
	<html>
	<head>
     <title "lsof dat thang!" />
   </head>

   <body>
     <table>
       <tbody>
         ${pgmdata}
       </tbody>
     </table>
   </body>
   </html>
	'''

   # create the template using our initial html string
	T = string.Template(html)

	# fill it in
	html = T.safe_substitute({'pgmdata':pgmdata})

	# finally, send it back to the browser
	return html


@route("/<path:re:.*>", method = "ANY")
def future(path):
	##allow only certain addresses accsess

	if path == '':
		path = 'index.html'

	if not path in ("cube.jpg", "page2.html", "batarang.jpg", "index.html", "sunflower.jpg"):
		abort(404, "filenotfound")

	if path == "":
		path = "index.html"

	return static_file (path, root = "/home/nick/projects/blackport")

run(host = "10.255.0.67", port = 1069, debug = True)
