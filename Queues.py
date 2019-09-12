'''
Created on Sep 12, 2019

Queues in Python
@author: asharda
'''

from collections import deque
queue=deque([1,2,3,4,5,6])
#Print Queue
print(queue)
#Insert into Queue
queue.append(7)
print(queue.popleft())
print(queue)
