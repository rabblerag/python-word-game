#necessary modules
import time, pyglet, itertools, enchant, random, string, final_menu, yaml, os, tkinter as tk
from functools import partial

#get path
path = os.path.realpath(__file__) + "\\..\\..\\assets\\"

# φορτωση ήχων ως static sources
oops=pyglet.media.load(path +'mixkit-system-beep-buzzer-fail-2964.wav',streaming=False)
wins=pyglet.media.load(path +'win.wav',streaming=False)
newlettersound=pyglet.media.load(path +'mixkit-retro-game-notification-212.wav',streaming=False)
click = pyglet.media.load(path +'sound-16.wav',streaming=False)

vowels = ['a','e','i','o','u']  # Μια λίστα με τα φωνίεντα του αγγλικού αλφάβητου με σκοπό κάθε φορά το πρόγραμμα να διαλέγει οτυλάχιστον ένα από αυτά
Dictionary = enchant.Dict("en_US") # Το αγγλικό λεξιλόγιο που χρησιμοποιείται για τον έλεγχο των λέξεων

def game(bg, sfx, player):

    global bg_color, sfx_multiplier, player_2, score, multiplier, click
    
    score = 0
    multiplier = 1
    bg_color = bg
    sfx_multiplier = sfx
    player_2 = player

    #initialize graphics
    root = tk.Tk()
    MyApp(root)
    root.mainloop()

    #go to main menu once mainloop is over, only happens when user chooses to return to main menu
    player_2.delete()
    final_menu.main()


class Restart():            ###parathiro epibebaiosis restart

    global bg_color, sfx_multiplier, player_2

    def __init__(self, win3, app):
        
        win3.title("")
        self.win3 = win3
        self.root = app.root
        win3.geometry("600x100+500+200")
        self.rf = tk.Frame(win3)
        self.rf.pack(side = "top",fill = "x",expand=1)
        self.rl = tk.Label(self.rf, text = "Are you sure you want to start a new game? \nCurrent game progress will be lost.",
                            font ="Arial 14", justify = "left")
        self.rl.pack(fill = "x",expand = 1)
        self.rf2 = tk.Frame(win3)
        self.rf2.pack(side = "bottom", fill ="x", expand = 1)
        self.rb1 = tk.Button(self.rf2 , text = "cancel", font = "Arial 14",
                                command = self.nobtn, width = 10)
        self.rb1.bind('<Enter>',partial(self.color_config, self.rb1, "red")) 
        self.rb1.bind("<Leave>", partial(self.color_config, self.rb1, "black"))  
        self.rb1.pack(side = "right", padx = 10, pady = 10,expand = 1)
        self.rb2 = tk.Button(self.rf2, text ="Yes", font = "Arial 14",
                                command = self.yesbtn, width = 10)
        self.rb2.bind('<Enter>',partial(self.color_config, self.rb2, "red")) 
        self.rb2.bind("<Leave>", partial(self.color_config, self.rb2, "black"))  
        self.rb2.pack(side = "right", pady = 10, expand = 1)

    def yesbtn(self):
        click.play().volume = 1.5 * sfx_multiplier
        self.win3.destroy()
        self.root.destroy()
        game(bg_color, sfx_multiplier, player_2)

##------------------------------------------------------------    

    def nobtn(self): 
        click.play().volume = 1.5 * sfx_multiplier
        self.win3.destroy()

    #changes color of button when hovered
    def color_config(self,widget, color, event): widget.config(foreground=color)
        
        
