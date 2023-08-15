#试图做一个乒乓球运动轨迹的程序
Dajiv='秋名山上行人稀,常有车手较高低.如今车道依旧在,不见当年老司机.'#彩蛋而已啦
import os
import pygame
from pygame.locals import*
from sys import exit
from random import randint
import time
import _thread
import threading
import json
#引入各种模块
os.system('install pygame')
pygame.init()
Myfont=pygame.font.Font('chinese//chineseFont.ttf',60)
myfont=pygame.font.Font('chinese//chineseFont.ttf',25)
cirlR=10
cirlr=int(cirlR/2)
rectX=25
rectY=50
screen=pygame.display.set_mode((800,600))
game_score=0
#设置各种颜色，方便使用
red=(255,0,0)
white=(255,255,255)
blue=(0,0,255)
orange=(255,128,0)
black=(0,0,0)
#
score_list=[]
def main():
    
        
    break_command=0
    pygame.mixer.music.load('music//game_music.mp3')
    pygame.mixer.music.play()
    BREAK=0
    Daja=''
    yper=0
    xper=0
    bgname='background.png'
    Time=pygame.time.Clock()
    FPS=Time.tick()
    a=1
    V=1*FPS/1000
    XV=int(randint(10,15))
    x=30
    y=int(300)
    move_x=int(0)
    move_X=0
    move_y=int(randint(200,350))
    move_Y=0
    pygame.mixer.music.play()
    _thread.start_new_thread(get_time,(break_command,))#开启一个新线程
    game_score_json=open('time.txt','r')
    
#--------------上面初始化，下面是主程序-----------------------------------
    while True:
        break_command=open('command.txt','w+')
        break_command.write('go')
        game_score=game_score_json.read()
        gameover=myfont.render('Game Over',False,red)
        daja=myfont.render(Daja,False,(0,0,0))
        background=pygame.image.load(bgname).convert()
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            else:
                if(event.type==KEYDOWN):
                    if event.key==K_a:
                        move_X=-5
                    if event.key==K_d:
                        move_X=5
                    if event.key==K_w:
                        move_Y=-5
                    if event.key==K_s:
                        move_Y=5
                    if event.key==K_j:
                        Daja=Dajiv
                elif(event.type==KEYUP):
                    move_X=0
                    move_Y=0
        
#--------------下面写画面生成---------------------------------------------
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        if y>520:
            score_list.append(game_score)
            screen.blit(myfont.render('Best:{}'.format(max(score_list)),False,red),(200,100))
            screen.blit(gameover,(50,100))
            pygame.display.update()
            #time.sleep(2)#感觉写错地方了
            BREAK=1
        screen.blit(daja,(50,150))
        pygame.draw.rect(screen,blue,(move_x,move_y,rectX,rectY))#球拍1（宽rectX，高rectY）
        pygame.draw.circle(screen,orange,(x,y),cirlR)#球，半径cirlR
        pygame.draw.rect(screen,white,Rect(50,500,700,100))
        pygame.display.update()
#---------------下面写动作判断--------------------------------------------
        
        move_x+=move_X
        move_y+=move_Y
        y+=int(V)
        x+=int(XV)
        xlist=Xspeed(v=XV,x=x,y=y,move_x=move_x,move_y=move_y,xper=xper,yper=yper,YV=V)
        LIST=speed(v=V,y=y,yper=yper,xper=xper)
        V=LIST[0]+LIST[1]+xlist[4]
        if(xlist[4]>0):
            if(V<0):
                V=abs(V)
        XV=xlist[0]+LIST[2]+xlist[3]
        xper=xlist[2]
        yper=xlist[1]
        break_command.close()
        if BREAK==1:
            
            break_command=open('command.txt','w+')
            break_command.write('1')
            
            
            break
        else:
            pass
def speed(v,y,xper,yper):
    #计算小球竖直移动加速度
    List=[]
    if(y<500):
        v+=1
    elif(y>500):
        v=-abs(v)
        yper+=1
        xper+=1
    elif(y==500):
        v=v
    List=[v,yper,xper]
    return List
