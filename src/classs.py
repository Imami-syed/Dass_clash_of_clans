import os
import sys
from time import sleep
from colorama import init, Fore, Back, Style
from requests import head
import math
row = 54
col = 140
class board():
    def __init__(self):
        self.board = [[' ' for i in range(140)] for j in range(54)]
        self._rows=54
        self._cols=140
        self.k=0
        for val in range(self._cols):
            self.board[0][val]='█'
            self.board[self._rows-1][val]='█'
        for val in range(self._rows):
            self.board[val][0]='█'
            self.board[val][self._cols-1]='█'
        # self.board[0][0]='█'
        # self.board[0][0]='▪' ▚
        # self.board[0][self._cols-1]='█'
        # self.board[self._rows-1][0]='█'
        # self.board[self._rows-1][self._cols-1]='█'

    def show(self):
        for i in range(54):
            for j in range(140):
                print(self.board[i][j], end="")
            print()
        print()
    def statusss(self):
        # for i in range(54):
        #     for j in range(140):
        #         if(self.board[i][j]!='T' and self.board[i][j] !='W' or self.board[i][j]!='C' or self.board[i][j]!='H'):
        #             print("YOU WON THE GAME!!")
        troops=0
        for i in range(54):
            for j in range(140):
                if(self.board[i][j]=='T' or self.board[i][j] =='W' or self.board[i][j]=='C' or self.board[i][j]=='H'):
                    print("YOU WON THE GAME!!")
        

class building:
    def __init__(self) -> None:
        self.health = 100
        self.x=0
        self.y=0
        self.k=0     
class troop:
    def __init__(self) -> None:
        self.health = 100
        self.x=0
        self.y=0
class townhall(building):
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='T'
        board.board[x][y+1]='T'
        board.board[x][y+2]='T'
        board.board[x][y+3]='T'
        board.board[x+1][y]='T'
        board.board[x+1][y+1]='T'
        board.board[x+1][y+2]='T'
        board.board[x+1][y+3]='T'
        board.board[x+2][y]='T'
        board.board[x+2][y+1]='T'
        board.board[x+2][y+2]='T'
        board.board[x+2][y+3]='T'
    
    def remove(self,board):
        x=self.x
        y=self.y
        board.board[x][y]=' '
        board.board[x][y+1]=' '
        board.board[x][y+2]=' '
        board.board[x][y+3]=' '
        board.board[x+1][y]=' '
        board.board[x+1][y+1]=' '
        board.board[x+1][y+2]=' '
        board.board[x+1][y+3]=' '
        board.board[x+2][y]=' '
        board.board[x+2][y+1]=' '
        board.board[x+2][y+2]=' '
        board.board[x+2][y+3]=' '

    def set(self,board):
        if self.health<30:
            x=self.x
            y=self.y
            board.board[x][y]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x][y+1]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x][y+2]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x][y+3]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+1][y]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+1][y+1]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+1][y+2]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+1][y+3]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+2][y]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+2][y+1]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+2][y+2]=Fore.RED+'T'+Style.RESET_ALL
            board.board[x+2][y+3]=Fore.RED+'T'+Style.RESET_ALL
        elif self.health<70:
            x=self.x
            y=self.y
            board.board[x][y]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x][y+1]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x][y+2]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x][y+3]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+1][y]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+1][y+1]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+1][y+2]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+1][y+3]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+2][y]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+2][y+1]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+2][y+2]=Fore.YELLOW+'T'+Style.RESET_ALL
            board.board[x+2][y+3]=Fore.YELLOW+'T'+Style.RESET_ALL
        else:
            x=self.x
            y=self.y
            board.board[x][y]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x][y+1]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x][y+2]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x][y+3]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+1][y]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+1][y+1]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+1][y+2]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+1][y+3]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+2][y]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+2][y+1]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+2][y+2]=Fore.GREEN+'T'+Style.RESET_ALL
            board.board[x+2][y+3]=Fore.GREEN+'T'+Style.RESET_ALL
