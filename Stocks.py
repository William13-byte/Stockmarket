
from re import S
from bs4 import BeautifulSoup
from time import sleep
import requests
import string 

def main(företag):

    class URL:
        def __init__(self, stock,price = 0):
            self.stock = stock
            self.price = price
        def pris(self):
            url = f"https://finance.yahoo.com/quote/{self.stock}?p={self.stock}&.tsrc=fin-srch"
            page = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            })
            soup = BeautifulSoup(page.text, 'html.parser')
            self.price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
            


    def update(företag):
        for värde in företag:
            aktie = URL(värde)
            företag[värde] = aktie.pris()
            #print(i)
        return företag

    def text_to_number(sträng):
        for index in range(len(sträng)):
            if type(sträng[index]) == str:
                isolerad = sträng[index]
                if isolerad.find(","):
                    lista_utan_comma = isolerad.split(",")
                    #print (temp)
                    isolerad = "".join(lista_utan_comma)
                
                sträng[index] = (float(isolerad))
                
        return sträng


    def main(företag):
        lista = []
        index = 0
       
        företag = update(företag)
        for värde in företag:
            lista.append(företag[värde])
            lista = text_to_number(lista)
            företag[värde] = lista[index]
            
            index+=1 
        return företag
        
    företag = main(företag)
    lista = []
    for värde in företag.values():
        #print (värde,1 )
        lista.append(värde)
    #print(lista)
    return lista
    
#simulation
"""
test = {"AMZN": 0, "TSLA":0, "AAPL":0, "ITECH.ST":0}
for loop in range (5):
    print(main(test))
"""