import pygame

pygame.init()

WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))

class rectangle():
    def __init__(self,color, x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.dimensions= (self.x, self.y, self.width, self.height)
        self.color=color
        self.surface=screen
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.dimensions)

rect1=rectangle((255,127,80),250,150, 300,300)
rect2=rectangle((255,127,80),600,300, 100,300)
rect1.draw()
rect2.draw()

run=True

while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.display.update()