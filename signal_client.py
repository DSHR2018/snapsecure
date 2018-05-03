import os
from hashlib import md5
from json import loads
from fabric.operations import local
from fabric.context_managers import quiet

class SignalClient():
	def __init__(self, username=None):
		try:
			self.user_data = {}

			assert username is not None

			self.user_data[u'username'] = username
			self.user_data.update(self.__query_scli_manifest(['registered']))
			
		except Exception as e:
			print e, type(e)

	def __query_scli_manifest(self, keys):
		try:
			manifest_path = os.path.join(os.path.expanduser('~'), ".config", "signal", "data", self.user_data['username'])
			assert os.path.exists(manifest_path)

			with open(manifest_path, 'rb') as SCLI_MANIFEST:
				return {key : value for key, value in loads(SCLI_MANIFEST.read()).iteritems() if key in keys}

		except Exception as e:
			print e, type(e)

		return {}

	def __run_scli_cmd(self, cmd):
		### XXX HERE!!!
		try:
			with quiet():
				return local("signal-cli -u %s %s" % (self.user_data['username'], cmd), capture=True)

		except Exception as e:
			print e, type(e)

		return None

	def __message_to_dict(self, raw_message):
		try:
			message = {}

			for m in raw_message:
				kvp = m.split(":", 1)
				message[kvp[0].replace(" ", "_").lower()] = kvp[1]

			### XXX HERE!!!
			message['from_alias'] = md5(message['envelope_from']).hexdigest()

			return message
		except Exception as e:
			print e, type(e)

		return None

	def scli_post_image(self):
		try:
			### send off the image to all the people
			return True
		except Exception as e:
			print e, type(e)

		return False

	def scli_poll_messages(self):
		try:
			return [self.__message_to_dict(raw_message) for raw_message in [m.split('\n') for m in self.__run_scli_cmd("receive").split('\n\n')]]

		except Exception as e:
			print e, type(e)

		return None

	def scli_verify(self, verification_code):
		try:
			return self.__run_scli_cmd("verify %s" % verification_code).succeeded

		except Exception as e:
			print e, type(e)

		return False

	def scli_register(self, username):
		try:
			self.user_data['username'] = username
			return self.__run_scli_cmd("register").succeeded

		except Exception as e:
			print e, type(e)

		return False