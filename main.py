'''
warthunder_auto_recorder
'''
from WarThunder import telemetry
from datetime import datetime, timedelta
import time
import obsws_python as obs
import os
import tomli
import define_window_size

define_window_size.op()

f = open("config.toml", "rb")
toml_dict = tomli.load(f)
print(toml_dict)
path = toml_dict.get('storage').get('save_path')
save_days = toml_dict.get('storage').get('save_days')
files = os.listdir(path)
starttime = datetime.now()
d1 = starttime + timedelta(days=-save_days)
date1 = str(d1)
index = date1.find('.')
datatime01 = date1[:index]
for file in files:
    filePath = path + "/" + file
    last1 = os.stat(filePath).st_mtime  # 获取文件的时间戳
    filetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last1))  # 将时间戳格式化成时间格式的字符串
    if datatime01 > filetime:
        print(filePath + " was removed!")
        os.remove(filePath)

cl = obs.ReqClient()
print("obs web socket connected!")
telem = telemetry.TelemInterface()

while True:
    if telem.get_telemetry():
        cl.start_record()
        print("A new match starts")
        while telem.get_telemetry():
            time.sleep(1)
        cl.stop_record()
        print("The match ends")
    time.sleep(1)
