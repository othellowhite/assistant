import http.server

HTTP_PORT = 8282

def exec():
	httpd = http.server.ThreadingHTTPServer(("",HTTP_PORT), http.server.SimpleHTTPRequestHandler)
	httpd.serve_forever()