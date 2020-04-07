class Platforms():
    
    def __init__(self, pfX,pfY,pfWidth,pfHeight):
        self.x = pfX
        self.y = pfY
        self.wid = pfWidth
        self.hei = pfHeight
    def draw(self):
        fill(0)
        rect(self.x,self.y,self.wid,self.hei)
    
