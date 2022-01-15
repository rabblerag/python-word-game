#necessary modules
import yaml, pyglet, game_gui, leaderboard, tkinter as tk, sys
from tkinter import colorchooser
from functools import partial

#for reinitialization
def main(player = None):
    global bg_color, music_multiplier, sfx_multiplier, muted, click, player_2, config
    
    #initialize settings by reading settings file, create one if it doesn"t exist
    try:
        with open("assets\\" + "config.yaml", "r") as f: config = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        with open("assets\\" + "config.yaml", "w") as f: 
            config = {"bg_color": "#1125ae", "music_multiplier": 0.50, "sfx_multiplier": 0.50, "muted": False}
            yaml.dump(config, f)
    bg_color = config["bg_color"]
    music_multiplier = config["music_multiplier"]
    sfx_multiplier = config["sfx_multiplier"]
    muted = config["muted"]
    
    #configure music players
    click = pyglet.media.load("assets\\" +"sound-16.wav",streaming=False)
    music= pyglet.media.load("assets\\" +"jazzy-abstract-beat-11254.mp3", streaming=False) #StaticSource object
        
    #initializes the background music player if it doesn"t already exist
    if player: player_2 = player
    else:

        pyglet.options["audio"] = ("openal", "pulse", "directsound", "silent")
        player_2 = pyglet.media.Player()
        player_2.queue(music)
        player_2.volume = 0.5 * music_multiplier

        if not muted: player_2.play()

    #initialize graphics
    root=tk.Tk()
    root.title("Python Word Game")
    root.geometry("1000x600+140+30")
    Menu(root)
    root.mainloop()

