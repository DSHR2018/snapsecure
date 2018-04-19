from time import sleep
import tornado.ioloop, tornado.web, tornado.httpserver, tornado.template
from signal_client import SignalClient
import views


class WebClient(tornado.web.Application):
	def __init__(self):
		port = 8080
		routes = [
			(r"/", self.IndexHandler),
			(r"/register", self.RegistrationHandler),
			(r"/verify", self.VerificationHandler),
			(r"/chat/([a-z0-9]+)", self.ChatHandler),
			(r"/new", self.ChosseFriendsHandler)
		]

		tornado.web.Application.__init__(self, routes, ui_modules=views, template_path="html")
		
		self.listen(port)
		tornado.ioloop.IOLoop.current().start()

	class WebAppTemplate(tornado.web.RequestHandler, SignalClient):
		def initialize(self):
			### XXX HERE!!!
			SignalClient.__init__(self, username=self.get_cookie("username"))

		def get(self, tmpl, **kwargs):
			self.render(tmpl, **kwargs)

	class IndexHandler(WebAppTemplate):
		def get(self):
			try:
				assert self.user_data['registered']

				super(WebClient.IndexHandler, self).get("index.html", title="Home", chats=self.scli_poll_messages())
			except Exception as e:
				print e, type(e)
				self.redirect("/register")

	class RegistrationHandler(WebAppTemplate):
		def get(self):
			super(WebClient.RegistrationHandler, self).get("register.html", title="Register")

		def post(self):
			### XXX HERE!!!
			username = self.get_argument('phone_number')

			if self.scli_register(username):
				self.set_cookie("username", username)
				self.redirect("/verify")
				return
			
			sleep(4)
			self.redirect("/register")

	class VerificationHandler(WebAppTemplate):
		def get(self):
			super(WebClient.VerificationHandler, self).get("verify.html", title="Verify")

		def post(self):
			### XXX HERE!!!
			verification_code = self.get_argument('verification_code')

			if self.scli_verify(verification_code):
				self.redirect("/")
				return

			sleep(4)
			self.redirect("/register")

	class ChatHandler(WebAppTemplate):
		def get(self):
			chat_id = None
			super(WebClient.ChatHandler, self).get("chat.html", title="Chat with %s" % chat_id)

	class ChosseFriendsHandler(WebAppTemplate):
		def get(self):
			super(WebClient.ChosseFriendsHandler, self).get("choose_friends.html", title="Choose Friends...")

		def post(self):
			friends_ids = self.get_argument("friend_ids")

if __name__ == "__main__":
    w = WebClient()