import tornado.httpclient
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url

def open_file(name):
    f = open(name, 'r')
    f.read()

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield open_file('test.txt')
        # http.fetch("https://api.twitch.tv/kraken/streams/AntVenom")
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(json))

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