class hut(building):
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='H'
        # board.damagek=20
    def remove(self,x,y,board):
        board[x][y]=' '
    
    def set(self,board):
        if self.health<30:
            board.board[self.x][self.y]=Fore.RED+'H'+Style.RESET_ALL
        elif self.health<70:
            board.board[self.x][self.y]=Fore.YELLOW+'H'+Style.RESET_ALL
        else:
            board.board[self.x][self.y]=Fore.GREEN+'H'+Style.RESET_ALL
    def healthcheck(self, health):
        if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbyking(self, board):
        if board.board[self.x-1][self.y]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbyb(self, board):
        if board.board[self.x-1][self.y]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbya(self, board):
        if board.board[self.x-1][self.y]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbybarbarian(self, board):
        if board.board[self.x-1][self.y]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbyqueen(self, board):
        for t in range(6,10,1):
            if(self.x-t > 0):
                if board.board[self.x-t][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.x+t < row):
                if board.board[self.x+t][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.y+t < col):
                if board.board[self.x][self.y+t]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.y-t > 0):
                if board.board[self.x][self.y-t]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
    def aqea(self,board):
        for i in range(16, 16+9, 1):
            if self.x-i > 0:
                if board.board[self.x-i][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.x+i < row:
                if board.board[self.x+i][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.y-i > 0:
                if board.board[self.x][self.y-i]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.y+i < col:
                if board.board[self.x][self.y+i]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
class cannon(building):
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='C'+Fore.GREEN
        self.damageb=25
        self.damagek=10
        self.damage=15

    def remove(self,x,y,board):
        board[x][y]=' '
    def attackking(self,king, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='K'):
                king.health -= self.damagek 
            if(board.board[self.x+i][self.y]=='K'):
                king.health -= self.damagek 
            if(board.board[self.x][self.y-i]=='K'):
                king.health -= self.damagek 
            if(board.board[self.x][self.y+i]=='K'):
                king.health -= self.damagek 
    def attackqueen(self,queen, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='Q'):
                queen.health -= self.damagek
            if(board.board[self.x+i][self.y]=='Q'):
                queen.health -= self.damagek 
            if(board.board[self.x][self.y-i]=='Q'):
                queen.health -= self.damagek 
            if(board.board[self.x][self.y+i]=='Q'):
                queen.health -= self.damagek   
    def attackwall(self, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='◈'):
                board.board[self.x][self.y]=' '
            if(board.board[self.x+i][self.y]=='◈'):
                board.board[self.x][self.y]=' '
            if(board.board[self.x][self.y-i]=='◈'):
                board.board[self.x][self.y]=' '
            if(board.board[self.x][self.y+i]=='◈'):
                board.board[self.x][self.y]=' '
    def attackbar(self,barbarian, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='B'):
                barbarian.health -= self.damageb 
            if(board.board[self.x+i][self.y]=='B'):
                barbarian.health -= self.damageb 
            if(board.board[self.x][self.y-i]=='B'):
                barbarian.health -= self.damageb 
            if(board.board[self.x][self.y+i]=='B'):
                barbarian.health -= self.damageb
    def attackedbybarbarian(self, board):
        if board.board[self.x-1][self.y]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    # def cannonattack(self,x, y, board):
    #     king1=king(x, y, board)
    #     queen1=queen(x, y, board)
    #     for t in range(-5,5,1):
    #         for m in range(-5, 5, 1):
    #             if(board.board[self.x-t][self.y-m] == 'K'):
    #                 king1.healthupdate(king1.health-self.damagek)
    #             if(board.board[self.x-t][self.y-m] == 'Q'):
    #                queen1.healthupdate(queen1.health-self.damagek)
                
    # def attackfrmcannon(self,x, y,board):
    #     king1=king(x,y,board)
    #     for i in range(5,5,1):
    #         for j in range(-5,5,1):
    #             if(board.board[self.x-i][self.y-j]=='K'):
    #                 # boardking1.health-=self.damagek
    #                 king.healthdisplay(board)
    #             if(board.board[self.x-i][self.y-j]=='Q'):
    #                 king1.health-=self.damageq
    #             if(board.board[self.x-i][self.y-j]=='H'):
    #                 king1.health-=self.damage
    #             if(board.board[self.x-i][self.y-j]=='T'):
    #                 king1.health-=self.damage
    #             if(board.board[self.x-i][self.y-j]=='◈'):
    #                 king1.health-=self.damage
    
    def set(self,board):
        if self.health<30:
            board.board[self.x][self.y]=Fore.RED+'C'+Style.RESET_ALL
        elif self.health<70:
            board.board[self.x][self.y]=Fore.YELLOW+'C'+Style.RESET_ALL
        else:
            board.board[self.x][self.y]=Fore.GREEN+'C'+Style.RESET_ALL
    def attackedbyking(self, board):
        if board.board[self.x-1][self.y]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbyqueen(self, board):
        for t in range(6, 10,1):
            if(self.x-t > 0):
                if board.board[self.x-t][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.x+t < row):
                if board.board[self.x+t][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.y+t < col):
                if board.board[self.x][self.y+t]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.y-t > 0):
                if board.board[self.x][self.y-t]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
    def aqea(self,board):
        for i in range(16, 16+9, 1):
            if self.x-i > 0:
                if board.board[self.x-i][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.x+i < row:
                if board.board[self.x+i][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.y-i > 0:
                if board.board[self.x][self.y-i]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.y+i < col:
                if board.board[self.x][self.y+i]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
class wizardtower(building):
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='W'+Fore.GREEN
        self.damageb=25
        self.damagek=10
        self.damage=15

    def remove(self,x,y,board):
        board[x][y]=' '
    def attackking(self,king, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='K'):
                king.health -= self.damagek 
            if(board.board[self.x+i][self.y]=='K'):
                king.health -= self.damagek 
            if(board.board[self.x][self.y-i]=='K'):
                king.health -= self.damagek 
            if(board.board[self.x][self.y+i]=='K'):
                king.health -= self.damagek 
    def attackedbybarbarian(self, board):
        if board.board[self.x-1][self.y]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='B' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbyb(self, board):
        if board.board[self.x-1][self.y]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='▚' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbya(self, board):
        if board.board[self.x-1][self.y]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='A' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackqueen(self,queen, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='Q'):
                queen.health -= self.damagek
            if(board.board[self.x+i][self.y]=='Q'):
                queen.health -= self.damagek 
            if(board.board[self.x][self.y-i]=='Q'):
                queen.health -= self.damagek 
            if(board.board[self.x][self.y+i]=='Q'):
                queen.health -= self.damagek 
    def attackwall(self, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='◈'):
                board.board[self.x][self.y]=' '
            if(board.board[self.x+i][self.y]=='◈'):
                board.board[self.x][self.y]=' '
            if(board.board[self.x][self.y-i]=='◈'):
                board.board[self.x][self.y]=' '
            if(board.board[self.x][self.y+i]=='◈'):
                board.board[self.x][self.y]=' '
    def attackbar(self,barbarian, board):
        for i in range(0,6,1):
            if(board.board[self.x-i][self.y]=='B'):
                barbarian.health -= self.damageb 
            if(board.board[self.x+i][self.y]=='B'):
                barbarian.health -= self.damageb 
            if(board.board[self.x][self.y-i]=='B'):
                barbarian.health -= self.damageb 
            if(board.board[self.x][self.y+i]=='B'):
                barbarian.health -= self.damageb 
    def set(self,board):
        if self.health<30:
            board.board[self.x][self.y]=Fore.RED+'W'+Style.RESET_ALL
        elif self.health<70:
            board.board[self.x][self.y]=Fore.YELLOW+'W'+Style.RESET_ALL
        else:
            board.board[self.x][self.y]=Fore.GREEN+'W'+Style.RESET_ALL
    def attackedbyking(self, board):
        if board.board[self.x-1][self.y]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x+1][self.y]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y+1]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
        if board.board[self.x][self.y-1]=='K' :
            self.health-=20
            self.set(board)
            if(self.health<=0):
                board.board[self.x][self.y]=' '
                self.health=0
    def attackedbyqueen(self, board):
        for t in range(6, 10,1):
            if(self.x-t > 0):
                if board.board[self.x-t][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.x+t < row):
                if board.board[self.x+t][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.y+t < col):
                if board.board[self.x][self.y+t]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if(self.y-t > 0):
                if board.board[self.x][self.y-t]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
    def aqea(self,board):
        for i in range(16, 16+9, 1):
            if self.x-i > 0:
                if board.board[self.x-i][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.x+i < row:
                if board.board[self.x+i][self.y]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.y-i > 0:
                if board.board[self.x][self.y-i]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
            if self.y+i < col:
                if board.board[self.x][self.y+i]=='Q' :
                    self.health-=15
                    self.set(board)
                    if(self.health<=0):
                        board.board[self.x][self.y]=' '
                        self.health=0
class wall(building):
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='◈' # ▩

    def remove(self,x,y,board):
        board[x][y]=' '
    def attackedbyking(self, board):
        if board.board[self.x-1][self.y]=='K' :
            board.board[self.x][self.y]=' '
        if board.board[self.x+1][self.y]=='K' :
            board.board[self.x][self.y]=' '
        if board.board[self.x][self.y-1]=='K' :
            board.board[self.x][self.y]=' '
        if board.board[self.x][self.y+1]=='K' :
            board.board[self.x][self.y]=' '
    def attackedbyqueen(self,board):
        for t in range(6, 10, 1):
            if board.board[self.x-t][self.y]=='Q' :
                board.board[self.x][self.y]=' '
            if board.board[self.x+t][self.y]=='Q' :
                board.board[self.x][self.y]=' '
            if board.board[self.x][self.y-t]=='Q' :
                board.board[self.x][self.y]=' '
            if board.board[self.x][self.y+t]=='Q' :
                board.board[self.x][self.y]=' '
    def aqea(self,board):
        for i in range(16, 16+9, 1):
            if self.x-i > 0:
                if board.board[self.x-i][self.y]=='Q' :
                    board.board[self.x][self.y]=' '
            if self.x+i < row:
                if board.board[self.x+i][self.y]=='Q' :
                    board.board[self.x][self.y]=' '
            if self.y-i > 0:
                if board.board[self.x][self.y-i]=='Q' :
                    board.board[self.x][self.y]=' '
            if self.y+i < col:
                if board.board[self.x][self.y+i]=='Q' :
                    board.board[self.x][self.y]=' '
class king():
    def __init__(self) -> None:
        self.health=100
        self.damage=20
        self.speed=1
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='K'
        self.health=100
        self.damage=20
        # self.target=0
        self.speed=1
    def remove(self,board):
        board.board[self.x][self.y]=' '
        self.health=0
    
    def move(self, board, input):
        if input=='w' and board.board[self.x-1][self.y]==' ':
            board.board[self.x-1][self.y]='K'
            board.board[self.x][self.y]=' '
            self.x -=1
        elif input=='a' and board.board[self.x][self.y-1]==' ':
            board.board[self.x][self.y-1]='K'
            board.board[self.x][self.y]=' '
            self.y -=1
        elif input=='s' and board.board[self.x+1][self.y]==' ':
            board.board[self.x+1][self.y]='K'
            board.board[self.x][self.y]=' '
            self.x +=1 
        elif input=='d' and board.board[self.x][self.y+1]==' ':
            board.board[self.x][self.y+1]='K'
            board.board[self.x][self.y]=' '
            self.y +=1
    def healthdisplay(self, health):
        if(health == 100) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 90) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 80) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 70) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 60) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 50) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 40) : 
            print("Health >>  🔵 🔵 🔵 🔵 ", health)
        elif(health == 30) : 
            print("Health >>  🔵 🔵 🔵 ", health)
        elif(health == 20) : 
            print("Health >>  🔵 🔵 ", health)
        elif(health == 10) : 
            print("Health >>  🔵 ", health)
        elif(health == 0):
            print("Health >>  ", health)
    def healthupdate(self, health):
        self.health = health
    def attack(self,x,y,board):
        pass   
