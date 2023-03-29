from methods import *
stock = Loader(model="stock")   # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")

# for i in stock.objects[1].stock:
#     print(i)

# ware1 = stock.objects[1]
# result = ware1.search_item("funny laptop")
# for i in result:
#     print(i)



# for i in personnel.objects:
#     my_employees.append(i.__dict__)
# for i in my_employees:
#     if len(i["head_of"]) > 0:
#         for _ in i["head_of"]:
#             my_employees.append(_.__dict__)


# for i in my_employees:
#     print(i)
