import heapq
li=[1,5,10,2,0,-6]
heapq.heapify(li)
print("Created heap is ")
print(list(li))
heapq.heappush(li,3)
print("Modified heap after push is ")
print(list(li))
print("Largest number in the list if ",heapq.nlargest(1,li))
print("Smallest number in the list if ",heapq.nsmallest(1,li))
