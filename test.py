
import urllib.request
import re

search_keyword="iphone 12"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + '+'.join(search_keyword.split()))
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

ret = []
for x in range(8):
    video = urllib.request.urlopen(f"https://www.youtube.com/watch?v={video_ids[x]}")
    results = re.findall(r"<\/title><meta name=\"title\" content=\"(.+?(?=\"))|<link itemprop=\"name\" content=\"(.+?(?=\"))", video.read().decode())
    title, author = results[0][0], results[1][1]
    ret.append([title, author])

print(ret)