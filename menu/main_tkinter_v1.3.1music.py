#needed for settings class
import yaml
import tkinter as tk
from tkinter import ttk
from functools import partial
import pyglet
##click = pyglet.media.load('sound-16.wav',streaming=False)
##import pyaudio
##from pydub import AudioSegment
##from pydub.playback import play

#click = pyglet.media.load('sound-16.wav',streaming=False)

###from playsound import playsound


#class for the menu GUI, separate from settings
class Menu():
    #add tkinter etc.
    def __init__(self,root):
        #click = pyglet.media.load('sound-16.wav',streaming=False)
        #self.click=click
        self.player_2=player_2
        self.player_2.loop=True
        self.root=root
        self.f1=tk.Frame(root,width=1000)
        self.f1.pack(side='top')
        label1=tk.Label(self.f1,text="Python Word Game", font='Vivaldi 40',bg='#069486',width=1000)
        label1.pack(expand=1,fill='x')
        label2=tk.Label(self.f1,text='MENU', font='Stencil 40',bg="#069486",width=1000)
        label2.pack()
        self.f4=tk.Frame(root,width=500,bg='#069486')
        self.f4.pack(side='top',expand=1,fill='both')
        self.f2=tk.Frame(root,width=500,bg='#069486')
        self.f2.pack(side='top',expand=1,fill='both')
        #PLAY
        self.play_button=tk.Button(self.f2,text='PLAY',font='Arial 16',relief='groove',bg='#942706',command=self.play_game)
        self.play_button.pack(side='top')
        #self.play_button.bind('<Enter>',self.color_config(self.play_button, "red",event)) 
        #self.play_button.bind("<Leave>", partial(self.color_config, self.play_button, "black"))
        self.play_button.bind('<Enter>',partial(self.color_config, self.play_button, "red")) 
        self.play_button.bind("<Leave>", partial(self.color_config, self.play_button, "black"))
        #https://docs.python.org/3/library/functools.html  
        #https://stackoverflow.com/questions/10239292/changing-text-color-when-hovering-over-text-with-tkinter
        #
        #LEADERBOARD
        self.leader_button=tk.Button(self.f2,text='LEADERBOARD',font='Arial 16',relief='groove',bg='#1d7b72',command=self.leaderboard)
        self.leader_button.pack(side='top')
        self.leader_button.bind('<Enter>',partial(self.color_config, self.leader_button, "red"))
        self.leader_button.bind("<Leave>", partial(self.color_config, self.leader_button, "black"))
        #SETTINGS
        self.settings_button=tk.Button(self.f2,text='SETTINGS',font='Arial 16',relief='groove',bg='#942706',command=self.settings)
        self.settings_button.pack(side='top')
        self.settings_button.bind('<Enter>',partial(self.color_config, self.settings_button, "red")) #"#942706" complementary color
        self.settings_button.bind("<Leave>", partial(self.color_config, self.settings_button, "black"))
        #QUIT
        self.quit_button=tk.Button(self.f2,text='EXIT',font='Arial 16',relief='groove',bg='#1d7b72',command=self.game_exit)
        self.quit_button.pack(side='top')
        self.quit_button.bind('<Enter>',partial(self.color_config, self.quit_button, "red")) #"#942706" complementary color
        self.quit_button.bind("<Leave>", partial(self.color_config, self.quit_button, "black"))

        

    #start main game, WIP
    def play_game(self):
        click.play()
        global options_window
        
        options_window=tk.Toplevel(root,bg='#069486',height=400,width=400)
        self.options_window=options_window
        #top.geometry("180x100")
        self.options_window.geometry('500x250+300+175')
        self.option1=tk.Button(self.options_window,text='HARD',bg='#1d7b72',font='Arial 12',relief='groove')### ADD command!!!!!!!!!
        self.option1.pack()
        self.option1.bind('<Enter>',partial(self.color_config,self.option1,'red'))
        self.option1.bind("<Leave>", partial(self.color_config, self.option1, "black"))
        self.option2=tk.Button(self.options_window,text='MEDIUM',bg='#1d7b72',font='Arial 12',relief='groove')### ADD command!!!!!!!!!
        self.option2.pack()
        self.option2.bind('<Enter>',partial(self.color_config,self.option2,'red'))
        self.option2.bind("<Leave>", partial(self.color_config, self.option2, "black"))
        self.option3=tk.Button(self.options_window,text='EASY',bg='#1d7b72',font='Arial 12',relief='groove')### ADD command!!!!!!!!!
        self.option3.pack()
        self.option3.bind('<Enter>',partial(self.color_config,self.option3,'red'))
        self.option3.bind("<Leave>", partial(self.color_config, self.option3, "black"))
        self.option4=tk.Button(self.options_window,text='EXIT',bg='#1d7b72',font='Arial 12',relief='groove',command=self.close_options)
        self.option4.pack()
        self.option4.bind('<Enter>',partial(self.color_config,self.option4,'red'))
        self.option4.bind("<Leave>", partial(self.color_config, self.option4, "black"))
        
    def close_options(self):
        #song = AudioSegment.from_wav('sound-16.wav')
        #play(song)
        click.play()
        options_window.destroy()  

       
    def color_config(self,widget, color, event):
        '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
        widget.configure(foreground=color)


    #show leaderboards, WIP
    def leaderboard(self):
        click.play()


    #exit the game, replace quit() with tkinter kill()
    def game_exit(self):
        click.play()
        root.destroy()
        quit()
        
    #go to settings GUI
    def settings(self):
        click.play()
        self.settings_window=tk.Toplevel(root,bg='#069486',height=400,width=400)
        self.settings = Settings(self.settings_window,self) #οπως 5ο εργαστηριο #class SETTINGS
        self.settings_window.geometry('100x100')
