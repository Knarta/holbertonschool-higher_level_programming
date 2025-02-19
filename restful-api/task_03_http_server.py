#!/usr/bin/python3

"""Task 3: Create an HTTP server that serves the posts from the API"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):
    def send_text(self, data, status=200):
        """Helper function to send plain text responses"""
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

    def send_json(self, data, status=200):
        """Helper function to send JSON responses"""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_json(data)
        elif self.path == '/status':
            self.send_text("OK")
        elif self.path == '/info':
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"}
            self.send_json(info)
        elif self.path == '/':
            self.send_text("Hello, this is a simple API!")
        else:
            self.send_text("Endpoint not found", 404)


if __name__ == "__main__":
    host = "localhost"
    port = 8000
    httpd = HTTPServer((host, port), RequestHandler)
    print("Starting server on http://localhost:8000")
    httpd.serve_forever()
