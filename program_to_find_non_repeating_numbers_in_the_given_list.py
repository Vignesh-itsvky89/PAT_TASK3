a = [10,501,22,37,100,999,87,351,10]
def odd_occurring_num(a):
    return [i for i in a if a.count(i) < 2]

b= (odd_occurring_num(a))

print("First non repeating number in  the given list is:" ,b[0] )
