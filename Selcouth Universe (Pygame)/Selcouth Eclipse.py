#Selcouth Universe
#Lily Zheng | NOVA
from gamelib import*

game=Game(900,500,"Selcouth Universe")

#Backgrounds
SS=Image("Uni.jpg",game)
SS.resizeBy(-76)

BRoom=Image("BRoom.jpg",game)
BRoom.resizeBy(-53)

bk2=Image("TRoom.jpg",game)
bk2.resizeBy(-52)

Forest1=Image("Forest1.png",game)

OverScreen=Image("Wings.jpg",game)

#Characters
SK=[]
SK.append(Animation("SKcrouch.png",4,game,212/4,31,10)) #0
SK.append(Animation("SKfall.png",2,game,106/2,45,5))
SK.append(Image("SKhurt.png",game))
SK.append(Image("SKjump.png",game))
SK.append(Animation("SKrun.png",6,game,354/6,35,5))
SK.append(Animation("SKslash.png",4,game,285/4,41,2))
SK.append(Animation("SKslash2.png",4,game,284/4,36))
SK.append(Animation("SKslash3.png",3,game,484/3,84))
SK.append(Image("SKstand.png",game))
SK.append(Animation("SKstand2.png",4,game,212/4,34,7))

SK.append(Animation("SKst.png",4,game,232/4,42,5))

SK.append(Animation("SKcrouchl.png",4,game,212/4,31,10))
SK.append(Animation("SKfalll.png",2,game,106/2,45,5))
SK.append(Image("SKhurtl.png",game))
SK.append(Image("SKjumpl.png",game))
SK.append(Animation("SKrunl.png",6,game,354/6,35,5))
SK.append(Animation("SKslashl.png",4,game,285/4,41,2))
SK.append(Animation("SKslash2l.png",4,game,284/4,36))
SK.append(Animation("SKslash3l.png",3,game,484/3,84))
SK.append(Image("SKstandl.png",game))
SK.append(Animation("SKstand2l.png",4,game,212/4,34,7))

for index in range(21):
    SK[index].resizeBy(100)


KK=[]
KK.append(Animation("KKintro.png",5,game,280/5,45,7))
KK.append(Animation("KKstand.png",3,game,153/3,45,7))

for index in range(2):
    KK[index].resizeBy(100)
    KK[index].moveTo(game.width/2,game.height-168)



Health=[]
Health.append(Shape("bar",game,100,14,(46,209,106)))
Health.append(Shape("bar",game,104,18,(0,0,0)))
Health.append(100)
Health.append(0)

Health[0].moveTo(100,25)
Health[1].moveTo(98,23)



S0=[]
S0.append(Shape("rectangle",game,60,400,(0,0,0)))
S0.append(Shape("rectangle",game,130,75,(0,0,0)))
S0.append(Shape("rectangle",game,80,110,(0,0,0)))
S0.append(Shape("rectangle",game,90,120,(0,0,0)))
S0.append(Shape("rectangle",game,110,110,(0,0,0)))
S0.append(Shape("rectangle",game,150,90,(0,0,0)))
S0.append(Shape("rectangle",game,270,130,(0,0,0)))
S0.append(Shape("rectangle",game,80,110,(0,0,0)))
S0.append(Shape("rectangle",game,100,150,(0,0,0)))
S0.append(Shape("rectangle",game,90,140,(0,0,0)))

#Additional
DGE=Image("DGE.png",game)
SpeechB=Image("Speech.png",game)
Tri=Image("Triangle.png",game)
Tri2=Image("Triangle2.png",game)

Opt=[]
Opt.append(Image("Border.png",game))
Opt.append(Image("Border.png",game))

for index in range(2):
    Opt[index].resizeTo(game.width,40)

#Avatars
AV=[]
AV.append(Image("SK.png",game))
AV.append(Image("SK.png",game))
AV.append(Image("KK.png",game))

AV[0].resizeBy(80)

for index in range(2):
    AV[index+1].resizeBy(70)
    AV[index+1].moveTo(50,game.height-50)
    AV[index+1].visible=False

#Scenes
Start=True
Scene0=True
Scene1=True
Scene2=True
Scene3=True
Scene4=True
End=True

#Initial Settings
Tri.resizeBy(-95)
Tri.rotateTo(180)
Tri.moveTo(game.width-20,game.height-20)

Tri2.resizeBy(-95)
Tri2.rotateTo(270)

AV[0].moveTo(50,50)

S0[0].moveTo(80,game.height/2)
S0[1].moveTo(175,150)
S0[1].rotateTo(15)
S0[2].moveTo(310,200)
S0[3].moveTo(270,330)
S0[3].rotateTo(50)
S0[4].moveTo(game.width/2+25,game.height/2-30)
S0[5].moveTo(game.width/2+20,game.height/2+90)
S0[6].moveTo(game.width/2+20,game.height/2+220)
S0[7].moveTo(660,210)
S0[8].moveTo(790,140)
S0[8].rotateTo(80)
S0[9].moveTo(700,355)
S0[9].rotateTo(140)
SK[10].moveTo(game.width/2+240,game.height-65)

S0D2 = ["Random boxes and your books.","The book you're reading currently is called:","Fabricated Universe"]
S0D2x = [game.width/2-100,game.width/2-150,game.width/2-70]

S0D3 = ["Your bed.","Go to sleep?"]
S0D3x = [game.width/2-35,game.width/2-50]

S0D5 = ["The tables and chairs in your dorm.","What did you expect?"]
S0D5x = [game.width/2-140,game.width/2-90]

