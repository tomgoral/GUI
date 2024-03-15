from tkinter import filedialog as fd

def open_file_selection():
    filetypes = (
        ('xl files', '*.xlsx *.xlsm *.xlsb *.xls'),
        ('json files', '*.json')
                )
    files = fd.askopenfilenames(
        filetypes=filetypes,
        initialdir='/Users/thomasgoral/myCode/finance/portfolios'
    )
    print(files)
    
    
    
def open_from_dialog(self):
        path = tkinter.filedialog.askopenfilename()
        if len(path) > 0:
            self.open(path)   

open_file_selection()
