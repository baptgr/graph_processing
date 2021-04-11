from random import randint, choice, sample
from itertools import combinations

frame_width = 1200
frame_height = 900
drawers = []

def setup(): 
    size(1200, 900)
    background(0)
    stroke(255)
    drawers.append(Graph())
    create_verticle_grid(drawers[0])
    drawers[0].edges = get_full_connected_edges(drawers[0].verticles)
    
    
def draw():  
    background(0)
    drawers[0].display_verticles()
    drawers[0].display()
    drawers[0].move()
    saveFrame("image_####.jpg")
    

class Graph: 
    def __init__(self): 
        self.verticles = []
        self.edges = []
        
    def display(self): 
        for edge in self.edges : 
            edge.display()
            
    def display_verticles(self): 
        for verticle in self.verticles : 
            verticle.display()
        
    def move(self): 
        for verticle in self.verticles : 
            verticle.move()

        

class Verticle: 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self._stepx = rotation_step(self.y)
        self._stepy = 0
        
    def display(self): 
        point(self.x, self.y)
        
    def move(self): 
        self.x += self._stepx
        self.y += self._stepy
        if (self.x <= 150) or (self.x >= width -150) or (self.y <= 0) or (self.y >= height) :
            self._stepx = - self._stepx
            self._stepy = - self._stepy

        
class Edge: 
    def __init__(self, verticle1, verticle2): 
        self._verticle1 = verticle1
        self._verticle2 = verticle2
        
    def display(self):
        line(self._verticle1.x, 
             self._verticle1.y, 
             self._verticle2.x, 
             self._verticle2.y)
        
def create_verticle_grid(graph): 
    for i in range(300, width - 150, 150) : 
        for j in range(150, height, 150) : 
            print(i, j)
            graph.verticles.append(Verticle(i, j))

def get_full_connected_edges(verticles): 
    l=[]
    edges = combinations(verticles, 2)
    for edge in edges : 
        l.append(Edge(edge[0], edge[1]))
    return l

def rotation_step(y) : 
    return (float(y) / height - 0.5)* 7
    
