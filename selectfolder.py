#Import the tkinter module
import tkinter as tk
from tkinter import filedialog

def choosefolder():
    #Choose folder
    root = tk.Tk()
    root.withdraw()

    folder_path=filedialog.askdirectory()

    return folder_path
