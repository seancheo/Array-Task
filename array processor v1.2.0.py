######################################################################
# Array Processor                                                    #
# This program sorts arrays and searches for values                  #
# Author: Martin Vu and Sean Cheong                                  #
# Date: 10/4/2020                                                    #
# Version number 1.2.0                                               #
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
        label.grid(row = 1, column = 2)
        
        LArray = tk.Label(self, text="Array: ")
        LArray.grid(row = 3, column = 1)
        inputframe = tk.Frame(self)
        inputframe.grid(row = 3, column = 2)
        inputf = tk.Text(inputframe, height=1, width=15)
        inputf.grid()

        LTarget = tk.Label(self, text="Target: ")
        LTarget.grid(row = 4, column = 1)
        inputframe = tk.Frame(self)
        inputframe.grid(row = 4, column = 2)
        inputf = tk.Text(inputframe, height=1, width=15)
        inputf.grid()

        TOutput = tk.Label(self, text="Output: ")
        TOutput.grid(row = 5, column = 1)
        outputframe = tk.Frame(self)
        outputframe.grid(row = 5, column = 2)
        Output = tk.Text(outputframe, state="disabled", height=1, width=15)
        Output.grid()
                
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.grid(column = 2)


class Sort(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sort", font=controller.title_font)
        label.grid(row = 1, column = 1, columnspan = 2)
        options_label = tk.Label(self, text='Ascending or Descending: ')
        options_label.grid(row = 3, column = 1, columnspan = 2)
        options_value = tk.IntVar()
    
        Ascending = tk.Radiobutton( self , text = 'Ascending' ,
            variable = options_value , value = 1 )
        Descending = tk.Radiobutton( self , text = 'Descending' ,
            variable = options_value , value = 2 )
        Ascending.grid(row = 5, column = 1, columnspan = 2)
        Descending.grid(row = 6, column = 1, columnspan = 2)
        options_value.set(1)

        LArray = tk.Label(self, text="Array: ")
        LArray.grid(row = 8, column = 1)
        inputframe = tk.Frame(self)
        inputframe.grid(row = 8, column = 2)
        inputf = tk.Text(inputframe, height=1, width=15)
        inputf.grid()
                
        LOutput = tk.Label(self, text="Sorted Array: ")
        LOutput.grid(row = 10, column = 1)
        outputframe = tk.Frame(self)
        outputframe.grid(row = 10, column = 2)
        Output = tk.Text(outputframe, state="disabled", height=1, width=15)
        Output.grid()
        
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.grid(column = 2)
        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

