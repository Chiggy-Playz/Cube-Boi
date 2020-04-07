class Platforms():
    
    def __init__(self, pfX,pfY,pfWidth,pfHeight):
        self.x = pfX
        self.y = pfY
        self.wid = pfWidth
        self.hei = pfHeight
    def draw(self):
        fill(0)
        rect(self.x,self.y,self.wid,self.hei)
    def collisionDetection(self, posX, posY):
        if ( (posX + 60 >= self.x) and (posX <= self.x + self.wid) and ( posY + 60 >= self.y) and (posY <= self.y + self.hei) ):#(posX >= self.x) and (posX < self.x + self.wid) and (posY < self.y + self.hei) and posY <= self.y):
           
            fill(0,0,255)
            textSize(32)
            text("Colliding!", (width/2) - 100, height/2)
           # saveFrame()
        else:
            fill(255,0,0)
            text("NOT Colliding!", (width/2) - 100, height/2)    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
