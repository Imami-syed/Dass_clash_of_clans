import signal
import os
from time import sleep

from matplotlib.pyplot import bar
from numpy import min_scalar_type
from src.input import *
from src.classs import *

row = 54
col = 140
os.system("clear")
val = input ("Select the character role to spawn King(🤴: K ) or Queen(👸 : Q) >> ")
while(1):
    if val == "K" : 
        b=board()
        b.show()
        # b.k=king(50,136,b)
        # player=king(50,136,b)
        player=king()
        player.coor(50,136,b)
        break
    elif val == "Q" : 
        b=board()
        b.show()
        # player=queen(50,136,b)
        player=queen()
        player.coor(50,136,b)   
        # b.k=queen(50,136,b)
        break
    else:
        val=input("please enter correct input in K or Q : ")
# # b.k=queen(28,78,b) and 30, 80 now 54, 140
pq=Get()
h=[hut() for i in range(5)]
h[0].coor(5,105,b)
h[1].coor(32,95,b)
h[2].coor(15,25,b)
h[3].coor(35,55,b)
h[4].coor(45,45,b)
h[0].set(b)
h[1].set(b)
h[2].set(b)
h[3].set(b)
h[4].set(b)
c=[cannon() for i in range(2)]
c[0].coor(45,95,b)
c[1].coor(15,55,b)
c[0].set(b)
c[1].set(b)
wiz=[wizardtower() for i in range(2)]
wiz[0].coor(32,15,b)
wiz[1].coor(15,115,b)
wiz[0].set(b)
wiz[1].set(b)
t=townhall()
t.coor(27,70,b)
t.set(b)
w=[wall() for i in range(100)]
w[0].coor(25,68,b)
w[1].coor(25,69,b)
w[2].coor(25,70,b)
w[3].coor(25,71,b)
w[4].coor(25,72,b)
w[5].coor(25,73,b)
w[6].coor(25,74,b)
w[7].coor(25,75,b)
w[8].coor(26,68,b)
w[9].coor(26,75,b)
w[10].coor(27,68,b)
w[11].coor(27,75,b)
w[12].coor(28,68,b)
w[13].coor(28,75,b)
w[14].coor(29,68,b)
w[15].coor(29,75,b)
w[16].coor(30,68,b)
w[17].coor(30,75,b)
w[18].coor(31,68,b)
w[19].coor(31,69,b)
w[20].coor(31,70,b)
w[21].coor(31,71,b)
w[22].coor(31,72,b)
w[23].coor(31,73,b)
w[24].coor(31,74,b)
w[25].coor(31,75,b)
barb=[barbarians() for i in range(3)]    
bal=[balloon() for i in range(3)]
a=[archer() for i in range(3)]
i = 1
# def minhut(self,x, y):
#     # for b6 in barb:
#     b6=barb[0]
#     xmin = b6.dist(b6.x,h[0].x,b6.y,h[0].y)
#     for h6 in h:
#         req=h6
#         x6=b6.dist(b6.x,h6.x,b6.y,h6.y)
#         if(xmin > x6):
#             x6=xmin 
#             req=h6
#         self.x=req.x
#         self.y=req.y
#         if barb[0].x <self.x:
#             for i in range(self.x-barb[0].x):
#                 if(board.board[barb[0].x+i][barb[0].y]==' '):
#                     board.board[barb[0].x+i][barb[0].y]='B'
#                 board.board[barb[0].x][barb[0].y]=' '
#                 barb[0].x +=1
#         if barb[0].x >self.x:
#             for i in range(barb[0].x-self.x):
#                 if(board.board[barb[0].x-i][barb[0].y]==' '):
#                     board.board[barb[0].x-i][barb[0].y]='B'
#                 board.board[barb[0].x][barb[0].y]=' '
#                 barb[0].x -=1
#         if barb[0].y <self.y:
#             for i in range(self.y-barb[0].y):
#                 if(board.board[barb[0].x][barb[0].y+i]==' '):
#                     board.board[barb[0].x][barb[0].y+i]='B'
#                 board.board[barb[0].x][barb[0].y]=' '
#                 barb[0].y +=1
#         if barb[0].y >self.y:
#             for i in range(barb[0].y-self.y):
#                 if(board.board[barb[0].x][barb[0].y-i]==' '):
#                     board.board[barb[0].x][barb[0].y-i]='B'
#                 board.board[barb[0].x][barb[0].y]=' '
#                 barb[0].y -=1
#         # print('happening')
    
while os.path.exists("replays/replay%s.txt" % i):
    i += 1
