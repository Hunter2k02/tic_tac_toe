import tkinter as tk 
from tkinter import messagebox  
from random import randint

class Application():
    def __init__(self):
        
        self.flag = 1 
        self.create_menu()   
        
        
        
    def create_menu(self):
        #Creating menu window
        
        self.root = tk.Tk()
        self.root.title("TTT")
        self.root.resizable(width=False, height=False)
        self.root.geometry("510x325+700+200")
        #Menu Buttons 
        
        self.OnePlayerButt = tk.Button(self.root, text="Player vs Computer", font="sans 12 bold", width=50, height=5, command=self.OnePlayer).grid(row=0,column=0)
        self.TwoPlayersButt = tk.Button(self.root, text="Player vs Player", font="sans 12 bold",  width=50, height=5, command=self.TwoPlayers).grid(row=1,column=0)
        self.ExitGame = tk.Button(self.root, text="Exit", width=50, height=5, font="sans 12 bold", command=self.ExitGame).grid(row=2,column=0)
        self.root.mainloop()
        
    def CreateBoard(self):
        #Creating app window
        
        self.app = tk.Tk()
        self.app.resizable(width=False, height=False)
        self.app.title("TTT")
        self.app.geometry("700x710+600+150")
        self.label = tk.Label(text="X's turn",font="sans 20 bold" )
        self.label.grid(row=0, column=1)
        
        #Creating grid
        self.buttons = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
                        ]
        self.rules = [
           [2,2,2],
           [2,2,2],
           [2,2,2],
                        ]
        
        self.buttons[0][0] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(0,0))
        self.buttons[0][1] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(0,1))
        self.buttons[0][2] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(0,2))
        self.buttons[1][0] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(1,0))
        self.buttons[1][1] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(1,1))
        self.buttons[1][2] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(1,2))
        self.buttons[2][0] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(2,0))
        self.buttons[2][1] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(2,1))
        self.buttons[2][2] = tk.Button(self.app, text="", font='sans 12 bold', height=10, width=20, command=lambda: self.Rules(2,2))
        
        for i in range(1,4):
            for j in range(3):
                self.buttons[i-1][j].grid(row=i, column=j,pady=7, padx=7)
                
        self.app.mainloop()   
        
    def Rules(self,row, column):
        #Rules of game
        if self.flag:
            self.rules[row][column] = 1
            self.label.config(text="O's turn")
            self.buttons[row][column].config(state= tk.DISABLED, text="X", disabledforeground="red", font='sans 12 bold')
            
            #Victory rules
                #Horizontall lines
            if (((self.rules[0][0]==1 and self.rules[0][1]==1 and self.rules[0][2]==1) or
                 (self.rules[1][0]==1 and self.rules[1][1]==1 and self.rules[1][2]==1) or
                 (self.rules[2][0]==1 and self.rules[2][1]==1 and self.rules[2][2]==1)) or
                
                #Vertical lines
                ((self.rules[0][0]==1 and self.rules[1][0]==1 and self.rules[2][0]==1) or
                 (self.rules[0][1]==1 and self.rules[1][1]==1 and self.rules[2][1]==1) or
                 (self.rules[0][2]==1 and self.rules[1][2]==1 and self.rules[2][2]==1)) or
                #Cross lines
                ((self.rules[0][0]==1 and self.rules[1][1]==1 and self.rules[2][2]==1) or
                 (self.rules[0][2]==1 and self.rules[1][1]==1 and self.rules[2][0]==1))):
                self.PlayerOneWon()
                exit()
                #Tie rules
            if 2 in self.rules[0] or 2 in self.rules[1] or 2 in self.rules[2]:
                pass
            else:
                self.Tie()
            
            if self.HowMany==2:   
                self.flag=0
            else:
                if 2 in self.rules[0] or 2 in self.rules[1] or 2 in self.rules[2]:
                    pass
                else:
                    self.Tie()
                while(self.rules[row][column]!=2):
                    row = randint(0,2)
                    column=randint(0,2)  
                
                self.rules[row][column] = 0
                self.buttons[row][column].config(state= tk.DISABLED, text="O", disabledforeground="Blue", font='sans 12 bold')
                if (((self.rules[0][0]==0 and self.rules[0][1]==0 and self.rules[0][2]==0) or
                (self.rules[1][0]==0 and self.rules[1][1]==0 and self.rules[1][2]==0) or
                (self.rules[2][0]==0 and self.rules[2][1]==0 and self.rules[2][2]==0)) or
                
                
                ((self.rules[0][0]==0 and self.rules[1][0]==0 and self.rules[2][0]==0) or
                (self.rules[0][1]==0 and self.rules[1][1]==0 and self.rules[2][1]==0) or
                (self.rules[0][2]==0 and self.rules[1][2]==0 and self.rules[2][2]==0)) or
                
                ((self.rules[0][0]==0 and self.rules[1][1]==0 and self.rules[2][2]==0) or
                (self.rules[0][2]==0 and self.rules[1][1]==0 and self.rules[2][0]==0))):
                    self.PlayerTwoWon()
                    exit()
            
           
                  
        else:
            
            self.rules[row][column] = 0  
            self.label.config(text="X's turn")
            self.buttons[row][column].config(state= tk.DISABLED, text="O", disabledforeground="blue", font='sans 12 bold')
            self.flag=1
            #Victory rules
                #Horizontall lines
            if (((self.rules[0][0]==0 and self.rules[0][1]==0 and self.rules[0][2]==0) or
                (self.rules[1][0]==0 and self.rules[1][1]==0 and self.rules[1][2]==0) or
                (self.rules[2][0]==0 and self.rules[2][1]==0 and self.rules[2][2]==0)) or
                
                #Vertical lines
                ((self.rules[0][0]==0 and self.rules[1][0]==0 and self.rules[2][0]==0) or
                (self.rules[0][1]==0 and self.rules[1][1]==0 and self.rules[2][1]==0) or
                (self.rules[0][2]==0 and self.rules[1][2]==0 and self.rules[2][2]==0)) or
                #Cross lines
                ((self.rules[0][0]==0 and self.rules[1][1]==0 and self.rules[2][2]==0) or
                (self.rules[0][2]==0 and self.rules[1][1]==0 and self.rules[2][0]==0))):
                self.PlayerTwoWon()
                exit()
                #Tie rules
            if 2 in self.rules[0] or 2 in self.rules[1] or 2 in self.rules[2]:
                pass
            else:
                self.Tie()
            
    def PlayerOneWon(self):
        messagebox.showinfo("Result of match ","Player One Won!") 
        self.app.destroy()
        
        
    def PlayerTwoWon(self):
        messagebox.showinfo("Result of match ","Player Two Won!") 
        self.app.destroy()
    
    def Tie(self):
        messagebox.showinfo("Result of match ","Tie!") 
        self.app.destroy()          
         
    def ExitGame(self):
        self.root.destroy()
        
    def OnePlayer(self):
        self.HowMany = 1
        self.root.destroy()
        self.CreateBoard()
        
    def TwoPlayers(self):
        self.HowMany = 2
        self.root.destroy()
        self.CreateBoard()
        
    
        
        
    
        
Application()

    
    
   