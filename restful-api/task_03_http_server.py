#!/usr/bin/python3

"""Task 3: Create an HTTP server that serves the posts from the API"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            data = requests.get('https://jsonplaceholder.typicode.com/posts')
            statuscode = data.status_code
            json_data = json.dumps(data.json())
            if statuscode == 200:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_data.encode("utf-8"))
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, a simple API")
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            json_info = json.dumps({
                "status": 200,
                "message": "This is a simple API"
            })
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_info.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


host = 'localhost'
port = 8000

server = HTTPServer((host, port), RequestHandler)
print(f"Server running on {host}:{port}")

server.serve_forever()
