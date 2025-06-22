import pygame

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("blue")

class c():
    def __init__(self,color,x,y,r):
        self.surf=screen
        self.color=color
        self.x=x
        self.y=y
        self.r=r
        self.pos=(self.x,self.y)
    def draw(self):
        pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def moveup(self):
        self.y-=10
        self.pos=(self.x,self.y)
        pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def moveleft(self):
        self.x-=10
        self.pos=(self.x,self.y)
        pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def moveright(self):
        self.x+=10
        self.pos=(self.x,self.y)
        pygame.draw.circle(self.surf,self.color,self.pos,self.r)
    def movedown(self):
        self.y+=10
        self.pos=(self.x,self.y)
        pygame.draw.circle(self.surf,self.color,self.pos,self.r)
        


#cir=c((148,179,224),50,50,50)
#cir.draw()
#circ=c("green",750,50,50)
#circ.draw()
circl=c("pink", 375,550,50)

run=True

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            circl.draw()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circle=c((148,179,224),pos[0],pos[1],5)
            circle.draw()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                screen.fill("blue")
                circl.moveup()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                screen.fill("red")
                circl.moveleft()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                screen.fill("green")
                circl.moveright()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                screen.fill("orange")
                circl.movedown()
            
        pygame.display.update()