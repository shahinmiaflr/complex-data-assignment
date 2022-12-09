mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}


#  Your Code Starts from here
exchnage_rate = mobile_data.get('exchnage_rate')
mobile_specification = mobile_data.get('data')
for brand_details in mobile_specification:
    mobile_name = brand_details.get('name')
    mobile_price = brand_details.get('price')
    usd_price = float(mobile_price.replace(' USD',''))
    country = brand_details.get('made')
    # print(mobile_name, mobile_price, country)
    print(f'{mobile_name} made in {country} is {mobile_price}. It is equal'
          f' to {exchnage_rate * usd_price} in BDT.')
# print(mobile_name)
# print(mobile_name)
# for mobile in mobile_data:
#     print(mobile)