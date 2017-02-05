import heapq
import numpy as np


class Node:
    def __init__(self,x,y,value):
        self.value = value
        self.x = x 
        self.y = y
        self.priority = 0 
    
    def position(self):
        return (self.x,self.y)
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.value == other.value
    
    def __hash__(self):
        return hash((self.x,self.y))
    def __repr__(self):
        return "Node: [ ({},{}) {} ]".format(self.x,self.y,self.value)
    
class Graph:
    def __init__(self):
        f = open('dossier/problem81.txt')
        self.table = np.zeros(shape=(80,80), dtype=np.object) 
        i = 0
        for line in f:
            line = (line.strip()).split(',')
            j = 0
            for num in line:
                node = Node(i,j,int(num))
                self.table[i][j] = node
                j += 1
            i += 1
                
        
    def neighbors(self,node):
        pt = node.position()
        i = pt[0]
        j = pt[1]
        if i == 79:
            i -= 1
        yield self.table[i+1][j]
        if j == 79:
            j -= 1
        yield self.table[i][j+1]

    
    
    def __repr__(self):
        rep ='Graph:'

        return rep + str(self.table)
    
    def djisktra(self,x1,y1, x2,y2):
        source = self.table[x1][y1]
        goal = self.table[x2][y2]
        queue = PQ()
        visited = set()
        queue.push(source)
        visited.add(source)
         
        while not queue.isEmpty():
            node = queue.pop()
            if node == goal:
                return node.priority
            for v in self.neighbors(node):
                p = node.value + v.value 
                if v not in visited:
                    v.priority = p
                    visited.add(v)
                    queue.push(v)
                else:
                    
                    if v.priority > p:
                        v.priority = p
        return None
                     
            
            

class PQ:
    def __init__(self):
        self._queue = []
        self._index = 0
        

    def push(self, item):
        heapq.heappush(self._queue, (item.priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
    def isEmpty(self):
        return len(self._queue) == 0
    

    
            
g = Graph()
print(g.djisktra(0, 0, 79, 79))
a = Node(1,1,34)
b = Node(0,2,45)
c = Node(2,3,56)
a.priority = 4
b.priority = 2
c.priority = 6
p =PQ()
p.push(a)
p.push(b)
p.push(c)

print(p.pop())
print(p.pop())
print(p.pop())






















