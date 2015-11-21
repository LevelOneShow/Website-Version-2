# Volta Streaming Backend - Asynchronous Web Server
# Written by Nick Pleatsikas - pleatsikas.me

# Contact admin@volta.network to report any bugs.
# View the README for more information.

# Modules: ---------------------------------------------------------------------

# Full Modules:
import tornado

# Partial Modules:
from tornado import gen
from tornado.ioloop import IOLoop 
from tornado.web import RequestHandler, Application, url
from tornado.httpclient import AsyncHTTPClient

# Global Variables: ------------------------------------------------------------

# Port:
port = 8001

# Functions:  ------------------------------------------------------------------

# element_generator : List -> String
# Takes an array with twitch/beam data and turns it into a string readable by 
# the browser.
def element_generator(ary, service):
    for item in ary:
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
class HomepageHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
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
class APIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://localhost:9000/api_data.txt")
        self.write(response.body.decode("utf-8"))
        
# /api/enroll: Handles request for adding new API keys. Stub page.
class EnrollKeys(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Enrolling Keys Coming Soon</h1>")
        
# /*(404: non-existent page): Default handler. Handles request for pages that
# don't exist.
class DefaultHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Oops. Looks like this page doesn't exist.</h1>")

# App Generation: --------------------------------------------------------------

# Settings:
settings = {
    "autoescape": None,
    "default_handler_class": DefaultHandler,
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

# App Routes & Settings:
def make_app():
    return Application([
        (r"/", HomepageHandler), # Homepage
        (r"/api", APIHandler), # API
        (r"/api/enroll", EnrollKeys) # Enroll new API Keys
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