##        self.w = tk.Scale(settings_window, from_=0.0, to=100, orient='horizontal',bg='#069486')
##        self.w.pack()
##        self.a=self.w.get()
##        click.volume=self.a
        #Settings.adjust_sfx(self.a)
        #find a way to simply change the layout instead of creating a new window

#class for settings GUI, separate from menu
#store settings in a .yaml file
class Settings():
    def __init__(self,window,menu):
        self.player_2=player_2     #player
        self.player_2.loop=True
        self.window=window
        self.menu=menu
        self.root=self.menu.root #arxiko para8yro
        self.sfx_button=tk.Button(self.window,text='sound settings',relief='groove',bg='#942706',command=self.adjust_sfx)
        self.sfx_button.pack()
        self.sfx_button.bind('<Enter>',partial(self.menu.color_config,self.sfx_button,'red'))
        self.sfx_button.bind("<Leave>", partial(self.menu.color_config, self.sfx_button, "black"))
        self.music_button=tk.Button(self.window,text='music',relief='groove',command=self.adjust_music)
        self.music_button.pack()
        #exit,save button
        self.exit_button=tk.Button(self.window,text='exit',relief='groove',command=self.settings_exit)
        self.exit_button.pack()
        


        
        with open("config.yaml", "r") as f: self.config = yaml.safe_load(f)
        self.sfx_multiplier = self.config["sfx_multiplier"]
        self.music_multiplier = self.config["music_multiplier"]
        self.selected_color = self.config["selected_color"]
        #add tkinter 

    #sound effects volume slider(?) 0-100
    def adjust_sfx(self):
        self.sfx_window=tk.Toplevel(self.root,bg='#069486',height=400,width=400)
        self.w = tk.Scale(self.sfx_window, from_=0.0, to=100, orient='horizontal',bg='#069486')
        self.w.pack()
        self.inp=self.w.get()
        click.volume=self.inp
        self.config["sfx_multiplier"] = self.sfx_multiplier = self.inp/100 #change 100 as necessary so input is in range
        #find sounds to add, find module for sound manipulation in python
        

    #music volume slider(?) 0-100
    def x(self):
        self.inp=self.w.get()
        self.player_2.volume=self.inp/100
        self.config["music_multiplier"] = self.music_multiplier = self.inp/100
        
        
    def adjust_music(self):
        self.music_window=tk.Toplevel(self.root,bg='#069486',height=400,width=400)
        self.play_button=tk.Button(self.music_window,text='play',relief='groove',command=self.player_2.play)
        self.play_button.pack()
        self.pause_button=tk.Button(self.music_window,text='pause',relief='groove',command=self.player_2.pause)
        self.pause_button.pack()
        self.w = tk.Scale(self.music_window, from_=0.0, to=100, orient='horizontal',bg='#069486')
        self.w.pack()
        #self.w.set(self.music_multiplier)

    
        self.ok_button=tk.Button(self.music_window,text='ok',relief='groove',command=self.x)
        self.ok_button.pack()
        #self.x lambda :self.w.get()
        #click.volume=self.inp
        #self.player_2.volume=self.inp
        #self.config["music_multiplier"] = self.music_multiplier = self.inp/100 
        #same as above

    #exit settings GUI, replace quit() with tkinter kill()
    def settings_exit(self): 
        #implement in tkinter with buttons
        #x = input("Save changes?(Y/N):")
        if x == "Y": 
            with open("config.yaml", "w") as f: yaml.dump(self.config, f)
        quit()
        #root.kill() or equivalent

    #let the user choose a bg color
    def bg_color(self, choice):
        choice = colorchooser.askcolor(title = "Select a color")[1]
        self.config["bg_color"], self.bg_color = choice
        #set_bg_color(self.selected_color)

        #options: black, white, red, blue etc.
        #or: let user change the color based on RGB values on 3 sliders
        if choice in self.config["bg_colors"]: self.config["selected_color"] = self.selected_color = choice
        #set_bg_color(self.selected_color)
        
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
click = pyglet.media.load('sound-16.wav',streaming=False)
player_2 = pyglet.media.Player()
music= pyglet.media.load('jazzy-abstract-beat-11254.mp3', streaming=False)
player_2.queue(music)
player_2.loop=True
with open("config.yaml", "r") as f:
    fruits_list = yaml.safe_load(f)

    print(fruits_list)
#volume = yaml.safe_load(f, Loader=yaml.FullLoader)
#player_2.volume=self.music_multiplier
player_2.play()
root=tk.Tk()
root.title('Python Word Game')
root.geometry('1000x500+50+50')
Menu(root)
root.mainloop()

