######################################################################
# Array Processor                                                    #
# This program sorts arrays and searches for values                  #
# Author: Martin Vu and Sean Cheong                                  #
# Date: 10/4/2020                                                    #
# Version number 9.0                                                 #
######################################################################


import tkinter as tk            
from tkinter import font as tkfont
from tkinter import messagebox
import math

class main(tk.Tk):

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
        def LinearB(): 
            Linear_search()
            Output.config(state="normal")
            Output.delete(0.0, "end")
            Output.insert("insert", Result)
            Output.config(state="disabled")
            
        def Linear_search():
            array = inputA.get()
            array = array.split(",")
            target = int(inputT.get())
            index = 0
            found = False
            global Result
            while index < len(array) and found == False:
                if int(array[index]) == target:
                    found = True
                else:
                    index = index + 1
            
            if found == True:
                Result = "found"
            else:
                 Result = "not found"

        def BinaryB():
            Binary_search()
            Output.config(state="normal")
            Output.delete(0.0, "end")
            Output.insert("insert", Result)
            Output.config(state="disabled")
            
        def Binary_search():
            array = inputA.get()
            array = array.split(",")
            target = int(inputT.get())
            found = False
            low = 0
            high = len(array)
            global Result
            while high >= low and found == False:
                mid = ((high + low)//2)
                if target < int(array[mid]):
                    high = mid - 1
                elif target == int(array[mid]):
                    found = True
                else:
                    low = mid + 1
                    
            if found == True:
                Result = "found"
            else:
                 Result = "not found"

        def clear():
            inputA.delete(0, "end")
            inputT.delete(0, "end")
            Output.config(state="normal")
            Output.delete(1.0, "end")
            Output.config(state="disabled")
        def Help():
            messagebox.showinfo( "Help", "Search Array\n"
"\n"
"Input the array and input a value that you want to be searched\n"
"Select the type of search:\n"
"Linear or Binary\n"
"\n"
"Note if you select binary the array must be in order\n")

                                                                          
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search", font=controller.title_font)
        label.grid(row = 1, column = 2)

        seperator1 = tk.Frame(self, height=2, bd=1)
        seperator1.grid(padx=10, pady=10, sticky = "we")
        
        
        arrayL = tk.Label(self, text="Array: ")
        arrayL.grid(row = 3, column = 1)
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
        
        LinearB = tk.Button(self, text="Linear",padx=20, command=LinearB)
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

        ClearB = tk.Button(self, text="Clear",padx=20,command = clear)
        ClearB.grid(row=23,column = 1, columnspan = 2, sticky = "es", pady=10)

        HelpB = tk.Button(self, text="Help",padx=20,command = Help)
        HelpB.grid(row=23,column = 1, columnspan = 2, sticky = "s", pady=10)
                
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.grid(column = 2)



class Sort(tk.Frame):

    def __init__(self, parent, controller):


        def BubbleB():
            if options_value.get()== 1:
                BubbleA_sort()
            else:
                BubbleD_sort()
            Output.config(state="normal")
            Output.delete(0.0, "end")
            Output.insert("insert", Result)
            Output.config(state="disabled")

        def BubbleA_sort():

            array = inputA.get()
            array = array.split(",")
            global Result
            for index in range(len(array)):
                for index in range(len(array)-1):
                    if array[index] > array[index+1]:
                        array[index], array[index+1] = array[index+1], array[index]
            Result = array

        def BubbleD_sort():

            array = inputA.get()
            array = array.split(",")
            global Result
            for index in range(len(array)):
                for index in range(len(array)-1):
                    if array[index] < array[index+1]:
                        array[index], array[index+1] = array[index+1], array[index]
            Result = array
            
            

        def SelectionB():
                if options_value.get()== 1:
                    SelectionA_sort()
                else:
                    SelectionD_sort()
                Output.config(state="normal")
                Output.delete(0.0, "end")
                Output.insert("insert", Result)
                Output.config(state="disabled")

        def SelectionA_sort():
            array = inputA.get()
            array = array.split(",")
            global Result
            for index in range(len(array)-1):
                Min = index
                for unsorted in range(index+1, len(array)):
                    if array[Min] < array[unsorted]:
                        unsorted = Min
                array[index], array[unsorted] = array[unsorted], array[index]
            Result = array

        def SelectionD_sort():
            array = inputA.get()
            array = array.split(",")
            global Result
            for index in range(len(array)-1):
                Min = index
                for unsorted in range(index+1, len(array)):
                    if array[Min] > array[unsorted]:
                        unsorted = Min
                array[index], array[unsorted] = array[unsorted], array[index]
            Result = array
            
        def InsertionB():
            
            if options_value.get()== 1:
                InsertionA_sort()
            else:
                InsertionD_sort()
            Output.config(state="normal")
            Output.delete(0.0, "end")
            Output.insert("insert", Result)
            Output.config(state="disabled")
            
        def InsertionA_sort():
            array = inputA.get()
            array = array.split(",")
            global Result
            for posofnext in range(1, len(array)):
                Next = array[posofnext]
                current = posofnext-1
                while current >= 0 and Next < array[current]:
                    array[current + 1] = array[current]
                    current -= 1
                array[current + 1] = Next
            Result = array

        def InsertionD_sort():
            array = inputA.get()
            array = array.split(",")
            global Result
            for posofnext in range(1, len(array)):
                Next = array[posofnext]
                current = posofnext-1
                while current >= 0 and Next > array[current]:
                    array[current + 1] = array[current]
                    current -= 1
                array[current + 1] = Next
            Result = array

        def clear():
            inputA.delete(0, "end")
            Output.config(state="normal")
            Output.delete(1.0, "end")
            Output.config(state="disabled")
        def Help():
            messagebox.showinfo( "Help", "Sorting Array\n"
"\n"
"Select Ascending if you want your array to be sorted in ascending order\n"
"or select Desending if you want your array to be sorted in descending order\n"
"\n"
"Input the array you want to be sorted\n"
"\n"
"Select a type sort:\n"
"Bubble, Selection or Insertion")

            
                              
        
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
        inputA= tk.Entry(inputframe, width=25)
        inputA.grid()

        seperator2 = tk.Frame(self, height=2, bd=2)
        seperator2.grid(padx=5, pady=5, sticky = "we")
                
        BubbleB = tk.Button(self, text="Bubble",padx = 20,command=BubbleB)
        BubbleB.grid(row = 11, column = 1, sticky = "es")
        SelectionB = tk.Button(self, text="Selection",padx = 20, command=SelectionB)
        SelectionB.grid(row = 11, column = 2, sticky = "s")
        InsertionB = tk.Button(self, text="Insertion",padx = 20, command=InsertionB)
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

        ClearB = tk.Button(self, text="Clear",padx=20,command = clear)
        ClearB.grid(row=23,column = 1, columnspan = 2, sticky = "es", pady=10)

        HelpB = tk.Button(self, text="Help",padx=20,command = Help)
        HelpB.grid(row=23,column = 1, columnspan = 2, sticky = "s", pady=10)

        
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"))
        button.grid(column = 2)




if __name__ == "__main__":
    main = main()
    main.mainloop()

