#needed for settings class
from pyglet.media import player
import yaml
import tkinter as tk
from tkinter import ttk
from functools import partial
import pyglet
import game_gui
from tkinter import colorchooser
import leaderboard



#for reinitialization
def main(player=None):
    global bg_color, music_multiplier, muted, click,player_2, config
    
    #initialize settings
    with open("config.yaml", "r") as f: config = yaml.load(f, Loader=yaml.FullLoader)
    bg_color = config["bg_color"]
    music_multiplier = config["music_multiplier"]
    muted = config["muted"]
    try: player_2.delete()
    except Exception: pass
    
    #click = pyglet.media.load('sound-16.wav',streaming=False)
    #player_2 = pyglet.media.Player()
    #music= pyglet.media.load('jazzy-abstract-beat-11254.mp3', streaming=False) #StaticSource object
    #player_2.queue(music)
    #player_2.loop=True
    #player_2.queue(music)
    try:
        player_2.volume= 0.6 * music_multiplier * int(not(config["muted"]))
    except:
        pass
    player_2.play()
    #initializ
    root=tk.Tk()
    root.title('Python Word Game')
    root.geometry('1000x600+140+30')
    Menu(root)
    root.mainloop()





#class for the menu GUI, separate from settings
class Menu():

    global bg_color, music_multiplier, click, player_2

    
    def __init__(self,root):

        self.click=click                 #sound effect for click defined as part of the class
        self.player_2=player_2           #music player as part of the class
        #self.player_2.play()             #music starts playing(this command has no effect on the player if the player is already playing
        self.root=root                   #cannot be connected with other modules without this
        #Frame 1
        self.f1=tk.Frame(root,width=1000)
        self.f1.pack(side='top')
        self.label1=tk.Label(self.f1,text="Python Word Game", font='Vivaldi 40',bg=bg_color,width=1000)
        #αν ο χρήστης κάνει το background color μαύρο από τα settings, τα γράμματα θα γίνονται άσπρα
        if config["bg_color"]=='#000000':self.label1.configure(foreground='white')
        self.label1.pack(expand=1,fill='x')
        self.label2=tk.Label(self.f1,text='MENU', font='Stencil 40',bg=bg_color,width=1000)
        if config["bg_color"]=='#000000':self.label2.configure(foreground='white')
        self.label2.pack()
        self.f4=tk.Frame(root,width=500,bg=bg_color)
        self.f4.pack(side='top',expand=1,fill='both')
        self.f2=tk.Frame(root,width=500,bg=bg_color)
        self.f2.pack(side='top',expand=1,fill='both')
        #PLAY Button
        self.play_button=tk.Button(self.f2,text='PLAY',font='Arial 16',relief='groove',bg='#1d7b72',command=self.play_game)
        self.play_button.pack(side='top')
        #self.play_button.bind('<Enter>',self.color_config(self.play_button, "red",event)) 
        #self.play_button.bind("<Leave>", partial(self.color_config, self.play_button, "black"))
        self.play_button.bind('<Enter>',partial(self.color_config, self.play_button, "red")) 
        self.play_button.bind("<Leave>", partial(self.color_config, self.play_button, "black"))
        #partial 'freezes' a function at a specific instant, therefore we dont have to create different function for each color 
        
        #LEADERBOARD Button
        self.leader_button=tk.Button(self.f2,text='LEADERBOARD',font='Arial 16',relief='groove',bg='#1d7b72',command=self.leaderboard)
        self.leader_button.pack(side='top')
        self.leader_button.bind('<Enter>',partial(self.color_config, self.leader_button, "red"))
        self.leader_button.bind("<Leave>", partial(self.color_config, self.leader_button, "black"))
        
        #SETTINGS Button
        self.settings_button=tk.Button(self.f2,text='SETTINGS',font='Arial 16',relief='groove',bg='#1d7b72',command=self.settings)
        self.settings_button.pack(side='top')
        self.settings_button.bind('<Enter>',partial(self.color_config, self.settings_button, "red")) #"#942706" complementary color
        self.settings_button.bind("<Leave>", partial(self.color_config, self.settings_button, "black"))

        #CREDITS
        self.credits_button=tk.Button(self.f2,text='CREDITS',font='Arial 16',relief='groove',bg='#1d7b72',command=self.credits)
        self.credits_button.pack(side='top')
        self.credits_button.bind('<Enter>',partial(self.color_config, self.credits_button, "red")) #"#942706" complementary color
        self.credits_button.bind("<Leave>", partial(self.color_config, self.credits_button, "black"))        
        
        #QUIT Button
        self.quit_button=tk.Button(self.f2,text='EXIT',font='Arial 16',relief='groove',bg='#f53b57',command=self.game_exit)
        self.quit_button.pack(side='top')
        self.quit_button.bind('<Enter>',partial(self.color_config, self.quit_button, "blue")) #"#f53b57" complementary color
        self.quit_button.bind("<Leave>", partial(self.color_config, self.quit_button, "black"))

    def play_game(self):
        'χρησιμοποιείται από το START BUTTON που συνδέει το μενού με το game gui'
        click.play()
        player_2.pause()  #stop the menu music
        self.root.destroy()    #close the menu window
        game_gui.game(bg_color, music_multiplier)        #from game_gui module function game ->initializes the game

    #COLOR CHANGE WHEN MOUSE HOVERS OVER BUTTONS  
    def color_config(self,widget, color, event):
        '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
        widget.config(foreground=color)


    #show leaderboards, WIP
    def leaderboard(self):
        click.play()
        #self.player_2.delete()   #delete the music player when ecxiting the game
        self.root.destroy()
        leaderboard.lmain(bg_color, player_2)

    def credits(self):
        click.play()
        self.credit_win=tk.Toplevel(self.root,bg=bg_color)
        self.credit_win.title('Credits')
        self.credit_win.geometry('400x400+100+100')
        self.foreground='black'
        if config["bg_color"]=='#000000':self.foreground='white'
        else:self.foreground='black'
        #frame 1
        self.f1=tk.Frame(self.credit_win,bg=bg_color)
        self.f1.pack(fill='both',expand=1)
        self.l1=tk.Label(self.f1,text='Royalty free sound effects from:',font='Arial 16',bg=bg_color,fg=self.foreground)
        #if config["bg_color"]=='#000000':self.l1.configure(foreground='white')
        self.l1.pack(fill='both',expand=1)
        self.l1.bind('<Enter>',partial(self.color_config, self.l1, "red"))
        self.l1.bind("<Leave>", partial(self.color_config, self.l1, self.foreground))
        #frame 2
        self.f2=tk.Frame(self.credit_win,bg=bg_color)
        self.f2.pack(fill='both',expand=1)
        self.l2=tk.Label(self.f2,text='Mixkit',font='Arial 16',bg=bg_color,fg=self.foreground)
        #if config["bg_color"]=='#000000':self.l2.configure(foreground='white')
        self.l2.pack(fill='both',expand=1)
        self.l2.bind('<Enter>',partial(self.color_config, self.l2, "red"))
        self.l2.bind("<Leave>", partial(self.color_config, self.l2, self.foreground))
        #frame 3
        self.f3=tk.Frame(self.credit_win,bg=bg_color)
        self.f3.pack(fill='both',expand=1)
        self.l3=tk.Label(self.f3,text='Creator Assets',font='Arial 16',bg=bg_color,fg=self.foreground)
        #if config["bg_color"]=='#000000':self.l3.configure(foreground='white')
        self.l3.pack(fill='both',expand=1)
        self.l3.bind('<Enter>',partial(self.color_config, self.l3, "red"))
        self.l3.bind("<Leave>", partial(self.color_config, self.l3, self.foreground))
        #frame 4
        self.f4=tk.Frame(self.credit_win,bg=bg_color)
        self.f4.pack(fill='both',expand=1)
        self.l4=tk.Label(self.f4,text='Pixabay',font='Arial 16',bg=bg_color,fg=self.foreground)
        #if config["bg_color"]=='#000000':self.l4.configure(foreground='white')
        self.l4.pack(fill='both',expand=1)
        self.l4.bind('<Enter>',partial(self.color_config, self.l4, "red"))
        self.l4.bind("<Leave>", partial(self.color_config, self.l4, self.foreground))        


    #exit the game, replace quit() with tkinter kill()
    def game_exit(self):
        click.play()
        self.root.destroy()
        player_2.delete()
        quit()
        
        
    #go to settings GUI
    def settings(self):
        click.play()
        #SETTINGS WINDOW
        self.settings_window=tk.Toplevel(self.root,bg=bg_color)  #παράθυρο ρυθμίσεων ήχου και μουσικής
        self.settings_window.geometry('200x166+440+217')
        self.settings = Settings(self.settings_window,self) #οπως 5ο εργαστηριο #class SETTINGS
        #self.settings_window.geometry('100x100')
        #Settings.adjust_sfx(self.a)
        #find a way to simply change the layout instead of creating a new window
        
    def letter_color(self):
        self.label1.configure(foreground='white')
        self.label2.configure(foreground='white')



