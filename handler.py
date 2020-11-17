from http.server import BaseHTTPRequestHandler
from finder import Finder
from urllib.parse import parse_qs
import json


class HTTPHandler(BaseHTTPRequestHandler):
    finder = Finder('recommends.csv')

    @staticmethod
    def parse_query_string_(qs):
        qs_dict = parse_qs(qs[2:])
        for q in qs_dict:
            qs_dict[q] = qs_dict[q][0]
        sku = qs_dict.get('sku', '')
        try:
            power = float(qs_dict.get('power', 0))
        except ValueError:
            power = 0
        return sku, power

    def do_GET(self):
        sku, power = self.parse_query_string_(self.path)
        if not sku:
            self.send_response(403, message='Bad Request')
            self.end_headers()
        else:
            rec = self.finder.find_rec(sku, power)
            if rec == -1:
                self.send_response(404, message='Product not found')
                self.end_headers()
            else:
                resp_dict = {'rec': rec}
                self.send_response(200, message='OK')
                self.end_headers()
                self.wfile.write(json.dumps(resp_dict).encode())
