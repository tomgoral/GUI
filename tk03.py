# Python program to specify the file 
# path in a tkinter file dialog 

# Import the libraries tk, ttk, filedialog 
import tkinter as tk 
from tkinter import ttk 
from tkinter import filedialog as fd 

# Create a GUI app 
app = tk.Tk() 

# Specify the title and dimensions to app 
app.title('Tkinter Dialog') 
app.geometry('600x350') 

# Create a textfield for putting the 
# text extracted from file 
text = tk.Text(app, height=12) 

# Specify the location of textfield 
text.grid(column=0, row=0, sticky='nsew') 

# Create a function to open the file dialog 


def open_text_file(): 

    # Specify the file types 
    filetypes = (('xl files', '*.xlsx *.xlsm *.xlsb *.xls'),
        ('json files', '*.json'))
   
    initialdir = '/Users/thomasgoral/myCode/finance/portfolios'

    # Show the open file dialog by specifying path 
    f = fd.askopenfile(filetypes = filetypes, 
                    initialdir = initialdir) 

    # Insert the text extracted from file in a textfield 
    text.insert('1.0', f.readlines()) 


# Create an open file button 
open_button = ttk.Button(app, text='Open a File', command=open_text_file) 

# Specify the button position on the app 
open_button.grid(sticky='w', padx=250, pady=50) 

# Make infinite loop for displaying app on the screen 
app.mainloop() 
