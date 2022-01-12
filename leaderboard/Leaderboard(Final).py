import tkinter as tk

class Leaderboard:
    def __init__(self, Leaderboard):
        
        #Get the scores located on the leadeboard.txt
        with open('leaderboard.txt') as f:
            file_contents=f.read()
            flist = file_contents.split()
            scoredictunsorted = {flist[i]: flist[i + 1] for i in range(0, len(flist), 2)}
        #Sort the dictionary by highest to lowest score   
        for value in scoredictunsorted:
            scoredictunsorted[value]=int(scoredictunsorted[value])
        scoredict = sorted(scoredictunsorted.items(), key=lambda x: x[1], reverse=True)


        #Create the interface
        self.root=Leaderboard
        #Creating the canvas the main frame and the scrollbar 
        self.canvas = tk.Canvas(self.root, borderwidth=0)
        self.frame = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw",tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        
        #Go home button
        self.b=tk.Button(self.frame,text='Back to the Game',font='Arial40',bg='red',activebackground="yellow",command=self.buttonPushed)
        self.b.pack(side="top",expand="True",fill="both")
        #Adding Labels for Player Names and there Scores
        self.f2=tk.Frame(self.frame,bg='grey')
        self.f2.pack(expand=1, fill='both', side='top')
        self.w=tk.Label(self.f2,text="PLAYER NAME",font=('Arial', 20),bg='grey')
        self.w.pack(side="left")
        self.w=tk.Label(self.f2,text="SCORE",font=('Arial', 20),bg='grey')
        self.w.pack(side="right")

        #Counters for ranking the players
        self.count=1
        self.position=()

        #Displaying the players names followed by there scores
        for key,value in scoredict:
            self.position="#"+str(self.count)
            self.f=tk.Frame(self.frame,bg='green', bd=10,padx=10,highlightbackground="grey",highlightthickness=2)
            self.f.pack(expand=1, fill='both', side='top')
            self.lb=tk.Label(self.f,text=self.position,font='Arial40')
            self.lb.pack(side="left")
            self.lb=tk.Label(self.f,text=[key],font='Arial40',padx=25)
            self.lb.pack(side="left")
            self.lb=tk.Label(self.f,text=[value],font='Arial400',padx=25)
            self.lb.pack(side="right")
            self.count=self.count+1


            
    def buttonPushed(self):
        
        self.root.destroy()#Later change to return to the main game!!!!!

            
    def onFrameConfigure(self, event):
            
        #Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        



root=tk.Tk()
root.title("Leaderoard")
root.geometry("500x400")
leaderboard = Leaderboard(root)
root.mainloop()
