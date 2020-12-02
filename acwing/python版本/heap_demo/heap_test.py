import heapq
from heapq_showtree import show_tree
from heapq_heapdata import get_randomNumber

heap = []
data=get_randomNumber(10)
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)