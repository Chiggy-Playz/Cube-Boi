class Player():
    
    def __init__(self):
    
        self.pos = PVector(50, 600)
        self.vel = PVector(0,0)
        self.acc = PVector(0,0)
        self.grav = PVector(0, 0.02)
        self.canJump = True
    
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
        rect(self.pos.x, self.pos.y-60, 60, 60)            
     
    def edges(self):
        if (self.pos.y > height or self.pos.y < 0):
           self.pos.y *=0
           self.pos.y = height 
         
    def render(self):
        if self.pos.y == 600.0 :
            self.canJump = True 
        background(210)
        self.vel.y += (self.grav.y)
       # translate(-self.pos.x + 100,0)
       # print(str(self.pos.y))
       # print(str(self.canJump))
        self.update()
        self.edges()
        self.display()          
        
        
        
