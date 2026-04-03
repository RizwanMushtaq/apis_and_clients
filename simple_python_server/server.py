from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from raw Python server!")

    def do_POST(self):
        print("Hallo")
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(f"Received POST data: {post_data}")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"post received")


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()
