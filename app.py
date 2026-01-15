import http.server, socketserver, subprocess, urllib.parse

PORT = 7860

CHANNELS = {
    "1": "https://cdn-rum.n2olabs1.pro/stream.m3u8?url=https%3A%2F%2Flivecdn.rumsport1.com%2Fstream%2F32%2Findex.m3u8&token=974f02da632f48a22f2d865568744dfacfe8c0d3&is_vip=false&verify=1768456800-xyD9GB8ljJJLq1CMQQRzkj5JNYjyEHemLgiMKirTeXg%3D"
}

UA = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
REF = "https://xiaolin.live/"

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True # পোর্ট জ্যাম হওয়া আটকাবে

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        channel_id = query.get('id', ['1'])[0]

        if channel_id in CHANNELS:
            self.send_response(200)
            self.send_header('Content-type', 'video/mp2t')
            self.send_header('Access-Control-Allow-Origin', '*') # প্লেয়ারে প্লে হওয়ার অনুমতি
            self.send_header('Connection', 'keep-alive')
            self.end_headers()
            
            link = CHANNELS[channel_id]
            # বাফারিং ফ্রি সেটিংস
            cmd = ['streamlink', '--stdout', '--hls-live-edge', '2', '--hls-segment-threads', '3', '--http-header', f'User-Agent={UA}', '--http-header', f'Referer={REF}', link, 'best']
            
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None)
            try:
                while True:
                    data = proc.stdout.read(16384) # ১৬ কিলোবাইট বাফার
                    if not data: break
                    self.wfile.write(data)
            except:
                proc.kill()
        else:
            self.send_response(404)
            self.end_headers()

# 0.0.0.0 ব্যবহার করা হয়েছে যাতে Ngrok এটিকে খুঁজে পায়
with ThreadedHTTPServer(("0.0.0.0", PORT), H) as httpd:
    print(f"Server started on port {PORT}")
    httpd.serve_forever()
