import pygame as pg
import sys
from dataclasses import dataclass
import copy
import random 
pg.init()
scr = screen_x,screen_y = 600,800
sizeGach = 40
bienGame = sizeGach * 10
screen = pg.display.set_mode(scr)
clock = pg.time.Clock()

l = [   [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
        [[0,0,0],[2,2,2],[0,0,2]],
        [[0,3,3],[0,3,3],[0,0,0]],
        [[0,0,4],[4,4,4],[0,0,0]],
        [[0,5,5],[5,5,0],[0,0,0]],
        [[6,6,0],[0,6,6],[0,0,0]],
        [[0,0,0],[7,7,7],[0,7,0]]]

colo = [(255,0,0),(255,255,0),(0,255,255),(255,0,255),(0,255,100),(0,0,255),(0,255,0)]
 
@dataclass
class bricks():
    l: list
    col:int = 4
    row:int = 0
    def show(self):
        for t,i in enumerate(self.l):
            for k,j in enumerate(i):
                if j > 0:
                    pg.draw.rect(screen, colo[j-1], ((self.col + k) * sizeGach,(self.row + t) * sizeGach,sizeGach - 2,sizeGach -2))
    def route(self):
        cd = copy.deepcopy(self.l)
        for i,n in enumerate(cd):
            for j,m in enumerate(n):
                self.l[j][len(n)-1-i] = m
        if not self.check(self.row,self.col):
            self.l = cd
    def update(self,c,r):
        if self.check(self.row+r,self.col+c):
            self.col += c
            self.row += r
            return True
        return False
    def check(self,row,col):
        for t,i in enumerate(self.l):
            for k,j in enumerate(i):
                if j > 0:
                    if row + t >= 20 or col+k<0 or col + k>= 10 or luoi[row+t][col+k]!= 0:
                        return False
        return True
def fail(ll,r,c):
    for t,i in enumerate(ll):
        for k,j in enumerate(i):
            if j > 0:
                luoi[r+t][c+k] = j
                    
def delrow():
    diem = 0
    for t,i in enumerate(luoi):
        for j in i: 
            if j == 0:
                break
        else:
            del luoi[t]
            luoi[0:0] = [[0]*10]
            print(len(luoi))
            diem += 1
    return diem
def ve(data,h):
    if h >0:
        sizx = 30
    else:
        sizx = sizeGach
    for t,i in enumerate(data):
        for k,j in enumerate(i):
            if j > 0:
                pg.draw.rect(screen, colo[j-1], ((h + k) * sizx,t * sizx,sizx - 2,sizx -2))
luoi = [[0]*10 for i in range(20)]
diem = 0
gach = bricks(random.choice(l))
nextB = random.randint(0,6)
h = 0
#tg = 3
while True:
    tg = 3
    screen.fill((0,0,0))
    pg.draw.rect(screen, (200,200,200),(0,0,bienGame,screen_y), 2)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                gach.route()
            elif event.key == pg.K_a:
                gach.update(-1,0)
            elif event.key == pg.K_d:
                gach.update(1,0)
            elif event.key == pg.K_s:
                tg = 1000
        if event.type == pg.QUIT:
            pg.exit()
            sys.exit()

    
    ve(l[nextB],15)
    if not gach.update(0,1):
        fail(gach.l,gach.row,gach.col)
        gach = bricks(l[nextB])
        nextB = random.randint(0,6)
    diem += delrow()
    ve(luoi,0)
    
    text = pg.font.SysFont("Arial",20).render( f'Score:{diem}',False,(255,255,0))
    screen.blit(text,(11*sizeGach,6* sizeGach))
    gach.show()
    pg.display.update()
    clock.tick(tg)

