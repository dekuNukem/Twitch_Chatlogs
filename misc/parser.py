import sys
from datetime import datetime, timezone

def parse_ts(ts_str):
    try:
        return int(float(ts_str))
    except Exception:
        pass
    try:
        return datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc).timestamp()
    except Exception:
        pass
    try:
        return datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()
    except Exception:
        pass
    raise ValueError

def read_chatlog(chatlog_line):
    try:
        line_split = chatlog_line.split(' ', 1)
        timestamp = parse_ts(line_split[0])
        message = line_split[1].split(": ", 1)
        user = message[0].lower()
        comment = message[1].rstrip("\n").rstrip("\r")
    except Exception as e:
        return '','',''
    return timestamp, user, comment

if len(sys.argv) != 2:
    print("usage: parser.py filename")
    exit()

input_file = open(sys.argv[1], 'r')

while 1:
    this_line = input_file.readline()
    if this_line == "":
        break
    timestamp, username, message = read_chatlog(this_line)
    if username == "":
        continue
    print(username + ": " + message)

input_file.close()