class queen():
    def __init__(self) -> None:
        self.health=100
        self.damage=15
        self.speed = 1
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='Q'
        self.health=100
        self.damage=15
        # self.target=0
        self.speed=1   
    def remove(self,board):
        board.board[self.x][self.y]=' '
        self.health=0
    def move(self, board, input):
        if input=='w' and board.board[self.x-1][self.y]==' ':
            board.board[self.x-1][self.y]='Q'
            board.board[self.x][self.y]=' '
            self.x -=1
        elif input=='a' and board.board[self.x][self.y-1]==' ':
            board.board[self.x][self.y-1]='Q'
            board.board[self.x][self.y]=' '
            self.y -=1
        elif input=='s' and board.board[self.x+1][self.y]==' ':
            board.board[self.x+1][self.y]='Q'
            board.board[self.x][self.y]=' '
            self.x +=1 
        elif input=='d' and board.board[self.x][self.y+1]==' ':
            board.board[self.x][self.y+1]='Q'
            board.board[self.x][self.y]=' '
            self.y +=1
    def healthdisplay(self, health):
        if(health == 100) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 90) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 80) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 70) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 60) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 50) : 
            print("Health >>  🔵 🔵 🔵 🔵 🔵 ", health)
        elif(health == 40) : 
            print("Health >>  🔵 🔵 🔵 🔵 ", health)
        elif(health == 30) : 
            print("Health >>  🔵 🔵 🔵 ", health)
        elif(health == 20) : 
            print("Health >>  🔵 🔵 ", health)
        elif(health == 10) : 
            print("Health >>  🔵 ", health)
        elif(health == 0):
            print("Health >>  ", health)
    def healthupdate(self, health):
        self.health = health
    def attack(self,x,y,board):
        pass
