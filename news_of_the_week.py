import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request, urllib.parse, urllib.error
import numpy as np
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://dixit.io/week"
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs(html, 'html.parser')


clicks = []
click = soup.select("big span")
for i in click:
    clicks.append((i.text).strip())
    
headers = []
head = soup.find_all("h2")
for i in head:
    headers.append((i.text).strip())

links = []
for i in soup.select("h2 a"):
    links.append(i.get("href"))
    
df = pd.DataFrame()
df["clicks"] = clicks
df["headers"] = headers
df["links"] = links

# for i, n in zip(range(9, -1, -1), range(10,0,-1)):
#     print("[La Noticia de la semana: numero"," ", n,"]", 
#     "\n", df.loc[ i ,'headers'], "\n", df.loc[ i ,'links'], sep="")
#     sleep(1) 



# for i, n in zip(range(9, -1, -1), range(10,0,-1)):
#     x = "[La Noticia de la semana: numero " + str(n) + "]"
#     y = df.loc[i ,'headers']
#     z = df.loc[i ,'links']
#     tweet = "\n".join([x, y, z])
#     print(tweet)
    
    
