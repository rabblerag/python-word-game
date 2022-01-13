import tkinter as tk
#import game_gui
import final_menu
import pyglet
from functools import partial
import yaml

def lmain(bg, player):
    global bg_color, click, player_2
    player_2 = player
    bg_color = bg
    click = pyglet.media.load('sound-16.wav',streaming=False)
    #music_multiplier = config["music_multiplier"]
    #player_2.volume= 0.5 * music_multiplier
    #initializ
    root=tk.Tk()
    root.title("Leaderoard")
    root.geometry("500x400")
    leaderboard = Leaderboard(root)
    root.mainloop()



class Leaderboard:
    def __init__(self, Leaderboard):
        global click
        
        #Get the scores located on the leadeboard.txt
        with open('leaderboard.yaml') as f: scoredict = yaml.load(f, Loader = yaml.FullLoader)
        scoredict = sorted(scoredict.items(), key=lambda x: x[1], reverse=True)


        #Create the interface
        self.root=Leaderboard

        
        self.click=click
        #Creating the canvas the main frame and the scrollbar 
        self.canvas = tk.Canvas(self.root, borderwidth=0, bg=bg_color)
        self.frame = tk.Frame(self.canvas,bg=bg_color)
        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw",tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        
        #Go home button
        self.b=tk.Button(self.frame,text='Back to the Menu',font='Arial40',bg='#1d7b72',activebackground="red",relief='groove',command=self.buttonPushed)
        self.b.bind('<Enter>',partial(self.color_config, self.b, "red")) 
        self.b.bind("<Leave>", partial(self.color_config, self.b, "black"))
        self.b.pack(side="top",expand="True",fill="both")
        #Adding Labels for Player Names and there Scores
        self.f2=tk.Frame(self.frame,bg='grey')
        self.f2.pack(expand=1, fill='both', side='top')
        self.w=tk.Label(self.f2,text="PLAYER NAME",font=('Arial', 15),bg='grey')
        self.w.pack(side="left")
        self.w=tk.Label(self.f2,text="SCORE",font=('Arial', 15),bg='grey')
        self.w.pack(side="right")

        #Counters for ranking the players
        self.count=1
        self.position=()

        #Displaying the players names followed by there scores
        for key,value in scoredict:
            self.position="#"+str(self.count)
            self.f=tk.Frame(self.frame,bg=bg_color, bd=10,padx=10,highlightbackground="grey",highlightthickness=2)
            self.f.pack(expand=1, fill='both', side='top')
            self.lb=tk.Label(self.f,text=self.position,font='Arial40')
            self.lb.pack(side="left")
            self.lb=tk.Label(self.f,text=[key],font='Arial40',padx=25)
            self.lb.pack(side="left")
            self.lb=tk.Label(self.f,text=[value],font='Arial400',padx=25)
            self.lb.pack(side="right")
            self.count=self.count+1

    #taken from final menu
    def color_config(self,widget, color, event):
        '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
        widget.config(foreground=color)
        
    def buttonPushed(self):
        self.click.play()
        
        self.root.destroy()#Later change to return to the main game
        final_menu.main(player_2)

            
    def onFrameConfigure(self, event):
            
        #Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
