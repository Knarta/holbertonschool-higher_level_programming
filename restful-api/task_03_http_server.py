#!/usr/bin/python3

"""Task 3: Create an HTTP server that serves the posts from the API"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/data':
                sample_data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(sample_data).encode("utf-8"))
            elif self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Hello, this is a simple API!")
            elif self.path == '/status':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"OK")
            elif self.path == '/info':
                json_info = json.dumps({
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                })
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json_info.encode("utf-8"))
            else:
                self.send_error(404, "Endpoint not found")
        except Exception as e:
            self.send_error(500, str(e))


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running at localhost:{port}")
    httpd.serve_forever()
    
