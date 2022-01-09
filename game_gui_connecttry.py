import tkinter as tk
import time
import pyglet
#import sys
#sys.path.append('C:\\Users\\USER\\Documents\\project\\python-word-game-main\\menu')
import final_menu
from functools import partial
import itertools
from random import choice
from random import randint
import enchant
import random
import string
#from final_menu import color_config   #(self,widget, color, event)

##import importlib.util
##spec = importlib.util.spec_from_file_location("final_menu.py", 'C:\\Users\\USER\\Documents\\project\\python-word-game-main\\menu')
##foo = importlib.util.module_from_spec(spec)
##spec.loader.exec_module(foo)
##foo.MyClass()
###from 'C:\\Users\\USER\\Documents\\project\\python-word-game-main\\menu' import final_menu


newlettersound=pyglet.media.load('mixkit-retro-game-notification-212.wav',streaming=False)
k = ["a","b","c","d","e"]

def game():
    class Restart():            ###parathiro epibebaiosis restart
        def __init__(self,win3):
            win3.title("")
            self.win3 = win3
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
            root.destroy()
            game()
    ##------------------------------------------------------------
            
        def nobtn(self):
            self.win3.destroy()
            
            
    class MyMenu():         ####parathuro epibebaiosis epistrofi sto menou
        def __init__(self,win):   #win=window
            self.root=root
            win.title("")
            win.geometry("410x100+500+200")
            self.win = win
            self.q = tk.Frame(win)
            self.q.pack(side = "top",fill = "x",expand=1)
            self.q1 = tk.Label(self.q, text = "Are you sure you want to go to the main menu? \nYour current game will be deleted.",
                               font ="Arial 14")
            self.q1.pack(side = "left", fill = "x",expand = 1)
            self.q2 = tk.Frame(win)
            self.q2.pack(side = "bottom", fill ="x", expand = 1)
            self.b1 = tk.Button(self.q2 , text = "cancel", font = "Arial 14", command = self.clw, width = 10)
            self.b1.pack(side = "right", padx = 10, pady = 10,expand = 1)
            self.b2 = tk.Button(self.q2, text ="Yes", font = "Arial 14", command = self.mainmenu, width = 10)
            self.b2.pack(side = "right", pady = 10, expand = 1)

        def clw(self):
            self.win.destroy()             

        def mainmenu(self):
            self.root.destroy()
            #self.win.destroy()
            root2=tk.Tk()
            root2.title('Python Word Game')
            root2.geometry('1000x500+50+50')
            final_menu.Menu(root2)
            root2.mainloop()
            #        self.mainMenu()
            #root.destroy()


       
    class MyApp():
        def __init__(self,root):
            self.root = root
            root.title("python word game")
            root.geometry("600x500+400+100")
            self.create_canvas()
        def color_config(self,widget, color,event):
            '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
            widget.configure(foreground=color)


        def take_word(self):      ###apothikeuei ti leksi sti metabliti word otan o xristis pataei to koumpi me to belaki
            word = self.entrytext
    ##       elegxos leksis kai score 
            self.entrytext.set("")
            self.entry["textvariable"] = self.entrytext


            
        def showText(self):
            text = self.entry.get()
            print(text)

        def menu(self):
            win = tk.Toplevel(self.root)
            mymenu = MyMenu(win)
            win.mainloop()

        def restartButton(self):
            win3 = tk.Tk()
            restart = Restart(win3)
            win3.mainloop()


        def new_letters(self):
            newlettersound.play()   #sfx
    ##------------------------------------------------------------------------------------- NEW LETTERS
            vowels = ['a','e','i','o','u']
            n = random.randint(4,8)
            for _ in itertools.repeat(None, n):
                letters = [random.choice(string.ascii_lowercase)]
          #print((letters), sep='', end=' ', flush=True)
     #print([random.choice(vowels)])
            letters = [letters+[random.choice(vowels)]]
    ##-------------------------------------------------------------------------------------
            k = list(letters)      #list  grammata
    ##------------------------------------------------------------------------------------
            self.f2.pack_forget()
            self.f2.destroy()
            self.f2 = tk.Frame(self.f1, bg = "#123456")
            self.f2.pack(side = "top", expand = 1)
            #a = len(k)
            #z = str(k[0])
            for x in k:
                y = str(x)
                self.y = tk.Label(self.f2, text = y, font = "Arial 15",
                                  fg = "black", bg = "grey",relief = "raised")
                self.y.pack(side = "left", expand = 1)

        def activebutton(self, event):
            event.widget["activeforeground"]="white"
            event.widget["activebackground"]="purple"


            

        def create_canvas(self):
