import os
import sys

face_list = [':O', ":)", ":(", ":o", ":z", "B)", ":/", ";)", ";p", ":p", "R)", "o_O", ":D", ">(", "<3"]
url_flag = ["http", "www.", ".com", ".net", '.edu', '.tv']
english_alphabet = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

def get_list(filename):
	ret = []
	with open(filename, 'r') as fp:
		for line in fp:
			line = line.lstrip().rstrip('\n').rstrip('\r')
			if len(line) <= 0 or line[0] == ';' and line not in ret:
				continue
			ret.append(line)
	return ret

def is_unicode(c):
	return ord(c) > 127

def remove_emote(message):
	for item in global_emote_list + face_list:
		message = message.replace(item, '')
	return message

def is_url_simple(message):
	message = message.lower()
	for item in url_flag:
		if item in message:
			return True
	return False

def text_ratio(message):
	return len([x for x in message if x in english_alphabet]) / len(message)

def text_sig(message):
	return ("".join([c for c in message if c in english_alphabet])).lower()

def unicode_sig(message):
	return "".join([c for c in message if is_unicode(c)])



def read_chatlog(chatlog_line):
	try:
		line_split = chatlog_line.split(' ', 1)
		message = line_split[1].split(": ", 1)
		user = message[0].lower()
		comment = message[1].rstrip('\n').rstrip('\r').replace(chr(1) + "ACTION", '')
	except Exception as e:
		print("error parsing chatlog")
		print(e)
		print(chatlog_line)
		return '',''
	return user, comment

if(len(sys.argv) != 2):
	print (__file__ + ' <pasta_file>')
	exit()

input_file = open(sys.argv[1], 'r')
global_emote_list = get_list("global_emotes.txt") + get_list("bttv_emotes.txt")
text_sig_dict = {}
unicode_sig_dict = {}

count = 0
while 1:
	this_line = input_file.readline()
	if this_line == "":
		break

	count += 1;
	if count % 10000 == 0:
		print(count)

	username, message_orig = read_chatlog(this_line)
	if len(message_orig) <= 50 or username == "" or message_orig.count(':') >= 2 or message_orig.count('@') >= 2 or is_url_simple(message_orig):
		continue
	message_no_emote = remove_emote(message_orig)
	if len(message_no_emote) <= 20:
		continue

	tratio = text_ratio(message_no_emote)

	if 0.3 < tratio < 0.9:
		pasta_sig = text_sig(message_no_emote)
		if len(pasta_sig) < 10:
			 continue
		if pasta_sig not in text_sig_dict:
			text_sig_dict[pasta_sig] = [set(), message_orig]
			text_sig_dict[pasta_sig][0].add(username)
		else:
			text_sig_dict[pasta_sig][0].add(username)
	else:
		pasta_sig = unicode_sig(message_orig)
		if len(pasta_sig) < 5:
			 continue
		if pasta_sig not in unicode_sig_dict:
			unicode_sig_dict[pasta_sig] = [set(), message_orig]
			unicode_sig_dict[pasta_sig][0].add(username)
		else:
			unicode_sig_dict[pasta_sig][0].add(username)

output_unicode = open("pasta_unicode_" + sys.argv[1], 'w')
for key in unicode_sig_dict:
	if len(unicode_sig_dict[key][0]) > 2:
		output_unicode.write(unicode_sig_dict[key][1] + "\r\n")
output_unicode.close()

output_text = open("pasta_text_" + sys.argv[1], 'w')
for key in text_sig_dict:
	if len(text_sig_dict[key][0]) > 2:
		output_text.write(text_sig_dict[key][1] + "\r\n")
output_text.close()