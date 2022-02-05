# Exercise 12
from urllib.request import Request, urlopen
# Getting the latest round
req = Request('https://drand.cloudflare.com/public/latest', headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 \
Firefox/31.0'})
data = urlopen(req).read()
a=str(data).split(",")
a=a[0].split(":")
round=a[1]
print("Latest round: ", round)
# Getting the last 100 randomness values
randomness=[]
for i in range(100):
    req = Request('https://drand.cloudflare.com/public/'+str(int(round)-i), \
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) \
    Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    b=str(data).split('"')
    randomness.append(b[5])
# Combining randomness values to one sequence
seq=""
for i in range(len(randomness)):
    seq+=bin(int(randomness[i], 16))[2:]
# Finding the longest sequences of 1's and 0's
c=list(seq)
last_digit=c[0]
if(last_digit=='1'):
    count_0=0
    count_1=1
else:
    count_0=1
    count_1=0
max_0=-1
max_1=-1
for i in range(1,len(c)):
    if(last_digit=='0'):
        if(c[i]=='0'):
            count_0+=1
        else:
            if(max_0<count_0):
                max_0=int(count_0)
            count_0=0
            count_1=1
    else:
        if(c[i]=='1'):
            count_1+=1
        else:
            if(max_1<count_1):
                max_1=int(count_1)
            count_1=0
            count_0=1
    last_digit=c[i]
print("Longest sequence of 1's: ", max_1, "\nLongest sequence of 0's: ", max_0)
