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