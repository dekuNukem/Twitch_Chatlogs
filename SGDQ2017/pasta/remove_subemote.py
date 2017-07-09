import os
import sys

def get_set(filename):
	ret = []
	with open(filename, 'r') as fp:
		for line in fp:
			line = line.lstrip().rstrip('\n').rstrip('\r')
			if len(line) <= 0 or line[0] == ';' and line not in ret:
				continue
			ret.append(line)
	return ret

def has_sub_emote(msg):
	for item in sub_emote_set:
		if item in msg:
			return True
	return False

if(len(sys.argv) != 2):
	print (__file__ + ' <pasta_file>')
	exit()

input_file = open(sys.argv[1], 'r')
sub_emote_set = get_set("sub_emotes.txt")

while 1:
	this_line = input_file.readline()
	if this_line == "":
		break
	if has_sub_emote(this_line):
		continue

	print(this_line)