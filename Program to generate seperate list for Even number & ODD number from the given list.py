List = [10, 501,22, 37, 100,999,87,351]
Even_List= []
ODD_List= []
for i in List:
    if i%2 == 0:
        Even_List.append(i)
    if i%2 != 0:
        ODD_List.append(i)
print("Even number list is:" , Even_List)
print("ODD number list is:" , ODD_List)