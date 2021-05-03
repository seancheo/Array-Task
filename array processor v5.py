######################################################################
# Array Processor                                                    #
# This program sorts arrays and searches for values                  #
# Author: Martin Vu and Sean Cheong                                  #
# Date: 10/4/2020                                                    #
# Version number 4.0                                                 #
######################################################################


import tkinter as tk            
from tkinter import font as tkfont
from tkinter import messagebox
import math

class main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='arial', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Search, Sort):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
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

        def BinaryB():
            
            binary_search()
            Output.config(state="normal")
            Output.delete(0.0, "end")
            Output.insert(0.0, Result)
            Output.config(state="disabled")
        def binary_search():
            array = int(inputA.get())
            target = int(inputT.get())
            global Result
            Result = (array+target)


        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search", font=controller.title_font)
        label.grid(row = 1, column = 2)

        seperator1 = tk.Frame(self, height=2, bd=1)
        seperator1.grid(padx=10, pady=10, sticky = "we")
        
        
        array = tk.Label(self, text="Array: ")
        array.grid(row = 3, column = 1)
        inputframe = tk.Frame(self)
        inputframe.grid(row = 3, column = 2)
        inputA= tk.Entry(inputframe, width=25)
        inputA.grid()

        target = tk.Label(self, text="Target: ")
        target.grid(row = 4, column = 1)
        inputframe = tk.Frame(self)
        inputframe.grid(row = 4, column = 2)
        inputT = tk.Entry(inputframe, width=25)
        inputT.grid()


        seperator1 = tk.Frame(self, height=5, bd=1)
        seperator1.grid(padx=10, pady=10, sticky = "we")
        
        LinearB = tk.Button(self, text="Linear",padx=20)
        LinearB.grid(row = 5, column = 1, columnspan = 2, sticky = "es", pady=10)
        BinaryB = tk.Button(self, text="Binary", padx=20, command=BinaryB)
        BinaryB.grid(row = 5, column = 1, columnspan = 2, sticky = "s", pady=10)

        seperator1 = tk.Frame(self, height=2, bd=1)
        seperator1.grid(padx=10, pady=10, sticky = "we")
        
        TOutput = tk.Label(self, text="Output: ")
        TOutput.grid(row = 9, column = 1)
        outputframe = tk.Frame(self)
        outputframe.grid(row = 9, column = 2)
        Output = tk.Text(outputframe, state="disabled", height=1, width=25)
        Output.grid()

                
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.grid(column = 2)



class Sort(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sort", font=controller.title_font)
        label.grid(row = 1, column = 1, columnspan = 2)
    
        seperator1 = tk.Frame(self, height=2, bd=1)
        seperator1.grid(padx=10, pady=10, sticky = "we")
        
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
        inputf = tk.Text(inputframe, height=1, width=25)
        inputf.grid()

        seperator2 = tk.Frame(self, height=2, bd=2)
        seperator2.grid(padx=5, pady=5, sticky = "we")
                
        BubbleB = tk.Button(self, text="Bubble",padx = 20)
        BubbleB.grid(row = 11, column = 1, sticky = "es")
        SelectionB = tk.Button(self, text="Selection",padx = 20)
        SelectionB.grid(row = 11, column = 2, sticky = "s")
        InsertionB = tk.Button(self, text="Insertion",padx = 20)
        InsertionB.grid(row = 11, column = 3, sticky = "s")
        
        seperator3 = tk.Frame(self, height=2, bd=1)
        seperator3.grid(padx=5, pady=5, sticky = "we")

        LOutput = tk.Label(self, text="Sorted Array: ")
        LOutput.grid(row = 14, column = 2, rowspan = 3)
        outputframe = tk.Frame(self)
        outputframe.grid(row = 19, column = 2, rowspan = 3)
        Output = tk.Text(outputframe, state="disabled", height=1, width=25)
        Output.grid()
        
        seperator4 = tk.Frame(self, height=2, bd=1)
        seperator4.grid(padx=5, pady=5, sticky = "we")

        
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.grid(column = 2)




if __name__ == "__main__":
    main = main()
    main.mainloop()
