import os
import tkinter as tk
from tkinter import filedialog
from bg_remover import remove_background
from directory_works import select_folder

if __name__ == "__main__":
    source_dir = select_folder("Select Source Image Directory")

    image_files = os.listdir(source_dir)
    for file_name in image_files:
        image_path = os.path.join(source_dir, file_name)
        save_dir = remove_background(image_path, source_dir)
        if save_dir:
            print(f"Background-removed image saved at: {save_dir}")