# Volta Streaming Backend - Asynchronous Web Server
# Written by Nick Pleatsikas - pleatsikas.me

# Contact admin@volta.network to report any bugs.
# View the README for more information.

# Modules: ---------------------------------------------------------------------

# Full Modules:
import tornado.httpclient

# Partial Modules:
from tornado import gen
from tornado.ioloop import IOLoop 
from tornado.web import RequestHandler, Application, url

# Global Variables: ------------------------------------------------------------

# Port:
port = 8001

# Functions:  ------------------------------------------------------------------

# query_data : GET -> String
# Asychronously reads text file on localhost:9000 and outputs the response.
@tornado.gen.coroutine
def query_data():
    http = tornado.httpclient.AsyncHTTPClient()
    response = yield http.fetch("http://localhost:9000/api_data.txt")
    return response.body

# insert_to_DOM : List -> String
# Takes streamer data and turns it into a string readable by the browser.
def insert_to_DOM(ary, service):
    for item in ary:
        if item.get('service') == service:
            title = item.get("title")
            url = item.get("url")
            return "<a href=%s>%s</a>" % (url, title, )
        else:
            continue
# Gives HTML templates access to this function.
template.execute(insert_to_DOM=insert_to_DOM)

# Pages: -----------------------------------------------------------------------

# /: Generates the homepage with active streamers.
class HomepageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("/html/home.template.html", stream_data=query_data())

# /api: Handles requests to the streamer API.
class APIHanlder(tornado.web.RequestHandler):
    def get(self):
        self.write(query_data())
        
# /api/enroll: Handles request for adding new API keys. Stub page.
class EnrollKeys(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Enrolling Keys Coming Soon</h1>")

# App Generation: --------------------------------------------------------------

# App Routes & Settings:
def make_app():
    return Application([
        (r"/", HomepageHandler), # Homepage
        (r"/api", APIHandler), # API
        (r"/api/enroll", EnrollKeys) # Enroll new API Keys
    ])

# Startup: ---------------------------------------------------------------------

# Startup app with these functions and base settings.
def main():
    app = make_app()
    app.listen(port)
    IOLoop.current().start()

# Init:
if __name__ == '__main__':
    main()