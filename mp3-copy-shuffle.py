#!/usr/bin/env python3

"""
Copies and Shuffles MP3 Files For Download to MP3 Player
Author: @edurso
"""


import os
import random
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import filedialog


def copy_mp3_files(src_dir, dest_dir):
    mp3_files = [f for f in
                 [os.path.abspath(os.path.join(root_path, file)) for root_path, dirs, files in os.walk(src_dir) for file
                  in files] if f.lower().endswith('.mp3')]
    random.shuffle(mp3_files)

    for src_path in mp3_files:
        filename = Path(src_path).name
        dest_path = os.path.join(dest_dir, filename)
        shutil.copy2(src_path, dest_path)


def get_directory():
    return filedialog.askdirectory()


def on_copy_button_click():
    source_directory = Path(source_entry.get())
    destination_directory = Path(destination_entry.get())

    if source_directory and destination_directory:
        if len(os.listdir(destination_directory)) > 0:
            status_label.config(text="Copy cannot be executed, please copy into empty directory.")
        else:
            status_label.config(text="Copy in progress.")
            copy_mp3_files(source_directory, destination_directory)
            status_label.config(text="Copy completed.")
    else:
        status_label.config(text="Please select source and destination directories.")


if __name__ == '__main__':
    # Main Window
    root = tk.Tk()
    root.title("MP3 Copy Utility")
    source_frame = tk.Frame(root)
    source_frame.pack(pady=10)

    # Components
    source_label = tk.Label(source_frame, text="Source Directory:")
    source_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    source_entry = tk.Entry(source_frame, width=40)
    source_entry.grid(row=0, column=1, padx=5, pady=5)

    source_browse_button = tk.Button(source_frame, text="Browse",
                                     command=lambda: source_entry.insert(tk.END, get_directory()))
    source_browse_button.grid(row=0, column=2, padx=5, pady=5)

    destination_frame = tk.Frame(root)
    destination_frame.pack(pady=10)

    destination_label = tk.Label(destination_frame, text="Destination Directory:")
    destination_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    destination_entry = tk.Entry(destination_frame, width=40)
    destination_entry.grid(row=0, column=1, padx=5, pady=5)

    destination_browse_button = tk.Button(destination_frame, text="Browse",
                                          command=lambda: destination_entry.insert(tk.END, get_directory()))
    destination_browse_button.grid(row=0, column=2, padx=5, pady=5)

    copy_button = tk.Button(root, text="Copy", command=on_copy_button_click)
    copy_button.pack(pady=10)

    status_label = tk.Label(root, text="")
    status_label.pack()

    # Run the GUI
    root.mainloop()
