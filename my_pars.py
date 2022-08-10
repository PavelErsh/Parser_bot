from http.client import FOUND
from unicodedata import name
import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

''''names = []
prices =[]

def create_file(name,price):
    with open(f'./Steam_{name}_prices.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name","Price $","YYYY-MM-DD + HR:MIN:SEC"])

def add_info(name,price):
    with open(f'./Steam_{name}_prices.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price, datetime.now()])

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

def separator():
    print("-----------------------------------------------------------")

def parcing():
    page_urls = ["https://store.steampowered.com/app/268910/Cuphead/", "https://store.steampowered.com/app/252490/Rust/", "https://store.steampowered.com/app/287310/ReVolt/"]
    for i in page_urls:
        page = urllib2.urlopen(i)
        soup = BeautifulSoup(page,'html.parser')

        #Price parcing
        price_box_normal = soup.find('div',attrs={'class':'game_purchase_price price'})
        price_box_discount = soup.find('div',attrs={'class':'discount_final_price'})

            #Usual price
        price_normal = price_box_normal.text.strip()
        separator()
        print(f"Normal Price : {price_normal}")

            #Discount price
        price_discount = price_box_discount.text.strip()
        print(f"Discount Price : {price_discount}")

            #Adds the prices to the lists
        if price_discount < price_normal:
            prices.append(price_discount)
        else:
            prices.append(price_normal)
        
        #Name parcing
        name_box = soup.find('div',attrs={'id':'appHubAppName'})
        name = name_box.text.strip()
        print(name)
        names.append(name)

        #Date
        print(datetime.now())
        separator()

        if price_discount < price_normal:
            findfile("./Discount_prices")
            route = "Steam_game_prices/Discount_prices/Steam{names[i]}prices.csv"
        
        else:
            findfile("./Normal_prices")
            route = "Steam_game_prices/Normal_prices/Steam{names[i]}prices.csv"



for i in range(len(names)):

    if price_discount < price_normal:
        filepath = findfile(f"Steam_{names[i]}_prices.csv",f"/Users/abdulazizsuleymanov/Desktop/Python/Python_Automation_Book_Tasks/Parcing/Steam_game_prices/Normal prices/Steam_{names[i]}_prices.csv")
    
    else:
        filepath = findfile(f"Steam_{names[i]}_prices.csv",f"/Users/abdulazizsuleymanov/Desktop/Python/Python_Automation_Book_Tasks/Parcing/Steam_game_prices/Discount prices/Steam_{names[i]}_prices.csv")
    
    #filepath = findfile(f"Steam_{names[i]}_prices.csv", f"/Users/abdulazizsuleymanov/Desktop/Python/Python_Automation_Book_Tasks/Parcing/Steam_game_prices/")

    if filepath == None:
        print(filepath)
        create_file(names[i],prices[i])
        add_info(names[i],prices[i])
    
    if filepath != None:
        print("helllllo")
        add_info(names[i],prices[i])

    
'''
