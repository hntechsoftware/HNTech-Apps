import tkinter as tk
from tkinter import ttk
import tkinter

#Initialize Window
window = tk.Tk()
window.title("PixelArt")
window.geometry("500x300")
window['background']='#c7e5fc'
window.resizable(True,True)

#Define Framebuild

def print_dict_to_text_box(dict, usertext):
  usertext.delete(1.0, tk.END)
  for key, value in dict.items():
    if value == 0 or value == 1:
      usertext.insert('end', f'{value}')

def change_button_color(button, button_colors):
    global usertext
    # Get the current button color
    current_color = button_colors[button]

    # If the button is white (0), turn it black (1)
    if current_color == 0:
        button.config(bg="black")
        button_colors[button] = 1

    # If the button is black (1), turn it white (0)
    elif current_color == 1:
        button.config(bg="white")
        button_colors[button] = 0
    print_dict_to_text_box(button_colors, usertext)



def copy_text_to_clipboard(usertext):
    # Get the text from the text box
    text = usertext.get('1.0', 'end-1c')

    # Copy the text to the clipboard
    window.clipboard_append(text)


def framebuild():
    global usertext
    rows = int(height.get())
    columns = int(width.get())
    framewindow = tk.Toplevel()

    # Create a dictionary to store the button colors
    button_colors = {}

    for i in range(rows):
        for j in range(columns):
            button = tk.Button(framewindow, width=2, height=1, bg="white")
            columnnew = j + 1

            # Store the button color in the dictionary
            button_colors[button] = 0

            # Add a click event to the button
            button.config(command=lambda button=button: change_button_color(button, button_colors))

            # Place the button on the grid
            button.grid(row=i, column=columnnew)
            
    usertext = tk.Text(width = columns, height = rows)
    usertext.grid(row=0,column=1,rowspan=5,padx=30)
    printcode = tk.Button(text="Copy to Clipboard", bg="grey",fg="white",command=lambda: copy_text_to_clipboard(usertext))
    printcode.grid(row = 6, column =1)
    #Add Scrollbar
    sb = tk.Scrollbar(
        window,
        orient=tk.VERTICAL,
        activebackground="blue",
        troughcolor="blue",
        )
    usertext.config(yscrollcommand=sb.set)
    sb.config(command=usertext.yview)
    sb.grid(row=0,column=2,rowspan=5,sticky="NSW")
            


#Framebuild end

#Initialize Widgets

fontstyle = ("Candara", 20)

greetext = tk.Label(
    text="Welcome to PixelArt",
    fg="black",
    bg="#c7e5fc"
    )
greetext.configure(font = fontstyle)
greetext.grid(row=0,column=0)

widthtext = tk.Label(
    text="Select Width:",
    fg="black",
    bg="#c7e5fc"
    )
widthtext.grid(row=1,column=0,pady=5)
width = ttk.Spinbox(
    from_=0,
    to=30,
    wrap=True)
width.grid(row=2,column=0)

heighttext = tk.Label(
    text="Select Height:",
    fg="black",
    bg="#c7e5fc"
    )
heighttext.grid(row=3,column=0,pady=5)
height = ttk.Spinbox(
    from_=0,
    to=30,
    wrap=True)
height.grid(row=4,column=0,pady=10)
new = tk.Button(
    text="Generate",
    fg="white",
    bg="grey",
    command=framebuild,
    )
new.grid(row=5,column=0,pady=10)



window.mainloop()
    
