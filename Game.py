from board import Board
from tkinter import messagebox
from tkinter import *


class Game:
    def __init__(self,gamepannel):
        self.gamepannel=gamepannel
        self.end=False
        self.won=False


    def start(self):
        #genrate 2 on random location
        self.gamepannel.random_cell()
        self.gamepannel.random_cell()
        self.gamepannel.paintGrid()
        self.gamepannel.window.bind('<Key>',self.link_key)
        self.gamepannel.window.mainloop()

    def link_key(self,event):
        if self.end or self.won:
            return
        self.gamepannel.compress=False
        self.gamepannel.merge=False
        self.gamepannel.moved=False

        presed_key=event.keysym
        
        #Up movement
        if presed_key=='Up':
            self.gamepannel.transpose()
            self.gamepannel.compressGrid()
            self.gamepannel.mergeGrid()
            self.gamepannel.moved=self.gamepannel.compress or self.gamepannel.merge
            self.gamepannel.compressGrid()
            self.gamepannel.transpose()

        #down movement
        elif presed_key=='Down':
            self.gamepannel.transpose()
            self.gamepannel.reverse()
            self.gamepannel.mergeGrid()
            self.gamepannel.moved=self.gamepannel.compress or self.gamepannel.merge
            self.gamepannel.compressGrid()
            self.gamepannel.reverse()
            self.gamepannel.transpose()
        
        #left movement
        elif presed_key=='Left':
            self.gamepannel.compressGrid()
            # self.gamepannel.left_compressGrid()
            self.gamepannel.mergeGrid()
            self.gamepannel.moved=self.gamepannel.compress or self.gamepannel.merge
            self.gamepannel.compressGrid()
            # self.gamepannel.left_compressGrid()

        #Right movement
        elif presed_key=='Right':
            self.gamepannel.reverse()
            self.gamepannel.compressGrid()
            self.gamepannel.mergeGrid()
            self.gamepannel.moved=self.gamepannel.compressGrid or self.gamepannel.mergeGrid
            self.gamepannel.compressGrid()
            self.gamepannel.reverse()
        
        else:
            pass


        self.gamepannel.paintGrid()
        print(self.gamepannel.score)


        flag=0
        for i in range (4):
            for j in range (4):
                if(self.gamepannel.gridCell[i][j]==2048):
                    flag=1
                    break
        if (flag==1):
            self.won=True
            messagebox.showinfo('2048', message='You Wonn!!')
            print('won')
            return
        

        #if 2048 is not create
        for i in range(4):
            for j in range(4):
                if self.gamepannel.gridCell[i][j]==0:
                    flag=1
                    break
        if not (flag or self.gamepannel.can_merge()):
            self.end=True
            messagebox.showinfo('2048', 'Game Over!!!')
            print('Over')
        if self.gamepannel.moved:
            self.gamepannel.random_cell()

        self.gamepannel.paintGrid()



        
        

