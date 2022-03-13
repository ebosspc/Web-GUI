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

# Set up the ping button
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"))
ping_btn.pack()

# Set up the tracert button
tracert_btn = tk.Button(frame, text="Check how long it takes to access that URL", command=lambda:do_command("tracert"))
tracert_btn.pack()

#Set up the nslookup button
nslookup_btn = tk.Button(frame, text="See the site's IP address", command=lambda:do_command("nslookup"))
nslookup_btn.pack()

# Creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# Decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # Change font
url_entry.pack(side=tk.LEFT)

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

frame = tk.Frame(root,  bg="black") # Change frame color
frame.pack()

# Make the GUI persistent
root.mainloop()