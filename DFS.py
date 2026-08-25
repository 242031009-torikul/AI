
from collections import deque

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(tree, start):
    order=[]
    queue = deque([start])
    while queue:
        order.append(queue.popleft())
        node = order[-1]
      
        for child in reversed(tree[node]):
             queue.appendleft(child)

    return order


start = 'A'

result = bfs(tree, start)

print("Traversal Order:",result)
