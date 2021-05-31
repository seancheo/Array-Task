######################################################################
# Array Processor                                                    #
# This program sorts arrays and searches for values                  #
# Author: Martin Vu and Sean Cheong                                  #
# Date: 13/5/2020                                                    #
# Version number 15.0                                                #
######################################################################


import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox


class app(tk.Tk):  # inherits functions of tkinter within class

    def __init__(self, *args, **kwargs):  # when class main is called fucntion is initialized
        tk.Tk.__init__(self, *args, **kwargs)  # initialises tkinter
        # args (arguments) passes unlimited amount of variables
        # kwargs (keyword arguemnts) passes dictionaries

        self.title_font = tkfont.Font(family='arial', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)  # creates frame for container
        container.pack(side="top", fill="both", expand=True)# fills empty space within pack
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Search, Sort, Astring):  # loop for the pages
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")# stretches everything in frame to nsew

        self.show_frame("Home")

    def show_frame(self, page_name):  # Shows a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()  # raises the given frame to the top fo the stack which is the visible one


class Home(tk.Frame):  # home page, inherits everthing from frame

    def __init__(self, parent, controller):  # parent main class
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Array Processor",font=controller.title_font) #Title
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Choose either Search or Sort: ", font='arial')# Choosing sort label
        label.pack(side="top", fill="x", pady=10)

        SearchB = tk.Button(self, text="Search",command=lambda: controller.show_frame("Search"))  # search button
        SortB = tk.Button(self, text="Sort",command=lambda: controller.show_frame("Sort"))  # sort button
        AstringB = tk.Button(self, text="Array of strings",command=lambda: controller.show_frame("Astring"))  # sort button
        SearchB.pack(pady=5)
        SortB.pack()
        AstringB.pack()
        


