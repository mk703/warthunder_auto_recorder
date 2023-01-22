import tomli
import os
from datetime import datetime, timedelta
import time


def op():
    f = open("config.toml", "rb")
    toml_dict = tomli.load(f)
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


if __name__ == '__main__':
    op()
