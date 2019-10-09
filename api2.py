import requests
import pymysql
url = 'https://44da213ed141ea5c381cba467af57557:c2e8c6f1df7c301f8d9c195886389af9@tkees1.myshopify.com/admin/api/2019-07/customers/644734287945/addresses.json'
url = 'https://44da213ed141ea5c381cba467af57557:c2e8c6f1df7c301f8d9c195886389af9@tkees1.myshopify.com/admin/api/2019-07/customers.json?limit=1&page=1'
url = 'https://44da213ed141ea5c381cba467af57557:c2e8c6f1df7c301f8d9c195886389af9@tkees1.myshopify.com/admin/api/2019-07//products/count.json'
resp = requests.get(url)
print (resp.status_code)
print(resp.json())


try:
    pass
except expression as identifier:
    pass
else:
    pass