class MyMenu():         ####parathuro epibebaiosis epistrofi sto menou

    global bg_color, music_multiplier

    def __init__(self, win, app):   

        self.root = app.root
        self.win = win
        self.win.title("")
        self.win.geometry("410x100+500+200")
        self.q = tk.Frame(self.win)
        self.q.pack(side = "top",fill = "x",expand=1)
        self.q1 = tk.Label(self.q, text = "Are you sure you want to go to the main menu? \nYour current game will be deleted.",
                            font ="Arial 14")
        self.q1.pack(side = "left", fill = "x",expand = 1)
        self.q2 = tk.Frame(self.win)
        self.q2.pack(side = "bottom", fill ="x", expand = 1)
        self.b1 = tk.Button(self.q2 , text = "cancel", font = "Arial 14", command = self.clw, width = 10)
        self.b1.bind('<Enter>',partial(self.color_config, self.b1, "red"))
        self.b1.bind("<Leave>", partial(self.color_config, self.b1, "black"))
        self.b1.pack(side = "right", padx = 10, pady = 10,expand = 1)
        self.b2 = tk.Button(self.q2, text ="Yes", font = "Arial 14", command = self.mainmenu, width = 10)
        self.b2.bind('<Enter>',partial(self.color_config, self.b2, "red"))
        self.b2.bind("<Leave>", partial(self.color_config, self.b2, "black"))
        self.b2.pack(side = "right", pady = 10, expand = 1)

    #clears the window, nothing happens
    def clw(self): 
        click.play().volume = 1.5 * sfx_multiplier
        self.win.destroy()             
    #returns to main menu
    def mainmenu(self):
        click.play().volume = 1.5 * sfx_multiplier
        self.win.destroy()
        self.root.destroy()
        player_2.play()

    #changes color of button when hovered
    def color_config(self,widget, color, event): widget.config(foreground=color)

class MyApp():

    global bg_color, sfx_multiplier
    
    def __init__(self, root):

        self.root = root
        self.root.title("Python Word Game")
        self.root.geometry("600x500+400+100")
        self.create_canvas()
        start = time.time()

    def take_word(self, event = None):      ###apothikeuei ti leksi sti metabliti word otan o xristis pataei to koumpi me to belaki
        word = self.entrytext
        words = word.get()
##       elegxos leksis kai score 
        self.entrytext.set("")
        self.entry["textvariable"] = self.entrytext
        if words in old_words:
            oops.play().volume = 1.5 * sfx_multiplier
            self.entrytext.set("Την έχεις πει ήδη")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())
            
        elif len(words) == 1:
            self.entrytext.set("You've already said this word")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())
            
        elif all(letter in letters for letter in words):
            try:
                self.is_word(words)
                old_words.append(words)
            except Exception:
                pass
        else:
            oops.play().volume = 1.5 * sfx_multiplier
            self.entrytext.set("Wrong letters")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())

    def wordreset(self):
        self.entrytext.set("")
        self.entry["textvariable"] = self.entrytext
        self.entry.configure(fg = "black")
    def is_word(self, words):

        if Dictionary.check(words) == True:
             wins.play().volume = 1.5 * sfx_multiplier
             global score, multiplier
             score = score + multiplier
             self.scorevar.set(score)
             multiplier += 1
                 
        else:
            oops.play().volume = 1.5 * sfx_multiplier       #για να μην υπαρχει καθυστερηση ο ήχος παιζει πρώτος
            self.entrytext.set("This word does not exist")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())    

    def menu(self):
        win = tk.Toplevel(self.root)
        MyMenu(win, self)
        win.mainloop()

    def restart_button(self):
        win3 = tk.Tk()
        Restart(win3, self)
        win3.mainloop()
        
    def new_letters(self):
        global letters
        letters = []
        count = 0
        global old_letters
        old_letters = []
        global multiplier
        multiplier = 1
        n = random.randint(4,9)
        for _ in itertools.repeat(None, n):
          new_letter = random.choice(string.ascii_lowercase)
          if new_letter in old_letters:
               count = count =+ 1
               if count >= 1:
                    continue
          else:
          if new_letter not in old_letters:
               old_letters.append(new_letter)
               letters.append(new_letter)
        letters.append(random.choice(vowels))

          else:
               continue   
        self.last_letter()
    #This function makes sure that there is always a vowel present in the list 
    def last_letter(self):
        last_letter = random.choice(vowels)
        if last_letter in old_letters:
            self.last_letter()
        else:
            letters.append(last_letter)
            random.shuffle(letters)
            self.give_letters()

    #This function shows the list of letters to the playerr
    def give_letters(self):
        newlettersound.play().volume = 1.5 * sfx_multiplier
        self.f2.pack_forget()
        self.f2.destroy()
        self.f2 = tk.Frame(self.f1, bg = bg_color)
        self.f2.pack(side = "top", expand = 1)
        a = int(len(letters))
        z = str(letters[0])
        for x in range(0,a):
            y = str(letters[x])
            self.y = tk.Label(self.f2, text = y, font = "Arial 15",
                                fg = "black", bg ='grey',relief = "raised", width = 2)
            self.y.pack(side = "left", padx = 5, expand = 1)
        

    def activebutton(self, event):
        event.widget["activeforeground"]="white"
        event.widget["activebackground"]=bg_color
    def color_config(self,widget, color, event): widget.config(foreground=color)

    def countdown(self,count):
        # change text in label        
        self.timevar.set(str(count))
        self.root.update_idletasks
        if count > 0:
            
            self.root.after(1000, self.countdown, count-1)
            
        else:
            
            self.mainf.pack_forget()
            self.mainf2 = tk.Frame(self.root, bg = bg_color)
            self.mainf2.pack(fill = "both", expand = 1)
            self.root.update_idletasks()

            for x in range(3):
                self.tmlbl = tk.Label(self.mainf2, text = "TIME UP",
                                      font = "Arial 18", fg = "red", bg = "grey",relief = "raised", width = 15, height = 5 )
                self.tmlbl.pack(pady = 30)
                self.root.update_idletasks()
                time.sleep(0.5)

                self.tmlbl.pack_forget()
                self.root.update_idletasks()
                self.tmlbl2 = tk.Label(self.mainf2, text = "TIME UP",
                                      font = "Arial 18", fg = "black", bg = "grey",relief = "raised", width = 15, height = 5 )
                self.tmlbl2.pack(pady = 30)
                self.root.update_idletasks()
                time.sleep(0.5)
                self.tmlbl2.pack_forget()
                self.root.update_idletasks()

            self.tmlbl3 = tk.Label(self.mainf2, text = "TIME UP",
                                      font = "Arial 18", fg = "red", bg = "grey",relief = "raised", width = 15, height = 5 )
            self.tmlbl3.pack(pady = 30)
            self.get_name()
            self.root.update_idletasks

    def create_canvas(self):
