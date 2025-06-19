#! python3
# -*- coding: utf-8 -*-

import os
import urllib.request
import re
import urllib
import time
import sys
from datetime import datetime
import threading

#datetime_dat = datetime.now()
#cPath = datetime_dat.strftime("%Y%m%d")

# 讀取 IP 位置

for j in range(1,133):
    
#    target = line0.strip()
    i = str(j)
    url = "http://www.chienmou.com:81/webQRcode/ebook/2025%E8%87%BA%E5%8C%97%E5%B8%82%E4%B8%AD%E6%AD%A3%E5%8D%80%E6%9D%B1%E9%96%80%E5%9C%8B%E6%B0%91%E5%B0%8F%E5%AD%B8%E7%95%A2%E6%A5%AD%E7%B4%80%E5%BF%B5%E5%86%8A/files/page/" + i + ".jpg"
#    url = "http://" + target + "/onvif-http/snapshot?auth=YWRtaW46MTEK"  # 設定請求網址

    imgurl = url
    

    cFile = i + ".jpg"
    
    try:
        urllib.request.urlretrieve(imgurl,cFile)
    except :
        print("connect fail")
        #break
    

    # if os.path.isfile(cFile):
        # os.rename(cFile, cPath + "/" + cFile)  # 利用更改檔名方式執行檔案移動
        # result_file = open("success.txt", "a")  # 開啟成功檔案，並將IP寫入檔案中
        # result_file.write(target + '\n')
        # result_file.write("==============================\n")
        # result_file.close()
"""     else:
            pass """

#file0.close()   # 關閉檔案
