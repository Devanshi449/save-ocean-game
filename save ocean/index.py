import pygame
from random import randint
import time


clock=pygame.time.Clock()

#Initialize
pygame.init()
w=1366
h=768

icon=pygame.image.load("icon.jpg")
GD=pygame.display.set_mode((w,h),pygame.FULLSCREEN)
pygame.display.set_caption("Snakes N Ladders")
pygame.display.set_icon(icon)
pygame.display.update()

#Graphics:
black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)

board= pygame.image.load("boardSnakeAndLadder.png")
dice1=pygame.image.load("WhiteDice1_.png")
dice2=pygame.image.load("WhiteDice2_.png")
dice3=pygame.image.load("WhiteDice3_.png")
dice4=pygame.image.load("WhiteDice4_.png")
dice5=pygame.image.load("WhiteDice5_.png")
dice6=pygame.image.load("WhiteDice6_.png")

blackDice1=pygame.image.load("BlackDice1_.png")
blackDice2=pygame.image.load("BlackDice2_.png")
blackDice3=pygame.image.load("BlackDice3_.png")
blackDice4=pygame.image.load("BlackDice4_.png")
blackDice5=pygame.image.load("BlackDice5_.png")
blackDice6=pygame.image.load("BlackDice6_.png")

redgoti=pygame.image.load("redgoti.png")
yellowgoti=pygame.image.load("yellowgoti.png")
greengoti=pygame.image.load("greengoti.png")
bluegoti=pygame.image.load("bluegoti.png")
menubg=pygame.image.load("menu.jpg")
p=pygame.image.load("playbg.jpg")
intbg=pygame.image.load("intropic.png")
intbg2=pygame.image.load("intropic2.jpg")
intbg3=pygame.image.load("intropic3.jpg")
intbg4=pygame.image.load("intropic4.jpg")
intbg5=pygame.image.load("intropic5.jpg")
credits1=pygame.image.load("credits.jpg")

pygame.mixer.music.load("music.wav")
snakesound=pygame.mixer.Sound("snake.wav")
win=pygame.mixer.Sound("win.wav")
lose=pygame.mixer.Sound("lose.wav")
ladder=pygame.mixer.Sound("ladder.wav")

#mouse pos
mouse=pygame.mouse.get_pos()
click=pygame.mouse.get_pressed()

d=41
posList=[[868,382]]
startX=868
startY=382-d
for i in range(9):
    for j in range(9):
        if(j==0):
            posList.append([startX,startY])
            continue
        if(i%2==0):
            startX-=d
        else:
            startX+=d
        posList.append([startX,startY])
    startY-=d

negList=[]
startX=868
startY=382
for i in range(9):
    for j in range(9):
        if(j==0):
            negList.append([startX,startY])
            continue
        if(i%2==0):
            startX-=d
        else:
            startX+=d
        negList.append([startX,startY])
    startY+=d
lad=[False,False,False,False]
sna=[False,False,False,False]
Plane=[False,False,False,False]
player=[True,True,True,True]

#Message displaying for buttons
def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

   

def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

#Message displaying for field
def message_display1(text,x,y,fs,c):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)
    

def text_objects1(text, font,c):
    textSurface = font.render(text, True,c)
    return textSurface, textSurface.get_rect()

#Goti movement function
def goti(a):
    global posList
    global negList
    if(a>=0):
        return posList[a][0],posList[a][1]
    else:
        return negList[(-a)][0],negList[(-a)][1]
     

def text_objects1(text, font):
    textSurface = font.render(text, True,black)
    return textSurface, textSurface.get_rect()

#Ladder check
def ladders(x):
    if x==3: return 16
    elif x==17:return 20
    elif x==22:return 32
    elif x==25:return 30
    elif x==41:return 51
    elif x==46:return 63
    elif x==49:return 78
    elif x==58:return 69
    elif x==-12:return -5
    elif x==-26:return -10
    elif x==-33:return -21
    elif x==-46:return -42
    elif x==-52:return -37
    elif x==-66:return -59
    elif x==-68:return -50
    else:return x

