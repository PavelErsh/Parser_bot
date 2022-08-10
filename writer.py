from libraries import *
from parser import names,prices_discount,prices_normal,prices
from finder import filepath,findfile


def create_file(name,price):
    with open(f'./Steam_{name}_prices.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name","Price $","YYYY-MM-DD + HR:MIN:SEC"])

def add_info(name,price):
    with open(f'./Steam_{name}_prices.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price, datetime.now()])

def file_writer():

    for i in range(len(names)):

        ''''for price_normal in prices_normal :
        #if prices_discount[i] < prices_normal[i]:
            filepath = "Steam_game_prices/Discount_prices/Steam{names[i]}prices.csv"
            findfile("./Discount_prices",filepath)
        
        for price_discount in prices_discount:
            filepath = "Steam_game_prices/Normal_prices/Steam{names[i]}prices.csv"
            findfile("./Normal_prices",filepath)
        #else:
            


    if filepath == None:
        print(filepath)
        create_file(names[i],prices[i])
        add_info(names[i],prices[i])
                
    if filepath != None:
        add_info(names[i],prices[i])'''