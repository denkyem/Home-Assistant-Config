#!/usr/local/bin/python
# coding: utf8
import json
#import sys

######################################
######################################

#          Under development         #

######################################
######################################

        



with open('/config/.shopping_list.json') as data_file:
    shoppingListData = json.load(data_file)


for entry in shoppingListData:
    entry['complete'] = "True"
        

with open('/config/.shopping_list.json') as outfile:
    json.dump(shoppingListData, outfile)





# class lista:
#     item = []

# class shoppingList:
#     content = u""
#     not_complete = 0
#     state = u""
#     lista = []

# myList = shoppingList()

# myList.not_complete = 0
# myList.state = ""
# myList.content = ""
# myList.lista = []

# #content = u""
# #not_complete = 0

# for entry in shoppingListData:
#     if not entry['complete']:
#         myList.content += u"- %s\n" % entry['name']
#         myList.lista.append(entry['name'])
#         myList.not_complete += 1



# if myList.not_complete == 0:
#     myList.state = u"empty"

# else:
#     myList.state = u"not_empty"


# # data = {
# #     "content": "aboboras",
# #     "not_complete": 1,
# #     "state": "not_empty"

# # }



print(json.dumps(shoppingListData))
# #print(shoppingListData)
# #print(json.dumps(myList.__dict__))

# print(str(sys.argv))