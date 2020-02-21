from http.server import BaseHTTPRequestHandler, HTTPServer  # python3
from logparser_bit import string_parse
from socketserver import ThreadingMixIn
import json
import threading
import chardet
USE_HTTPS = False


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        '''Setting headers'''
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        '''Receive get requests'''
        self._set_headers()
        self.wfile.write(b'received get request\n')

    def do_POST(self):
        '''Receive get requests and read post request body'''
        self._set_headers()
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        content_type = (chardet.detect(post_body))
        print(content_type)
        dec_body = post_body.decode('latin_1')
        thread_number = threading.currentThread().getName()[-1]
        json_file_name = 'data{0}.json'.format(thread_number)
        with open(json_file_name, "w") as file_j:   # Here we create our files depending on thread
            file_j.write('[')
        wrong_file_name = 'wrong{0}.txt'.format(thread_number)
        with open(wrong_file_name, "w") as wrong_f:
            pass
        count_right = 0
        count_wrong = 0
        for i in dec_body.split('\n'):  # Here we use our parser for lines and add processed lines to files
            answer = string_parse(i)
            if type(answer) == dict:
                count_right += 1
                with open(json_file_name, "a") as file_j:
                    json.dump(answer, file_j)
            else:
                count_wrong += 1
                with open(wrong_file_name, "a") as wrong_f:
                    wrong_f.write(answer + '\n')
        with open(json_file_name, "a") as file_j:
            file_j.write(']')
        self.wfile.write(b'received post request\nCount of right strings = ' + str(count_right).encode() + b'\n'
                         + b'Count of wrong strings = ' + str(count_wrong).encode() + b'\n')    # Return answer

    def do_PUT(self):
        self.do_POST()


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    '''Starting our threads'''
    pass


if __name__ == "__main__":
    host = ''
    port = 8443
    server = ThreadingSimpleServer((host, port), HandleRequests)
    if USE_HTTPS:   # If you want to use ssl then change USE_HTTPS to True
        import ssl

        server.socket = ssl.wrap_socket(server.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True)
    try:
        server.serve_forever()  # Starting our server
    except KeyboardInterrupt:
        pass
