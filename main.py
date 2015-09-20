import tornado.httpclient
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://localhost/test.txt")
        self.write(response.body)

def make_app():
    return Application([
        (r"/", MainHandler)
    ])

def main():
    app = make_app()
    app.listen(8080)
    IOLoop.current().start()

if __name__ == '__main__':
    main()