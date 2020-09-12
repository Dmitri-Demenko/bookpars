import csv
import requests
from bs4 import BeautifulSoup
from itertools import combinations_with_replacement as comb, product
import time
from multiprocessing import Pool

list_comb=[]
list_comb_url=[]
res=[]
l = ['a','e','b','f','j','t'] 

def combination():
    p=list(product(l, repeat=4))
    for g in p:
        strr=''
        for item in g:
            strr+=item
        list_comb.append(strr)
def url_combination(list_comb):
    for comb in list_comb:
        stro='https://books.theoilandgasyear.com/books/'+comb
        list_comb_url.append(stro)
    
def result(list_comb_url):
    number=0
    for url in list_comb_url:
        request = requests.get(url,verify= False)
        result=(request.status_code)
        if result==200:
            res.append(url)
        print(res)
        number=number+1
        print(number)
    #time.sleep(10)

def csv_writer(res, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow([line])

def main():
   
    path = "rezultat.csv"
    combination()
    url_combination(list_comb)
    result(list_comb_url)
    csv_writer(res, path)

if __name__ == "__main__":
    main()
    