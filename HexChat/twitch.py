import hexchat

__module_name__ = 'Twitch'
__module_author__ = 'TingPing'
__module_version__ = '0'
__module_description__ = 'Better integration with Twitch.tv'
# Very much a work in progress...

# Best used with my 'mymsg.py' script so you can sync your messages with the web clients.

# Commands from http://help.twitch.tv/customer/portal/articles/659095-chat-moderation-commands
# /ban may conflict with other scripts nothing we can do about that
# /clear is an existing command, just override it
commands = ['timeout', 'slow', 'slowoff', 'subscribers', 'subscribersoff',
  		'mod', 'unmod', 'mods', 'clear', 'ban', 'unban', 'commercial']

def is_twitch():
	if 'twitch.tv' in hexchat.get_info('server'):
		return True
	else: return False

# Print jtv messages in front tab.. to improve.
def msg_cb(word, word_eol, userdata):
	if is_twitch() and hexchat.nickcmp(word[0], 'jtv') == 0:
		hexchat.find_context().emit_print('Private Message', word[0], word[1])
		return hexchat.EAT_ALL

# Eat any message starting with a '.', twitch eats all of them too.
def yourmsg_cb(word, word_eol, userdata):
	if is_twitch() and word[1][0] == '.':
		return hexchat.EAT_ALL

# Just prefix with a '.'.
def command_cb(word, word_eol, userdata):
	if is_twitch():
		hexchat.command('say .{}'.format(word_eol[0]))
		return hexchat.EAT_ALL

for cmd in commands:
	hexchat.hook_command(cmd, command_cb)
hexchat.hook_print('Private Message to Dialog', msg_cb)
hexchat.hook_print('Your Message', yourmsg_cb)