class barbarians(troop):
    # val = 'B'+Fore.BLACK+Back.WHITE+Style.RESET_ALL
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='B'
        self.health=100
        self.damage=18
        self.target=0
        self.speed=1
    def remove(self,x,y,board):
        board.board[x][y]=' '
    def attack(self,x,y,board):
        pass
    def dist(self, a, b,c,d):
        return math.sqrt((a-c)**2 + (b-d)**2)
        # pass
    def movetowards(self,x,y,board):
        if self.x < x:
            for i in range(x-self.x):
                if(board.board[self.x+1][self.y]==' '):
                    board.board[self.x+1][self.y]='B'
                    board.board[self.x][self.y]=' '
                    self.x +=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.x > x:
            for i in range(self.x-x):
                if(board.board[self.x-1][self.y]==' '):
                    board.board[self.x-1][self.y]='B'
                    board.board[self.x][self.y]=' '
                    self.x -=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.y < y:
            for i in range(y-self.y):
                if(board.board[self.x][self.y+1]==' '):
                    board.board[self.x][self.y+1]='B'
                    board.board[self.x][self.y]=' '
                    self.y +=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.y > y:
            for i in range(self.y-y):
                if(board.board[self.x][self.y-1]==' '):
                    board.board[self.x][self.y-1]='B'
                    board.board[self.x][self.y]=' '
                    self.y -=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
    def attackhut(self,x,y,board):
        if(board.board[x][y]=='H'):
            board.board[x][y]=Fore.GREEN+'H'+Style.RESET_ALL
            os.system('clear')
            board.show()
            sleep(0.1)
            board.board[x][y]=Fore.GREEN+'H'+Style.RESET_ALL
            os.system('clear')
            board.show()
            sleep(0.1)
            board.board[x][y]=Fore.YELLOW+'H'+Style.RESET_ALL
            os.system('clear')
            board.show()
            sleep(0.1)
            board.board[x][y]=Fore.YELLOW+'H'+Style.RESET_ALL
            os.system('clear')
            board.show()
            sleep(0.1)
            board.board[x][y]=Fore.RED+'H'+Style.RESET_ALL
            os.system('clear')
            board.show()
            sleep(0.1)
            board.board[x][y]=Fore.RED+'H'+Style.RESET_ALL
            os.system('clear')
            board.show()
            sleep(0.1)
        # pass
    
   