##--------------------------------------------------------------------------------------------------------- menubar           
        self.f = tk.Frame(self.root, bg = "grey")
        self.f.pack(side = "top", fill = "both")
        #MENU BUTTON
        self.mn = tk.Button(self.f, text = "MENU", font = "Arial 14",
                            fg ="black", bg = "grey", command = self.menu)
        self.mn.pack(side = "left", fill = "both")
        self.mn.bind('<Enter>',partial(self.color_config, self.mn, "red")) #"#f53b57" complementary color
        self.mn.bind("<Leave>", partial(self.color_config, self.mn, "black"))

        #self.mn.bind("<Enter>",self.activebutton)
        #RESTART BUTTON
        self.rst = tk.Button(self.f, text = "RESTART",font = "Arial 14",
                                command = self.restart_button, fg = "black", bg = "grey")
        self.rst.pack(side = "left", padx = 1, fill = "both")
        self.rst.bind('<Enter>',partial(self.color_config, self.rst, "red")) #"#f53b57" complementary color
        self.rst.bind("<Leave>", partial(self.color_config, self.rst, "black"))

        #add quit button
        

        global old_words
        old_words = []

        #TIME?
        self.timevar = tk.StringVar()
        self.timevar.set("60")
        self.time = tk.Label(self.f, textvariable = self.timevar, font = "Arial 14",
                                fg = "red", bg = "grey", width = 10)
        self.time.pack(side="right",fill = "both")
    
        self.scorevar = tk.IntVar()
        self.scorevar.set('0')
        self.skr = tk.Label(self.f, textvariable = self.scorevar, font = "Arial 14",
                            fg = "green", bg = "grey", width = 10)
        self.skr.pack(side = "right",fill = "both")
        
#-------------------------------------------------------------------------------------------------------------- ready/start eidopoihsh
        self.root.update_idletasks()
        self.rdf = tk.Frame(self.root, bg = bg_color)
        self.rdf.pack(fill = "both", expand = 1)
        self.lbl = tk.Label(self.rdf,text = "READY",font = "Arial 18", bg = "grey", fg= "white",relief = "raised", width = 15, height = 5)
        self.lbl.pack(pady = 30)
        self.root.update_idletasks()
        time.sleep(2)
        self.rdf.pack_forget()
