import pygame,sys,os
from pygame.locals import *
import time
import random
import math
SIZE = 32
App_folder=os.path.dirname(os.path.realpath(sys.argv[0]))
class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.head = pygame.image.load((os.path.join(App_folder,".pictures/snake12.png")))
        self.image = pygame.image.load((os.path.join(App_folder,".pictures/bodyv.png")))
        self.direction = 'right'
        self.length = length
        self.x = [192]*length
        self.y = [192]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        
        self.boundary()
    def boundary(self):
        if self.x[0]>600:
            self.x[0]=0
        if self.x[0]<0:
            self.x[0]=576
        if self.y[0]>600:
            self.y[0]=0
        if self.y[0]<0:
            self.y[0]=576
        self.draw()
    def draw(self):
        self.parent_screen.blit(self.head, (self.x[0], self.y[0]))
        for i in range(1,self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()


class Apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.x = random.randint(1,18)*SIZE
        self.y = random.randint(1,18)*SIZE
        self.image=[]
        self.image.append(pygame.image.load((os.path.join(App_folder,".pictures/mango.png"))))
        self.image.append(pygame.image.load((os.path.join(App_folder,".pictures/apple.png"))))
        self.image.append(pygame.image.load((os.path.join(App_folder,".pictures/strawberry.png"))))
        self.image.append(pygame.image.load((os.path.join(App_folder,".pictures/orange-juice.png"))))
        self.image.append(pygame.image.load((os.path.join(App_folder,".pictures/watermelon.png"))))
        self.image1=random.choice(self.image)
    def draw(self):
        self.parent_screen.blit(self.image1, (self.x,self.y))
        pygame.display.flip()
    def move(self):
        self.image1=random.choice(self.image)
        self.x = random.randint(1,18)*SIZE
        self.y = random.randint(1,18)*SIZE
        self.checklevelpos()
        if (self.x,self.y) in game.level.list:
            self.move()
        if self.x in game.level.snake.x and self.y in game.level.snake.y:
            self.move()
    def checklevelpos(self):
        if game.levelclear=="Level: 1" or game.levelclear=="Level: 2":
            if self.x >=575 or self.y >=575 or self.x<=32 or self.y<=32:
                self.move()
        if game.levelclear=="Level: 2":
            if self.x in range(192,416) and self.y in (192,416):
                self.move()
        if game.levelclear=="Level: 3":
            if self.x in range(0,160) and self.y in (224,576):
                self.move()
            if self.x in range(288,448) and self.y in (224,576):
                self.move()
            if self.x in range(128,288) and self.y in (0,416):
                self.move()
            if self.x in range(480,608) and self.y in (0,416):
                self.move()
        if game.levelclear=="Level: 4":
            if self.x==288 and (self.y in range(64,192) or self.y==0):
                self.move()
            if (self.x in range(0,288) or self.x in range(384,672)) and self.y ==160:
                self.move()
            if self.y==416 and (self.x in range(0,224) or self.x in range(256,544)):
                self.move()
            if self.x==576 and (self.y in range(0,128) or self.y in range(480,608)):
                self.move()
            if self.x in range(0,288) and (self.y==256 or self.y==320):
                self.move()            
            if self.x==256 and self.y in range(448,576):
                self.move()
            
        
class Level4:
    def __init__(self,parent_surfacelevel):
        self.parent_surfacelevel=parent_surfacelevel
        self.snake = Snake(self.parent_surfacelevel, 5)
        self.snake.draw()
        self.speed=0.3
        self.brick=pygame.image.load((os.path.join(App_folder,".pictures/brickwall.png")))
        self.list=[]     
    def screen(self):
        for i in range(0,288,32):
            self.parent_surfacelevel.blit(self.brick,(i,160))
            self.list.append((i,168))
            self.parent_surfacelevel.blit(self.brick,(i+128,256))
            self.list.append((i+128,256))
            self.parent_surfacelevel.blit(self.brick,(i+128,320))
            self.list.append((i+128,320))
            self.parent_surfacelevel.blit(self.brick,(i+384,160))
            self.list.append((i+384,160))
            self.parent_surfacelevel.blit(self.brick,(i+256,416))
            self.list.append((i+2560,416))
        self.parent_surfacelevel.blit(self.brick,(288,0))
        self.list.append((228,0))
        for i in range(0,128,32):
            self.parent_surfacelevel.blit(self.brick,(288,i+64))
            self.list.append((228,i+64))
            self.parent_surfacelevel.blit(self.brick,(i,416))
            self.list.append((i,416))
            self.parent_surfacelevel.blit(self.brick,(576,i))
            self.list.append((576,i))
            self.parent_surfacelevel.blit(self.brick,(576,i+480))
            self.list.append((576,i+480))
            self.parent_surfacelevel.blit(self.brick,(256,i+448))
            self.list.append((256,i+448))
            self.parent_surfacelevel.blit(self.brick,(i+96,416))
            self.list.append((i+96,416))
            
    def over(self):
        for i in range(1,self.snake.length):
            if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                return(True)
        if self.snake.x[0]==288 and (self.snake.y[0] in range(64,192) or self.snake.y[0]==0):
            return(True)
        if (self.snake.x[0] in range(0,288) or self.snake.x[0] in range(384,672)) and self.snake.y[0] ==160:
            return(True)
        if self.snake.y[0]==416 and (self.snake.x[0] in range(0,224) or self.snake.x[0] in range(256,544)):
            return(True)
        if self.snake.x[0]==576 and (self.snake.y[0] in range(0,128) or self.snake.y[0] in range(480,608)):
            return(True)
        if self.snake.x[0] in range(128,416) and (self.snake.y[0]==256 or self.snake.y[0]==320):
            return(True)
        if self.snake.x[0]==256 and self.snake.y[0] in range(448,576):
            return(True)
        return(False)
    def play(self):
        self.screen()
        game.apple.draw()
        self.snake.walk()            
class Level3:
    def __init__(self,parent_surfacelevel):
        self.parent_surfacelevel=parent_surfacelevel
        self.snake = Snake(self.parent_surfacelevel, 5)
        self.snake.draw()
        self.speed=0.3
        self.brick=pygame.image.load((os.path.join(App_folder,".pictures/brickwall.png")))
        self.list=[]
    def screen(self):
        for i in range(0,160,32):
            self.parent_surfacelevel.blit(self.brick,(i,224))
            self.list.append((i,224))
            self.parent_surfacelevel.blit(self.brick,(i,576))
            self.list.append((i,576))
            self.parent_surfacelevel.blit(self.brick,(i+288,224))
            self.list.append((i+288,224))
            self.parent_surfacelevel.blit(self.brick,(i+288,576))
            self.list.append((i+288,576))
            self.parent_surfacelevel.blit(self.brick,(i+128,416))
            self.list.append((i+128,416))
            self.parent_surfacelevel.blit(self.brick,(i+128,0))
            self.list.append((i+128,0))
            self.parent_surfacelevel.blit(self.brick,(i+480,416))
            self.list.append((i+480,416))
            self.parent_surfacelevel.blit(self.brick,(i+480,0))
            self.list.append((i+480,0))
    def over(self):
        for i in range(1,self.snake.length):
            if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                return(True)
        if self.snake.x[0] in range(0,160) and self.snake.y[0] in (224,576):
            return(True)
        if self.snake.x[0] in range(288,448) and self.snake.y[0] in (224,576):
            return(True)
        if self.snake.x[0] in range(128,288) and self.snake.y[0] in (0,416):
            return(True)
        if self.snake.x[0] in range(480,608) and self.snake.y[0] in (0,416):
            return(True)
        return(False)
    def play(self):
        self.screen()
        game.apple.draw()
        self.snake.walk()
        
class Level2:
    def __init__(self,parent_surfacelevel):
        self.parent_surfacelevel=parent_surfacelevel
        self.snake = Snake(self.parent_surfacelevel, 5)
        self.snake.draw()
        self.speed=0.3
        self.list=[]
        self.brick=pygame.image.load((os.path.join(App_folder,".pictures/brickwall.png")))    
    def screen(self):
        for i in range(192,416,32):
            self.parent_surfacelevel.blit(self.brick,(i,192))
            self.parent_surfacelevel.blit(self.brick,(i,416))
            self.list.append((i,192))
            self.list.append((i,416))
        for i in range(0,608,32):
            self.parent_surfacelevel.blit(self.brick,(i,0))
            self.list.append((i,0))
            self.parent_surfacelevel.blit(self.brick,(i,568))
            self.list.append((i,568))
    def over(self):
        for i in range(1,self.snake.length):
            if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                return(True)
        if self.snake.x[0] in range(192,416) and self.snake.y[0] in (192,416):
            return(True)
        if self.snake.y[0]<32 or self.snake.y[0]>=576:
            return(True)
        return(False)
    def play(self):
        self.screen()
        game.apple.draw()
        self.snake.walk()
class Level1:
    def __init__(self,parent_surfacelevel):
        self.parent_surfacelevel=parent_surfacelevel
        self.snake = Snake(self.parent_surfacelevel, 5)
        self.snake.draw()
        self.speed=0.3
        self.brick=pygame.image.load((os.path.join(App_folder,".pictures/brickwall.png")))
        self.list=[]
    def screen(self):
        for i in range(0,608,32):
            self.parent_surfacelevel.blit(self.brick,(0,i))
            self.parent_surfacelevel.blit(self.brick,(i,0))
            self.parent_surfacelevel.blit(self.brick,(i,576))
            self.parent_surfacelevel.blit(self.brick,(576,i))
            self.list.append((0,i))
            self.list.append((i,0))
            self.list.append((i,576))
            self.list.append((576,i))
    def over(self):
        for i in range(1,self.snake.length):
            if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                return(True)
        if self.snake.x[0]<32 or self.snake.x[0]>=576 or self.snake.y[0]<32 or self.snake.y[0]>=576:
            return(True)
        return(False)
    def play(self):
        self.screen()
        game.apple.draw()
        self.snake.walk()
    
class Level0:
    def __init__(self,parent_surfacelevel):
        self.parent_surfacelevel=parent_surfacelevel
        self.snake = Snake(self.parent_surfacelevel, 5)
        self.snake.draw()
        self.speed=0.3
        self.list=[]
        
    def over(self):
        for i in range(1,self.snake.length):
            if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                return(True)
        return(False)
    def play(self):
        game.apple.draw()
        self.snake.walk()
        
class Game:
    def __init__(self):
        pygame.display.set_caption("Snake and Apple")
        icon=pygame.image.load((os.path.join(App_folder,".pictures/snakes.png")))
        pygame.display.set_icon(icon)
        self.bg=pygame.image.load((os.path.join(App_folder,".pictures/backg1.jpg"))) 
        self.Point=0
        pygame.init()
        self.surface = pygame.display.set_mode((608,650))
        self.point=pygame.font.Font("freesansbold.ttf",32)
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.level=Level0(self.surface)
        self.levelclear="Level: 0"
    def eat(self):
        self.Point+=1
        self.level.speed-=0.01
        if self.level.snake.direction=="left":
            self.level.snake.x.append(self.level.snake.x[-1]-SIZE)
            self.level.snake.y.append(self.level.snake.x[-1])
        if self.level.snake.direction=="right":
            self.level.snake.x.append(self.level.snake.x[-1]+SIZE)
            self.level.snake.y.append(self.level.snake.x[-1])
        if self.level.snake.direction=="up":
            self.level.snake.y.append(self.level.snake.y[-1]-SIZE)
            self.level.snake.x.append(self.level.snake.x[-1])
        if self.level.snake.direction=="down":
            self.level.snake.y.append(self.level.snake.y[-1]+SIZE)
            self.level.snake.x.append(self.level.snake.x[-1])
        self.level.snake.length+=1
    def checklevel(self):
        if self.Point==20 and self.levelclear=="Level: 0":
                self.level=Level1(self.surface)
                self.levelclear="Level: 1"
                self.apple.move()
        if self.Point==40 and self.levelclear=="Level: 1":
                self.level=Level2(self.surface)
                self.levelclear="Level: 2"
                self.level.snake.x[0]=32
                self.apple.move()
        if self.Point==60 and self.levelclear=="Level: 2":
                self.level=Level3(self.surface)
                self.levelclear="Level: 3"
                self.apple.move()
        if self.Point==80 and self.levelclear=="Level: 3":
                self.level=Level4(self.surface)
                self.levelclear="Level: 4"
                self.apple.move()
        
    def run(self):
        running = True
        while running:
            self.surface.blit(self.bg,(0,0))
            self.show=self.point.render("Point: "+str(self.Point), True,(16, 62, 97))
            self.surface.blit(self.show,(32,610))
            self.show2=self.point.render(self.levelclear, True,(16, 62, 97))
            self.surface.blit(self.show2,(450,610))
            self.checklevel()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.level.snake.move_left()

                    if event.key == K_RIGHT:
                        self.level.snake.move_right()

                    if event.key == K_UP:
                        self.level.snake.move_up()

                    if event.key == K_DOWN:
                        self.level.snake.move_down()

                elif event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            if (self.level.snake.x[0]==self.apple.x)and (self.level.snake.y[0]==self.apple.y):
                self.apple.move()
                self.apple.draw()
                self.eat()
            self.level.play()
            if self.level.over():
                running=False
                over_text=pygame.font.Font("freesansbold.ttf",55)
                over_text1=pygame.font.Font("freesansbold.ttf",32)
                over1=over_text.render("GAME - OVER", True,(16, 62, 97))
                over2=over_text1.render("Press space to Retry", True,(16, 62, 97))
                self.surface.blit(over1,(150,250))
                self.surface.blit(over2,(180,300))
                pygame.display.update()
            time.sleep(self.level.speed)

if __name__ == '__main__':
    game = Game()
    game.run()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        game = Game()
                        game.run()
            
    