#class for the menu GUI, separate from settings
class Menu():

    global bg_color, music_multiplier, sfx_multiplier, click, player_2

    
    def __init__(self,root):

        self.root=root                   #cannot be connected with other modules without this
        #Frame 1
        self.f1=tk.Frame(root,width=1000)
        self.f1.pack(side="top")
        self.label1=tk.Label(self.f1,text="Python Word Game", font="Vivaldi 40",bg=bg_color,width=1000)

        #if bg color is black, turn letters white
        if config["bg_color"]=="#000000":self.label1.configure(foreground="white")
        self.label1.pack(expand=1,fill="x")
        self.label2=tk.Label(self.f1,text="MENU", font="Stencil 40",bg=bg_color,width=1000)
        if config["bg_color"]=="#000000":self.label2.configure(foreground="white")
        self.label2.pack()
        self.f4=tk.Frame(root,width=500,bg=bg_color)
        self.f4.pack(side="top",expand=1,fill="both")
        self.f2=tk.Frame(root,width=500,bg=bg_color)
        self.f2.pack(side="top",expand=1,fill="both")

        #PLAY Button
        self.unmute_button=tk.Button(self.f2,text="PLAY",font="Arial 16",relief="groove",bg="#1d7b72",command=self.play_game)
        self.unmute_button.pack(side="top", expand = 1)
        self.unmute_button.bind("<Enter>",partial(self.color_config, self.unmute_button, "red")) 
        self.unmute_button.bind("<Leave>", partial(self.color_config, self.unmute_button, "black"))
        #partial "freezes" a function at a specific instant, therefore we don"t have to create different function for each color 
        
        #LEADERBOARD Button
        self.leader_button=tk.Button(self.f2,text="LEADERBOARD",font="Arial 16",relief="groove",bg="#1d7b72",command=self.leaderboard)
        self.leader_button.pack(side="top", expand = 1)
        self.leader_button.bind("<Enter>",partial(self.color_config, self.leader_button, "red"))
        self.leader_button.bind("<Leave>", partial(self.color_config, self.leader_button, "black"))
        
        #SETTINGS Button
        self.settings_button=tk.Button(self.f2,text="SETTINGS",font="Arial 16",relief="groove",bg="#1d7b72",command=self.settings)
        self.settings_button.pack(side="top", expand = 1)
        self.settings_button.bind("<Enter>",partial(self.color_config, self.settings_button, "red")) #"#942706" complementary color
        self.settings_button.bind("<Leave>", partial(self.color_config, self.settings_button, "black"))
        
        #HOW-TO-PLAY Button
        self.settings_button=tk.Button(self.f2,text="HOW-TO-PLAY",font="Arial 16",relief="groove",bg="#1d7b72",command=self.howtoplay)
        self.settings_button.pack(side="top", expand = 1)
        self.settings_button.bind("<Enter>",partial(self.color_config, self.settings_button, "red")) #"#942706" complementary color
        self.settings_button.bind("<Leave>", partial(self.color_config, self.settings_button, "black"))

        #CREDITS
        self.credits_button=tk.Button(self.f2,text="CREDITS",font="Arial 16",relief="groove",bg="#1d7b72",command=self.credits)
        self.credits_button.pack(side="top", expand = 1)
        self.credits_button.bind("<Enter>",partial(self.color_config, self.credits_button, "red")) #"#942706" complementary color
        self.credits_button.bind("<Leave>", partial(self.color_config, self.credits_button, "black"))        
        
        #QUIT Button
        self.quit_button=tk.Button(self.f2,text="EXIT",font="Arial 16",relief="groove",bg="#f53b57",command=self.game_exit)
        self.quit_button.pack(side="top", expand = 1)
        self.quit_button.bind("<Enter>",partial(self.color_config, self.quit_button, "blue")) #"#f53b57" complementary color
        self.quit_button.bind("<Leave>", partial(self.color_config, self.quit_button, "black"))

    #start the game
    def play_game(self):

        click.play().volume = 1.5 * sfx_multiplier
        player_2.pause()  #stop the menu music
        self.root.destroy()    #close the menu window
        game_gui.game(bg_color, sfx_multiplier, player_2)        #from game_gui module function game ->initializes the game

    #COLOR CHANGE WHEN MOUSE HOVERS OVER BUTTONS  
    def color_config(self,widget, color, event): widget.config(foreground=color)
        
    #HOW-TO-PLAY text menu
    def howtoplay(self):
        
        click.play().volume = 1.5 * sfx_multiplier
        self.howtoplay=tk.Toplevel(self.root,bg=bg_color)
        self.howtoplay.title("HOW TO PLAY")
        self.howtoplay.geometry("810x500+100+100")
        self.foreground="black"
        if config["bg_color"]=="#000000":self.foreground="white"
        else:self.foreground="black"

        
        self.f5=tk.Frame(self.howtoplay,bg=bg_color)
        self.f5.pack(fill="both",expand=1)
        self.text=tk.Text(self.f5, height = 100, width = 100,bg=bg_color)
        #self.text.pack(fill="both",expand=1)
        self.text.tag_configure("big_text", font=("Verdana",20,"bold"))
        self.text.insert("end","\nHOW-TO-PLAY\n","big_text")
        
        message="""
#Welcome to our “INSERT NAME HERE”. In this game you have to find as many words as you can with the #given letters in 60 seconds.
#Welcome to our Python Word Game. In this game you have to find as many words as you can with the #given letters in 60 seconds.
#
#You can change the given letters as many times as you want but remember that when you find multiple#words with the same letters you get bonus points.
#
#Each letter can be used multiple times.
        """
        self.text.insert("end",message)
        self.text.config(state="disable")
        self.text.pack(side="left")


    #show local leaderboard
    def leaderboard(self):

        click.play().volume = 1.5 * sfx_multiplier
        self.root.destroy()
        leaderboard.lmain(bg_color, player_2, sfx_multiplier)
        
    #defining the color of the letters in the credit window depending on the background
    def credits(self):

        click.play().volume = 1.5 * sfx_multiplier
        self.credit_win=tk.Toplevel(self.root,bg=bg_color)
        self.credit_win.title("Credits")
        self.credit_win.geometry("400x400+100+100")
        self.foreground="black"
        if config["bg_color"]=="#000000":self.foreground="white"
        else:self.foreground="black"

        #frame 1
        self.f1=tk.Frame(self.credit_win,bg=bg_color)
        self.f1.pack(fill="both",expand=1)
        self.l1=tk.Label(self.f1,text="Sound effects taken from: ",font="Arial 16",bg=bg_color,fg=self.foreground)
        self.l1.pack(fill="both",expand=1)
        self.l1.bind("<Enter>",partial(self.color_config, self.l1, "red"))
        self.l1.bind("<Leave>", partial(self.color_config, self.l1, self.foreground))   #defaultcolor=self.foreground

        #frame 2
        self.f2=tk.Frame(self.credit_win,bg=bg_color)
        self.f2.pack(fill="both",expand=1)
        self.l2=tk.Label(self.f2,text="mixkit.co",font="Arial 16",bg=bg_color,fg=self.foreground)
        self.l2.pack(fill="both",expand=1)
        self.l2.bind("<Enter>",partial(self.color_config, self.l2, "red"))
        self.l2.bind("<Leave>", partial(self.color_config, self.l2, self.foreground))

        #frame 3
        self.f3=tk.Frame(self.credit_win,bg=bg_color)
        self.f3.pack(fill="both",expand=1)
        self.l3=tk.Label(self.f3,text="creatorassets.com",font="Arial 16",bg=bg_color,fg=self.foreground)
        self.l3.pack(fill="both",expand=1)
        self.l3.bind("<Enter>",partial(self.color_config, self.l3, "red"))
        self.l3.bind("<Leave>", partial(self.color_config, self.l3, self.foreground))

        #frame 4
        self.f4=tk.Frame(self.credit_win,bg=bg_color)
        self.f4.pack(fill="both",expand=1)
        self.l4=tk.Label(self.f4,text="pixabay.com",font="Arial 16",bg=bg_color,fg=self.foreground)
        self.l4.pack(fill="both",expand=1)
        self.l4.bind("<Enter>",partial(self.color_config, self.l4, "red"))
        self.l4.bind("<Leave>", partial(self.color_config, self.l4, self.foreground))

        #exit_button
        self.exit =tk.Button(self.credit_win, bg = "#1d7b72", text = "Return to main menu", command = self.credit_win.destroy)
        self.exit.bind("<Enter>",partial(self.color_config, self.exit, "red"))
        self.exit.bind("<Leave>", partial(self.color_config, self.exit, self.foreground))
        self.exit.pack()



    #exit the game
    def game_exit(self):
        click.play().volume = 1.5 * sfx_multiplier
        self.root.destroy()
        player_2.delete()
        sys.exit()
        
        
    #go to settings GUI
    def settings(self):
        click.play().volume = 1.5 * sfx_multiplier
        #SETTINGS WINDOW
        self.settings_window=tk.Toplevel(self.root,bg=bg_color)  #παράθυρο ρυθμίσεων ήχου και μουσικής
        self.settings_window.geometry("300x166+440+217")
        self.settings_window.title("Settings Window")
        self.settings = Settings(self.settings_window,self) #οπως 5ο εργαστηριο #class SETTINGS
        #self.settings_window.geometry("100x100")
        #Settings.adjust_sfx(self.a)
        #find a way to simply change the layout instead of creating a new window
        
    #change the credits letter color  
    def letter_color(self):
        self.label1.configure(foreground="white")
        self.label2.configure(foreground="white")

