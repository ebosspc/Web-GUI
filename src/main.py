# Import necessary libraries
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

# Define a function to run ping, tracert, and nslookup commands on a target site
def do_command(command):
    global command_textbox, url_entry

    # Grab the url entry, format it, and set it to localhost if the user doesn't enter anything
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # Set the url to localhost
        url_val = "::1"
    url_val = " " + str(url_val) # Newly formatted string
    
    # Inform the user the command is working
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    # Run the inputted command based on the user's inputs
    p = subprocess.Popen(command + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get results and errors
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)


# Define a function to save the scrolling text widget output
def mSave():
    filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
    if filename is None:
        return
    file = open (filename, mode = 'w')
    text_to_save = command_textbox.get("1.0", tk.END)

    file.write(text_to_save)
    file.close()


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

# Add a button to save the outputted text in a specificed document
save_btn = tk.Button(frame, text="Save output",command=lambda:mSave())
save_btn.pack()

# Creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# Decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("Times", 14),
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

# Repack the frame
frame = tk.Frame(root,  bg="black") # Change frame color
frame.pack()

# Make the GUI persistent
root.mainloop()