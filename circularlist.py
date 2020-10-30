#Implement Circular Linked List
from itertools import cycle
list=[1,2,3,4,5]
lstlength=len(list)*2
print(lstlength)
pool=cycle(list)
i=0
#To avoid infinite loop break when you have iterated twice size of the list
for items in pool:
    print(items)
    if i >lstlength:
        break
    i += 1
