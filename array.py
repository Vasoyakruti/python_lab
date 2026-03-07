#integer array

from array import array
arr = array('i',[10,20,30,40])
print(arr)
print(type(arr))

#basic array operation
#len() number of element

from array import array
arr = array('i',[10,20,30,40,50])
print(len(arr))

#append(x)-add element at end

from array import array
arr = array('i',[10,20,30])
arr.append(40)
print(arr)


#insert(pos,x)-insert at position

from array import array
arr = array('i',[10,20,30,40])
arr.insert(2,30)
print(arr)


#remove(x)-remove first occurrence

from array import array
arr = array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)


#pop()-remove and retuen last element

from array import array
arr = array('i',[10,20,30,20,40])
x = arr.pop()
print("removed:",x)
print(arr)


#index(x) find index of element

from array import array
arr=array('i',[10,20,30,40])   
print(arr.index(30))


#count(x) find index of element

from array import array
arr=array('i',[10,20,30,40])  
print(arr.count(20))


#reverse()-reverse array

from array import array
arr=array('i',[10,20,30,40])  
arr.reverse()
print(arr)
