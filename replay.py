import signal
import os
from time import sleep
from src.input import *
from src.classs import *
speed=input("Speed: ")

row = 54
col = 140
os.system("clear")
val = input ("Select the character role to spawn King(🤴: K ) or Queen(👸 : Q) >> ")
while(1):
    if val == "K" : 
        b=board()
        b.show()
        b.k=king(52,138,b)
        break
    elif val == "Q" : 
        b=board()
        b.show()
        b.k=queen(52,138,b)
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
t=townhall()
t.coor(27,70,b)
t.set(b)
w=[wall() for i in range(50)]
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
f=sys.argv[1]

with open(f,"r") as f:
    while(1):
        os.system("clear")
        b.show()
        b.k.healthdisplay(b.k.health)
        
        # print("Health:",b.k.health)
        p=f.read(1)
        sleep(0.1/float(speed))
        if p == '.':
            if(b.k.health<=0):
                print("Your ",val,"is dead and you lose the game")
                message = '''
                __     __           ___              __    _         __
                \ \   / /           | |             | |   | |   _   / /
                 \ \_/ /__  _   _   | |     ___  ___| |_  | |  (_) | |
                  \   / _ \| | | |  | |    / _ \/ __| __| | |      | |
                   | | (_) | |_| |  | |___| (_) \__ \ |_  |_|   _  | |
                   |_|\___/ \__,_|  |______\___/|___/\__| (_)  (_) | |
                                                                    \_\\
                '''
                print(message)
                break
            print("Health >> " ,str(b.k.health))
            # pass
        else:
            if p=='q':
                print("You quit the game!!")
                message = '''
                __     __           ___              __    _         __
                \ \   / /           | |             | |   | |   _   / /
                 \ \_/ /__  _   _   | |     ___  ___| |_  | |  (_) | |
                  \   / _ \| | | |  | |    / _ \/ __| __| | |      | |
                   | | (_) | |_| |  | |___| (_) \__ \ |_  |_|   _  | |
                   |_|\___/ \__,_|  |______\___/|___/\__| (_)  (_) | |
                                                                    \_\\
                '''
                print(message)
                break
            elif p=='f':
                s=spell("f",b,k)
            elif p=='h':
                s=spell("h",b,k)
            elif p=='w':
                b.k.move(b,'w')
            elif p=='a':
                b.k.move(b,'a')
            elif p=='s':
               b.k.move(b, 's')
            elif p=='d':
                b.k.move(b, 'd')
            elif p=='l':
                x=b.k.x
                y=b.k.y
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
                if val == "Q" :
                    for i in range(b.k.x-1,b.k.x+2):
                        for j in range(b.k.y-1,b.k.y+2):
                            if b.board[i][j]==Fore.YELLOW+'T'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'T'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'T'+Style.RESET_ALL:
                                t.health-=b.k.damage
                                t.set(b)
                                if(t.health<=0):
                                    t.remove(b)
                                    t.health=0
                                    break
                                break
                else: 
                    for i in range(b.k.x-1,b.k.x+2):
                        for j in range(b.k.y-1,b.k.y+2):
                            if b.board[i][j]==Fore.YELLOW+'T'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'T'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'T'+Style.RESET_ALL:
                                t.health-=b.k.damage
                                t.set(b)
                                if(t.health<=0):
                                    t.remove(b)
                                    t.health=0
                                    break
                                break
                for i in range(len(w)):
                    if val == "Q" : w[i].attackedbyqueen(b)
                    else: w[i].attackedbyking(b)
            elif p=='o':
                for i in range(len(w)):
                    w[i].aqea(b)
                for i in range(len(c)):
                    c[i].aqea(b)
                for i in range(len(h)):
                    h[i].aqea(b)
                for i in range(b.k.x-1,b.k.x+2):
                        for j in range(b.k.y-1,b.k.y+2):
                            if b.board[i][j]==Fore.YELLOW+'T'+Style.RESET_ALL or b.board[i][j]==Fore.RED+'T'+Style.RESET_ALL or b.board[i][j]==Fore.GREEN+'T'+Style.RESET_ALL:
                                t.health-=b.k.damage
                                t.set(b)
                                if(t.health<=0):
                                    t.remove(b)
                                    t.health=0
                                    break
                                break