class archer(troop):
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='A'+Fore.BLACK+Back.WHITE+Style.RESET_ALL
        self.health=50 # half of barbarian
        self.damage=9 # half of barbarian
        self.target=0
        self.speed=2 # twice of barbarian
        # range of archer -> 3
    def remove(self,x,y,board):
        board.board[x][y]=' '
    def attack(self,x,y,board):
        pass
    def movetowards(self,x,y,board):
        if self.x < x:
            for i in range(x-self.x):
                if(board.board[self.x+1][self.y]==' '):
                    board.board[self.x+1][self.y]='A'
                    board.board[self.x][self.y]=' '
                    self.x +=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.x > x:
            for i in range(self.x-x):
                if(board.board[self.x-1][self.y]==' '):
                    board.board[self.x-1][self.y]='A'
                    board.board[self.x][self.y]=' '
                    self.x -=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.y < y:
            for i in range(y-self.y):
                if(board.board[self.x][self.y+1]==' '):
                    board.board[self.x][self.y+1]='A'
                    board.board[self.x][self.y]=' '
                    self.y +=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.y > y:
            for i in range(self.y-y):
                if(board.board[self.x][self.y-1]==' '):
                    board.board[self.x][self.y-1]='A'
                    board.board[self.x][self.y]=' '
                    self.y -=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
    def move(self,x,y,board):
        pass
