import os
import tkinter as tk
from tkinter import filedialog

def select_folder(title):
    root = tk.Tk()
    root.withdraw()
    source_dir = filedialog.askdirectory(title=title)
    return source_dir

def create_directory(source_dir):
    save_dir = os.path.join(source_dir, "Background_Removed")
    os.makedirs(save_dir, exist_ok=True)
    return save_dir
