#!/usr/bin/env python3
"""
Usage:
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class S(BaseHTTPRequestHandler):
    team1score = 0
    team2score = 0
    


    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()

    def do_OPTIONS(self):         
        self._set_response()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
        
        #print(post_data)
        
        data = str(post_data)
        #print(data.find(':'))
        section = data[4:data.find(":") - 1]
        print(section)
        value = data[data.rfind(":") + 2:data.rfind("|")]
        #print(value)
        
        
        
        if(section == "team1score"):
            f = open("team1score.txt", "r")
            team1score = int(f.read())
            f.close();
            f = open("team1score.txt", "w")
            team1score += 1
            f.write(str(team1score))
            f.close()
        elif(section == "team2score"):
            f = open("team2score.txt", "r")
            team2score = int(f.read())
            f.close();
            f = open("team2score.txt", "w")
            team2score += 1
            f.write(str(team2score))
            f.close()
        elif(section == "reset"):
            f = open("team1score.txt", "w")
            team1score = 0;
            f.write(str(team1score))
            f.close();
            f = open("team2score.txt", "w")
            team2score = 0;
            f.write(str(team2score))
            f.close();
        
def run(server_class=HTTPServer, handler_class=S, port=28015):
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
