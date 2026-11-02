# EX01 Developing a Simple Webserver
## Date: 28.09.2026

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>EXP 1</title>
    </head>
    <body>
        <i> <u> <h2>Rajamaruthu M</h2> </u> </i>
        <h4>26014342</h4>
        <table border="1" cellspacing="5" cellpadding="5">
            <caption>Device Info</caption>
            <tr>
                <th>S.No</th>
                <th>Device name</th>
                <th>Processor</th>
                <th>Installed RAM</th>
                <th>Graphics card</th>
                <th>Storage	</th>
                <th>Device ID</th>
            </tr>
            <tr>
                <td>1</td>
                <td>TL15-53M-G2</td>
                <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
                <td>16.0 GB (15.7 GB usable)</td>
                <td>Intel(R) Graphics (128 MB)</td>
                <td>477 GB</td>
                <td>666393F2-F183-4046-B4B0-856B06B6E40A</td>
            </tr>


        </table>

    </body>
</html> 
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2026-11-02 220840.png>)

![alt text](<Screenshot 2026-11-02 220948.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
