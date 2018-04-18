from fabric import settings, local

def register_phone_number(phone_number)
	command = "signal-cli -u %s register" % phone_number
	with settings("hide_everything"):
		result = local(command)

	return result.success

	if result.success =