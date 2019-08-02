import http.server as server
import socketserver
import os
import json
import re
import tempfile
from controllers.MotorController import MotorController
from controllers.CameraController import CameraController


class WebUi:
    def __init__(self):
        self.port = 5000
        self.handler = HandlerFactory(Context(), RequestHandler)
        self.handler.protocol_version = "HTTP/1.1"
        self.httpd = socketserver.TCPServer(("", self.port), self.handler)

    def serve(self):
        print("serving at port", self.port)
        self.httpd.serve_forever()

class HandlerFactory(object):
    def __init__(self, ctx, halder_class):
        self.ctx = ctx
        self.handler_class = halder_class

    def __call__(self, *args, **kwargs):
        return self.handler_class(self.ctx, *args, **kwargs)


class Context(object):
    def __init__(self):
        self.images_path = ''
        self.htdocs = ''
        self.ssh_key = ''

class RequestHandler(server.SimpleHTTPRequestHandler):
    def __init__(self, ctx, *args, **kwargs):
        self.simple_handler = SimpleHandler()
        server.SimpleHTTPRequestHandler.__init__(
            self, *args, **kwargs)

    def do_GET(self):
        go = re.match(r'/go', self.path)
        camera = re.match(r'/camera', self.path)
        if go:
            self.simple_handler.handle_go(self.path)
        elif camera:
            self.simple_handler.handle_camera(self.path)
        return server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        return server.SimpleHTTPRequestHandler.do_POST(self)

    def send_head(self):
        """Common code for GET and HEAD commands.
        This sends the response code and MIME headers.
        Return value is either a file object (which has to be copied
        to the output file by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.
        """
        path = self.path
        ctype = self.guess_type(path)
        try:
            # Always read in binary mode. Opening files in text mode may cause
            # newline translations, making the actual size of the content
            # transmitted *less* than the content-length!
            payload = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found ({0})".format(path))
            return None

        if self.command == 'POST':
            self.send_response(202)
        else:
            self.send_response(200)

        stat = os.fstat(payload.fileno())

        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-type", ctype)
        self.send_header("Content-Length", str(stat.st_size))
        self.send_header("Last-Modified", self.date_time_string(stat.st_mtime))
        self.end_headers()

        return payload
        

class SimpleHandler:
    def __init__(self):
        self.motor_controller = MotorController()
        self.camera_controller = CameraController()
        
    def get_params(self, path):
        # split by ? and get all parameters string
        splited_path = path.split('?')[1]
        # split & to get all parameters
        splited_params = splited_path.split('&')
        params = {}
        for param in splited_params:
            splited_param = param.split('=')
            key = splited_param[0]
            value = splited_param[1]
            params[key] = value
        return params
        
    def handle_go(self, path):
        params = self.get_params(path)
        if 'direction' in params:
            direction = params['direction']
            if direction == 'forward':
                self.motor_controller.forward()
            elif direction == 'reverse':
                self.motor_controller.reverse()
            elif direction == 'right':
                self.motor_controller.turn_right()
            elif direction == 'left':
                self.motor_controller.turn_left()
            elif direction == 'pivot_right':
                self.motor_controller.pivot_right()
            elif direction == 'pivot_left':
                self.motor_controller.pivot_left()
            else:
                pass
                
    def handle_camera(self, path):
        params = self.get_params(path)
        if 'direction' in params:
            direction = params['direction']
            if direction == 'left':
                self.camera_controller.move_left()
            elif direction == 'right':
                self.camera_controller.move_right()
            elif direction == 'center':
                self.camera_controller.move_center()
            else:
                pass
        
                
        
