import json

import os

import requests

from lxml import etree

import re

# 防止因https证书问题报错
res = """/
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:13
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:12.500000,
4217490.ts
#EXTINF:8.333333,
4217491.ts
#EXTINF:12.500000,
4217492.ts
#EXTINF:8.333333,
4217493.ts
#EXTINF:8.333333,
4217494.ts
#EXTINF:12.500000,
4217495.ts
#EXTINF:8.333333,
4217496.ts
#EXTINF:12.500000,
4217497.ts
#EXTINF:8.333333,
4217498.ts
#EXTINF:8.333333,
4217499.ts
#EXTINF:12.500000,
42174910.ts
#EXTINF:8.333333,
42174911.ts
#EXTINF:12.500000,
42174912.ts
#EXTINF:8.333333,
42174913.ts
#EXTINF:8.333333,
42174914.ts
#EXTINF:12.500000,
42174915.ts
#EXTINF:8.333333,
42174916.ts
#EXTINF:12.500000,
42174917.ts
#EXTINF:8.333333,
42174918.ts
#EXTINF:8.333333,
42174919.ts
#EXTINF:12.500000,
42174920.ts
#EXTINF:8.333333,
42174921.ts
#EXTINF:12.500000,
42174922.ts
#EXTINF:8.333333,
42174923.ts
#EXTINF:8.333333,
42174924.ts
#EXTINF:12.500000,
42174925.ts
#EXTINF:8.333333,
42174926.ts
#EXTINF:12.500000,
42174927.ts
#EXTINF:8.333333,
42174928.ts
#EXTINF:8.333333,
42174929.ts
#EXTINF:12.500000,
42174930.ts
#EXTINF:8.333333,
42174931.ts
#EXTINF:12.500000,
42174932.ts
#EXTINF:8.333333,
42174933.ts
#EXTINF:8.333333,
42174934.ts
#EXTINF:12.500000,
42174935.ts
#EXTINF:5.916667,
42174936.ts
#EXT-X-ENDLIST
"""
ts=res.split('\n')
print(ts)
for tss in ts:
    if ".ts" in tss:
        url = "https://cdn.91p07.com//m3u8/421749/"+ tss
        r=requests.get(url).content
        filename = ("E:/result/").encode("utf-8").decode("utf-8") + tss
        with open(filename,mode="wb") as fs:
            fs.write(r)
            fs.flush()
        print("已下载"+tss)
    else:
        print("不包含ts:",tss)
os.system("copy /b E:/result/*.ts E:/result/hello.mp4")
print("完成下载")