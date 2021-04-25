# With the help of : 
# https://discourse.processing.org/t/fill-a-mesh-delaunay-object/3341/4


add_library('triangulate')

from random import randint 
from java.util import ArrayList

n_vertex = 2000
v_list = list()

def setup(): 
    size(800, 800)
    background(0)
    stroke(255)
    
    for _ in range(n_vertex): 
        v_list.append(Verticle(randint(-200, width + 200), randint(-200, height + 200)))
    print(v_list)

    
def draw(): 
    background(0)
    
    pvlist = ArrayList()
    
    for verticle in v_list:
        pvlist.add(PVector(verticle.x, verticle.y))
        verticle.move()

    triangles = Triangulate.triangulate(pvlist)

    beginShape(TRIANGLES)
    for t in triangles:
        fill(0)
        vertex(t.p1.x, t.p1.y)
        vertex(t.p2.x, t.p2.y)
        vertex(t.p3.x, t.p3.y)
    endShape()
    print("******")
    saveFrame("output_2000/image_####.jpg")


class Verticle: 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self._stepx = randomGaussian() * 2
        self._stepy = randomGaussian() * 2
        
    def move(self): 
        self.x += self._stepx
        self.y += self._stepy
        if ((self.x <= -200) or (self.x >= width + 200) 
            or (self.y <= -200) or (self.y >= height + 200)) :
            self._stepx = - self._stepx
            self._stepy = - self._stepy


    

       