with open("replays/replay%s.txt" % i, "w") as f:
    while(1):
        os.system("clear")
        b.show()
        player.healthdisplay(player.health)
        if(player.health<=0): 
            print("Your player's health is Zero, Spawn other troops to continue the game!")
            player.remove(b)
        # b.statusss()
        p=input_to(pq,0.1)
        if p == None:
            p='.'
            pass
        else:
            while(True):
                if t.health!=0: break
                for i in range(5):  
                    if h[i].health!=0: break
                for i in range(2):
                    if c[i].health!=0: break
                for i in range(2):
                    if wiz[i].health!=0: break
            for i in range(len(c)):
                if val== 'Q' : c[i].attackqueen(player, b)
                else : c[i].attackking(player, b)
            for i in range(len(wiz)):
                if val== 'Q' : wiz[i].attackqueen(player, b)
                else : wiz[i].attackking(player, b)
            if p=='q':
                print("You quit the game!!")
                break
            elif p=="f":
                if val == 'Q' : s=spellq.change("f",player)
                else : spell.change("f",player)
            elif p=="h":
                if val == 'Q' : s=spellq.change("h",player)
                else : spell.change("h", player)
                pass
            elif p=='w':
                if player.health > 0 : player.move(b,'w')
            elif p=='a':
                if player.health > 0 : player.move(b,'a')
            elif p=='s':
               if player.health > 0 : player.move(b, 's')
            elif p=='d':
                if player.health > 0 :  player.move(b, 'd')
            elif p=='1':
                barb[0].coor(4,6,b)
                barb[0].movetowards(15,25,b)
                h[2].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[2].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[2].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[2].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[2].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                barb[0].movetowards(15,55,b)
                c[1].attackedbybarbarian(b)
                # c[1].attackbar(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[1].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[1].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[1].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[1].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
            elif p=='2':
                barb[1].coor(4,4,b)
                barb[1].movetowards(35,55,b)
                h[3].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                barb[1].movetowards(45,45,b)
                h[4].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                barb[1].movetowards(45,93,b)
                c[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                c[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
            elif p=='3':
                # bar3.coor(50,4,b)
                barb[2].coor(4,8,b)
                barb[2].movetowards(32,15,b)
                wiz[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbybarbarian(b)
                os.system('clear')
                b.show()
                sleep(0.1)
            elif p=='4':
                # a1.coor(25,35,b)
                a[0].coor(4,134,b)
            elif p=='5':
                a[1].coor(4,136,b)
                a[1].movetowards(5,105,b)
                h[0].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[0].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[0].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[0].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[0].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                a[1].movetowards(5,105,b)
                wiz[1].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[1].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[1].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[1].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[1].attackedbya(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                # a2.coor(4,61,b)
            elif p=='6':
                a[2].coor(4,132,b)
            elif p=='7':
                bal[0].coor(50,4,b)
                bal[0].movetowards(32,15,b)
                wiz[0].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                wiz[0].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
            elif p=='8':
                bal[1].coor(50,6,b)
                bal[1].movetowards(45,45,b)
                h[4].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[4].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                bal[1].movetowards(35,55,b)
                h[3].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
                h[3].attackedbyb(b)
                os.system('clear')
                b.show()
                sleep(0.1)
            elif p=='9':
                bal[2].coor(50,8,b)
            elif p=='l':
                x=player.x
                y=player.y
                for i in range(x-5,x+5):
                    for j in range(y-7,y+7):
                        if b.board[i][j]==Fore.YELLOW+'H'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'H'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'H'+Style.RESET_ALL:
                            for k in range(len(h)):
                                if(i==h[k].x) and (j==h[k].y):
                                    b.board[i][j]=' '
                                    h[k].health=0
                        if b.board[i][j]==Fore.YELLOW+'C'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'C'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'C'+Style.RESET_ALL:
                            for ki in range(len(c)):
                                if(i==c[ki].x) and (j==c[ki].y):
                                    b.board[i][j]=' '
                                    c[ki].health=0
                        if b.board[i][j]==Fore.YELLOW+'T'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'T'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'T'+Style.RESET_ALL:
                            t.health-=30
                            t.set(b)
                            
            elif p==' ':
                for i in range(len(h)):
                    if val == "Q" : h[i].attackedbyqueen(b)
                    else : h[i].attackedbyking(b)
                for i in range(len(c)):
                   if val == "Q" :  c[i].attackedbyqueen(b)
                   else: c[i].attackedbyking(b)
                for i in range(len(w)):
                    if val == "Q" :  w[i].attackedbyqueen(b)
                    else: w[i].attackedbyking(b)
                if val == "Q" :
                    for i in range(player.x-1-10,player.x+2+10):
                        for j in range(player.y-1-10,player.y+2+10):
                            if b.board[i][j]==Fore.YELLOW+'T'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'T'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'T'+Style.RESET_ALL:
                                t.health-=player.damage
                                t.set(b)
                                if(t.health<=0):
                                    t.remove(b)
                                    t.health=0
                                    break
                                break
                else: 
                    for i in range(player.x-1,player.x+2):
                        for j in range(player.y-1,player.y+2):
                            if b.board[i][j]==Fore.YELLOW+'T'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'T'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'T'+Style.RESET_ALL:
                                t.health-=player.damage
                                t.set(b)
                                if(t.health<=0):
                                    t.remove(b)
                                    t.health=0
                                    break
                                break
                for i in range(len(wiz)):
                    if val == "Q" : wiz[i].attackedbyqueen(b)
                    else: wiz[i].attackedbyking(b)
            elif p=='o':
                for i in range(len(w)):
                    w[i].aqea(b)
                for i in range(len(c)):
                    c[i].aqea(b)
                for i in range(len(wiz)):
                    wiz[i].aqea(b)
                for i in range(len(h)):
                    h[i].aqea(b)
                for i in range(player.x-1-16,player.x+2+16):
                        for j in range(player.y-1-16,player.y+2+16):
                            if b.board[i][j]==Fore.YELLOW+'T'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'T'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'T'+Style.RESET_ALL:
                                t.health-=player.damage
                                t.set(b)
                                if(t.health<=0):
                                    t.remove(b)
                                    t.health=0
                                    break
                                break
        
        f.write(str(p))