#class for settings GUI, separate from menu
#store settings in a .yaml file
class Settings():

    global bg_color, music_multiplier, muted, click, player_2, config

    def __init__(self,window,menu):
        #self.player_2=player_2     #player
        #self.player_2.loop=True
        #self.click=click
        self.window=window
        self.menu=menu
        self.root=self.menu.root #αρχικο παραθυρο απο την κλάση μενού
        
        #MUSIC BUTTON
        self.music_button=tk.Button(self.window,text='music',relief='groove',command=self.adjust_music)
        self.music_button.bind('<Enter>',partial(self.color_config,self.music_button,'red'))
        self.music_button.bind("<Leave>", partial(self.color_config, self.music_button, "black"))
        self.music_button.pack()
        #BACKROUND COLOR BUTTON
        self.color_button=tk.Button(self.window,text='color',relief='groove',command=self.color_choice)
        self.color_button.bind('<Enter>',partial(self.color_config,self.color_button,'red'))
        self.color_button.bind("<Leave>", partial(self.color_config, self.color_button, "black"))
        self.color_button.pack()
        #EXIT BUTTON
        self.exit_button=tk.Button(self.window,text='exit',relief='groove',command=self.settings_exit)
        self.exit_button.bind('<Enter>',partial(self.color_config,self.exit_button,'red'))
        self.exit_button.bind("<Leave>", partial(self.color_config, self.exit_button, "black"))
        self.exit_button.pack()

        #COLOR CHANGE WHEN MOUSE HOVERS OVER BUTTONS  
    def color_config(self,widget, color, event):
        '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
        widget.config(foreground=color)

    
