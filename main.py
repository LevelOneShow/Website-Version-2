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

# prettify_streaming : List -> DOM Element.
# Takes streamer data and turns it into readable DOM elements.
def prettify_streaming(ary):
    return ary
template.execute(prettify_online=prettify_online) # Add to template.

# Generates the homepage with active streamers.
class HomepageHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://localhost:9000/api_data.txt")
        self.write(response.body)
        # self.render("home.template.html", streams=response.body) <- Unlock when 
        #                                                                          sample page completed.

# Handles requests to the streamer API.
class APIHanlder(tornado.web.RequestHandler):
    def get(self):
        self.write("Data coming soon...")

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