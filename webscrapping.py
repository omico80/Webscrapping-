# Web Scrapping Assignment // Using the " Beautiful Soup" library 

# import the required library 
import os
import re
import requests 
from bs4 import BeautifulSoup
import pandas as pd

#Target URL to scap
url = "https://medium.com/@aminasaeed223/a-comprehensive-tutorial-on-miniconda-creating-virtual-environments-and-setting-up-with-vs-code-f98d22fac8e2"

#send request to download the file
response = requests.request("GET", url)

# parse the download data
data = BeautifulSoup(response.text,"html.parser")
print(data.prettify()[:10000])

data.title

for link in data.find_all("a"):
    print(link.get("href"))
    
print(data.get_text())

print(data.prettify()[0:1000])

for link in data.find_all("a",attrs={"href":re.compile("^http")}):
    print(link)
    
type(link)

file = open("parsed_data.txt","w")
for link in data.find_all("a",attrs={"href":re.compile("^http")}):
    data_link=str(link)
    print(data_link)
    file.write(data_link)
    
file.flush()
file.close()

%pwd
    

