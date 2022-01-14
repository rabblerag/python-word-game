import tkinter as tk
import time
import final_menu
import pyglet
from functools import partial
import itertools
import enchant
import random
import string

# φορτωση ήχων ως static sources
#endsound=pyglet.media.load('bbc_applause.mp3',streaming=False)
oops=pyglet.media.load('mixkit-system-beep-buzzer-fail-2964.wav',streaming=False)
wins=pyglet.media.load('win.wav',streaming=False)
newlettersound=pyglet.media.load('mixkit-retro-game-notification-212.wav',streaming=False)
vowels = ['a','e','i','o','u']  # Μια λίστα με τα φωνίεντα του αγγλικού αλφάβητου με σκοπό κάθε φορά το πρόγραμμα να διαλέγει οτυλάχιστον ένα από αυτά
Dictionary = enchant.Dict("en_US") # Το αγγλικό λεξιλόγιο που χρεισημοποιείται για τον έλεγχο των λέξεων

global score, multiplier
score = 0
multiplier = 1


def game(bg, music):
    global bg_color, music_multiplier
    bg_color = bg
    music_multiplier = music
    #with open('leaderboard.txt','w') as f:
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()


class Restart():            ###parathiro epibebaiosis restart

    global bg_color, music_multiplier

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
        self.rb1.pack(side = "right", padx = 10, pady = 10,expand = 1)
        self.rb2 = tk.Button(self.rf2, text ="Yes", font = "Arial 14",
                                command = self.yesbtn, width = 10)
        self.rb2.pack(side = "right", pady = 10, expand = 1)

    def yesbtn(self):
        self.win3.destroy()
        self.root.destroy()
        game(bg_color, music_multiplier)
##------------------------------------------------------------    
    def nobtn(self):
        self.win3.destroy()
        
        
class MyMenu():         ####parathuro epibebaiosis epistrofi sto menou

    global bg_color, music_multiplier

    def __init__(self, win, app):   #win=window
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
        self.b1.pack(side = "right", padx = 10, pady = 10,expand = 1)
        self.b2 = tk.Button(self.q2, text ="Yes", font = "Arial 14", command = self.mainmenu, width = 10)
        self.b2.pack(side = "right", pady = 10, expand = 1)

    def clw(self):
        self.win.destroy()             

    def mainmenu(self):
        self.win.destroy()
        self.root.destroy()
        #self.win.destroy() #to win καταστρεφεται αυτοματα ως tk.Toplevel
        final_menu.main()
        #self.mainMenu()
        #self.root.destroy()


    
class MyApp():

    global bg_color, music_multiplier
    
    def __init__(self, root):
        self.root = root
        self.root.title("efarmogi6")
        self.root.geometry("600x500+400+100")
        self.create_canvas()
        start = time.time()

    def take_word(self):      ###apothikeuei ti leksi sti metabliti word otan o xristis pataei to koumpi me to belaki
        word = self.entrytext
        words = word.get()
##       elegxos leksis kai score 
        self.entrytext.set("")
        self.entry["textvariable"] = self.entrytext
        if words in old_words:
            oops.play()
            self.entrytext.set("Την έχεις πει ήδη")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())
             
            print('Την έχεις πει ήδη')
            
        elif len(words) == 1:
            self.entrytext.set("Την έχεις πει ήδη")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())
            print('Δώσε μια λέξη')
            
        elif all(letter in letters for letter in words):
            try:
                self.is_word(words)
                old_words.append(words)
            except:
                pass
        else:
            oops.play()
            self.entrytext.set("Λάθος γράμματα")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())
            
            print('Λάθος γράμματα')

    def wordreset(self):
        self.entrytext.set("")
        self.entry["textvariable"] = self.entrytext
        self.entry.configure(fg = "black")
    def is_word(self, words):

        if Dictionary.check(words) == True:
             wins.play()
             global score, multiplier
             score = score + multiplier
             self.scorevar.set(score)
             multiplier += 1
             print('Score = {}'.format(score))
##             with open('leaderboard.txt','a') as f:
##                 f.write('Score = {}\n'.format(score))
                 
        else:
            oops.play()                                           #για να μην υπαρχει καθυστερηση ο ήχος παιζει πρώτος
            self.entrytext.set("Δεν υπάρχει αυτή η λέξη")
            self.entry.configure(fg = "red")
            self.entry["textvariable"] = self.entrytext
            self.root.update_idletasks()
            self.root.after(600, self.wordreset())
            #oops.play()
            print('Δεν υπάρχει αυτή η λέξη')
            
             
    def end():
        endsound.play()
        print('Τέλος παιχνιδιού')
    
        
    def showText(self):
        text = self.entry.get()
        print(text)

    def menu(self):
        win = tk.Toplevel(self.root)
        mymenu = MyMenu(win, self)
        win.mainloop()

    def restartButton(self):
        win3 = tk.Tk()
        restart = Restart(win3, self)
        win3.mainloop()
        
    def new_letters(self):
        global letters
        letters = []
        count = 0
        old_letters = []
        global multiplier
        multiplier = 1
        n = random.randint(4,9)
        for _ in itertools.repeat(None, n):
          new_letter = random.choice(string.ascii_lowercase)
          if new_letter in old_letters:
               count = count =+ 1
               if count >= 2:
                    continue
          else:
               old_letters.append(new_letter)
               letters.append(new_letter)
        letters.append(random.choice(vowels))
        newlettersound.play()
##-------------------------------------------------------------------------------------
       # k = ["g","j","d","i"]       #list  grammata
##------------------------------------------------------------------------------------
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
    def color_config(self,widget, color, event):
        '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
        widget.config(foreground=color)

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
                                command = self.restartButton, fg = "black", bg = "grey")
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
        self.f3 = tk.Frame(self.f1)
        self.f3.pack(side = "bottom", pady = 20, expand = 1)
        
        self.entrytext = tk.StringVar()
        self.entrytext.set("")
        self.entry = tk.Entry(self.f3, font = "Arial 17")
        self.entry.pack(side = "left", expand = 1)
        self.entry["textvariable"] = self.entrytext
        
        self.nxt = tk.Button(self.f3 , text = "-->",command = self.take_word, font = "Arial 12", fg = "black", bg = "grey")
        self.nxt.pack(side = "right", expand = 1)
        self.nxt.bind("<Enter>",self.activebutton)
        self.countdown(60)
        



