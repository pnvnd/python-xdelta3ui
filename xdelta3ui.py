# pip install pyinstaller
# Windows Freeze: Run > cmd > pyinstaller --onefile --noconsole xdelta3ui.py

import os
import subprocess
from subprocess import CREATE_NO_WINDOW
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Apply Patch
def patch():
    global path_patch
    path_patch = filedialog.askopenfilename()
    textbox_patch.config(text=path_patch)

def source():
    global path_source
    path_source = filedialog.askopenfilename()
    textbox_source.config(text=path_source)

def apply_patch():
    patched_file = os.path.splitext(path_source)[0] + "_patched" + os.path.splitext(path_source)[1]
    subprocess.run(["xdelta3", "-d", "-s", path_source, path_patch, patched_file], creationflags=CREATE_NO_WINDOW)
    popup = tk.Tk()
    popup.wm_title("Operation Completed!")
    popup_label = ttk.Label(popup, text="File patched successfully and saved at \n" + patched_file)
    popup_label.pack(side="top", fill="x", pady=10)
    popup_button = ttk.Button(popup, text="OK", command = popup.destroy)
    popup_button.pack()
    popup.mainloop()

# Create Patch
def original():
    global path_original
    path_original = filedialog.askopenfilename()
    textbox_original.config(text=path_original)

def modified():
    global path_modified
    path_modified = filedialog.askopenfilename()
    textbox_modified.config(text=path_modified)

def create_patch():
    patch_file = os.path.splitext(path_modified)[0] + "_patch.xdelta"
    subprocess.run(["xdelta3", "-f", "-e", "-s", path_original, path_modified, patch_file], creationflags=CREATE_NO_WINDOW)
    popup = tk.Tk()
    popup.wm_title("Operation Completed!")
    popup_label = ttk.Label(popup, text="Patch created successfully and saved at \n" + patch_file)
    popup_label.pack(side="top", fill="x", pady=10)
    popup_button = ttk.Button(popup, text="OK", command = popup.destroy)
    popup_button.pack()
    popup.mainloop()

# intializing the window
window = tk.Tk()
window.title("xdelta UI")

# configuring size of the window 
window.geometry("350x200")

label = tk.Label(window, text = "xdelta User Interface")
label.pack(side=tk.TOP)

#Create Tab Control
TAB_CONTROL = ttk.Notebook(window)
TAB1 = ttk.Frame(TAB_CONTROL)
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.pack(expand = 1, fill ="both")

#Tab1
TAB_CONTROL.add(TAB1, text="Apply Patch")
TAB_CONTROL.add(TAB2, text="Create Patch")

# Patch
label_patch = ttk.Label(TAB1, text="Patch:")
label_patch.grid(row=0, column=0, columnspan=6, sticky="news")

textbox_patch = ttk.Label(TAB1, text="Please select a path...                    ", borderwidth=2, relief="groove")
textbox_patch.grid(row=1, column=0, columnspan=5, sticky="news")

button_patch = ttk.Button(TAB1, text="Browse", command = patch)
button_patch.grid(row=1, column=5, sticky="e")

# Source
label_source = ttk.Label(TAB1, text="Source:")
label_source.grid(row=2, column=0, columnspan=6, sticky='news')

textbox_source = ttk.Label(TAB1, text="Please select a path...                    ", borderwidth=2, relief="groove")
textbox_source.grid(row=3, column=0, columnspan=5, sticky="news")

button_source = ttk.Button(TAB1, text="Browse", command = source)
button_source.grid(row=3, column=5, sticky="news")

# Execute Command
button_apply = ttk.Button(TAB1, text="Patch", command = apply_patch)
button_apply.grid(row=4, column=0, sticky="W")

#Tab2


# Original
label_original = ttk.Label(TAB2, text="Original File:")
label_original.grid(row=0, column=0, columnspan=6, sticky="news")

textbox_original = ttk.Label(TAB2, text="Please select a path...                    ", borderwidth=2, relief="groove")
textbox_original.grid(row=1, column=0, columnspan=5, sticky="news")

button_original = ttk.Button(TAB2, text="Browse", command = original)
button_original.grid(row=1, column=5, sticky="e")

# Modified
label_modified = ttk.Label(TAB2, text="Modified File:")
label_modified.grid(row=2, column=0, columnspan=6, sticky='news')

textbox_modified = ttk.Label(TAB2, text="Please select a path...                    ", borderwidth=2, relief="groove")
textbox_modified.grid(row=3, column=0, columnspan=5, sticky="news")

button_modified = ttk.Button(TAB2, text="Browse", command = modified)
button_modified.grid(row=3, column=5, sticky="news")

# Execute Command
button_create = ttk.Button(TAB2, text="Patch", command = create_patch)
button_create.grid(row=4, column=0, sticky="W")

#Calling Main()
window.mainloop()
