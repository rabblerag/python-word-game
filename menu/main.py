#needed for settings class
import yaml

#class for the menu GUI, separate from settings
class Menu():
    #add tkinter etc.
    def __init__(self): pass


    #start main game, WIP
    def play_game(self): pass


    #show leaderboards, WIP
    def leaderboard(self): pass


    #exit the game, replace quit() with tkinter kill()
    def game_exit(self): 
        quit()
        #root.kill()


    #go to settings GUI
    def settings(self): 
        settings = Settings()
        #find a way to simply change the layout instead of creating a new window

#class for settings GUI, separate from menu
#store settings in a .yaml file
class Settings():
    def __init__(self): 
        with open("config.yaml", "r") as f: self.config = yaml.safe_load(f)
        self.sfx_multiplier = self.config["sfx_multiplier"]
        self.music_multiplier = self.config["music_multiplier"]
        self.selected_color = self.config["selected_color"]
        #add tkinter 

    #sound effects volume slider(?) 0-100
    def adjust_sfx(self, inp): 
        self.config["sfx_multiplier"] = self.sfx_multiplier = inp/100 #change 100 as necessary so input is in range
        #find sounds to add, find module for sound manipulation in python

    #music volume slider(?) 0-100
    def adjust_music(self, inp): 
        self.config["music_multiplier"] = self.music_multiplier = inp/100 
        #same as above

    #exit settings GUI, replace quit() with tkinter kill()
    def settings_exit(self): 
        #implement in tkinter with buttons
        x = input("Save changes?(Y/N):")
        if x == "Y": 
            with open("config.yaml", "w") as f: yaml.dump(self.config, f)
        quit()
        #root.kill() or equivalent

    #let the user choose a bg color
    def bg_color(self, choice):
        #options: black, white, red, blue etc.
        #or: let user change the color based on RGB values on 3 sliders
        if choice in self.config["bg_colors"]: self.config["selected_color"] = self.selected_color = choice
        #set_bg_color(self.selected_color)
