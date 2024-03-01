def find_triplets(list1, n):  
    triplets = []  
    flag = False  
    for i in range(0, n-2):  
        
        for j in range(i+1, n-1):  
            
            for k in range(j+1, n):  
                
                if (list1[i] + list1[j] + list1[k] == 59):  
                    triplets.append([list1[i], list1[j], list1[k]])  
                    flag = True  
        
                
  
    if (flag == False):  
        print(" not exist ")  
          
    return triplets  
    
  
list1 = [10,20,30,9]  
n = len(list1)  
print(find_triplets(list1, n))  