#Snake Check
def snakes(x): 
    if x==13:return -1
    elif x==35:return -1
    elif x==11:return -1
    elif x==43:return -1
    elif x==55:return -1
    elif x==-8:return -1
    elif x==-16:return -1
    elif x==-35:return -1
    elif x==-40:return -1
    elif x==-64:return -1
    elif x==-70:return -1
    return x

def aeroplane(x): 
    if x==75:return -1
    return x

def dice(a, sign):
    if sign==1:
        if a==1:
            a=dice1
        elif a==2:
            a=dice2
        elif a==3:
            a=dice3
        elif a==4:
            a=dice4
        elif a==5:
            a=dice5
        elif a==6:
            a=dice6

        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1000:
            GD.blit(a,(300,500))
            pygame.display.update()
    else:
        if a==1:
            a=blackDice1
        elif a==2:
            a=blackDice2
        elif a==3:
            a=blackDice3
        elif a==4:
            a=blackDice4
        elif a==5:
            a=blackDice5
        elif a==6:
            a=blackDice6

        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1000:
            GD.blit(a,(300,500))
            pygame.display.update()

#for mute and unmute    
def button2(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)    
    
    






#Buttons for playing:
def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
    

#Turn
def turn(score,l,s,plane):
    Dice = randint(1,2)
    sign=-1
    if Dice==1:
        sign=1
    a=randint(1,6)#player dice roll
    if a==6:
        six=True
    else:
        six=False
    p=dice(a, sign)
    if(plane == False):
        score+=sign*a
    else:
        if(a==2):
            score+=sign*a
            plane=False
    if score>=0 and score<=81:
        lad=ladders(score) #checking for ladders for player
        if lad!=score:
            l=True
            pygame.mixer.Sound.play(ladder)
            time=pygame.time.get_ticks()
            score=lad 
        snk=snakes(score)
        if snk!=score: #checking for snakes for player
            s=True
            pygame.mixer.Sound.play(snakesound)
            score-=sign*3
            #score=snk
        pln=aeroplane(score)
        if pln!=score:
            plane=True
    elif score<0 and score>=-81:
        lad=ladders(score) #checking for ladders for player
        if lad!=score:
            l=True
            pygame.mixer.Sound.play(ladder)
            time=pygame.time.get_ticks()
            score=lad 
        snk=snakes(score)
        if snk!=score: #checking for snakes for player
            s=True
            pygame.mixer.Sound.play(snakesound)
            score-=sign*3
            #score=snk
        pln=aeroplane(score)
        if pln!=score:
            plane=True
    else: #checks if player score is not grater than 100
        score-=sign*a
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1500:
            message_display1("Can't move!",650,50,35,black)
            pygame.display.update()
    return score,l,s,plane,six
    

#Quitting:
def Quit():
    pygame.quit()
    quit()

#Buttons:
def button(text,xmouse,ymouse,x,y,w,h,i,a,fs,b):
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            if b==1:
                options()
            elif b==5:
                return 5
            elif b==0:
                Quit()
            elif b=="s" or b==2 or b==3 or b==4:
                return b
            elif b==7:
                options()
            else :return True
                
            
            
            
                
            
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)


#def pause():
    #j=True
    #while j:
        #mouse pos
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #GD.blit(pause_bg,(0,0))
        #mouse=pygame.mouse.get_pos()
        #click=pygame.mouse.get_pressed()
        #if button("Resume",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,10):
            #j=False
        #if button("Main Menu",mouse[0],mouse[1],(w/2)-150,500,300,50,red,b_red,30,10):
            #main()
        #pygame.display.update()
    
