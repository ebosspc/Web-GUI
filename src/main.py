# Import necessary libraries
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

# Define a function to do a specied command
def do_command():
    subprocess.call("ping localhost")

# Add a frame
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Set up button to run the do_command function
ping_btn = tk.Button(frame, text="ping", command=do_command)
ping_btn.pack()

# Make the GUI persistent
root.mainloop()