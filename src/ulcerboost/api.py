from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import time

from ulcerboost.model import predict_ulcer_risk
from ulcerboost.storage import save_patient, load_patients


STATIC_DIR = Path(__file__).resolve().parent / "static"
HOST = "127.0.0.1"
PORT = 8080


class UlcerBoostHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/patients":
            self.send_json({"patients": load_patients()})
            return
        if self.path == "/api/health":
            self.send_json({"status": "ok", "app": "UlcerBoost"})
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/predict":
            self.send_json({"error": "Endpoint not found."}, status=404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        payload = self.rfile.read(length).decode("utf-8") if length else "{}"
        features = json.loads(payload)
        prediction = predict_ulcer_risk(features)
        record = {
            "id": f"PUD-{str(int(time.time() * 1000))[-6:]}",
            "name": features.get("name", "New Patient"),
            "age": features.get("age"),
            **prediction,
        }
        save_patient(record)
        self.send_json({"prediction": record}, status=201)

    def send_json(self, payload, status=200):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    server = ThreadingHTTPServer((HOST, PORT), UlcerBoostHandler)
    print(f"UlcerBoost preview running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
