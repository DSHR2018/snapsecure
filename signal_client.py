from fabric.operations import local
from fabric.context_managers import quiet


class SignalClient():
	def __init__(self, phone_number=None):
		self.phone_number = phone_number

	def __run_signal_cmd(self, cmd):
		with quiet():
			r = local("signal-cli -u %s %s" % (self.phone_number, cmd), capture=True)

		return r

	def verify(self, verification_code):
		try:
			r = self.__run_signal_cmd("verify", verification_code)
			return r.succeeded

		except Exception as e:
			print e, type(e)

		return False


	def register(self):
		try:
			r = self.__run_signal_cmd("register")
			return r.succeeded

		except Exception as e:
			print e, type(e)

		return False