def Xspeed(v,x,y,move_x,move_y,xper,yper,YV):
    #小球横向移动及反弹速度,v是速度
    List=[]
    if(x<800):
        v=v
        addx=0
        addy=0
    elif(x>800):
        v=-v
        addx=0
        addy=0
    elif(x==800):
        v=v
        addx=0
        addy=0
    if(x<0):
        v=-v
        addx=0
        addy=0
    elif(x==0):
        v=v
        addx=0
        addy=0
#碰撞体积 真难写mmp
    if(x+cirlr<move_x and x+cirlr>move_x+rectX and y+cirlr<move_y and y+cirlr>move_y+rectY or x-cirlr<move_x and x-cirlr>move_x+rectX and y-cirlr<move_y and y-cirlr>move_y+rectY):
        v=v
    if(x+cirlr>move_x and x+cirlr<move_x+rectX and y+cirlr>move_y and y+cirlr<move_y+rectY or x-cirlr>move_x and x-cirlr<move_x+rectX and y-cirlr>move_y and y-cirlr<move_y+rectY):
        v=-v
        addy=5
        addx=7
        if(YV>150):
            addy=0
            addx=0
    if(x==move_x and x==move_x+rectX and y==move_y and y==move_y+rectY):
        v=v
        addx=0
        addy=0
    List=[v,yper,xper,addy,addx]
    return List
def move():
    if(event.type==KEYDOWN):
        if event.key==K_a:
            move_x-=1
        elif event.key==K_d:
            move_x+=1
        elif event.key==K_w:
            move_y-=1
        elif event.key==K_s:
            move_y+=1
def beginning():#开始界面ヽ(￣ω￣(￣ω￣〃)ゝ
    Break=0
    color=(155,35,200)
    main_BGM=pygame.mixer.music.load('music//BGM.mp3')
    pygame.mixer.music.play()
    while True:
        
        Myfont=pygame.font.Font('chinese//chineseFont.ttf',60)
        myfont=pygame.font.Font('chinese//chineseFont.ttf',25)
        text1=Myfont.render('你能坚持一分钟吗？',False,white)
        text2=myfont.render('正常模式',False,white,color)
        text3=myfont.render('GM模式',False,white,color)
        text4=myfont.render('退出',False,white,color)
        screen.blit(text1,(150,100))
        screen.blit(text2,(200,350))
        screen.blit(text3,(200,400))
        screen.blit(text4,(200,450))
        pygame.display.update()
        a=pygame.mouse.get_pressed()
        b=pygame.mouse.get_pos()
        for event in pygame.event.get():
            #if a[0]==1:
                #print(pygame.mouse.get_pos())
            if b[0]>=200 and b[0]<=300 and b[1]>=350 and b[1]<=380:
                if a[0]==1:
                    xrect=25
                    yrect=50
                    List=[xrect,yrect]
                    Break=1
            if b[0]>=200 and b[0]<=280 and b[1]>=400 and b[1]<=430:
                if a[0]==1:
                    Break=1
                    xrect=25
                    yrect=250
                    List=[xrect,yrect]
            if b[0]>=200 and b[0]<=250 and b[1]>=450 and b[1]<=480:
                if a[0]==1:
                    exit()
            


        if Break==1:
            break
        else:
            pass
    try:
        return List
    except:
        return 0
def get_time(break_command):#时间计算线程
    myfont=pygame.font.Font('chinese//chineseFont.ttf',25)
    game_time=0
    while True:
        sys_command=open('command.txt','r')
        game_score_return=open('time.txt','w+')
        break_command=sys_command.read()
        game_time+=0.1
        time.sleep(0.1)
        game_score_return.write(str(game_time))
        Game_time=int(game_time)
        game_score_return.write(str(game_time))
        game_score=myfont.render('time:{}s'.format(str(Game_time)),False,red)
        screen.blit(game_score,(200,50))
        pygame.display.update()
        if break_command=='1':
            break
        else:
            sys_command.close()
    







#-------------------------------------------------------------------------
while True:
    POLIST=beginning()
    #音乐
    pygame.mixer.music.stop()
    #音乐
    if POLIST==0:
        pass
    else:
        rectX=POLIST[0]
        rectY=POLIST[1]
    main()
    time.sleep(2)
    #音乐
    pygame.mixer.music.stop()
    #音乐

