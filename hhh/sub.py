import http.server
import socketserver
import subprocess

# Define the port number for the server
PORT = 8080

# Define the handler to serve the requests
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Run your Python code and capture the output
        output = subprocess.check_output(['python', 'come.py'])
        
        # Set the response headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Send the output as the response body
        self.wfile.write(output)

# Create the server with the specified handler
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
