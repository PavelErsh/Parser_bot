from parser import prices_discount,prices_normal,names
from libraries import *

filepath = None

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

def check_discount_or_normal():
    global filepath
    for i in range(len(names)):
        if prices_discount[i] < prices_normal[i]:
            filepath = findfile(f"Steam_{names[i]}_prices.csv",f"/Users/abdulazizsuleymanov/Desktop/Python/Python_Automation_Book_Tasks/Parcing/Steam_game_prices/Normal prices/Steam_{names[i]}_prices.csv")
        
        else:
            filepath = findfile(f"Steam_{names[i]}_prices.csv",f"/Users/abdulazizsuleymanov/Desktop/Python/Python_Automation_Book_Tasks/Parcing/Steam_game_prices/Discount prices/Steam_{names[i]}_prices.csv")