S0D9 = ["Your roommate's bed, not yours.","Wonder where they went?"]
S0D9x = [game.width/2-110,game.width/2-100]

instr=200
DI=-1
a=-1
choice=False
blink=0
timeout1=0
Scene3Secret=0
Scene3Secret2=0

DGE.resizeBy(-52.5)
DGE.visible=False
DGE.moveTo(game.width/2,game.height/2+10)

S0F1=Font((185,191,255),34,black,"AmaticSC-Regular.ttf")
S0F2=Font((185,191,255),32,black,"Amatic-Bold.ttf")

OverScreen.resizeBy(-50)
OverScreen.moveTo(game.width/2,game.height/2+30)


def End1():
    blink=0
    End = True
    while End==True:
        game.processInput()
        OverScreen.draw()
        game.drawText("Better Luck Next Time...",game.width/2-240,game.height/2-100,Font((186,17,51),60,black,"caveat-bold.ttf"))
        if blink>-14:
            blink-=1
        if blink==-14:
            blink+=28
        if blink>-5:
            game.drawText("P   r   e   s   s       [Q]       t   o       Q   u   i   t",game.width/2-145,game.height/2+70,Font((37,160,217),35,black,"Amatic-Bold.ttf"))
        if keys.Pressed[K_q]:
            game.quit()
        game.update(30)

#Game
while Start==True:
    game.processInput()
    SS.draw()
    game.drawText("N",65,50,Font((186,17,51),42,black,"caveat-regular.ttf"))
    game.drawText("OVA PRESENTS:",90,50,Font(white,42,black,"caveat-regular.ttf"))
    game.drawText("S",game.width/2-170,game.height/2-50,Font((186,17,51),60,black,"caveat-bold.ttf"))
    game.drawText("elcouth",game.width/2-140,game.height/2-45,Font(white,50,black,"caveat-bold.ttf"))
    game.drawText("U",game.width/2,game.height/2-50,Font((186,17,51),60,black,"caveat-bold.ttf"))
    game.drawText("niverse",game.width/2+30,game.height/2-45,Font(white,50,black,"caveat-bold.ttf"))
    game.drawText("G",game.width-280,game.height-150,Font((26,111,201),42,black,"caveat-regular.ttf"))
    game.drawText("ame",game.width-260,game.height-150,Font(white,42,black,"caveat-regular.ttf"))
    game.drawText("D",game.width-190,game.height-150,Font((26,111,201),42,black,"caveat-regular.ttf"))
    game.drawText("eveloper:",game.width-168,game.height-150,Font(white,42,black,"caveat-regular.ttf"))
    game.drawText("Lily Zheng",game.width-200,game.height-105,Font(white,42,black,"caveat-regular.ttf"))
    game.drawText("LEFT CLICK TO CONTINUE",20,game.height-60,Font((64,214,149),37,black,"AmaticSC-Regular.ttf"))
    if mouse.LeftClick:
        Start=False
    game.update(30)

