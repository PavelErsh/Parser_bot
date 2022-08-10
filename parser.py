from libraries import *

names = []
prices = []
prices_discount = []
prices_normal = []


def separator():
    print("-----------------------------------------------------------")


def parcing():
    page_urls = ["https://store.steampowered.com/app/268910/Cuphead/", "https://store.steampowered.com/app/252490/Rust/", "https://store.steampowered.com/app/1110910/Mortal_Shell/"]
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
        if price_discount > price_normal:
            prices_normal.append(price_normal)
            prices.append(prices_normal)
        if price_discount < price_normal:
            #prices.append(price_normal)
            prices_discount.append(price_discount)
            prices.append(prices_discount)
        

        #Name parcing
        name_box = soup.find('div',attrs={'id':'appHubAppName'})
        name = name_box.text.strip()
        print(name)
        names.append(name)

        #Date
        print(datetime.now())
        separator()