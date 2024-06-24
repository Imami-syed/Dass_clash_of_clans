    def attackfrmcannon(self,board):
        for i in range(5):
        	for j in range(5):
        		x=[self.x-i,self.x+i]
        		y=[self.x-j,self.x+j]
                for p in x:
                    for q in y:
                        if(p>=0 and p<54 and q>=0 and q<140):
                            if(board.board[p][q]=='C'):
                                self.health=self.health-20