##### MUSIC VOLUME FUNCTIONS  ######
        
    def x(self):
        'USED BY ok button to change the volume'
        global muted
        music_multiplier=self.w.get()/100
        #config["music_multiplier"] = music_multiplier
        player_2.volume=self.w.get()/100
        config["music_multiplier"] = player_2.volume
        with open("config.yaml", "w") as f: yaml.dump(config, f)
        self.root.destroy()
        main()

    def mute(self):
        global muted
        muted = True
        config["muted"] = True
        player_2.volume = 0
        with open("config.yaml", "w") as f: yaml.dump(config, f)

    def unmute(self):
        global muted
        muted = False
        config["muted"] = False
        player_2.volume = 0.6 * music_multiplier
        with open("config.yaml", "w") as f: yaml.dump(config, f)
        
    #MUSIC WINDOW    
    def adjust_music(self):
        'creates the music toplevel,slider,buttons'
        click.play()
        self.music_window=tk.Toplevel(self.root,bg=bg_color,height=400,width=400)
        self.music_window.geometry('400x200')
        #mute button
        self.pause_button=tk.Button(self.music_window,text='mute',relief='groove',command=self.mute)
        self.pause_button.pack()
        #unmute button
        self.play_button=tk.Button(self.music_window,text='unmute',relief='groove',command=self.unmute)
        self.play_button.pack()
        #slider
        self.w = tk.Scale(self.music_window, from_=0.0, to=100, orient='horizontal',bg=bg_color)
        self.w.set(music_multiplier*100)
        self.w.pack()
        #ok button    
        self.ok_button=tk.Button(self.music_window,text='ok',relief='groove',command=self.x)
        self.ok_button.pack()

        
    #Αποθήκευση ρυθμίσεων, ξανατρέχει η main (για να εφαρμοστούν οι αλλαγές του χρήστη)
    def settings_exit(self): 
        with open("config.yaml", "w") as f: yaml.dump(config, f)
        self.root.destroy()
        main(player_2)

    #BACKROUND COLOR BUTTON COMMAND
    def color_choice(self):
        click.play()
        config["bg_color"] = colorchooser.askcolor(title = "Select a color", color = bg_color)[1]
        #Μολις επιλέξει χρώμα ο χρήστης η main ξανατρέχει και έτσι εφαρμόζονται οι αλλαγές του χρήστη
        #στην περιπτωση που το χρωμα γινει μαυρο καθως η main ξανακαλειται μεσω της self.settings_exit(), τα labels γίνονται άσπρα
        self.settings_exit()





#main ptrogram#



pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
click = pyglet.media.load('sound-16.wav',streaming=False)
player_2 = pyglet.media.Player()
music= pyglet.media.load('jazzy-abstract-beat-11254.mp3', streaming=False) #StaticSource object

player_2.queue(music)

if __name__=='__main__': main()
