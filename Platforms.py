class Platforms():
    
    def __init__(self, pfX,pfY,pfWidth,pfHeight):
        self.x = pfX
        self.y = pfY
        self.wid = pfWidth
        self.hei = pfHeight
    def draw(self):
        fill(0)
        rect(self.x,self.y,self.wid,self.hei)
        
    def collisionDetection(self, posX, posY, player):
          
        if ( (posX + 60 >= self.x) and (posX <= self.x + self.wid) and ( posY + 60 >= self.y) and (posY <= self.y + self.hei) ):
            player.isColliding = True
            #fill(0,0,255)
            #textSize(32)
            #text("Colliding!", (width/2) - 100, height/2)
         #   player.grav.y = 0
           # saveFrame()
            player.canJump = True
            if posY > self.y:
                player.vel.y = 1.8
             #   print("first")
            elif posY +55 <= self.y:
                player.pos.y = self.y - 60
             #   print("second")
            elif posX< self.x:
                player.pos.x = self.x - 60
                player.vel.y = 1.8
             #   print("Third")
            
            elif posX + 2 >= self.x + self.wid:
                player.pos.x = self.x + self.wid   
                player.vel.y = 1.8
                #   print("Fourth")
            

    
    
    
    
    
    
    
    
    
    
    
    
    
            
