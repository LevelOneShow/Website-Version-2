# Volta Streaming Backend - Asynchronous Web Server
# Written by Nick Pleatsikas - pleatsikas.me

# Contact admin@volta.network to report any bugs.
# View the README for more information.

# Modules: ---------------------------------------------------------------------

# Full Modules:
import tornado.httpclient
import json

# Partial Modules:
from tornado import gen
from tornado.ioloop import IOLoop 
from tornado.web import RequestHandler, Application, url

# Global Variables: ------------------------------------------------------------

# Port:
port = 8001

# Functions:  ------------------------------------------------------------------

# prettify_online : List -> DOM Element.
# ...
def prettify_online(ary):
    return ary
template.execute(prettify_online=prettify_online) # Add to template.

# Handles all requests to homepage.
class HomepageHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://localhost/test.txt")
        self.write(response.body)
        # self.render("home.template.html", online_streamers_raw=response.body) <- Unlock when 
        #                                                                          sample page completed.

# App Generation: --------------------------------------------------------------

# App Routes & Settings:
def make_app():
    return Application([
        (r"/", HomepageHandler)
    ])

# Startup: ---------------------------------------------------------------------

# Startup app with these functions and base settings.
def main():
    app = make_app()
    app.listen(port )
    IOLoop.current().start()

# Init:
if __name__ == '__main__':
    main()