while Scene0==True:
    game.processInput()
    for index in range(10):
        S0[index].draw()
    BRoom.draw()
    DGE.draw()
    if timeout1>0:
        timeout1-=1
    if instr>0:
        game.drawText("Interact with objects on the screen by left-clicking.",game.width/2-230,50,S0F1)
        instr-=1
    if blink>-14:
        blink-=1
    if DI==-1 and choice==False:
        for index in range(10):
            S0[index].visible=True

    for index in range(10):
        if S0[index].collidedWith(mouse,"rectangle"):
            SpeechB.moveTo(mouse.x,mouse.y)
            SpeechB.draw()
        if S0[index].collidedWith(mouse,"rectangle") and mouse.LeftClick:
            DGE.visible=True
            timeout1=10
            blink=10
            if index==0:
                DI=0
                a=randint(1,3)
            if index==1:
                DI=1
                a=randint(1,2)
            if index==2:
                DI=2
                a=0
            if index==3:
                DI=3
                a=0
            if index==4:
                DI=4
                a=randint(1,2)
            if index==5:
                DI=5
                a=0
            if index==6:
                DI=6
                a=randint(1,2)
            if index==7:
                DI=7
                a=randint(1,2)
            if index==8:
                DI=8
                a=randint(1,2)
            if index==9:
                DI=9
                a=0
                
    if DI==0:
        if a==1:
            game.drawText("It's a mirror. Fascinating.",game.width/2-100,game.height-50,S0F2)
        if a==2:
            game.drawText("You look tired. Well, it is midnight.",game.width/2-140,game.height-50,S0F2)
        if a==3:
            game.drawText("The reflection of your fatigued eyes stares back at you.",game.width/2-200,game.height-50,S0F2)
    if DI==1:
        if a==1:
            game.drawText("Some paintings you drew over the summer.",game.width/2-160,game.height-50,S0F2)
        if a==2:
            game.drawText("Maybe you'll become an artist one day.",game.width/2-150,game.height-50,S0F2)
    if DI==2:
        if a<len(S0D2):
            game.drawText(S0D2[a],S0D2x[a],game.height-50,S0F2)
            if mouse.LeftClick and timeout1==0:
                a+=1
                timeout1=10
        else:
            DGE.visible=False
            DI=-1
            a=-1
    if DI==3:
        if a<len(S0D3):
            game.drawText(S0D3[a],S0D3x[a],game.height-50,S0F2)
            if mouse.LeftClick and timeout1==0:
                a+=1
                timeout1=10
        else:
            DGE.visible=False
            DI=-1
            a=-1
            choice=1
    if DI==4:
        if a==1:
            game.drawText("Luminous night skies are beautiful.", game.width / 2 - 140, game.height - 50, S0F2)
        if a==2:
            game.drawText("Can't really stargaze without any stars. You should sleep.",game.width/2-220,game.height-50,S0F2)
    if DI==5:
        if a<len(S0D5):
            game.drawText(S0D5[a],S0D5x[a],game.height-50,S0F2)
            if mouse.LeftClick and timeout1==0:
                a+=1
                timeout1=10
        else:
            DGE.visible=False
            DI=-1
            a=-1
    if DI==6:
        if a==1:
            game.drawText("A carpet that came with the dorm.",game.width/2-130,game.height-50,S0F2)
        if a==2:
            game.drawText("It's quite new.",game.width/2-60,game.height-50,S0F2)
    if DI==7:
        if a==1:
            game.drawText("Your roommate's property.",game.width/2-110,game.height-50,S0F2)
        if a==2:
            game.drawText("I don't think it's a good idea to touch them.",game.width/2-160,game.height-50,S0F2)
    if DI==8:
        if a==1:
            game.drawText("The posters your roommate collected randomly.",game.width/2-170,game.height-50,S0F2)
        if a==2:
            game.drawText("Who even are those on the posters?",game.width/2-130,game.height-50,S0F2)
    if DI==9:
        if a<len(S0D9):
            game.drawText(S0D9[a],S0D9x[a],game.height-50,S0F2)
            if mouse.LeftClick and timeout1==0:
                a+=1
                timeout1=10
        else:
            DGE.visible=False
            DI=-1
            a=-1

    if DI>-1:
        for index in range(10):
            S0[index].visible=False
        if blink==-14:
            blink+=28
        if blink>0:
            Tri.draw()
        if timeout1==0 and mouse.LeftClick:
            DGE.visible=False
            DI=-1
            a=-1

    if choice==True:
        Opt[0].moveTo(game.width/2,game.height/2-50)
        Opt[1].moveTo(game.width/2,game.height/2+50)
        for index in range(2):
            Opt[index].draw()
        game.drawText("Go to Sleep",game.width/2-50,game.height/2-70,Font((185,191,255),30,black,"caveat-regular.ttf"))
        game.drawText("Nevermind",game.width/2-50,game.height/2+30,Font((185,191,255),30,black,"caveat-regular.ttf"))
        if Opt[0].collidedWith(mouse,"rectangle"):
            Tri2.moveTo(game.width/2-120,game.height/2-50)
            Tri2.draw()
            if mouse.LeftClick:
                Scene0=False
        if Opt[1].collidedWith(mouse,"rectangle"):
            Tri2.moveTo(game.width/2-120,game.height/2+50)
            Tri2.draw()
            if mouse.LeftClick:
                choice=False
                DI=-1

    game.update(30)

choice=False
timeout2=0
instr=30
str1=False

S1D1 = ["It better had. Or else I would have had you executed.","Trying three times was enough.","Anymore and there wouldn't be anymore people to use."]
S1D1x = [game.width/2-200,game.width/2-120,game.width/2-200]

S1F1=Font((185,191,255),25,black,"caveatbrush-regular.ttf")
S1F2=Font((185,191,255),25,black,"caveat-regular.ttf")

