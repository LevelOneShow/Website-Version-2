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

# prettify_streaming : List -> DOM Element
# Takes streamer data and turns it into readable DOM elements.
def prettify_streaming(ary):
    return ary
template.execute(prettify_online=prettify_online) # Add to template.

# Pages: -----------------------------------------------------------------------

# /: Generates the homepage with active streamers.
class HomepageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(query_data())
        # self.render("home.template.html", streams=query_data()) <- Unlock when 
        #                                                            sample page completed.

# /api: Handles requests to the streamer API.
class APIHanlder(tornado.web.RequestHandler):
    def get(self):
        self.write(query_data())

# App Generation: --------------------------------------------------------------

# App Routes & Settings:
def make_app():
    return Application([
        (r"/", HomepageHandler), # Homepage
        (r"/api", APIHandler), # API
        (r"/api/enroll", tornado.web.RedirectHandler, dict(url=r"/")), # Enroll new API Keys
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