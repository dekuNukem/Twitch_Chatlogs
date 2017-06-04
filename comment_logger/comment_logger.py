import os
import sys
import time
import socket
import irc_bot
from datetime import datetime

# change it to your own
# get your oauth here: https://twitchapps.com/tmi/
username = "Twitch_Plays_3DS"
oauth = 'oauth:qmdwk3rsm4qau59zf2dpxixsf4wxzf'

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        print("creating directory " + dir_path)
        os.makedirs(dir_path)

def log_add(path, content):
	ensure_dir(current_directory + '/comment_log')
	ensure_dir(current_directory + '/comment_log_raw')
	with open(path, mode='a', encoding='utf-8') as log_file:
		log_file.write(content)

def safe_print(content):
	try:
		print(content)
	except UnicodeEncodeError:
		print(content.encode('utf-8'))

if(len(sys.argv) != 2):
    print(__file__ + ' channel')
    sys.exit(0)

chat_channel = sys.argv[1]
chat_server = ["irc.chat.twitch.tv", 6667]

current_directory = os.path.dirname(os.path.abspath(__file__))
log_path = current_directory + '/comment_log/' + chat_channel + '.txt'
raw_log_path = current_directory + '/comment_log_raw/' + chat_channel + '.txt'
bot = irc_bot.irc_bot(username, oauth, chat_channel, chat_server[0], chat_server[1], membership = 1, commands = 1, tags = 1, timeout = 180)

while 1:
	msg_list = bot.get_parsed_message()
	for item in msg_list:
		timestamp = datetime.utcnow().isoformat(sep='T') + "Z"
		log_add(raw_log_path, timestamp + ' ' + item.raw_message + '\n')
		username, message = irc_bot.filter_user_msg(item)
		if username != '':
			safe_print(chat_channel + " " + username + ": " + message)
			log_add(log_path, timestamp + ' ' + username + ': ' + message + '\n')
			
