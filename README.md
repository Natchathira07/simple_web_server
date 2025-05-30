# EX01 Developing a Simple Webserver

# Date:27/03/2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
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
```
# OUTPUT:
![Screenshot 2025-05-30 103036](https://github.com/user-attachments/assets/fe21d0a1-ad33-4683-9e47-8891ba330785)

![alt text](<Screenshot 2025-04-09 232049.png>)

# RESULT:
The program for implementing simple webserver is executed successfully.