while Scene1==True:
    game.processInput()
    game.clearBackground((0,0,0))
    DGE.draw()
    if str1==False:
        if instr>0:
            instr-=1
        if instr==0:
            DI=0
            blink=0
            str1=True
    if timeout1>0:
        timeout1-=1
    if timeout2>0:
        timeout2-=1
    if blink>-14:
        blink-=1
        
    if DI==0:
        game.drawText("???",100,game.height-100,S1F1)
        game.drawText("Finally, the spell worked!",game.width/2-90,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            DI=1
            a=0
            DGE.visible=False
            timeout2=10
    if DI==1 and timeout2==0:
        game.drawText("???",100,game.height-100,S1F1)
        if a<len(S1D1):
            game.drawText(S1D1[a],S1D1x[a],game.height-50,S1F2)
            if mouse.LeftClick and timeout1==0:
                a+=1
                timeout1=10
        else:
            DI=2
            a=-1
            DGE.visible=False
            timeout2=10
    if DI==2 and timeout2==0:
        game.drawText("???",100,game.height-100,S1F1)
        game.drawText("F- forgive me, your majesty.",game.width/2-110,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            DI=3
            DGE.visible=False
            timeout2=10
    if DI==3 and timeout2==0:
        game.drawText("'Majesty?'",100,game.height-100,S1F1)
        game.drawText("Regardless, why isn't he waking up?",game.width/2-130,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            DI=4
            DGE.visible=False
            timeout2=10
    if DI==4 and timeout2==0:
        game.drawText("???",100,game.height-100,S1F1)
        game.drawText("Certainly he would wake up soon, your majesty.",game.width/2-180,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            DI=5
            choice=True
            DGE.visible=False
            timeout2=10
    if choice==True and DI==5:
        Opt[0].moveTo(game.width/2,game.height/2-50)
        Opt[1].moveTo(game.width/2,game.height/2+50)
        for index in range(2):
            Opt[index].draw()
        game.drawText("Pretend you're sleeping",game.width/2-100,game.height/2-70,Font((185,191,255),30,black,"caveat-regular.ttf"))
        game.drawText("Wake up",game.width/2-50,game.height/2+30,Font((185,191,255),30,black,"caveat-regular.ttf"))
        if Opt[0].collidedWith(mouse,"rectangle"):
            Tri2.moveTo(game.width/2-120,game.height/2-50)
            Tri2.draw()
            if mouse.LeftClick and timeout2==0:
                choice=False
                timeout2=15
                DI=5.1
                ####ADD SCREEN SHAKE HERE
        if Opt[1].collidedWith(mouse,"rectangle"):
            Tri2.moveTo(game.width/2-120,game.height/2+50)
            Tri2.draw()
            if mouse.LeftClick and timeout2==0:
                choice=False
                timeout2=10
                DI=7
    if DI==5.1 and timeout2==0:
        game.drawText("'Majesty?'",100,game.height-100,S1F1)
        game.drawText("Drag him out and execute him.",game.width/2-120,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            DI=5.2
            DGE.visible=False
            timeout2=10
    if DI==5.2 and timeout2==0:
        game.drawText("???",100,game.height-100,S1F1)
        game.drawText("I beg for your forgiveness, my King!",game.width/2-140,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            DI=5.3
            DGE.visible=False
            timeout2=10
    if DI==5.3 and timeout2==0:
        game.drawText("King",100,game.height-100,S1F1)
        game.drawText("...",game.width/2,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            DI=6
            choice=True
            DGE.visible=False
            timeout2=10
    if choice==True and DI==6:
        Opt[0].moveTo(game.width/2,game.height/2-50)
        Opt[1].moveTo(game.width/2,game.height/2+50)
        for index in range(2):
            Opt[index].draw()
        game.drawText("Continue Pretending",game.width/2-80,game.height/2-70,Font((185,191,255),30,black,"caveat-regular.ttf"))
        game.drawText("Wake up",game.width/2-50,game.height/2+30,Font((185,191,255),30,black,"caveat-regular.ttf"))
        if Opt[0].collidedWith(mouse,"rectangle"):
            Tri2.moveTo(game.width/2-120,game.height/2-50)
            Tri2.draw()
            if mouse.LeftClick and timeout2==0:
                choice=False
                timeout2=15
                DI=6.1
        if Opt[1].collidedWith(mouse,"rectangle"):
            Tri2.moveTo(game.width/2-120,game.height/2+50)
            Tri2.draw()
            if mouse.LeftClick and timeout2==0:
                choice=False
                timeout2=10
                DI=7
    if DI==6.1 and timeout2==0:
        game.drawText("'Majesty'",100,game.height-100,S1F1)
        game.drawText("Kill him too.",game.width/2-30,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            ###ADD function to GAMEOVER
            Scene1=False
            End1()
    if DI==7 and timeout2==0:
        game.drawText("You open your eyes.",game.width/2-60,game.height-50,S0F2)
        if timeout1==0 and mouse.LeftClick:
            DI=-1
            Scene1=False

    if DI>-1:
        if timeout1==0 and timeout2==0 and choice==False:
            DGE.visible=True
        if blink==-14:
            blink+=28
        if blink>0 and timeout1==0 and timeout2==0 and choice==False:
            Tri.draw()

    game.update(30)

timeout1=10
str1=False
instr=10
DGE.moveTo(game.width/2,game.height/2+50)
#Time with animation of waking up.
##ADD AVATAR OF THE KING
##ADD AVATAR FOR PROP KNIGHT
##Change visiblity of the avatars
##in scene 3 add interactiveness with knights
##ADD THE KNIGHTS

S2D2=["My castle.","You are the summoned hero and you must...","Kill the Demon King on the other side of the continent."]
S2D2x=[game.width/2-50,game.width/2-170,game.width/2-220]
S2D4=["For you to return home, you must kill him.","He has gone berserk and the people are endangered!"]
S2D4x=[game.width/2-170,game.width/2-200]


while Scene2==True:
    game.processInput()
    bk2.draw()
    ###Add animation where you wake up
    KK[1].draw()
    SK[10].draw()
    Health[1].draw()
    Health[0].draw()
    Health[0].width=Health[2]
    Health[1].width=Health[2]+4
    DGE.draw()
    for index in range(3):
        AV[index].draw()

    if str1==False:
        if instr>0:
            instr-=1
        if instr==0:
            DI=0
            blink=0
            str1=True
    if DI==0:
        AV[2].visible=True
        game.drawText("King",100,game.height-100,S1F1)
        game.drawText("Oh? You're awake?",game.width/2-90,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            AV[2].visible=False
            DI=1
            DGE.visible=False
            timeout1=10
    if DI==1 and timeout1==0:
        AV[1].visible=True
        game.drawText("You",100,game.height-100,S1F1)
        game.drawText("Where am I?",game.width/2-80,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            AV[1].visible = False
            DI=2
            a=0
            DGE.visible=False
            timeout1=3
    if DI==2:
        if a<len(S2D2):
            AV[2].visible=True
            game.drawText("King",100,game.height-100,S1F1)
            game.drawText(S2D2[a],S2D2x[a],game.height-50,S1F2)
            if mouse.LeftClick and timeout1==0:
                a+=1
                timeout1=10
        else:
            AV[2].visible=False
            DGE.visible=False
            DI=3
            a=-1
            timeout1=10
    if DI==3 and timeout1==0:
        AV[1].visible = True
        game.drawText("You",100,game.height-100,S1F1)
        game.drawText("You're kidding me.",game.width/2-80,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            AV[1].visible = False
            DI=4
            a=0
            DGE.visible=False
            timeout1=3
    if DI==4:
        if a<len(S2D4):
            AV[2].visible=True
            game.drawText("King",100,game.height-100,S1F1)
            game.drawText(S2D4[a],S2D4x[a],game.height-50,S1F2)
            if mouse.LeftClick and timeout1==0:
                a+=1
                timeout1=10
        else:
            AV[2].visible=False
            DGE.visible=False
            DI=5
            a=-1
            timeout1=20
    if DI==5 and timeout1==0:
        AV[1].visible=True
        game.drawText("You",100,game.height-100,S1F1)
        game.drawText("...",game.width/2-20,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            AV[1].visible=False
            DI=6
            DGE.visible=False
            timeout1=3
    if DI==6 and timeout1==0:
        AV[1].visible=True
        game.drawText("You",100,game.height-100,S1F1)
        game.drawText("Huh?",game.width/2-20,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            AV[1].visible=False
            DI=7
            DGE.visible=False
            timeout1=10
    if DI==7 and timeout1==0:
        AV[2].visible=True
        game.drawText("King",100,game.height-100,S1F1)
        game.drawText("Off you go now!",game.width/2-50,game.height-50,S1F2)
        if timeout1==0 and mouse.LeftClick:
            AV[2].visible=False
            DI=-1
            DGE.visible=False
            Scene2=False

    if timeout1>0:
        timeout1-=1
    if blink>-14:
        blink-=1
        
    if DI>-1:
        if timeout1==0 and choice==False:
            DGE.visible=True
        if blink==-14:
            blink+=28
        if blink>0 and timeout1==0 and choice==False:
            Tri.draw()
    game.update(30)

for index in range(21):
    SK[index].moveTo(game.width/2-100,game.height-62)
left=False
right=False
str1=False
timeout1=0
timeout2=0

while Scene3==True:
    game.processInput()
    bk2.draw()
    AV[0].draw()
    KK[1].draw()
    Health[1].draw()
    Health[0].draw()
    Health[0].width=Health[2]
    Health[1].width=Health[2]+4
    if left==True and timeout1==0:
        SK[20].visible=True
        for index in range(20):
            SK[index].visible=False
    if right==True and timeout1==0:
        SK[9].visible=True
        for index in range(9):
            SK[index].visible=False
        for index in range(11):
            SK[index+10].visible=False
    SK[9].draw()
    SK[4].draw()
    SK[20].draw()
    SK[15].draw()
    if timeout1>0:
        timeout1-=1
    if timeout2>0:
        timeout2-=1
    if str1==False:
        right=True
        str1=True

    if keys.Pressed[K_LEFT] and not SK[0].x<=40:
        for index in range(21):
            SK[index].visible=False
        SK[15].visible=True
        for index in range(21):
            SK[index].x-=5
        left=True
        right=False
        timeout1=1

    if keys.Pressed[K_RIGHT]:
        for index in range(21):
            SK[index].visible=False
        SK[4].visible=True
        for index in range(21):
            SK[index].x+=5
        left=False
        right=True
        timeout1=1
    if SK[0].x<=40 and timeout2==0 and Scene3Secret<5:
        timeout2=40
    if Scene3Secret2>0:
        DGE.visible=True
        DGE.draw()
        game.drawText("Fine. Here's 50 more health points.",game.width/2-140,game.height-50,S0F2)
    if timeout2>0:
        DGE.visible=True
        DGE.draw()
        game.drawText("Nothing here.",game.width/2-60,game.height-50,S0F2)
    if Scene3Secret2>0:
        Scene3Secret2-=1
    if timeout2==40:
        Scene3Secret+=1
    if Scene3Secret==5:
        Health[2]+=50
        Scene3Secret2=25
        timeout2=0
        Scene3Secret=6
    if SK[9].x>=game.width+50 or SK[4].x>=game.width+50:
        Scene3=False

    game.update(30)



for index in range(21):
    SK[index].moveTo(10,game.height-72)

x=[]
y=[]

def slime(s):
    s.append(Image("SlimeFall.png",game))
    s.append(Animation("SlimeIdle.png",6,game,288/6,27,5))
    s.append(Animation("SlimeLand.png",5,game,330/5,31,4))
    s.append(Animation("SlimeWalk.png",9,game,540/9,27,5))

def slimev(v):
    v.append(True)
    v.append(0)
    v.append(False)
    v.append(True)
    v.append(False)
    v.append(100)
    v.append(0)
    v.append(False)
    v.append(False)
    v.append(1)
    v.append(Shape("bar",game,100,10,(38,189,118)))
    v.append(Shape("bar",game,104,14,(0,0,0)))
    v.append(10)
    v.append(False)

def cooldown(v):
    if v[1]==15:
        lr=randint(0,1)
        move=randint(0,1)
        if lr==0:
            v[3]=True
            v[4]=False
        if lr==1:
            v[4]=True
            v[3]=False
        if move==0:
            v[2]=False
            v[0]=True
        if move==1:
            v[0]=False
            v[2]=True
        v[1]=0

def Idle(s,v):
    if v[5]<=0:
        for index in range(4):
            s[index].visible=False
    if v[3]==True and v[0]==True and v[7]==False and v[8]==True:
        s[1].flipV=True
        s[1].visible=True
        s[0].visible=False
        s[2].visible=False
        s[3].visible=False
        if v[1]<15:
            v[1]+=1
    if v[4]==True and v[0]==True and v[7]==False and v[8]==True:
        s[1].flipV=False
        s[1].visible=True
        s[0].visible=False
        s[2].visible=False
        s[3].visible=False
        if v[1]<15:
            v[1]+=1

def Walking(s,v):
    if v[3]==True and v[2]==True and v[7]==False and v[8]==True:
        if s[1].x>750-Forest1.x:
            s[3].flipV=True
            s[3].visible=True
            s[0].visible=False
            s[1].visible=False
            s[2].visible=False
            for index in range(4):
                s[index].x-=3
        if v[1]<15:
            v[1]+=1
        if s[1].x<=750-Forest1.x:
            if v[1]<15:
                v[1]+=1
    if v[4]==True and v[2]==True and v[7]==False and v[8]==True:
        if s[1].x<Forest1.x+730:
            s[3].flipV=False
            s[3].visible=True
            s[0].visible=False
            s[1].visible=False
            s[2].visible=False
            for index in range(4):
                s[index].x+=3
        if v[1]<15:
            v[1]+=1
        if s[1].x>=Forest1.x+730:
            if v[1]<15:
                v[1]+=1

def HitR(s,v):
    if SK[5].collidedWith(s[1]) and tackle1==7 or SK[5].collidedWith(s[3]) and tackle1==7:
        v[5]-=20
        v[3]=True
        v[4]=False
        v[6]=10

def HitL(s,v):
    if SK[16].collidedWith(s[1]) and tackle1==7 or SK[16].collidedWith(s[3]) and tackle1==7:
        v[5]-=20
        v[3]=False
        v[4]=True
        v[6]=10


def SlimeHit(s,v):
    if v[5]==0:
        v[13]=True
    if v[13]==True:
        v[13]=False
        v[5]=-1
        Health[3]+=1
        if Health[2]<=150:
            Health[2]+=20
    if v[6]>0:
        if v[3]==True:
            v[4]=False
            v[8]=False
            v[7]=True
            s[0].flipV=True
            s[0].visible=True
            for index in range(3):
                s[index+1].visible=False
            v[6]-=1
            for index in range(4):
                s[index].x+=12*v[9]
                s[index].y-=12*v[9]
        if v[4]==True:
            v[3]=False
            v[8]=False
            v[7]=True
            s[0].flipV=False
            s[0].visible=True
            for index in range(3):
                s[index+1].visible=False
            v[6]-=1
            for index in range(4):
                s[index].x-=12*v[9]
                s[index].y-=12*v[9]
        v[9]*=0.90
        if v[9]<0.05:
            v[7]=False
            v[9]=1
            
    if not s[1].y>=game.height-50:
        for index in range(4):
            s[index].y+=3
    if s[1].y>=game.height-50:
        v[7]=False
        v[8]=True

Slime1=[]
Slime1_V=[]
slime(Slime1)
slimev(Slime1_V)

Slime2=[]
Slime2_V=[]
slime(Slime2)
slimev(Slime2_V)

Slime3=[]
Slime3_V=[]
slime(Slime3)
slimev(Slime3_V)

Slime4=[]
Slime4_V=[]
slime(Slime4)
slimev(Slime4_V)

Slime5=[]
Slime5_V=[]
slime(Slime5)
slimev(Slime5_V)

Slime6=[]
Slime6_V=[]
slime(Slime6)
slimev(Slime6_V)

Slime7=[]
Slime7_V=[]
slime(Slime7)
slimev(Slime7_V)

          
for index in range(4):
    Slime1[index].resizeBy(20)
    Slime2[index].resizeBy(30)
    Slime3[index].resizeBy(35)
    Slime4[index].resizeBy(15)
    Slime5[index].resizeBy(20)
    Slime6[index].resizeBy(25)
    Slime7[index].resizeBy(40)

for index in range(7):
    x.append(randint(150,1400))

for index in range(4):
    Slime1[index].moveTo(x[0],game.height-50)
    Slime2[index].moveTo(x[1],game.height-50)
    Slime3[index].moveTo(x[2],game.height-50)
    Slime4[index].moveTo(x[3],game.height-50)
    Slime5[index].moveTo(x[4],game.height-50)
    Slime6[index].moveTo(x[5],game.height-50)
    Slime7[index].moveTo(x[6],game.height-50)

Slime1[1].visible=True
Slime2[1].visible=True
Slime3[1].visible=True
Slime4[1].visible=True
Slime5[1].visible=True
Slime6[1].visible=True
Slime7[1].visible=True

Forest1.resizeBy(5)
Forest1.x=750

tackle=False
tackle1=0
tackle2=0
instr=200

jumping=False
landed=False
factor=1

def SKhit(s,v):
    if s[1].collidedWith(SK[1],"rectangle") or s[3].collidedWith(SK[12],"rectangle") or s[1].collidedWith(SK[3],"rectangle") or s[3].collidedWith(SK[14],"rectangle") or s[1].collidedWith(SK[4],"rectangle") or s[3].collidedWith(SK[15],"rectangle") or s[1].collidedWith(SK[9],"rectangle") or s[3].collidedWith(SK[20],"rectangle"):
         if s[1].visible==True and v[5]>0:
            if v[12]==10:
                Health[2]-=5
            v[12]=0
    if v[12]<10:
        v[12]+=1


while Scene4==True:
    game.processInput()
    Forest1.draw()
    AV[0].draw()
    Health[1].draw()
    Health[0].draw()
    Health[0].width=Health[2]
    Health[1].width=Health[2]+4
    if instr>0:
        instr-=1
        game.drawText("Press [a] to attack. Press [SPACE] to jump.",game.width/2-150,50,S0F2)
    if left==True and timeout1==0 and tackle==False and landed==True:
        SK[20].visible=True
        for index in range(20):
            SK[index].visible=False

    if right==True and timeout1==0 and tackle==False and landed==True:
        SK[9].visible=True
        for index in range(9):
            SK[index].visible=False
        for index in range(11):
            SK[index+10].visible=False

    if Slime1_V[5]>0:
        Slime1[0].draw()
        Slime1[1].draw()
        Slime1[2].draw()
        Slime1[3].draw()
        Slime1_V[11].draw()
        Slime1_V[11].moveTo(Slime1[1].x-37,Slime1[1].y-27)
        Slime1_V[11].width=Slime1_V[5]+4
        Slime1_V[10].draw()
        Slime1_V[10].moveTo(Slime1[1].x-35,Slime1[1].y-25)
        Slime1_V[10].width=Slime1_V[5]

    if Slime2_V[5]>0:
        Slime2[0].draw()
        Slime2[1].draw()
        Slime2[2].draw()
        Slime2[3].draw()
        Slime2_V[11].draw()
        Slime2_V[11].moveTo(Slime2[1].x-37,Slime2[1].y-27)
        Slime2_V[11].width=Slime2_V[5]+4
        Slime2_V[10].draw()
        Slime2_V[10].moveTo(Slime2[1].x-35,Slime2[1].y-25)
        Slime2_V[10].width=Slime2_V[5]

    if Slime3_V[5]>0:
        Slime3[0].draw()
        Slime3[1].draw()
        Slime3[2].draw()
        Slime3[3].draw()
        Slime3_V[11].draw()
        Slime3_V[11].moveTo(Slime3[1].x-37,Slime3[1].y-27)
        Slime3_V[11].width=Slime3_V[5]+4
        Slime3_V[10].draw()
        Slime3_V[10].moveTo(Slime3[1].x-35,Slime3[1].y-25)
        Slime3_V[10].width=Slime3_V[5]

    if Slime4_V[5]>0:
        Slime4[0].draw()
        Slime4[1].draw()
        Slime4[2].draw()
        Slime4[3].draw()
        Slime4_V[11].draw()
        Slime4_V[11].moveTo(Slime4[1].x-37,Slime4[1].y-27)
        Slime4_V[11].width=Slime4_V[5]+4
        Slime4_V[10].draw()
        Slime4_V[10].moveTo(Slime4[1].x-35,Slime4[1].y-25)
        Slime4_V[10].width=Slime4_V[5]

    if Slime5_V[5]>0:
        Slime5[0].draw()
        Slime5[1].draw()
        Slime5[2].draw()
        Slime5[3].draw()
        Slime5_V[11].draw()
        Slime5_V[11].moveTo(Slime5[1].x-37,Slime5[1].y-27)
        Slime5_V[11].width=Slime5_V[5]+4
        Slime5_V[10].draw()
        Slime5_V[10].moveTo(Slime5[1].x-35,Slime5[1].y-25)
        Slime5_V[10].width=Slime5_V[5]

    if Slime6_V[5]>0:
        Slime6[0].draw()
        Slime6[1].draw()
        Slime6[2].draw()
        Slime6[3].draw()
        Slime6_V[11].draw()
        Slime6_V[11].moveTo(Slime6[1].x-37,Slime6[1].y-27)
        Slime6_V[11].width=Slime6_V[5]+4
        Slime6_V[10].draw()
        Slime6_V[10].moveTo(Slime6[1].x-35,Slime6[1].y-25)
        Slime6_V[10].width=Slime6_V[5]

    if Slime7_V[5]>0:
        Slime7[0].draw()
        Slime7[1].draw()
        Slime7[2].draw()
        Slime7[3].draw()
        Slime7_V[11].draw()
        Slime7_V[11].moveTo(Slime7[1].x-37,Slime7[1].y-27)
        Slime7_V[11].width=Slime7_V[5]+4
        Slime7_V[10].draw()
        Slime7_V[10].moveTo(Slime7[1].x-35,Slime7[1].y-25)
        Slime7_V[10].width=Slime7_V[5]

    SKhit(Slime1,Slime1_V)
    SKhit(Slime2,Slime2_V)
    SKhit(Slime3,Slime3_V)
    SKhit(Slime4,Slime4_V)
    SKhit(Slime5,Slime5_V)
    SKhit(Slime6,Slime6_V)
    SKhit(Slime7,Slime7_V)

    SK[9].draw()
    SK[4].draw()
    SK[20].draw()
    SK[15].draw()
    SK[14].draw()
    SK[3].draw()
    SK[1].draw()
    SK[12].draw()

    Idle(Slime1,Slime1_V)
    cooldown(Slime1_V)
    Walking(Slime1,Slime1_V)
    
    Idle(Slime2,Slime2_V)
    cooldown(Slime2_V)
    Walking(Slime2,Slime2_V)

    Idle(Slime3,Slime3_V)
    cooldown(Slime3_V)
    Walking(Slime3,Slime3_V)
    
    Idle(Slime4,Slime4_V)
    cooldown(Slime4_V)
    Walking(Slime4,Slime4_V)

    Idle(Slime5,Slime5_V)
    cooldown(Slime5_V)
    Walking(Slime5,Slime5_V)

    Idle(Slime6,Slime6_V)
    cooldown(Slime6_V)
    Walking(Slime6,Slime6_V)

    Idle(Slime7,Slime7_V)
    cooldown(Slime7_V)
    Walking(Slime7,Slime7_V)

    if timeout1>0:
        timeout1-=1
    if str1==False:
        right=True
        str1=True
    if Forest1.x>=750 and keys.Pressed[K_LEFT] and not SK[0].x<=0 and tackle==False:
        for index in range(21):
            SK[index].visible=False
        SK[15].visible=True
        for index in range(21):
            SK[index].x-=5
        left=True
        right=False
        timeout1=1
    if Forest1.x>=170 and keys.Pressed[K_LEFT] and SK[0].x==250 and tackle==False:
        for index in range(21):
            SK[index].visible=False
        SK[15].visible=True
        Forest1.x+=5
        for index in range(4):
            Slime1[index].x+=4
            Slime2[index].x+=4
            Slime3[index].x+=4
            Slime4[index].x+=4
            Slime5[index].x+=4
            Slime6[index].x+=4
            Slime7[index].x+=4
        left=True
        right=False
        timeout1=1
    if Forest1.x<=170 and keys.Pressed[K_LEFT] and SK[0].x>=250 and tackle==False:
        for index in range(21):
            SK[index].visible=False
        SK[15].visible=True
        for index in range(21):
            SK[index].x-=5
        left=True
        right=False
        timeout1=1
    if keys.Pressed[K_RIGHT] and SK[0].x<250 and tackle==False:
        for index in range(21):
            SK[index].visible=False
        SK[4].visible=True
        for index in range(21):
            SK[index].x+=5
        left=False
        right=True
        timeout1=1
    if Forest1.x>170 and keys.Pressed[K_RIGHT] and SK[0].x>=250 and tackle==False:
        for index in range(21):
            SK[index].visible=False
        SK[4].visible=True
        for index in range(4):
            Slime1[index].x-=4
            Slime2[index].x-=4
            Slime3[index].x-=4
            Slime4[index].x-=4
            Slime5[index].x-=4
            Slime6[index].x-=4
            Slime7[index].x-=4
        Forest1.x-=5
        left=False
        right=True
        timeout1=1
    if Health[3]<5:
        if Forest1.x<=170 and keys.Pressed[K_RIGHT] and SK[0].x>=250 and tackle==False and SK[0].x<=game.width+10:
            for index in range(21):
                SK[index].visible=False
            SK[4].visible=True
            for index in range(21):
                SK[index].x+=5
            left=False
            right=True
            timeout1=1
    if Health[3]>=5:
        if Forest1.x<=170 and keys.Pressed[K_RIGHT] and SK[0].x>=250 and tackle==False:
            for index in range(21):
                SK[index].visible=False
            SK[4].visible=True
            for index in range(21):
                SK[index].x+=5
            left=False
            right=True
            timeout1=1
    if SK[0].x>=game.width+10 and Health[3]<5:
        game.drawText("You need to kill at least 5 slimes.",game.width/2-120,50,S0F2)
    if SK[0].x>=game.width+40 and Health[3]>=5:
        End1()

    if keys.Pressed[K_a] and tackle2==0:
        tackle=True
        tackle1=7
        tackle2=30

    if tackle==True and tackle1>0 and right==True and jumping==False and landed==True:
        SK[5].visible=True
        SK[5].draw()
        for index in range(5):
            SK[index].visible=False
        for index in range(15):
            SK[index+6].visible=False
        HitR(Slime1,Slime1_V)
        HitR(Slime2,Slime2_V)
        HitR(Slime3,Slime3_V)
        HitR(Slime4,Slime4_V)
        HitR(Slime5,Slime5_V)
        HitR(Slime6,Slime6_V)
        HitR(Slime7,Slime7_V)
        
    if tackle==True and tackle1>0 and left==True and jumping==False and landed==True:
        SK[16].visible=True
        SK[16].draw()
        for index in range(16):
            SK[index].visible=False
        for index in range(4):
            SK[index+17].visible=False
        HitL(Slime1,Slime1_V)
        HitL(Slime2,Slime2_V)
        HitL(Slime3,Slime3_V)
        HitL(Slime4,Slime4_V)
        HitL(Slime5,Slime5_V)
        HitL(Slime6,Slime6_V)
        HitL(Slime7,Slime7_V)
        
    SlimeHit(Slime1,Slime1_V)
    SlimeHit(Slime2,Slime2_V)
    SlimeHit(Slime3,Slime3_V)
    SlimeHit(Slime4,Slime4_V)
    SlimeHit(Slime5,Slime5_V)
    SlimeHit(Slime6,Slime6_V)
    SlimeHit(Slime7,Slime7_V)
            
    if tackle1==0:
        SK[5].visible=False
        tackle=False
    if tackle1>0:
        tackle1-=1
    if tackle2>0:
        tackle2-=1
        
    if keys.Pressed[K_SPACE] and landed and not jumping and tackle==False:
        jumping=True
        
    if jumping:
        jumping=True
        landed=False
        for index in range(21):
            SK[index].y-=12*factor
        if left==True:
            SK[14].visible=True
            for index in range(14):
                SK[index].visible=False
            for index in range(6):
                SK[index+15].visible=False
        if right==True:
            SK[3].visible=True
            for index in range(3):
                SK[index].visible=False
            for index in range(17):
                SK[index+4].visible=False
        factor*=0.90
        if factor<0.05:
            jumping=False
            factor=1
    if not SK[0].y>=game.height-72:
        for index in range(21):
            SK[index].y+=2
    if jumping==False and landed==False:
        if left==True:
            SK[12].visible=True
            for index in range(12):
                SK[index].visible=False
            for index in range(8):
                SK[index+13].visible=False
        if right==True:
            SK[1].visible=True
            SK[0].visible=False
            for index in range(19):
                SK[index+2].visible=False
    if SK[0].y>=game.height-72:
        landed=True
    if Health[2]<=0:
        End1()
    game.update(30)

game.quit()
