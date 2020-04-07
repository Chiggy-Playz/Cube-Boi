from Player import *
from Platforms import *
######## Global Variables ##########

player = Player() 
platforms = []
debug = False
####### SETUP FUNCTION ########
def setup():
    global posX_s
    global posY_s
    global pfX_s
    global pfY_s  
    
    size(1100,600)
    platforms.append(Platforms(300,500,500,30))
    

      
######### DRAW ###########
        
def draw():
    global debug
    player.render()
    for pf in platforms:
        pf.draw()
        
    if debug:
        debugF()     
    platforms[0].collisionDetection(player.pos.x, player.pos.y, player)
   
######## Some Functions ###########
def debugF():
    fill(255,0,0)
    textSize(32)    
    text( ("PosX : " + str(player.pos.x)) ,50, 50)
    text( ("PosY : " + str(player.pos.y)), 50, 150 )
    text( ("PlatformX : " + str(platforms[0].x)), 800, 50 )
    text( ("PlatformY : " + str(platforms[0].y)), 800, 150)
    text(str(player.canJump), 50, 250)   
   
########## INPUT ############   
def keyPressed():
    
        
         global debug
         if (key == 'w') and (player.canJump) :
             
            player.vel.y = -1.8
            player.canJump = False
         elif key == 'd' :
            player.vel.x = 1.5
         elif key == 'a' :
             player.vel.x = -1.5   
            
         elif key == 'q':
             exit()
             
         elif keyCode == 114:
             if debug:
                 debug = False
             else:
                 debug = True           
            
def keyReleased():
    if key == 'd':
        player.vel.x = 0
    if key == 'a':
        player.vel.x = 0
                    
