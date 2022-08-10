from http.client import FOUND
from unicodedata import name
import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

names = []
prices =[]

'''def create_file(name,price):
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
            return os.path.join(dirpath, name)'''

def separator():
    print("-----------------------------------------------------------")





#page_urls = ["https://store.steampowered.com/app/252490/Rust/","https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/","https://store.steampowered.com/app/1091500/Cyberpunk_2077/","https://store.steampowered.com/app/268910/Cuphead/"]
page_urls = ["https://store.steampowered.com/app/268910/Cuphead/", "https://store.steampowered.com/app/252490/Rust/"]
for i in page_urls:
    page = urllib2.urlopen(i)
    soup = BeautifulSoup(page,'html.parser')

    #Price parcing
    price_box_normal = soup.find('div',attrs={'class':'game_purchase_price price'})
    price_box_discount = soup.find('div',attrs={'class':'discount_final_price'})
    
    price_normal = price_box_normal.text.strip()
    #print(f"Usual Price of {names[i]} : {price_normal}")

    price_discount = price_box_discount.text.strip()
    #print(f"Price with Discount for {names[i]} : {price_discount}")    

    if price_discount < price_normal:
        prices.append(price_normal)
    else:
        prices.append(price_discount)
    
    #Name parcing
    name_box = soup.find('div',attrs={'id':'appHubAppName'})
    name = name_box.text.strip()
    separator()
    print(name)
    names.append(name)

    print(f"Usual Price of {names[i]} : {price_normal}")
    print(f"Price with Discount for {names[i]} : {price_discount}")
    separator()
    
    #Date
    print(datetime.now())

    if price_discount < price_normal:
        route = "/Users/abdulazizsuleymanov/Desktop/Python/Python_Automation_Book_Tasks/Parcing/Steam_game_prices/Normal prices/Steam_{names[i]}_prices.csv"
    else:
        route = "/Users/abdulazizsuleymanov/Desktop/Python/Python_Automation_Book_Tasks/Parcing/Steam_game_prices/Discount prices/Steam_{names[i]}_prices.csv"

def create_file(name,price):
    with open(route, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name","Price $","YYYY-MM-DD + HR:MIN:SEC"])

def add_info(name,price):
    with open(route, 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price, datetime.now()])

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


    
'''for i in range(len(names)):
    with open(f'./Steam_{names[i]}_prices.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name","Price $","YYYY-MM-DD + HR:MIN:SEC"])
        writer.writerow([names[i], prices[i], datetime.now()])'''


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

    