class Search(tk.Frame):

    def __init__(self, parent, controller):
        def LinearB():  # Linear Search ouput button
            while True:
                try:
                    array = inputA.get()  # saves the input to array
                    array = array.split(" ")
                    map_object = map(int, array)  # converts each element into integers
                    array = list(map_object)  # saves each element to the array
                    target = int(inputT.get())  # saves the input to target
                    
                    break
                except ValueError:
                    messagebox.showerror(title="Error", message="Enter a numeric value")
                    app.mainloop()

            Result = Linear_search(array, target)# calls linear search subprogram
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end") 
            Output.insert("insert", Result)# inserts the variable Result
            Output.config(state="disabled")  # Output cannot be interacted with

        def Linear_search(array, target):  # Linear Search algorithm
            index = 0  # defines index
            found = False  # defines found
            while index < len(array) and found == False: #post test loop; array isnt transversed and target isnt found
                if int(array[index]) == target: #tests if pointer is on target
                    return "Found at postion "+(str(index+1)) #returns to LinearB()
                else:
                    index += 1 #increments index
            if found == False:
                return "Not Found" #returns to LinearB()

        def BinaryB():  # Binary Search output button
            while True:
                try:
                    array = inputA.get()  # saves the input to array
                    array = array.split(" ")  # splits the string into elements
                    map_object = map(int, array)  # converts each element into integer
                    target = int(inputT.get())  # saves the input to target
                    array = list(map_object)  # saves each element to the array
                    array = sorted(array) #sorts the array 
                    break
                except ValueError:
                    messagebox.showerror(title="Error", message="Enter a numeric value")
                    app.mainloop()

            Result = Binary_search(array, target)  # calls binary search
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end")
            Output.insert("insert", Result)# insert the variable Result
            Output.config(state="disabled")  # Output cannot be interacted with

        def Binary_search(array, target):  # Binary search algorithm
            found = False #defines found
            low = 0 #defines low
            high = len(array)-1 #defines high as n-1 as list referencing starts at 0
            while high >= low: #post test loop; stops searching if valid search area is vialated
                mid = ((high + low)//2) #defines and finds mid
                if target < int(array[mid]): # compares target to mid
                    high = mid - 1 #makes high of new search area the mid-1 of old search area
                elif target == int(array[mid]): #checks if target is at mid
                    return "Found at postion "+(str(mid+1)) #returns to BinaryB()
                else: # only other possibility is target > array[mid]
                    low = mid + 1 #makes low of new search area the mid+1 of old search area
            return "Not Found" #returns to BinaryB()

        def clear():  # Clear button subprogram
            inputA.delete(0, "end")  # clears input inside array
            inputT.delete(0, "end")  # clears input inside target
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(1.0, "end")
            Output.config(state="disabled")  # Output cannot be interacted with

        def Help():  # Help button subprogram
            messagebox.showinfo("Help", "Search Array\n"  # output for the message box
                                "\n"
                                "Input the array and input a value that you want to be searched\n"
                                "Select the type of search:\n"
                                "Linear or Binary\n"
                                "\n"
                                "Note if you select binary the array is sorted first and the target is in the new position of the array\n")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search", font=controller.title_font)# Title for Search
        label.grid(row=1, column=2)

        seperator1 = tk.Frame(self, height=2, bd=1)  # Creates space in the GUI
        seperator1.grid(padx=10, pady=10, sticky="we")

        arrayL = tk.Label(self, text="Array: ")  # Label for Array
        arrayL.grid(row=3, column=1)
        inputframe = tk.Frame(self)  # input frame for array
        inputframe.grid(row=3, column=2)
        inputA = tk.Entry(inputframe, width=35)  # Input box for the array
        inputA.grid()

        target = tk.Label(self, text="Target: ")  # Label for Target
        target.grid(row=4, column=1)
        inputframe = tk.Frame(self)  # input frame target
        inputframe.grid(row=4, column=2)
        inputT = tk.Entry(inputframe, width=35)  # Input box for the target
        inputT.grid()

        seperator1 = tk.Frame(self, height=5, bd=1)  # Creates space in the GUI
        seperator1.grid(padx=10, pady=10, sticky="we")

        LinearB = tk.Button(self, text="Linear", padx=20, command=LinearB)  # Button for linear search
        LinearB.grid(row=5, column=1, columnspan=2, sticky="es", pady=10)
        BinaryB = tk.Button(self, text="Binary", padx=20, command=BinaryB)  # Button for binary search
        BinaryB.grid(row=5, column=1, columnspan=2, sticky="s", pady=10)

        seperator2 = tk.Frame(self, height=2, bd=1)  # Creates space in the GUI
        seperator2.grid(padx=10, pady=10, sticky="we")

        OutputL = tk.Label(self, text="Result: ")  # Result label
        OutputL.grid(row=9, column=1)
        outputframe = tk.Frame(self)  # output frame for the result
        outputframe.grid(row=9, column=2)
        Output = tk.Text(outputframe, state="disabled", height=1,width=25)  # Output box for the Result
        Output.grid()

        # Button for clearing the inputs and outputs
        ClearB = tk.Button(self, text="Clear", padx=20, command=clear)
        ClearB.grid(row=23, column=1, columnspan=2, sticky="es", pady=10)

        HelpB = tk.Button(self, text="Help", padx=20,command=Help)  # Help button label
        HelpB.grid(row=23, column=1, columnspan=2, sticky="s", pady=10)

        HomeB = tk.Button(self, text="Home", command=lambda: controller.show_frame("Home"))  # Home button
        HomeB.grid(column=2)


class Sort(tk.Frame):

    def __init__(self, parent, controller):

        def BubbleB():
            while True:
                try:
                    array = inputA.get()  # input for the array
                    array = array.split(" ")  # splits the array with commas
                    map_object = map(int, array)  # makes elements in arrray integers
                    array = list(map_object)  # saves the int elements to array
                    break
                except ValueError:
                    messagebox.showerror(title="Error", message="Enter a numeric value")
                    app.mainloop()
            if options_value.get() == 1:  # calls bubble ascending when ascending radio button is selected
                Result = BubbleA_sort(array)
            else:  # calls bubble descending when descending radio button is selected
                Result = BubbleD_sort(array)
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end")# inserts variable Result into output
            Output.insert("insert", Result)
            Output.config(state="disabled")  # Output cannot be interacted with

        def BubbleA_sort(array):
            for index in range(len(array)): # transverses the array
                for index in range(len(array)-1): #transverses the array n-1 times
                    if array[index] > array[index+1]: #compares paired elements
                        array[index], array[index +1] = array[index+1], array[index] #swaps so larger element is to the right
            return array #returns to BubbleB()

        def BubbleD_sort(array):
            for index in range(len(array)): # transverses the array
                for index in range(len(array)-1): #transverses the array n-1 times
                    if array[index] < array[index+1]: #compares paired elements
                        array[index], array[index +1] = array[index+1], array[index] #swaps so larger element is to the right
            return array #returns to BubbleB()

        def SelectionB():
            while True:
                try:
                    array = inputA.get()  # input for the array
                    array = array.split(" ")  # splits the array with commas
                    map_object = map(int, array)  # makes elements in arrray integers
                    array = list(map_object)  # saves the int elements to array
                    break
                except ValueError:
                    messagebox.showerror(title="Error", message="Enter a numeric value")
                    app.mainloop()
            if options_value.get() == 1:  # calls selection ascending when ascending radio button is selected
                Result = SelectionA_sort(array)
            else:  # calls selection descending when descending radio button is selected
                Result = SelectionD_sort(array)
            Output.config(state="normal") # allows the output box to be interacted with
            Output.delete(0.0, "end")
            Output.insert("insert", Result) # inserts variable Result into output
            Output.config(state="disabled")  # Output cannot be interacted with

        def SelectionA_sort(array):
            for index in range(len(array)): #transverses the array
                Min = index #declares pointer of the sorted part of the array(assuming the first element is sorted)
                for unsorted in range(index+1, len(array)): #transverses through unsorted part of the array
                    if array[Min] > array[unsorted]: #compares unsorted element with sorted element
                        Min = unsorted #places the unsorted element in the sorted part
                array[Min], array[index] = array[index], array[Min] #swaps elements
            return array #returns to SelectionB()

        def SelectionD_sort(array):
            for index in range(len(array)): #transverses the array
                Min = index #declares pointer of the sorted part of the array(assuming the first element is sorted)
                for unsorted in range(index+1, len(array)): #transverses through unsorted part of the array
                    if array[Min] < array[unsorted]: #compares unsorted element with sorted element
                        Min = unsorted #places the unsorted element in the sorted part
                array[Min], array[index] = array[index], array[Min] #swaps elements
            return array #returns to SelectionB()

        def InsertionB():
            while True:
                try:
                    array = inputA.get()  # input for the array
                    array = array.split(" ")  # splits the array with commas
                    map_object = map(int, array)  # makes elements in arrray integers
                    array = list(map_object)  # saves the int elements to array
                    break
                except ValueError:
                    messagebox.showerror(title="Error", message="Enter a numeric value")
                    app.mainloop()
            if options_value.get() == 1:  # calls insertion ascending when ascending radio button is selected
                Result = InsertionA_sort(array)
            else:  # calls insertion descending when descending radio button is selected
                Result = InsertionD_sort(array)
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end")
            Output.insert("insert", Result) # inserts Result into output
            Output.config(state="disabled")  # Output cannot be interacted with

        def InsertionA_sort(array):
            for posofnext in range(1, len(array)): #transverses the array, note 1 assumes first element as sorted
                Next = array[posofnext] #saves value of unsorted element to be inserted
                current = posofnext-1 #defines position of sorted element
                while current >= 0 and Next < array[current]: #post test loop; keeps current within range, compares an unsorted and a sorted element
                    array[current + 1] = array[current] #makes space
                    current -= 1 #decrements current
                array[current + 1] = Next #inserts element in the correct position in the sorted part of the array
            return array #returns to InsertionB()

        def InsertionD_sort(array):
            for posofnext in range(1, len(array)): #transverses the array, note 1 assumes first element as sorted
                Next = array[posofnext] #saves value of unsorted element to be inserted
                current = posofnext-1 #defines position of sorted element
                while current >= 0 and Next > array[current]: #post test loop; keeps current within range, compares an unsorted and a sorted element
                    array[current + 1] = array[current] #makes space
                    current -= 1 #decrements current
                array[current + 1] = Next #inserts element in the correct position in the sorted part of the array
            return array #returns to InsertionB()

        def clear():  # clear button subprogram
            inputA.delete(0, "end")  # clears array inside input box
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(1.0, "end")
            Output.config(state="disabled")  # Output cannot be interacted with

        def Help():  # Help button subprogram
            messagebox.showinfo("Help", "Sorting Array\n"  # output for message box
                                "\n"
                                "Select Ascending if you want your array to be sorted in ascending order\n"
                                "or select Desending if you want your array to be sorted in descending order\n"
                                "\n"
                                "Input the array you want to be sorted\n"
                                "\n"
                                "Select a type sort:\n"
                                "Bubble, Selection or Insertion")

        tk.Frame.__init__(self, parent)
        # Title for sort
        label = tk.Label(self, text="Sort", font=controller.title_font)
        label.grid(row=1, column=1, columnspan=2)

        seperator1 = tk.Frame(self, height=2, bd=1)  # Creates space in the GUI
        seperator1.grid(padx=10, pady=10, sticky="we")

        # Label for Ascending or Descending
        options_label = tk.Label(self, text='Ascending or Descending: ')
        options_label.grid(row=3, column=1, columnspan=2)
        options_value = tk.IntVar()

        Ascending = tk.Radiobutton(self, text='Ascending', variable=options_value, value=1)  # Radiobutton for Ascending
        Descending = tk.Radiobutton(self, text='Descending', variable=options_value, value=2)  # Radio button for Ascending
        Ascending.grid(row=5, column=1, columnspan=2)
        Descending.grid(row=6, column=1, columnspan=2)
        options_value.set(1)  # makes the default radiobutton ascending

        LArray = tk.Label(self, text="Array: ")  # Label for Array
        LArray.grid(row=8, column=1)
        inputframe = tk.Frame(self)  # input frame for input
        inputframe.grid(row=8, column=2)
        inputA = tk.Entry(inputframe, width=35)  # input box for array
        inputA.grid()

        seperator2 = tk.Frame(self, height=2, bd=2)  # Creates space in the GUI
        seperator2.grid(padx=5, pady=5, sticky="we")

        BubbleB = tk.Button(self, text="Bubble", padx=20,command=BubbleB)  # Button for binary sort
        BubbleB.grid(row=11, column=1, sticky="es")
        SelectionB = tk.Button(self, text="Selection", padx=20, command=SelectionB)  # Button for selection sort
        SelectionB.grid(row=11, column=2, sticky="s")
        InsertionB = tk.Button(self, text="Insertion", padx=20, command=InsertionB)  # Button for insertion sort
        InsertionB.grid(row=11, column=3, sticky="s")

        seperator3 = tk.Frame(self, height=2, bd=1)  # Creates space in the GUI
        seperator3.grid(padx=5, pady=5, sticky="we")

        LOutput = tk.Label(self, text="Sorted Array: ")# Label for Sorted Array
        LOutput.grid(row=14, column=2, rowspan=3)
        outputframe = tk.Frame(self)  # output frame for sorted array
        outputframe.grid(row=19, column=2, rowspan=3)
        Output = tk.Text(outputframe, state="disabled", height=1,width=30)  # output box for sorted array
        Output.grid()

        seperator4 = tk.Frame(self, height=2, bd=1)  # Creates Space in the GUI
        seperator4.grid(padx=5, pady=5, sticky="we")

        ClearB = tk.Button(self, text="Clear", padx=20,
                           command=clear)  # Clear button
        ClearB.grid(row=23, column=1, columnspan=2, sticky="es", pady=10)

        HelpB = tk.Button(self, text="Help", padx=20,command=Help)  # Help Button
        HelpB.grid(row=23, column=1, columnspan=2, sticky="s", pady=10)

        HomeB = tk.Button(self, text="Home",command=lambda: controller.show_frame("Home"))  # help button
        HomeB.grid(column=2)
        
class Astring(tk.Frame):

    def __init__(self, parent, controller):
        def BubbleB():
            array = inputA.get()  # input for the array
            array = array.split(" ")  # splits the array with commas
            Result = BubbleA_sort(array)
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end")# inserts variable Result into output
            Output.insert("insert", Result)
            Output.config(state="disabled")  # Output cannot be interacted with
            
        def BubbleA_sort(array):
            for index in range(len(array)): # transverses the array
                for index in range(len(array)-1): #transverses the array n-1 times
                    if array[index] > array[index+1]: #compares paired elements
                        array[index], array[index +1] = array[index+1], array[index] #swaps so larger element is to the right
            return array #returns to BubbleB()
            
            
        def clear():  # clear button subprogram
            inputA.delete(0, "end")  # clears array inside input box
            inputT.delete(0, "end")  # clears array inside input box
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(1.0, "end")
            Output.config(state="disabled")  # Output cannot be interacted with
            
        def LinearB():
            array = inputA.get()  # saves the input to array
            array = array.split(" ")
            target = str(inputT.get())
            Result = Linear_search(array, target)# calls linear search subprogram
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end") 
            Output.insert("insert", Result)# inserts the variable Result
            Output.config(state="disabled")  # Output cannot be interacted with


        def Linear_search(array, target):  # Linear Search algorithm
            index = 0  # defines index
            found = False  # defines found
            while index < len(array) and found == False: #post test loop; array isnt transversed and target isnt found
                if str(array[index]) == target: #tests if pointer is on target
                    return (str(array))+" Found at postion " +(str(index+1)) #returns to LinearB()
                                    #return "Found at postion "+(str(index+1))+(str(array))
                else:
                    index += 1 #increments index
            if found == False:
                return "Not Found" #returns to LinearB()

        def BinaryB():  # Binary Search output button
            array = inputA.get()  # saves the input to array
            array = array.split(" ")  # splits the string into elements
            target = str(inputT.get())  # saves the input to target
            array = sorted(array) #sorts the array 
            Result = Binary_search(array, target)  # calls binary search
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end")
            Output.insert("insert", Result)# insert the variable Result
            Output.config(state="disabled")  # Output cannot be interacted wi
            

        def Binary_search(array, target):  # Binary search algorithm
            found = False #defines found
            low = 0 #defines low
            high = len(array)-1 #defines high as n-1 as list referencing starts at 0
            while high >= low: #post test loop; stops searching if valid search area is vialated
                mid = ((high + low)//2) #defines and finds mid
                if target < str(array[mid]): # compares target to mid
                    high = mid - 1 #makes high of new search area the mid-1 of old search area
                elif target == str(array[mid]): #checks if target is at mid
                    return (str(array))+" Found at postion " +(str(mid+1)) #returns to BinaryB()
                else: # only other possibility is target > array[mid]
                    low = mid + 1 #makes low of new search area the mid+1 of old search area
            return "Not Found" #returns to BinaryB()
        
        def outputB():
            array = inputA.get()
            array.split(" ")
            Result = (str(array))
            Output.config(state="normal")# allows the output box to be interacted with
            Output.delete(0.0, "end")
            Output.insert("insert", Result)# insert the variable Result
            Output.config(state="disabled")  # Output cannot be interacted wi

            
        def Help():  # Help button subprogram
            messagebox.showinfo("Help", "Array of Strings\n"  # output for message box
                                "\n"
                                "Input an array of strings\n"
                                "Input a target if you want to search\n"
                                "\n"
                                "Select a type of search:\n"
                                "Linear or Binary"
                                "\n"
                                "If you want to sort in ascending order select Bubble\n"
                                "Select Array of Strings if you want to output the array\n")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Title for sort
        label = tk.Label(self, text="Array of Strings", font=controller.title_font)
        label.grid(row=1, column=1, columnspan=2)

        seperator1 = tk.Frame(self, height=2, bd=1)  # Creates space in the GUI
        seperator1.grid(padx=10, pady=10, sticky="we")

        # Label for Ascending or Descending
        LArray = tk.Label(self, text="Array: ")  # Label for Array
        LArray.grid(row=8, column=1)
        inputframe = tk.Frame(self)  # input frame for input
        inputframe.grid(row=8, column=2)
        inputA = tk.Entry(inputframe, width=35)  # input box for array
        inputA.grid()
        
        target = tk.Label(self, text="Target: ")  # Label for Target
        target.grid(row=9, column=1)
        inputframe = tk.Frame(self)  # input frame target
        inputframe.grid(row=9, column=2)
        inputT = tk.Entry(inputframe, width=35)  # Input box for the target
        inputT.grid()

        seperator2 = tk.Frame(self, height=2, bd=2)  # Creates space in the GUI
        seperator2.grid(padx=5, pady=5, sticky="we")

        BubbleB = tk.Button(self, text="Bubble", padx=20,command = BubbleB)  # Button for binary sort
        BubbleB.grid(row=11, column=1, sticky="es")
        LinearB = tk.Button(self, text="Linear", padx=20,command = LinearB)  # Button for selection sort
        LinearB.grid(row=11, column=2, sticky="s")
        BinaryB = tk.Button(self, text="Binary", padx=20, command = BinaryB)  # Button for insertion sort
        BinaryB.grid(row=11, column=3, sticky="s")
        ArrayOB = tk.Button(self, text="Array of Strings", padx=20,command = outputB)  # Button for selection sort
        ArrayOB.grid(row=12, column=2, sticky="s")

        seperator3 = tk.Frame(self, height=2, bd=1)  # Creates space in the GUI
        seperator3.grid(padx=5, pady=5, sticky="we")

        LOutput = tk.Label(self, text="Output: ")# Label for Sorted Array
        LOutput.grid(row=14, column=2, rowspan=3)
        outputframe = tk.Frame(self)  # output frame for sorted array
        outputframe.grid(row=19, column=2, rowspan=3)
        Output = tk.Text(outputframe, state="disabled", height=2,width=35)  # output box for sorted array
        Output.grid()

        seperator4 = tk.Frame(self, height=2, bd=1)  # Creates Space in the GUI
        seperator4.grid(padx=5, pady=5, sticky="we")

        ClearB = tk.Button(self, text="Clear", padx=20,
                           command=clear)  # Clear button
        ClearB.grid(row=23, column=1, columnspan=2, sticky="es", pady=10)

        HelpB = tk.Button(self, text="Help", padx=20,command=Help)  # Help Button
        HelpB.grid(row=23, column=1, columnspan=2, sticky="s", pady=10)

        HomeB = tk.Button(self, text="Home",command=lambda: controller.show_frame("Home"))  # help button
        HomeB.grid(column=2)


if __name__ == "__main__":
    app = app()
    app.mainloop()
