__module_name__ = "No name... yet"
__module_version__ = "0.1"
__module_description__ = "No description... yet"

import xchat
from subprocess import call

# Select the rooms and the users that you want to receive notifications
# 'users' = ['', '']
# 'rooms' = ['#OeSC-Livre', '#ubuntu-br'],

config = {
	'users' : ['', '', '', ''],
	'rooms' : ['#OeSC-Livre', '#ubuntu-br'],
}


# Callback to notify when a new user join
def join_cb(word, word_eol, userdata):
	user = word[0].partition('!')[0][1:]
	room = word[2]

	if xchat.get_info("nick") != user:
		call(["notify-send", "--icon=avatar-default", user, "Is online at "+room+"."])	
	
	return xchat.EAT_NONE

# Callback to notify when a new private message
def private_cb(word, word_eol, userdata):
	user = word[0].partition('!')[0][1:]
	room = word[2]
	message = word_eol[3][2:]
	if xchat.get_info("nick") in message:
		call(["notify-send", "--icon=xchat", user + " at " + room + " says:", message])
	return xchat.EAT_NONE

# Callback to print a message when unload module
def unload_cb(userdata):
	print "Unload Join Notify module"

xchat.prnt("Join Notify module loaded")
xchat.hook_server("JOIN", join_cb)
xchat.hook_server("PRIVMSG", private_cb)
xchat.hook_unload(unload_cb)
