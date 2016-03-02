# Volta Streaming Backend - Asynchronous Web Server
# Written by Nick Pleatsikas - pleatsikas.me

# Contact admin@volta.network to report any bugs.
# View the README for more information.

# Modules: ---------------------------------------------------------------------

# Full Modules:
# import os

# Partial Modules:
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.httpclient import AsyncHTTPClient
from re import sub

# Global Variables: ------------------------------------------------------------

# Port:
port = 8001

# Functions:  ------------------------------------------------------------------

# element_generator : List -> String
# Takes an array with twitch/beam data and turns it into a string readable by
# the browser.
def element_generator(a, service):
    for item in a:
       if item == None:
            continue
       if item.get("service") == service and item.get("online") != False:
            title = item.get("data").get("title")
            url = item.get("data").get("url")
            yield "<a href=%s>%s</a>" % (url, title, )
       else:
            continue

# Pages: -----------------------------------------------------------------------

# /: Generates the homepage with active streamers.
class HomepageHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        # Get JSON from secondary server.
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://localhost:9000/api_data.txt")
        data_pack = tornado.escape.json_decode(response.body.decode("utf-8"))
        # Generate DOM elements.
        twitch_data = element_generator(data_pack, "twitch")
        beam_data = element_generator(data_pack, "beam")
        self.render("html/home.template.html",
            twitch_data=twitch_data,
            beam_data=beam_data)

# /api: Handles requests to the streamer API.
class APIHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://localhost:9000/api_data.txt")
        self.write(response.body.decode("utf-8"))

# /api/enroll: Handles request for adding new API keys. Stub page.
class EnrollKeys(RequestHandler):
    def get(self):
        self.write("<h1>Enrolling Keys Coming Soon</h1>")

# /*(404: non-existent page): Default handler. Handles request for pages
# that don't exist.
class DefaultHandler(RequestHandler):
    def root_url(self):
        url = str(self.request.full_url())
        uri = str(self.request.uri)
        return sub("\%s" % uri, "", url)
    def get(self):
        self.render("html/404.html",
            uri=self.request.uri,
            root_url=self.root_url())

# App Generation: --------------------------------------------------------------

# Settings:
settings = {
    "autoescape": None,
    "default_handler_class": DefaultHandler,
    # "static_path": os.path.join(os.path.dirname(__file__), "/html/bower_components/milligram/dist") This is kind of borked right now.
}

# App Routes & Settings:
def make_app():
    return Application([
        (r"/", HomepageHandler), # Homepage
        (r"/api", APIHandler), # API
        (r"/api/enroll", EnrollKeys), # Enroll new API Keys
    ], **settings)

# Startup: ---------------------------------------------------------------------

# Startup app with these functions and base settings.
def main():
    app = make_app()
    app.listen(port)
    IOLoop.current().start()

# Init:
if __name__ == '__main__':
    main()
