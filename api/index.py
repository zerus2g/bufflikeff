from http.server import BaseHTTPRequestHandler
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
import uvicorn

class VercelHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Serve the main app
        from fastapi.responses import HTMLResponse
        from fastapi import Request
        
        # Create a mock request
        request = Request(scope={
            'type': 'http',
            'method': 'GET',
            'path': self.path,
            'headers': []
        })
        
        # Get response from FastAPI app
        response = app.get("/")(request)
        self.wfile.write(response.body)
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Handle POST requests
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Process the request
        from fastapi import Request
        request = Request(scope={
            'type': 'http',
            'method': 'POST',
            'path': self.path,
            'headers': []
        })
        
        # Get response from FastAPI app
        response = app.post("/api/buff")(request)
        self.wfile.write(response.body)

def handler(request, context):
    """Vercel serverless function handler"""
    return VercelHandler(request, context) 