##        self.rdf.destroy()
        self.rdf2 = tk.Frame(self.root, bg = bg_color)
        self.rdf2.pack(fill = "both", expand = 1)
        self.lbl2 = tk.Label(self.rdf2,text = "START",font = "Arial 18", bg = "grey", fg= "white", relief = "raised", width = 15, height = 5)
        self.lbl2.pack(pady = 30)
        self.root.update_idletasks()
        time.sleep(2)
        self.rdf2.pack_forget()
##        self.rdf2.destroy()
#---------------------------------------------------------------------------
        self.mainf = tk.Frame(self.root, bg = bg_color)
        self.mainf.pack(side = "bottom", fill = "both", expand = 1)

        self.f1 = tk.Frame(self.mainf, bg = bg_color)
        self.f1.pack(padx = 5, pady = 120, fill = "both",expand = 1)
        
#------------------------------------------------------------------------------------------# label me ta grammata
        self.f2 = tk.Frame(self.f1, bg = bg_color)
        self.f2.pack(side = "top", expand = 1)
        self.new_letters()
##        a = int(len(letters))
##        z = str(letters[0])
##        for x in range(0,a):
##            y = str(letters[x])
##            self.y = tk.Label(self.f2, text = y, font = "Arial 15",
##                                fg = "black", bg = "grey", relief = "raised",width = 2)
##            self.y.pack(side = "left", padx = 5, expand = 1)
#--------------------------------------------------------------------------------------------
        self.nl = tk.Button(self.f1, text = "new letters", font = "Arial 14",
                            fg = "black", bg = "grey", command = self.new_letters)
        self.nl.pack(side = "bottom", expand = 1)
        self.nl.bind("<Enter>",self.activebutton)
        self.nl.bind('<Enter>',partial(self.color_config, self.nl, "red")) 
        self.nl.bind("<Leave>", partial(self.color_config, self.nl, "black"))
        self.f3 = tk.Frame(self.f1)
        self.f3.pack(side = "bottom", pady = 20, expand = 1)
        
        self.entrytext = tk.StringVar()
        self.entrytext.set("")
        self.entry = tk.Entry(self.f3, font = "Arial 17")
        self.entry.pack(side = "left", expand = 1)
        self.entry["textvariable"] = self.entrytext
        
        self.nxt = tk.Button(self.f3 , text = "-->",command = self.take_word, font = "Arial 12", fg = "black", bg = "grey")
        self.nxt.pack(side = "right", expand = 1)
        self.nxt.bind("<Enter>", partial(self.color_config, self.nxt, "red"))
        self.nxt.bind("<Leave>", partial(self.color_config, self.nxt, "black"))
        self.root.bind("<Return>", self.take_word)
        self.countdown(60)

    #Functions for adding user to leaderboard    
    def get_name(self):

        self.win = tk.Toplevel(self.root, bg = "grey")
        self.win.geometry("600x100+500+200")
        self.f = tk.Frame(self.win, bg = "grey")
        self.f.pack(side = "top", fill = "x", expand = 1)
        self.l = tk.Label(self.f, text="Type your name: ", font ="Arial 14", justify = "left", fg = "black", bg = "grey")
        self.l.pack(fill = "x", expand = 1)
        self.nameentry = tk.StringVar()
        self.n_entry = tk.Entry(self.f, font = "Arial 17", textvariable = self.nameentry)
        self.n_entry.pack(side = "left", expand = 1)
        self.ok = tk.Button(self.f , text = "Add to leaderboard",command = self.add_leaderboard, font = "Arial 12", fg = "black", bg = "grey")
        self.ok.pack(side = "right", expand = 1)
        self.ok.bind("<Enter>", partial(self.color_config, self.ok, "red"))
        self.ok.bind("<Leave>", partial(self.color_config, self.ok, "black"))
        self.win.bind("<Return>", self.add_leaderboard)

    def add_leaderboard(self, e=None):

        name = self.n_entry.get().strip()
        try:
            with open(path + "leaderboard.yaml", "r") as f: lboard = yaml.load(f, Loader = yaml.FullLoader)
        except Exception: lboard = {}
        if name not in lboard or (name in lboard and score > lboard[name]):
            lboard[name] = score
            with open(path + "leaderboard.yaml", "w") as f: yaml.dump(lboard, f)
        self.win.destroy()