#class for settings GUI, separate from menu
#stores settings in a .yaml file
class Settings():

    global bg_color, music_multiplier, sfx_multiplier, muted, click, player_2, config

    def __init__(self,window,menu):

        self.window=window
        self.menu=menu
        self.root=self.menu.root #αρχικο παραθυρο απο την κλάση μενού
        
        #MUSIC BUTTON
        self.music_button=tk.Button(self.window,text="Music settings",relief="groove",command=self.adjust_music ,bg="#1d7b72")
        self.music_button.bind("<Enter>",partial(self.color_config,self.music_button,"red"))
        self.music_button.bind("<Leave>", partial(self.color_config, self.music_button, "black"))
        self.music_button.pack(fill = "x", expand = 1)

        #SOUND EFFFECT BUTTONM
        self.sfx_button=tk.Button(self.window,text="Sound effects settings",relief="groove",command=self.adjust_sfx ,bg="#1d7b72")
        self.sfx_button.bind("<Enter>",partial(self.color_config,self.sfx_button,"red"))
        self.sfx_button.bind("<Leave>", partial(self.color_config, self.sfx_button, "black"))
        self.sfx_button.pack(fill = "x", expand = 1)

        #BACKROUND COLOR BUTTON
        self.color_button=tk.Button(self.window,text="Color settings",relief="groove",command = self.color_choice ,bg="#1d7b72")
        self.color_button.bind("<Enter>",partial(self.color_config,self.color_button,"red"))
        self.color_button.bind("<Leave>", partial(self.color_config, self.color_button, "black"))
        self.color_button.pack(fill = "x", expand = 1)

        #EXIT BUTTON
        self.exit_button=tk.Button(self.window,text="Close",relief="groove", command = partial(self.x, self.window) ,bg="#1d7b72")
        self.exit_button.bind("<Enter>",partial(self.color_config,self.exit_button,"red"))
        self.exit_button.bind("<Leave>", partial(self.color_config, self.exit_button, "black"))
        self.exit_button.pack(fill = "x", expand = 1)

    #play click sound when exiting settings window
    def x(self, w):
        click.play().volume = 1.5 * sfx_multiplier
        w.destroy()

    #COLOR CHANGE WHEN MOUSE HOVERS OVER BUTTONS  
    def color_config(self,widget, color, event): widget.config(foreground=color)

    
