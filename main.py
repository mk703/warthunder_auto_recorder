'''
warthunder_auto_recorder
'''
import time
import json
import obsws_python as obs
import urllib.request
import define_window_size
import delete_timeout_file

define_window_size.op()
delete_timeout_file.op()


def check_in_game():
    readfrom = "http://localhost:8111/map_info.json"
    rawdata = urllib.request.urlopen(readfrom).read()
    jsondata = json.loads(rawdata)
    return jsondata['valid']


cl = obs.ReqClient()
print("obs web socket connected!")

while True:
    if check_in_game():
        cl.start_record()
        print("A new match starts")
        while check_in_game():
            print("obs recording")
            time.sleep(1)
        cl.stop_record()
        print("The match ends")
    else:
        print("waiting for match")
    time.sleep(1)
