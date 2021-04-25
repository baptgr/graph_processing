# With the help of : 
# https://discourse.processing.org/t/fill-a-mesh-delaunay-object/3341/4

from random import randint, choice, sample
from itertools import combinations

frame_width = 800
frame_height = 450
n_verticles = 20
n_edges = 50

drawers = []

def setup(): 
    size(800, 450)
    background(0)
    stroke(255)
    noLoop()
    drawers.append(Graph())
    for _ in range(n_verticles): 
        drawers[0].verticles.append(create_new_verticle())
    
    l = get_full_connected_edges(drawers[0].verticles)
    drawers[0].edges = sample(l, n_edges)
    
    
    

def draw():  
    background(0)
    drawers[0].display_verticles()
    drawers[0].display()
    #drawers[0].move()
    

        
def mousePressed():
    redraw()
    

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
        
    def display(self): 
        point(self.x, self.y)
        
    def move(self): 
        self.x += randomGaussian() * 5
        self.y += randomGaussian() * 5
        
class Edge: 
    def __init__(self, verticle1, verticle2): 
        self._verticle1 = verticle1
        self._verticle2 = verticle2
        
    def display(self):
        line(self._verticle1.x, 
             self._verticle1.y, 
             self._verticle2.x, 
             self._verticle2.y)
        
        
def create_new_verticle(): 
    return Verticle(randint(0, frame_width), randint(0, frame_height))

def get_full_connected_edges(verticles): 
    l=[]
    edges = combinations(verticles, 2)
    for edge in edges : 
        l.append(Edge(edge[0], edge[1]))
    return l
    