def intro():
    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<2500:
        GD.blit(intbg,(0,0))
        pygame.display.update()
    while True:
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:    
            GD.blit(intbg2,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg3,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg4,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:
            GD.blit(intbg5,(0,0))
            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                return
        pygame.display.update()

def credit():
    while True:
        GD.blit(credits1,(0,0))
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()
        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if button("Back",mouse[0],mouse[1],w/2-100,700,200,50,red,b_red,25,20):
            main()
            
        pygame.display.update()
        
    


    
#Main Menu
def main():
        
    pygame.mixer.music.play(-1)

    
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()

        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        GD.blit(menubg,(0,0))
        button("Play",mouse[0],mouse[1],(w/2-100),h/2,200,100,green,b_green,60,1)

        button("Quit",mouse[0],mouse[1],(w/2-100),(h/2)+200,200,100,red,b_red,60,0)

        mouse=pygame.mouse.get_pos()
        if button2("Mute Music",mouse[0],mouse[1],1166,0,200,50,purple,b_purple,25):
            pygame.mixer.music.pause()
        if button2("Play Music",mouse[0],mouse[1],1166,75,200,50,purple,b_purple,25):
            pygame.mixer.music.unpause()
        if button2("Credits",mouse[0],mouse[1],1166,150,200,50,purple,b_purple,25):
            credit()
        
        pygame.display.update()


#Options Menu:
def options():
    
    flag=True
    while flag==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()


        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        b1=b2=b3=b4=b5=-1
        GD.blit(menubg,(0,0))
        #Single player button
        b1=button("Single Player",mouse[0],mouse[1],(w/2-150),250,300,50,green,b_green,30,"s")
        #2 player button
        b2=button("2 Players",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,2)
        #3 player
        b3=button("3 Players",mouse[0],mouse[1],(w/2)-150,450,300,50,green,b_green,30,3)
        #4 player
        b4=button("4 Players",mouse[0],mouse[1],(w/2)-150,550,300,50,green,b_green,30,4)
        #Back button
        b5=button("Back",mouse[0],mouse[1],0,650,200,50,red,b_red,30,5)
        if b5==5:
            main()
        if b1=="s":
            play(21)
        if b2==2:
            play(2)
        if b3==3:
            play(3)
        if b4==4:
            play(4)
        
        pygame.display.update()

def play(b):
    global lad
    global sna
    global player
    global Plane
    lad=[False,False,False,False]
    sna=[False,False,False,False]
    player=[True,True,True,True]
    Plane=[False,False,False,False]
    b6=-1
    time=3000
    if b6==7:
        options()
    GD.blit(p,(0,0))
    GD.blit(board,(w/2-150,h/2-380))
    xcr=xcy=xcg=xcb=868
    ycr=ycy=ycg=ycb=382
    GD.blit(redgoti,(xcy,ycy))
    if 5>b>1 or b==21:
        GD.blit(yellowgoti,(xcy,ycy))
            
    if 5>b>2 or b==21:

        GD.blit(greengoti,(xcg,ycg))
            
    if 5>b>2:
        GD.blit(bluegoti,(xcb,ycb))
    p1="Player 1"
    p1score=0
    if b==21:
        p2="Computer"
        p2score=0
    if 5>b>1:
        p2="Player 2"
        p2score=0
    if 5>b>2:
        p3="Player 3"
        p3score=0
    if 5>b>3:
        p4="Player 4"
        p4score=0
    t=1
    play=True
    while True:
        lad[0] = False
        lad[1] = False
        lad[2] = False
        lad[3] = False
        sna[0] = False
        sna[1] = False
        sna[2] = False
        sna[3] = False
        time=3000
        GD.blit(p,(0,0))
        GD.blit(board,(w/2-150,h/2-380))
        mouse=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                Quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Quit()

            
        if b==21:
            #(player,score,text,xmouse,ymouse,x,y,w,h,i,a,fs)
            
            if button1("Player 1",mouse[0],mouse[1],100,200,200,50,red,grey,30):
                if t==1 and player[0] == True:
                    p1score,lad[0],sna[0],Plane[0],six=turn(p1score,lad[0],sna[0],Plane[0])
                    #if not six:
                    t+=1
                    xcr,ycr=goti(p1score)
                    if p1score==81:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                    if p1score<-71:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 loses",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
            
            button1("Computer",mouse[0],mouse[1],100,300,200,50,yellow,grey,30)
            if True:
                if t==2 and player[1] == True:
                    p2score,lad[1],sna[1],Plane[1],six=turn(p2score,lad[1],sna[1],Plane[1])
                    xcy,ycy=goti(p2score)
                    #if not six:
                    t+=1
                    if b<3 or b==21:
                        t=1
                    
                    if p2score==81:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Computer Wins",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        break
                    if p2score<-71:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Computer loses",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break

        if 5>b>1:
            if button1("Player 1",mouse[0],mouse[1],100,200,200,50,red,grey,30):
                if t==1 and player[0]==True:
                    p1score,lad[0],sna[0],Plane[0],six=turn(p1score,lad[0],sna[0],Plane[0])
                    xcr,ycr=goti(p1score)
                    #if not six:
                    t+=1
                    if p1score==81:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                    if p1score<-71:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 loses",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        player[0]=False
                
            if button1("Player 2",mouse[0],mouse[1],100,300,200,50,yellow,grey,30):
                if t==2 and player[1]==True:
                    p2score,lad[1],sna[1],Plane[1],six=turn(p2score,lad[1],sna[1],Plane[1])
                    xcy,ycy=goti(p2score)
                    #if not six:
                    t+=1
                    if b<3:
                        t=1
                    
                    if p2score==81:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 2 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                    if p2score<-71:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 2 loses",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        player[1]=False
                else:
                    t+=1
                    if b<3:
                        t=1
                    
        if 5>b>2:
            if button1("Player 3",mouse[0],mouse[1],100,400,200,50,green,grey,30):
                if t==3:
                    p3score,lad[2],sna[2],Plane[2],six=turn(p3score,lad[2],sna[2],Plane[2])
                    xcg,ycg=goti(p3score)
                    #if not six:
                    t+=1
                    if b<4:
                        t=1
                    
                    if p3score==81:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 3 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                    if p3score<-71:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 3 loses",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        player[2]=False
                else:
                    t+=1
                    if b<4:
                        t=1
                
        if 5>b>3:   
            if button1("Player 4",mouse[0],mouse[1],100,500,200,50,blue,grey,30):
                if t==4 and player[3]==True:
                    p4score,lad[3],sna[3],Plane[3],six=turn(p4score,lad[3],sna[3],Plane[3])
                    xcb,ycb=goti(p4score)
                    #if not six:
                    t+=1
                    if b<5:
                        t=1
                    
                    if p4score==81:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 4 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
                    if p4score<-71:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 4 loses",650,50,50,black)
                            pygame.mixer.Sound.play(lose)
                            pygame.display.update()
                        player[3]=False
                else:
                    t+=1
                    if b<5:
                        t=1
        
        b6=button("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,7)
        GD.blit(redgoti,(xcr,ycr))
        if 5>b>1 or b==21:
            GD.blit(yellowgoti,(xcy+2,ycy))
            
            
        if 5>b>2:
            GD.blit(greengoti,(xcg+4,ycg))
            
             
        if 5>b>3:
            GD.blit(bluegoti,(xcb+6,ycb))
            
        if True in lad:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<200:
                message_display1("Environmental friendly!",650,50,35,black)
                pygame.display.update()
        if True in sna:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<200:
                message_display1("There's a Pollutant!",650,50,35,black)
                pygame.display.update()
        if True in Plane:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<200:
                message_display1("There's an aeroplane!",650,50,35,black)
                pygame.display.update()

        clock.tick(7)
        pygame.display.update()
        
            
        
intro()    
main()
