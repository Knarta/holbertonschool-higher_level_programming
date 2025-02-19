#!/usr/bin/python3

"""Task 3: Create an HTTP server that serves the posts from the API"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests


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
        try:
            if self.path == '/data':
                sample_data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                self.send_json(sample_data)
            elif self.path == '/':
                self.send_text("Hello, this is a simple API!")
            elif self.path == '/status':
                self.send_text("OK")
            elif self.path == '/info':
                json_info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
                self.send_json(json_info)
            elif self.path == '/info':
                info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"}
                self.send_json(info)
                json_info = json.dumps(info)
                self.send_json(json_info)
                self.send.response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_info.encode("utf-8"))
            else:
                self.send_text("Not found", 404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write("Not found".encode("utf-8"))


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()
