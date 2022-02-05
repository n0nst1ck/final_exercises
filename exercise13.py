# Exercise 13
import requests
import re

r=requests.get('https://drand.cloudflare.com/public/latest', headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 \
Firefox/31.0'})
data=r.json()
a=str(data).split(",")
a=a[1].split("'")
randomness=a[3]
print("Latest randomness: ", randomness)

seq=re.findall('.{1,2}', randomness)
for i in range(len(seq)):
    seq[i]=(int(seq[i], 16))%80

r=requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
data=r.json()
win=((data.get("last")).get("winningNumbers")).get("list")

set1=set(seq)
inter=set1.intersection(win)
print("The amount of numbers that would win are:", len(list(inter)))
