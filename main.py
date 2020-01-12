import requests
from bs4 import BeautifulSoup

querry = input("ENTER YOUR DORK : ")

google_url = ("https://www.google.com/search?q={}" + "&num=" + str(10)).format(querry)
response_1 = requests.get(google_url, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
soup_1 = BeautifulSoup(response_1.text, "html.parser")


bing_url = "https://www.bing.com/search?q={}".format(querry)
response_2 = requests.get(bing_url, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
soup_2 = BeautifulSoup(response_2.text, "html.parser")


result_div_1 = soup_1.find_all('div', attrs={'class': 'BNeawe UPmit AP7Wnd'})

result_div_2 = soup_2.find_all('cite')


print(" \n GOOGLE RESULTS \n")

for result in result_div_1 :
    print(result.text)

print(" \n BING RESULTS \n")

for result in result_div_2 :
    print(result.text)
