

''' create dictonary that contains product name,price and category
create 5 products

'''


# product={}
# product_list=[]
# print("Please Enter 5 product details :\n")
# for i in range(5):
#     product_name=input(str(i+1)+") Enter product name\n")
#     product_price = float(input(str(i+1) + ") Enter product price\n"))
#     product_cat = input(str(i+1) + ") Enter product category\n")
#     product_details={'Product Name':product_name,'Product Price':product_price,'Product Category':product_cat}
#     product_list.append(product_details)
#
# product["Products"]=product_list

import json
list_product=[
        {
            "product name":"samsung",
            "product price":14000,
            "product cat":"mobile"
        },
        {
            "product name":"samsung note",
            "product price":20000,
            "product cat":"mobile"

        },
    {
        "product name": "HP",
        "product price": 45335,
        "product cat": "laptop"

    }

        ]

dict_product={"product":list_product}

price_send=dict_product["product"][1]["product price"]
print(price_send)

# for product in products:
#     category=product['product cat']
#     if category=='mobile':
#         mobile+=1
#     if category=='laptop':
#         laptop+=1
#
#     price=product['product price']
#     if price>15000:
#         mobiles_20k.append(product)
#
# print("Mobiles availables :"+str(mobile))
# print(type(mobile))
# print(type(str(mobile)))
# print("Laptops availables :"+str(laptop))
# print(mobiles_20k)



