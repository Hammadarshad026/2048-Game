from tkinter import *
from tkinter import messagebox
import random
class Board:
    #background color of boxex
    bg_color={
        '2':'gray39',
        '4':'magenta2',
        '8':'OrangeRed2',
        '16':'IndianRed1',
        '32':'DarkOrange1',
        '64':'green4',
        '128':'DarkOrchid4',
        '256':'DarkOliveGreen2',
        '512':'Navy',
        '1024':'blue3',
        '2048':'red',
    }
    #colors of text on boxes
    color={
        '2':'#f9f6f2',
        '4':'#f9f6f2',
        '8':'#f9f6f2',
        '16':'#f9f6f2',
        '32':'#f9f6f2',
        '64':'#f9f6f2',
        '128':'#f9f6f2',
        '256':'#f9f6f2',
        '512':'#f9f6f2',
        '1024':'#f9f6f2',
        '2048':'#f9f6f2',     
    }
     

    def __init__(self):
        self.window=Tk()
        self.window.title("2048_Game         |Hammad Arshad|")
        self.gameArea=Frame(self.window,bg='yellow1')
        self.board=[]
        self.gridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        #loop to print board cellf
        for i in range (4):
            rows=[]
            for j in range (4):
                l=Label(self.gameArea, text='',bg='purple1', font=('arial',22, 'bold'), width=10,height=4)
                l.grid(row=i,column=j,padx=7,pady=7)
                rows.append(l)
            self.board.append(rows)
        self.gameArea.grid()


    #this fun perform revese values in rows
    #and controls the left and right movement
    def reverse(self):
        for ind in range (4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[i][ind]=self.gridCell[i][ind],self.gridCell[ind][i]
                i+=1
                j-=1


    #this fun cover the up and down movement
    #and cover the up and down merging
    def transpose(self):
        self.gridCell=[list(t) for t in zip(*self.gridCell)]

    #this fun align th e non zero at right corner
    def compressGrid(self):
        self.compress=False
        temp=[[0]*4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.gridCell=temp
    


    #if the two values are same then this fun merg these valuse and make the one 
    def mergeGrid(self):
        self.merge=False
        for i in range(4):
            for j in range(4-1):
                if self.gridCell[i][j]==self.gridCell[i][j+1] and self.gridCell[i][j] !=0:
                    self.gridCell[i][j]*=2
                    self.gridCell[i][j+1]=0
                    self.score+=self.gridCell[i][j]
                    self.merge=True


    #insert the 2 randomly where the value is zero
    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] ==0:
                    cells.append((i,j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]=2

    

    #this one check the two values are merge able or not 
    def can_merge(self):
        #checking in row wise
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j]==self.gridCell[i][j+1]:
                    return True
        #checking in column wise
        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j]==self.gridCell[i][j]:
                    return True
        return False
    
    #Paint the gridcell according to the values in it
    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='DodgerBlue2')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),bg=self.bg_color.get(str(self.gridCell[i][j])),fg=self.color.get(str(self.gridCell[i][j])))



                          
         