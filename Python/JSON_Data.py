import json
file = open('P2.json','r',encoding = "utf-8")
data = json.load(file)
# get = data["data"]['poi_list']
get = data['poi_list']
i = 1
for item in get:
    name, tel, address = '', '', ''
    if item['name'] == '':
        name = '|'
    else :
        name = item['name']
    if item['tel'] == '':
        tel = '|'
    else :
        tel = item['tel']
    if item['address'] == '':
        address = '|'
    else :
        address = item['address']
    print(i,name,tel,address)
    i+=1
