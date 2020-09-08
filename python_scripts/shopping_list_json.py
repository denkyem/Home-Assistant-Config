#!/usr/local/bin/python
# coding: utf8
import json


######################################
######################################

# Script to create custom sensor for shopping list
# 
# returns:
#   state: empty / not_empty
#   attributes:
#       not_complete: number of not completed items
#       content: List of not completed items, separated by /n (useful to display on a card)
#       lista: List of not completed items, separated by a comma (useful to send on a notification)

######################################
######################################





with open('/config/.shopping_list.json') as data_file:
   shoppingListData = json.load(data_file)

# shoppingListData_json = """
# [
#     {
#         "complete": true,
#         "id": "3c4ae426f1d04d07b2438022707c4a18",
#         "name": "Papel higi\u00e9nico"
#     },
#     {
#         "complete": false,
#         "id": "d3379a3a745d41ada0055164838c2d1e",
#         "name": "Rolo cozinha grande"
#     },
#     {
#         "complete": false,
#         "id": "04283e2da2914b149f5848a1a617816d",
#         "name": "Leite"
#     },
#     {
#         "complete": false,
#         "id": "e0930aa800ab4f5280b77168c1018cdd",
#         "name": "\u00c1gua"
#     }
# ]
# """
# shoppingListData = json.loads(shoppingListData_json)

class lista:
    item = u""

class shoppingList:
    content = u""
    not_complete = 0
    state = u""
    lista = []

myList = shoppingList()

myList.not_complete = 0
myList.state = ""
myList.content = ""
myList.lista = []

#content = u""
#not_complete = 0

for entry in shoppingListData:
    if not entry['complete']:
        myList.content += u"- %s\n" % entry['name']
        myList.lista.append(entry['name'])
        myList.not_complete += 1



if myList.not_complete == 0:
    myList.state = u"empty"

else:
    myList.state = u"not_empty"


# data = {
#     "content": "aboboras",
#     "not_complete": 1,
#     "state": "not_empty"

# }



#print(json.dumps(shoppingListData))
#print(shoppingListData)
print(json.dumps(myList.__dict__))