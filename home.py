import requests
from scrapy.selector import Selector

response = requests.get('https://toplearn.com/TodayDiscounts')
response.encoding = 'utf-8'
item_name = Selector(text=response.content).xpath('//h2/a/text()').getall()
item_free = Selector(text=response.content).xpath('//a[@class="discount"]/text()').getall()
item_price = Selector(text=response.content).xpath('//span[@class="price"]/i/text()').getall()

with open('test.txt','w',encoding='utf-8') as file:
    for item in range(len(item_name)):
        file.write(f"name: {item_name[item]} free count: {item_free[item]} price: {item_price[item]} \n")
    file.close()