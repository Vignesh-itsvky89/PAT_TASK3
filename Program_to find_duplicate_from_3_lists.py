a = [10,501,22,37,100,999,87,351]
b = [10,501,22]
c = [22,37,100,999,87,351,501]


common_elements = list(    set(a).intersection(b, c))
print("The Duplicate element in the given list is: ", common_elements)

