#!/usr/bin/env python3
"""Servidor estatico minimo para previa dos mockups Vela."""
import http.server
import socketserver
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 4178

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/avaliacoes/cadastro-avaliacao.html"
        return super().do_GET()

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"serving mockups at http://127.0.0.1:{PORT}/")
    httpd.serve_forever()
