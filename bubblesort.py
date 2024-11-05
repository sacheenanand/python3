list = [10,9,8,7,6,5,4,3,2,1]
def bubble_sort(list):
    for j in range(0,9):
        for i in range(0,9):
            if list[i] > list[i+1]:
                swap = list[i]
                list[i]= list[i+1]
                list[i+1] = swap
    return list 
            
   
print(bubble_sort(list))


        

list=[9,8,7]
def bubble(list):
    for j in range(0,2):
        for i in range(0,2):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i]=list[i+1]
                list[i+1]=temp
    return list
print(bubble(list))

    