##--------------------------------------------------------------------------------------------------------- menubar           
            self.f = tk.Frame(root, bg = "grey")
            self.f.pack(side = "top", fill = "both")
            self.mn = tk.Button(self.f, text = "menu", font = "Arial 14",
                                fg ="black", bg = "grey", command = self.menu)
            self.mn.pack(side = "left", fill = "both")
            #color of letters changibg when mouse hovers over them
            self.mn.bind('<Enter>',partial(self.color_config,self.mn,'red'))    #partial(function,instant)
            self.mn.bind("<Leave>", partial(self.color_config, self.mn, "black"))

            #self.mn.bind("<Enter>",self.activebutton)
            self.rst = tk.Button(self.f, text = "restart",font = "Arial 14",
                                 command = self.restartButton,  bg = "grey" )
            #color of letters changibg when mouse hovers over them
            self.rst.bind('<Enter>',partial(self.color_config,self.rst,'red'))    #partial(function,instant)
            self.rst.bind("<Leave>", partial(self.color_config, self.rst, "black"))   #color_config(self,widget=self.rst,color=black)
            self.rst.pack(side = "left", padx = 1, fill = "both")

            #self.rst.bind("<Enter>",self.activebutton)

            self.timevar = tk.StringVar()
            self.timevar.set("05:00")
            self.time = tk.Label(self.f, textvariable = self.timevar, font = "Arial 14",
                                 fg = "red", bg = "grey", width = 10)
            self.time.pack(side="right",fill = "both")

            self.scorevar = tk.IntVar()
            self.scorevar.set("0")
            self.skr = tk.Label(self.f, textvariable = self.scorevar, font = "Arial 14",
                                fg = "green", bg = "grey", width = 10)
            self.skr.pack(side = "right",fill = "both")
            
    #-------------------------------------------------------------------------------------------------------------- ready/start eidopoihsh
            root.update_idletasks()
            self.rdf = tk.Frame(root, bg = "#123456")
            self.rdf.pack(fill = "both", expand = 1)
            self.lbl = tk.Label(self.rdf,text = "READY",font = "Arial 18", bg = "purple", fg= "white",relief = "raised", width = 15, height = 5)
            self.lbl.pack(pady = 30)
            root.update_idletasks()
            time.sleep(2)
            self.rdf.pack_forget()
    ##        self.rdf.destroy()
            self.rdf2 = tk.Frame(root, bg = "#123456")
            self.rdf2.pack(fill = "both", expand = 1)
            self.lbl2 = tk.Label(self.rdf2,text = "START",font = "Arial 18", bg = "purple", fg= "white", relief = "raised", width = 15, height = 5)
            self.lbl2.pack(pady = 30)
            root.update_idletasks()
            time.sleep(2)
            self.rdf2.pack_forget()
    ##        self.rdf2.destroy()
    #---------------------------------------------------------------------------
            self.mainf = tk.Frame(root, bg = "#123456")
            self.mainf.pack(side = "bottom", fill = "both", expand = 1)

            self.f1 = tk.Frame(self.mainf, bg = "#123456")
            self.f1.pack(padx = 5, pady = 120, fill = "both",expand = 1)
            
    #------------------------------------------------------------------------------------------# label me ta grammata
    #------------------------------------------------------------------------------------------# label me ta grammata

            self.f2 = tk.Frame(self.f1, bg = "#123456")
            self.f2.pack(side = "top", expand = 1)
            a = int(len(k))
            z = str(k[0])
            for x in range(0,a):
                y = str(k[x])
                self.y = tk.Label(self.f2, text = y, font = "Arial 15",
                                  fg = "black", bg = "grey", relief = "raised",width = 2)
                self.y.pack(side = "left", padx = 5, expand = 1)
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
        def color_config(self,widget, color,event):
            '''αλλαγή χρώματος κουμπιού όταν το ποντίκι είναι απο πάνω του'''
            widget.configure(foreground=color)


        

    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
if __name__=='__main__':
    #newlettersound=pyglet.media.load('mixkit-retro-game-notification-212.wav',streaming=False)
    game()
    
