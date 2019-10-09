from base64 import b64encode
import requests

def update_product():

    url = 'https://6ac751e881954b1c2b923e1b8ee65fbe:789bf9c9c72233a19884061650196009@dagatechteste.myshopify.com/admin/api/2019-07/products/3652222255181.json'

    payload =  {
				'product': {
					'id': 3652222255181,
					'tags': 'Barnes & Noble, JohFav',
					'title': 'SEE IS IS GOIN',
					'body_html': 'MY BEAUTIFUL TEST ',
					'vendor': 'dAVIII',
					'product_type': 'teSTS',					
					'collection': 135466385485
					}
				}

    r = requests.put(url, json=payload,  headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

    print(r.json())

def create_product(number):
	nameProduct = 'NAME ' + str(number)

	url = 'https://6ac751e881954b1c2b923e1b8ee65fbe:789bf9c9c72233a19884061650196009@dagatechteste.myshopify.com/admin/api/2019-07/products.json'

	payload =  {
				'product': {
					'handle': number,
					'title': 'TSHIRT - ' + nameProduct,
					'body_html': 'This is the test product called - ' + str(number) ,
					'vendor': 'ALGARAVIAS',
					'product_type': 'TSHIRT',
					'variants': [{
						'barcode': 'CODE-' + str(number),
						'option1': 'Svartur',
						'option2': 'S',
						'price': '100',
						'sku': '6934282',
						'option3' :'black'
					  },{
						'barcode': '1006934283',
						'option1': 'Svartur',
						'option2': 'M',
						'price': '100',
						'sku': '6934283',
						'option3' :'black'
						
					  },{
						'barcode': '1006934284',
						'option1': 'Svartur',
						'option2': 'L',
						'price': '100',
						'sku': '6934284',
						'option3' :'black'
					  },{
						'barcode': '1007067943',
						'option1': 'Svartur',
						'option2': 'XL',
						'price': '100',
						'sku': '7067943',
						'option3' :'black'
					  },{
						'barcode': '1007492535',
						'option1': 'Svartur',
						'option2': 'XXL',
						'price': '100',
						'sku': '7492535',
						'option3' :'black'
					  }],
					'images': [
                        { 'src': 'https://cdn.shopify.com/s/files/1/0240/9693/1917/products/shopify_shirt_1024x1024@2x.png?v=1563562657'},
                        { 'src': 'https://cdn.shopify.com/s/files/1/0240/9693/1917/products/shopify_shirt_1024x1024@2x.png?v=1563562657'}], 
					'options': [
						{
							'name': 'Litur'
						},
						{
							'name': 'See'
						},
						{
							'name': 'color'
						}
					]
				}
			}
	r = requests.post(url, json=payload,  headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
for number in range(21,40):
	print(number)
	create_product(number)

try:
	pass
except expression as identifier:
	pass

