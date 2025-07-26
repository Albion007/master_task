# server.py
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

httpd = HTTPServer(('localhost', 3000), SimpleHandler)
print("Server started at http://localhost:3000")
httpd.serve_forever()
