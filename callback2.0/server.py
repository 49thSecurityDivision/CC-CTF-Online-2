#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

script = '''
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("Hmm... Doesn't seem right...\n".encode('utf-8'))

    def do_POST(self):
        self._set_response()
        if 'Jennys_Number' in self.headers:
          val = self.headers.get('Jennys_Number')
        
          if val != "8675309":
            self.wfile.write("Hmm.. Doesn't seem right...\n".encode('utf-8'))
          else:
            self.wfile.write("Printing flag!!!\n".encode('utf-8'))
            
        else:
          self.wfile.write("Hmm.. Doesn't seem right...\n".encode('utf-8'))
'''
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("{}".format(script).encode('utf-8'))

    def do_POST(self):
        self._set_response()
        if 'Jennys_Number' in self.headers:
          val = self.headers.get('Jennys_Number')
        
          if val != "8675309":
            self.wfile.write("Hmm.. Doesn't seem right...\n".encode('utf-8'))
          else:
            self.wfile.write("Printing flag!!!\n".encode('utf-8'))
            self.wfile.write("flag{kf1YOxYxXQOwEvO8z3OYvHNy8I8BPnCx}".encode('utf-8'))
            
        else:
          self.wfile.write("Hmm.. Doesn't seem right...\n".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
