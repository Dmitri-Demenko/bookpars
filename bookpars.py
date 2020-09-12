import csv
import requests
from bs4 import BeautifulSoup
from itertools import combinations_with_replacement as comb, product
import time
from multiprocessing import Pool

list_comb=[]
list_comb_url=[]
res=[]
path = "rezultat.csv"
l = ['b','f','j','t']

def combination(l):
    p=list(product(l, repeat=4))
    for g in p:
        strr=''
        for item in g:
            strr+=item
        list_comb.append(strr)
    for comb in list_comb:
        stro='https://books.theoilandgasyear.com/books/'+comb
        list_comb_url.append(stro)
    
def resultat(list_comb_url):
    rt=0
    for url in list_comb_url:
        request = requests.get(url,verify= False)
        result=(request.status_code)
        if result==200:
            res.append(url)
        print(res)
        rt=rt+1
        print(rt)
    #time.sleep(10)

def csv_writer(res, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in res:
            writer.writerow([line])


#def make_all(list_comb_url):
  #  result(list_comb_url)
   # csv_writer(resalt, path)

def main():
    combination(l)
    resultat(list_comb_url)
    csv_writer(res, path)

if __name__ == "__main__":
    main()
