class Player():
    
    def __init__(self):
    
        self.pos = PVector(550, 437)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.grav = PVector(0, 0.02)
        self.canJump = True
        self.isColliding = False
    
    def applyForce(self, force):
        self.acc.add(force)
    
    def stopMoving(self):
        self.vel.x = 0
        self.vel.y = 0
    
    def update(self) :
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.set(0,0)
        
    def display(self):
        fill(255)
        stroke(0)
        rect(self.pos.x, self.pos.y, 60, 60)            
     
    def edges(self):
        if (self.pos.y > 540 or self.pos.y < 0):
           self.pos.y *=0
           self.pos.y = 540 
         
    def render(self):
        if self.pos.y == 540.0 :
            self.canJump = True 
        background(210)
        if not self.isColliding:
            self.vel.y += (self.grav.y)
       # translate(-self.pos.x + 100,0)
       # print(str(self.pos.y))
       # print(str(self.pos.x))
        self.update()
        self.edges()
        self.display()          
        
        
        
