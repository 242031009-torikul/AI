from collections import deque

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H','I'],
    'E': [],
    'F': [],
    'G': []
}

label={}
label['A']=0
label['B']=1
label['C']=1
label['D']=2
label['E']=2
label['F']=2
label['G']=2
label['H']=3
label['I']=3

def bfs(tree, start, limit):
    order=[]
    queue = deque([start])
    while queue:
        order.append(queue.popleft())
        node = order[-1]
        if(label[node]<limit)
           for child in reversed(tree[node]):
               queue.appendleft(child)

    return order


start = 'A'
limit=2
result = bfs(tree, start, limit)

print("Traversal Order:",result)
