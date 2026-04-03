import json


# # ---------------- for loads the json file ---------------------------------
# with open(r'C:\Users\Admin\Desktop\Python-Learning\JSON\example.json', 'r') as file:
#     data=json.load(file)
# # print(data)

# #--------------------------------for dump data into json data---------------------------------
# jsonData={'name': 'John Smith', 'sku': '20223', 'price': 23.95, 'shipTo': {'name': 'Jane Smith', 'address': '123 Maple Street', 'city': 'Pretendville', 'state': 'NY', 'zip': '12345'}, 'billTo': {'name': 'John Smith', 'address': '123 Maple Street', 'city': 'Pretendville', 'state': 'NY', 'zip': '12345'},'hasChildren':False}
# personData=json.dumps(jsonData,indent=4)
# print(personData)

# #------------------------------ for loads the json data which we dumps into json format
# myData=json.loads(personData)
# print(myData)
# # ------------------------------ for creating the json file and dump dat into that file --------------------------------
# with open('myJson.json','w') as file:
#     json.dump(jsonData,file) 



#----------------------------- encode and decode class object into Json ----------------------------------

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Person):
            return {"name":obj.name,"age":obj.age}

        return super().default(obj)

def my_decoder(dct):
    if "name" or "age" in dct:
        return Person(name=dct.get("name"),
                      age=dct.get("age"))
    return dct
    
    
person=Person("Dhruv",23)

personData=json.dumps(person,cls=MyEncoder)
my_data=json.loads(personData,object_hook=my_decoder)
print(my_data.name)


    
