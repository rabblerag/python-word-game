import final_menu, yaml, pyglet, os, tkinter as tk
from functools import partial

#get programpath 
programpath = os.path.realpath(__file__) + "\\..\\..\\assets\\"

def lmain(bg, player, sfx):

    global bg_color, click, sfx_multiplier, player_2

    bg_color = bg
    player_2 = player
    sfx_multiplier = sfx
    click = pyglet.media.load(programpath + 'sound-16.wav',streaming=False)

    #initialize graphics
    root=tk.Tk()
    root.title("Leaderoard")
    root.geometry("500x400")
    Leaderboard(root)
    root.mainloop()

    #go to main menu once mainloop is over, only happens when user chooses to return to main menu
    final_menu.main(player_2)

class Leaderboard:

    global click

    def __init__(self, leaderboard):
        
        #Get the scores located on the leadeboard.txt
        try:
            with open(programpath + 'leaderboard.yaml') as f: scoredict = yaml.load(f, Loader = yaml.FullLoader)
            scoredict = sorted(scoredict.items(), key=lambda x: x[1], reverse=True)
        except Exception: scoredict = {}



        #Create the interface
        self.root = leaderboard

        #Creating the canvas the main frame and the scrollbar 
        self.canvas = tk.Canvas(self.root, borderwidth=0, bg=bg_color)
        self.frame = tk.Frame(self.canvas,bg=bg_color)
        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw",tags="self.frame")
        self.frame.bind("<Configure>", self.on_frame_configure)
        
        #menu button
        self.b=tk.Button(self.frame,text='Return to main menu',font='Arial40',bg='#1d7b72',activebackground="red",relief='groove',command=self.button_pushed)
        self.b.bind('<Enter>',partial(self.color_config, self.b, "red")) 
        self.b.bind("<Leave>", partial(self.color_config, self.b, "black"))
        self.b.pack(side="top",expand="True",fill="both")


        #Adding Labels for Player Names and their scores
        self.f2=tk.Frame(self.frame,bg='grey')
        self.f2.pack(expand=1, fill='both', side='top')
        self.w=tk.Label(self.f2,text="PLAYER NAME",font=('Arial', 15),bg='grey')
        self.w.pack(side="left")
        self.w=tk.Label(self.f2,text="SCORE",font=('Arial', 15),bg='grey')
        self.w.pack(side="right")

        #Counters for ranking the players
        self.count=1
        self.position=()

        #Displaying the players names followed by their scores
        for key,value in scoredict:
            self.position="#"+str(self.count)
            self.f=tk.Frame(self.frame,bg=bg_color, bd=10,padx=10,highlightbackground="grey",highlightthickness=2)
            self.f.pack(expand=1, fill='both', side='top')
            self.lb=tk.Label(self.f,text=self.position,font='Arial40')
            self.lb.pack(side="left")
            self.lb=tk.Label(self.f,text=key,font='Arial40',padx=25)
            self.lb.pack(side="left")
            self.lb=tk.Label(self.f,text=value,font='Arial400',padx=25)
            self.lb.pack(side="right")
            self.count=self.count+1

    #changes the color of buttons when hovered over
    def color_config(self,widget, color, event): widget.config(foreground=color)
        
    def button_pushed(self):
        click.play().volume = 1.5 * sfx_multiplier
        self.root.destroy()#Later change to return to the main game
        final_menu.main(player_2)

            
    def on_frame_configure(self, event):
            
        #Reset the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
