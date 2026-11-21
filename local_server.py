"""
server.py
Zero-dependency HTTP server & REST API for the Mealy <-> Moore Automata Simulator.
Can be started simply with:
    python server.py
Serves the web application at http://localhost:8000 and provides REST endpoints
for conversion and validation.
"""

import http.server
import socketserver
import json
import os
import sys
from urllib.parse import urlparse, parse_qs

# Import python core models & converter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from python_core.automata_models import MealyMachine, MooreMachine
from python_core.converter import mealy_to_moore, moore_to_mealy, verify_equivalence

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class AutomataRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        parsed = urlparse(self.path)
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            payload = json.loads(body.decode("utf-8")) if body else {}
        except Exception as e:
            self.send_error_json(400, f"Invalid JSON payload: {str(e)}")
            return

        if parsed.path == "/api/convert/mealy-to-moore":
            self.handle_mealy_to_moore(payload)
        elif parsed.path == "/api/convert/moore-to-mealy":
            self.handle_moore_to_mealy(payload)
        elif parsed.path == "/api/verify":
            self.handle_verify(payload)
        else:
            self.send_error_json(404, "Endpoint not found")

    def handle_mealy_to_moore(self, payload):
        try:
            mealy = MealyMachine.from_dict(payload)
            prune = payload.get("prune_unreachable", True)
            initial_out = payload.get("initial_moore_output", None)
            moore, steps = mealy_to_moore(mealy, initial_moore_output=initial_out, prune_unreachable=prune)
            response = {
                "success": True,
                "moore_machine": moore.to_dict(),
                "steps": [s.to_dict() for s in steps]
            }
            self.send_json_response(200, response)
        except Exception as e:
            self.send_error_json(400, str(e))

    def handle_moore_to_mealy(self, payload):
        try:
            moore = MooreMachine.from_dict(payload)
            mealy, steps = moore_to_mealy(moore)
            response = {
                "success": True,
                "mealy_machine": mealy.to_dict(),
                "steps": [s.to_dict() for s in steps]
            }
            self.send_json_response(200, response)
        except Exception as e:
            self.send_error_json(400, str(e))

    def handle_verify(self, payload):
        try:
            mealy = MealyMachine.from_dict(payload["mealy"])
            moore = MooreMachine.from_dict(payload["moore"])
            test_strings = payload.get("test_strings", ["", "0", "1", "101", "10101"])
            results = verify_equivalence(mealy, moore, test_strings)
            self.send_json_response(200, {"success": True, "results": results})
        except Exception as e:
            self.send_error_json(400, str(e))

    def send_json_response(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def send_error_json(self, code, message):
        self.send_json_response(code, {"success": False, "error": message})

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), AutomataRequestHandler) as httpd:
        print("=" * 70)
        print("🚀 AUTOSIM: Mealy <-> Moore Automata Simulator Server Running!")
        print(f"👉 Local Web App:  http://localhost:{PORT}")
        print(f"👉 Open in browser: http://127.0.0.1:{PORT}")
        print("=" * 70)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")


if __name__ == "__main__":
    run_server()