class balloon(troop):
    def coor(self,x,y,board):
        self.x=x
        self.y=y
        board.board[x][y]='▚'+Fore.BLACK+Back.WHITE+Style.RESET_ALL
        self.health=100 # same of barbarian
        self.damage=36 # twice of barbarian
        self.target=0
        self.speed=2 # twice of barbarian
        # attack cannons and wizards first then huts and townhalls
        # only attacks the target goes/flysover the other things
    def remove(self,x,y,board):
        board.board[x][y]=' '
    def attack(self,x,y,board):
        pass
    def move(self,x,y,board):
        pass
    def movetowards(self,x,y,board):
        if self.x < x:
            for i in range(x-self.x):
                if(board.board[self.x+1][self.y]==' '):
                    board.board[self.x+1][self.y]='▚'
                    board.board[self.x][self.y]=' '
                    self.x +=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.x > x:
            for i in range(self.x-x):
                if(board.board[self.x-1][self.y]==' '):
                    board.board[self.x-1][self.y]='▚'
                    board.board[self.x][self.y]=' '
                    self.x -=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.y < y:
            for i in range(y-self.y):
                if(board.board[self.x][self.y+1]==' '):
                    board.board[self.x][self.y+1]='▚'
                    board.board[self.x][self.y]=' '
                    self.y +=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
        if self.y > y:
            for i in range(self.y-y):
                if(board.board[self.x][self.y-1]==' '):
                    board.board[self.x][self.y-1]='▚'
                    board.board[self.x][self.y]=' '
                    self.y -=1
                    os.system('clear')
                    board.show()
                    sleep(0.1)
                else : pass
# class spell():
#     def change(name,bar,king):
#         if name=="f":
#             bar.damage*=2
#             king.damage*=2
#         else:
#             for i in range(1,len(bar)-1):
#                 bar[i-1].health*=1.5
#                 if bar[i-1].health>=100:
#                     bar[i-1].health=100
#             king.health*=1.5
#             if king.health>=100:
#                 king.health=100
class spell():
    def change(name,king):
        if name=="f":
            king.damage*=2
            pass
        else:
            king.health*=1.5
            if king.health>=100:
                king.health=100
class spellq():
    def change(name,queen):
        if name=="f":
            queen.damage*=2
        else:
            queen.health*=1.5
            if queen.health>=100:
                queen.health=100