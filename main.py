from menu import menu
import tkinter as tk

class App():

    def __init__(self, root):
        self.root = root
        self.container = tk.Frame(self.root) 
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (menu.Menu, menu.Settings, ):
            frame = F(self.container)
            self.frames[F] = frame
        self.show_frame(menu.Menu)

    def show_frame(self, cont):
        frame = self.frames[cont]



root=tk.Tk()
root.title('Python Word Game')
root.geometry('1000x500+50+50')
App(root)
root.mainloop()