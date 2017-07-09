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
    except Exception as e:
        return None
    return timestamp

if len(sys.argv) != 2:
    print("usage: parser.py filename")
    exit()

input_file = open(sys.argv[1], 'r')
last_timestamp = 0

while 1:
    this_line = input_file.readline()
    if this_line == "":
        break
    this_timestamp = read_chatlog(this_line)
    if this_timestamp == None:
        print(this_line)
        continue
    gap = int(this_timestamp - last_timestamp)
    if(gap > 300):
        print(str(gap) + " " + this_line)
    last_timestamp = this_timestamp

input_file.close()