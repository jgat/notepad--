#!/usr/bin/env python
"""Notepad-- : A very simple text editor."""

import sys
if sys.version_info < (3,):
    import Tkinter as tk
    import tkFileDialog as filedialog
else:
    import tkinter as tk
    from tkinter import filedialog

def create_gui(root):
    """Set up the GUI and functionality."""
    root.title("Notepad--")
    textbox = tk.Text(root)
    textbox.pack(expand=True, fill=tk.BOTH)

    # Functionality for opening and saving files.
    def open_file():
        """Open a file"""
        f = filedialog.askopenfile()
        if f:
            textbox.delete(1.0, tk.END)
            textbox.insert(tk.END, f.read())
            f.close()

    def save_file():
        """Save a file"""
        f = filedialog.asksaveasfile()
        if f:
            f.write(textbox.get(1.0, tk.END)[:-1])
            f.close()

    # Set up the command buttons
    frame = tk.Frame(root)
    frame.pack()
    tk.Button(frame, text="Open", command=open_file).pack(side=tk.LEFT)
    tk.Button(frame, text="Save", command=save_file).pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    create_gui(root)
    root.mainloop()
