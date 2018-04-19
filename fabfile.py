from fabric.api import settings, local
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
   

	def register_phone_number(phone_number):
		command = "signal-cli -u %s register" % phone_number
		with settings("hide_everything"):
			result = local(command)
		return result.success

	def verify_phone_number(phone_number, verify_number):
		command = "signal-cli -u %s verify %s" % (phone_number, verify_number)
		with settings("hide_everything"):
			result = local(command)
		return result.success

	def send_message(phone_number, message, receive_number):
		command = "signal-cli -u %s send -m ' %s ' %s" % (phone_number, message, receive_number)
		with settings("hide_everything"):
			result = local(command)
		return result.success

	def receive_message(phone_number, duration):
		command = "signal-cli -u %s receive -t %s" % (phone_number, duration)
		with settings("hide_everything"):
			result = local(command)
		return result.success

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()