from methods import *
stock = Loader(model="stock")   # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")

my_emps = get_emp_name(personnel)
for i in my_emps:
    #print(i.get_password())
    print(i._name)
#print(personnel.__dict__)
for i in personnel:
    pass
    #print(i.get_password())
