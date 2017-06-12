import os
import sys
import time
import datetime

if(len(sys.argv) < 3):
    print (__file__ + ' channel quality')
    exit()

chat_channel = sys.argv[1].lower().lstrip().rstrip()
quality = sys.argv[2].lower().lstrip().rstrip()

while 1:
	filename = chat_channel + "_" + str(datetime.datetime.now().isoformat())[:19].replace(":", "_") + ".mp4"
	cmd = "livestreamer --twitch-oauth-token ndkdmflbdmhlamdfkjnsdjgnskldg https://www.twitch.tv/" + chat_channel + " " + quality + " -o " + filename
	print(cmd)
	os.system(cmd)
	time.sleep(10)