##### MUSIC VOLUME FUNCTIONS  ######
        
    def exit_music(self):

        click.play().volume = 1.5 * sfx_multiplier

        #Used by ok button to change the volume and store changes
        global muted, music_multiplier

        music_multiplier = self.w.get()/100
        player_2.volume = 0.5 * music_multiplier
        config["music_multiplier"] = music_multiplier
        with open("assets\\" + "config.yaml", "w") as f: yaml.dump(config, f)
        self.window.destroy()


    def mute_music(self):

        click.play().volume = 1.5 * sfx_multiplier

        #mutes the music player and stores the choice
        global muted, player_2
        muted = True
        config["muted"] = True
        player_2.pause()
        with open("assets\\" + "config.yaml", "w") as f: yaml.dump(config, f)

    def unmute_music(self):

        click.play().volume = 1.5 * sfx_multiplier

        #unmutes the music player and stores the choice
        global muted, player_2
        muted = False
        config["muted"] = False
        player_2.play()
        with open("assets\\" + "config.yaml", "w") as f: yaml.dump(config, f)
        
    #MUSIC WINDOW    
    def adjust_music(self):

        # creates the music toplevel, slider, buttons
        click.play().volume = 1.5 * sfx_multiplier
        self.window=tk.Toplevel(self.root,bg=bg_color,height=400,width=400)
        self.window.geometry("400x200")
        self.window.title("Music Window")

        #mute button
        self.mute_button=tk.Button(self.window,text="Mute",relief="groove",command=self.mute_music ,bg="#1d7b72")
        self.mute_button.bind("<Enter>",partial(self.color_config,self.mute_button,"red"))
        self.mute_button.bind("<Leave>", partial(self.color_config, self.mute_button, "black"))
        self.mute_button.pack(expand = 1)

        #unmute button
        self.unmute_button=tk.Button(self.window,text="Unmute",relief="groove",command=self.unmute_music ,bg="#1d7b72")
        self.unmute_button.bind("<Enter>",partial(self.color_config,self.unmute_button,"red"))
        self.unmute_button.bind("<Leave>", partial(self.color_config, self.unmute_button, "black"))
        self.unmute_button.pack(expand = 1)

        #slider
        self.w = tk.Scale(self.window, from_=0.0, to=100, orient="horizontal",bg=bg_color)
        self.w.set(music_multiplier*100)
        self.w.pack(expand = 1, fill = "x")

        #ok button    
        self.close_button=tk.Button(self.window,text="Close",relief="groove",command=self.exit_music ,bg="#1d7b72")
        self.close_button.bind("<Enter>",partial(self.color_config,self.close_button,"red"))
        self.close_button.bind("<Leave>", partial(self.color_config, self.close_button, "black"))
        self.close_button.pack(expand = 1)

##### SOUND EFFECTS VOLUME FUNCTIONS  ######
    def exit_sfx(self):

        #Used by ok button to change sfx volume and store changes
        global sfx_multiplier

        sfx_multiplier = self.w.get()/100
        click.play().volume = 1.5 * sfx_multiplier
        config["sfx_multiplier"] = sfx_multiplier
        with open("assets\\" + "config.yaml", "w") as f: yaml.dump(config, f)
        self.window.destroy()

    def mute_sfx(self): self.w.set(0)
        
    #SFX WINDOW    
    def adjust_sfx(self):

        # creates the music toplevel, slider, buttons
        click.play().volume = 1.5 * sfx_multiplier
        self.window=tk.Toplevel(self.root,bg=bg_color,height=400,width=400)
        self.window.geometry("400x200")
        self.window.title("SFX Window")

        #mute button
        self.mute_button=tk.Button(self.window,text="Mute",relief="groove",command=self.mute_sfx ,bg="#1d7b72")
        self.mute_button.bind("<Enter>",partial(self.color_config,self.mute_button,"red"))
        self.mute_button.bind("<Leave>", partial(self.color_config, self.mute_button, "black"))
        self.mute_button.pack(expand = 1)

        #slider
        self.w = tk.Scale(self.window, from_=0.0, to=100, orient="horizontal",bg=bg_color)
        self.w.set(sfx_multiplier*100)
        self.w.pack(expand = 1, fill = "x")

        #ok button    
        self.close_button=tk.Button(self.window,text="Close",relief="groove",command=self.exit_sfx ,bg="#1d7b72")
        self.close_button.bind("<Enter>",partial(self.color_config,self.close_button,"red"))
        self.close_button.bind("<Leave>", partial(self.color_config, self.close_button, "black"))
        self.close_button.pack(expand = 1)

#BACKROUND COLOR BUTTON COMMAND
    def color_choice(self):

        click.play().volume = 1.5 * sfx_multiplier

        #store user settings and reinitialize
        config["bg_color"] = colorchooser.askcolor(title = "Select a color", color = bg_color)[1]
        with open("assets\\" + "config.yaml", "w") as f: yaml.dump(config, f)
        self.root.destroy()
        main(player_2)

if __name__=="__main__": main()
