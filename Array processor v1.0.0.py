######################################################################
# Array Processor                                                    #
# This program sorts arrays and searches for values                  #
# Author: Martin Vu and Sean Cheong                                  #
# Date: 23/3/2021                                                    #
# Version number 1.0.0                                               #
######################################################################


import tkinter as tk            
from tkinter import font as tkfont   

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='arial', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Search, Sort):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Array Processor", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Choose either Search or Sort: ", font= 'arial')
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Search",
                            command=lambda: controller.show_frame("Search"))
        button2 = tk.Button(self, text="Sort",
                            command=lambda: controller.show_frame("Sort"))
        button1.pack(pady = 5)
        button2.pack()


class Search(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.pack()


class Sort(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sort", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        options_label = tk.Label(self, text='Ascending or Descending: ')
        options_label.pack(side="top", fill="x", pady=10)
        options_value = tk.IntVar()
    
        Ascending = tk.Radiobutton( self , text = 'Ascending' ,
            variable = options_value , value = 1 )
        Descending = tk.Radiobutton( self , text = 'Descending' ,
            variable = options_value , value = 2 )
        Ascending.pack(side="top", fill="x")
        Descending.pack(side="top", fill="x", pady = 10)
        options_value.set(1)
        
        Larray = tk.Label(self, text="Array: ")
        Larray.pack(side = "left")
        arrayin = tk.Entry(self, bd =5)
        arrayin.pack(side = "right", pady = 10)
        
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.pack(side = "bottom")
        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
