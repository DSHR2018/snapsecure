import tornado.ioloop, tornado.web, tornado.httpserver
from signal_client import SignalClient

class WebClient(tornado.web.Application):
	def __init__(self):
		port = 8080
		routes = [
			(r"/", self.IndexHandler),
			(r"/register", self.RegistrationHandler),
			(r"/verify", self.VerificationHandler)
		]

		tornado.web.Application.__init__(self, routes)
		
		self.listen(port)
		tornado.ioloop.IOLoop.current().start()

	class IndexHandler(tornado.web.RequestHandler, SignalClient):
	    def get(self):
	        self.write("Hello, world")

	class RegistrationHandler(tornado.web.RequestHandler, SignalClient):
		def get(self):
			SignalClient.__init__(self)
			self.write("Register success" if self.register() else "Could not register phone number")

	class VerificationHandler(tornado.web.RequestHandler):
		def get(self):
			SignalClient.__init__(self)
			self.write("Verification success" if self.verify() else "Could not verify phone number")


if __name__ == "__main__":
    w = WebClient()