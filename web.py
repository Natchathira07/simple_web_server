from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
  <body>
    <h1 align="center">Device Specifications</h1>
    <h2 align="right">(Nakshatra)</h2>
    <h3 align="right">(24900864)</h3>
    <ol type="i">
        <li>Device Name - DESKTOP-MOHHBTU</li>
        <li>Processor - 13th Gen Intel Core</li>
        <li>Installed RAM - 16.0 GB</li>
        <li>Device ID - 15EEA3B2-7EF5-4DEC-903D-577382C3C005</li>
        <li>Product ID - 00342-42709-00692-AAOEM</li>
        <li>System type - 64-bit operating system, x64-based processor</li>
        <li>Pen and Touch - No pen or touch input is available for this display</li>
    </ol>
  </body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My web server is running on port 8000...")
httpd.serve_forever()
