from Player import *
from Platforms import *
######## Global Variables ##########

player = Player() 
platforms = []
####### SETUP FUNCTION ########
def setup():
    size(1100,600)
    platforms.append(Platforms(150,500,800,30))
    
   

######### DRAW ###########
        
def draw():
    

    player.render()
    for pf in platforms:
        pf.draw()
   
def keyPressed():

         if (key == 'w') and (player.canJump) :
             
            player.vel.y = -1.8
            player.canJump = False
         elif key == 'd' :
            player.vel.x = 1.5
         elif key == 'a' :
             player.vel.x = -1.5   
            
         elif key == 'q':
             exit()   
            
def keyReleased():
    if key == 'd':
        player.vel.x = 0
    if key == 'a':
        player.vel.x = 0
                    
