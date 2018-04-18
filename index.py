import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def register_phone_number(phone_number)
	command = "signal-cli -u %s register" % phone_number
	with settings("hide_everything"):
		result = local(command)

	return result.success

	def send_message(message)
	command = "signal-cli -u %s send" % phone_number
	with settings("hide_everything"):
		result = local(command)

	return result.success

	def receive_message(phone_number)
	command = "signal-cli -u %s register" % phone_number
	with settings("hide_everything"):
		result = local(command)

	return result.success

    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()