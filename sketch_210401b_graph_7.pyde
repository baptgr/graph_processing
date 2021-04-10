from random import randint, choice, sample
from itertools import combinations

frame_width = 800
frame_height = 800
n_verticles = 20
n_edges = 50

drawers = []

def setup(): 
    
    size(800, 800)
    background(0)
    stroke(255)
    #noLoop()
    drawers.append(Graph())
    for _ in range(n_verticles): 
        drawers[0].verticles.append(create_new_verticle())
    
    l = get_full_connected_edges(drawers[0].verticles)
    drawers[0].edges = sample(l, n_edges)
    
    
    

def draw():  
    
    fill(0, 5)
    rect(0, 0, width, height)
    drawers[0].display_verticles()
    drawers[0].display()
    drawers[0].move()
    #saveFrame("image_####.jpg")
    

        
#def mousePressed():
#    redraw()
    

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
        if (self.x <= 0) or (self.x >= width) or (self.y <= 0) or (self.y >= height) :
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
        
        
def create_new_verticle(): 
    return Verticle(randint(0, frame_width), randint(0, frame_height))

def get_full_connected_edges(verticles): 
    l=[]
    edges = combinations(verticles, 2)
    for edge in edges : 
        l.append(Edge(edge[0], edge[1]))
    return l

def rotation_step(y) : 
    return (float(y) / height - 0.5)* 3

def outward_step(x, y) : 
    center_x = width / 2
    center_y = height / 2
    
