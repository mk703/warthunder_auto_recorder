'''
warthunder_auto_recorder
'''
import time
import obsws_python as obs
import urllib.request
import define_window_size
import delete_timeout_file

define_window_size.op()
delete_timeout_file.op()


cl = obs.ReqClient()
print("obs web socket connected!")
readfrom = "http://localhost:8111/indicators"
read = urllib.request.urlopen(readfrom).read()[12]

while True:
    if urllib.request.urlopen(readfrom).read()[12] - 97:
        cl.start_record()
        print("A new match starts")
        while urllib.request.urlopen(readfrom).read()[12] - 97:
            time.sleep(1)
        cl.stop_record()
        print("The match ends")
    else:
        print("waiting for match")
    time.sleep(1)
