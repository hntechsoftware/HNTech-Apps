#ScratchPad code

#Import necessary modules
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.colorchooser import askcolor
import keyword
import re
from tkinter.messagebox import askyesno
from tkinter import messagebox
import autocorrect
from tkinter import font as tkfont
from tkinter import simpledialog
import os
import sys
from tkhtmlview import HTMLLabel
import markdown
import webbrowser
import ctypes
import ttkbootstrap as tb
from ttkbootstrap.dialogs.dialogs import FontDialog
from ttkbootstrap.toast import ToastNotification
ctypes.windll.shcore.SetProcessDpiAwareness(3) 
 

#Initialize scratchpadwindow
scratchpadwindow = tb.Window(themename="cerculean")
scratchpadwindow.title("ScratchPad")
scratchpadwindow.geometry("700x700")
scratchpadwindow['background']='#FFFFFF'
scratchpadwindow.resizable(True,True)

scratchpadwindow.tk.call('tk', 'scaling', 2.5)
 
photo = PhotoImage(file = "src/logo1.png")
scratchpadwindow.iconphoto(False, photo)

#init variables
syntax_highlighting_enabled = False
is_on = False

#Define markdown view
def preview_markdown(markdown_text):
    filecontent = markdown.markdown(markdown_text)
    with open("temp/mdarchive.html","w") as mda:
        mda.write(filecontent)
    newwin = tk.Toplevel()
    with open("temp/mdarchive.html","r") as lotr:
        contents = lotr.read()
    webframe = HTMLLabel(newwin, html=contents)
    webframe.configure(width=250,height=450)
    webframe.grid(row=1,column=0,sticky="NSEW")
    toast = ToastNotification(
        title="Markdown Preview",
        message="Markdown Preview Window successfully loaded.",
        duration=3000,
    )
    toast.show_toast()

#Test Reigon
def open_font():
	# Define Font Dialog
	fd = FontDialog()
	# Show the box
	fd.show()
	# Capture The Reult fd.result and update label
	usertext.config(font=fd.result)

# Example usage: pass the markdown text from another Text widget
def onyourmarks():
    markdown_text = usertext.get(1.0,tk.END)
    markdown_text = markdown_text.replace("→", ">")
    preview_markdown(markdown_text)

savearea = "temp/Notes.txt"

def customoutputdir():
    #Custom output dir for autosave
    global savearea
    outputdir = tk.filedialog.askdirectory()
    savearea = outputdir + "/ScratchPad-Notes.txt"

def arrow(event):
    usertext.insert(tk.INSERT,"→")



#Define Autosave
def autosave(event=None):
    if is_on is True:
        text_file = open(savearea, "w")
        filecontent = usertext.get(1.0,tk.END)
        filecontent = filecontent.replace("→", ">")
        text_file.write(filecontent)
        text_file.close()
#Define the open function
def open_file():

    """Open a file for editing."""

    filepath = askopenfilename(

        filetypes=[("Text Files", "*.txt"),("Python Files", "*.py"), ("All Files", "*.*")]

    )

    if not filepath:

        return

    usertext.delete("1.0", tk.END)

    with open(filepath, mode="r", encoding="utf-8") as input_file:

        text = input_file.read()

        usertext.insert(tk.END, text)

    scratchpadwindow.title(f"ScratchPad - {filepath}")
    toast = ToastNotification(
        title="File",
        message="File has been opened in the Editor Window.",
        duration=3000,
    )
    toast.show_toast()
#Define save function
def save_file():

    """Save the current file as a new file."""

    filepath = asksaveasfilename(

        defaultextension=".txt",

        filetypes=[("Text File", "*.txt"),("Markdown file", "*.md"),("Rich Text File", "*.rtf"),("Python File", "*.py"), ("All Files", "*.*")],

    )

    if not filepath:

        return

    with open(filepath, mode="w", encoding="utf-8") as output_file:

        text = usertext.get("1.0", tk.END)
        text = text.replace("→", ">")
        output_file.write(text)

    scratchpadwindow.title(f"ScratchPad - {filepath}")

#Closecode
def closecode():
    answer = askyesno(title='Confirmation',message='Do you want to Save before closing?')
    if answer:
        closecode11()
    else:
        scratchpadwindow.destroy()

def closecode11():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt"),("Markdown file", "*.md"),("Rich Text File", "*.rtf"),("Python File", "*.py"), ("All Files", "*.*")],)
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = usertext.get("1.0", tk.END)
        output_file.write(text)
    scratchpadwindow.destroy()

#Define the Customize function
def customize():
    colors = askcolor(title="Change Textbox colour")
    usertext.configure(bg=colors[1])
    colors2 = askcolor(title="Change Text colour")
    usertext.config(foreground=colors2[1])
#Define close
def close():
    closecode()

    
def quickrun():
    qrunfile = open("temp/qruncodec.py","w")
    qrunfile.write("import os")
    qrunfile.close()
    qrunfile = open("temp/qruncodec.py","a")
    qrunfile.write("\n")
    qruncode = usertext.get(1.0,tk.END)
    qrunfile.write(qruncode)
    qrunfile.close()
    qrunfile = open("temp/qruncodec.py","a")
    qrunfile.write("\n")
    qrunfile.write("os.system('pause')")
    qrunfile.close()
    toast = ToastNotification(
        title="Python Code Preview",
        message="Python code executed for preview. (Note: It will not work if the file has dependencies.)",
        duration=3000,
    )
    
    result = os.system("python temp/qruncodec.py")
    if result != 0:
        messagebox.showerror("Error","A problem occured")
    else:
        messagebox.showinfo("Task Preview","Code ran sucessfully.")
    toast.show_toast()
        
#define WordCount function
def wordcount():
    text = usertext.get("1.0", "end")
    num_characters = len(text) - 1
    num_words = len(text.split())
    num_lines = len(text.splitlines())
    messagebox.showinfo("Word Count", f"Total characters: {num_characters}\n Total words: {num_words}\n Total lines: {num_lines}")

#Print function
def print_file():
   with open("temp/printarchive.txt",mode="w") as pr:
       filecontent = usertext.get(1.0,tk.END)
       pr.write(filecontent)
       pr.close()
   file = os.path.abspath("temp/printarchive.txt") 
   if file:
      if sys.platform == "win32":
        import win32api
        os.startfile(file, "print")
      else:
        import cups
        import cupshelpers

        # Create a new connection and the list of available printers
        connection = cups.Connection()
        printers = cupshelpers.getPrinters(connection)

        # Select the first printer in the list...
        for p in printers:
            if p is not None:
                printer = printers[p]
                break

        # ...and print to it
        printer.connection.printFile(
            p,
            file,
            "Test this printer",
            {}
        )

#Define the .grid() sizes
scratchpadwindow.columnconfigure(0, weight=1)
scratchpadwindow.rowconfigure(0, weight=1, uniform=1)
scratchpadwindow.columnconfigure(1, weight=1)
#Init_Menubar
menubar = Menu(scratchpadwindow)
scratchpadwindow.config(menu=menubar)

#Code for the CodeMode dropdowns
langs = tk.Menu(menubar, tearoff=False)
langs.add_command(label="Toggle Python Syntax Highlight ",command=lambda: toggle_syntax_highlighting())
langs.add_command(label="Execute Python Code",command=quickrun)

optmenu = tk.Menu(menubar, tearoff=False)
optmenu.add_command(label="Print File",command=print_file)
optmenu.add_command(label="Word Count",command=wordcount)
optmenu.add_command(label="Preview as Markdown",command= onyourmarks)
optmenu.add_command(label="Change AutoSave Output Directory",command= customoutputdir)

#Add menubar
menubar.add_command(label="Open",command=open_file)
menubar.add_command(label="Save",command=save_file)
menubar.add_cascade(label="CodeMode", menu=langs)
menubar.add_command(label="Customize",command=customize)
menubar.add_cascade(label="Options",menu=optmenu)
menubar.add_command(label="Close",command=close)

#Create Sizegrip
sg = ttk.Sizegrip(scratchpadwindow)
sg.grid(row=2,column=3, sticky="SE")

#Create the tk text
usertext = tk.Text(undo=True,wrap="word")
#textFont = ("Helvetica", 12)
#usertext.config(font=textFont)
usertext.grid(row=0, column=0, sticky="nsew",columnspan=3)

#Bind Arrow function
usertext.bind("<F9>", arrow)

#Add Scrollbar
sb = tk.Scrollbar(
    scratchpadwindow,
    orient=VERTICAL,
    activebackground="blue",
    troughcolor="blue",
    )
usertext.config(yscrollcommand=sb.set)
sb.config(command=usertext.yview)
sb.grid(row=0,column=3,sticky="NSW")

currentfont = None

def slider_changed(event):
  global currentfont
  textsize = slider.get()
  size2 = round(textsize)
  wefont = currentfont
  new_font = (wefont, size2)
  usertext.configure(font=new_font)


    

#CODE FOR SCALEBAR
current_value = tk.DoubleVar()
style = ttk.Style()
# Create a new style with a blue background for the slider
style.configure('Custom.Horizontal.TScale', background='#c7e5fc')
slider = ttk.Scale(
    scratchpadwindow,
    from_=10,
    to=30,
    orient='horizontal',
    style='Custom.Horizontal.TScale',
    variable=current_value,
    command=slider_changed
)
slider.grid(row=2,column=0)
slider.set(12)

#Bind scratchpadwindowclose to savefunction
scratchpadwindow.protocol("WM_DELETE_WINDOW",closecode)

#CODE FOR FONT DEF FUNCTIONS

def helvetica():
    global currentfont
    helFont = ("Helvetica", round(slider.get()))
    usertext.config(font=helFont)
    currentfont = "Helvetica"
def Courier():
    global currentfont
    cFont = ("Courier New", round(slider.get()))
    usertext.config(font=cFont)
    currentfont = "Courier New"
def tnr():
    global currentfont
    tFont = ("Times New Roman", round(slider.get()))
    usertext.config(font=tFont)
    currentfont = "Times New Roman"
def calibri():
    global currentfont
    calFont = ("Calibri", round(slider.get()))
    usertext.config(font=calFont)
    currentfont = "Calibri"
def ael():
    global currentfont
    aelFont = ("Comic Sans MS", round(slider.get()))
    usertext.config(font=aelFont)
    currentfont = "Comic Sans MS"
def customfont():
    global currentfont
    new1font = simpledialog.askstring("Font","Enter the name of a font stored on this computer:")
    try:
        cusFont = (new1font, round(slider.get()))
        usertext.config(font=cusFont)
        currentfont = new1font
    except Exception:
        messagebox.showerror("Error","ERROR: Font not found.")

#Set default starting font
helvetica()

sliderguide = tk.Label(
    text = "Text Size:",
    bg="#c7e5fc",
    fg="grey",
    )
sliderguide.grid(row=1,column=0)
#CODE FOR SCALEBAR END


#CODE FOR FONT ADJUSTMENT
# Create a new style for the ttk.menubutton
style = ttk.Style()
style.configure('Custom.Menubutton', background='#03d3fc', foreground='grey')

#TEST
style.map('TMenubutton', background=[('pressed', '#03d3fc'), ('active', '#03d3fc')], foreground=[('pressed', 'white'), ('active', 'white')])
#TEST

font = tk.Menu(scratchpadwindow, tearoff=False)
# Add some items to the menu
font.add_command(label='Helvetica',command=helvetica )
font.add_command(label='Courier New',command=Courier )
font.add_command(label='Times New Roman',command=tnr )
font.add_command(label='Calibri',command=calibri )
font.add_command(label='Comic Sans MS',command=ael )
font.add_command(label='Select Font...',command=open_font )
font.add_command(label='Use Custom Font...',command=customfont )
# Create a menubutton widget
fontmenu = ttk.Menubutton(scratchpadwindow, menu=font, text='Adjust Font')
fontmenu.grid(row=2, column=1, sticky="NSEW")


fontguide = tk.Label(
    text = "Font:",
    bg="#c7e5fc",
    fg="grey",
    )
fontguide.grid(row=1,column=1)
#CODE FOR FONT ADJUSTMENT END

#CODE FOR AUTOSAVE
# Keep track of the button state on/off

# Define our switch function
def switch():
    global is_on
    # Determine is on or off
    if is_on:
        on_button.config(text="Disabled")
        on_button.config(bg="#0044b3")
        on_button.config(fg="#bad1ff")
        is_on = False
    else:
        on_button.config(text="Enabled")
        on_button.config(bg="#99c0ff")
        on_button.config(fg="#002b80")
        is_on = True

# Create A Button
on_button = tk.Button(
    scratchpadwindow,
    bd = 0,
    command = switch,
    text="Disabled",
    bg="#0044b3",
    fg="white",
    )
on_button.grid(row=2,column=2,padx=5)
saveguide = tk.Label(
    text = "AutoSave:",
    bg="#c7e5fc",
    fg="grey",
    )
saveguide.grid(row=1,column=2)
#CODE FOR AUTOSAVE END

#CODE FOR AUTOSAVE2
usertext.bind('<Any-KeyRelease>', autosave)
#CODE FOR AUTOSAVE2 END


#Bind the CodeEditor
# Extended the keywords dictionary to include built-in functions.
keywords = {k: 'orange' for k in keyword.kwlist}
keywords['print'] = 'orange'
keywords['input'] = 'orange'
keywords['int'] = 'orange'
keywords['bin'] = 'orange'
keywords['exec'] = 'orange'
keywords['float'] = 'orange'
keywords['True'] = 'orange'
keywords['id'] = 'orange'
keywords['len'] = 'orange'
keywords['range'] = 'orange'

#Define colours
syntax_colors = {
    'comment': 'grey',
    'string': 'green',
    'keyword': 'orange',
    'number': 'blue',
}


#define syntax coloring
def tag_keywords(event):
    for keyword, color in keywords.items():
        start = "1.0"
        while True:
            pos = usertext.search(r'\m{}\M'.format(keyword), start, stopindex=tk.END, regexp=True)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            usertext.tag_add("keyword", pos, end)
            start = end        
        usertext.tag_config("keyword", foreground=syntax_colors['keyword'])

def tag_comments(event):
    usertext.tag_configure("comment", foreground=syntax_colors['comment'])
    start = "1.0"
    while True:
        start = usertext.search("#", start, stopindex=tk.END)
        if not start:
            break
        end = usertext.search("\n", start, stopindex=tk.END)
        if not end:
            end = tk.END
        usertext.tag_add("comment", start, end)
        start = end

def tag_strings(event):
    usertext.tag_configure("string", foreground=syntax_colors['string'])
    start = "1.0"
    while True:
        start = usertext.search(r'[rR]?[bB]?"[^"\\]*(\\.[^"\\]*)*"', start, stopindex=tk.END, regexp=True)
        if not start:
            break
        end = usertext.search('"', start+"+1c", stopindex=tk.END, regexp=True)
        if not end:
            end = tk.END
        usertext.tag_add("string", start, end+"+1c")
        start = end

    start = "1.0"
    while True:
        start = usertext.search(r"[rR]?[bB]?'[^'\\]*(\\.[^'\\]*)*'", start, stopindex=tk.END, regexp=True)
        if not start:
            break
        end = usertext.search("'", start+"+1c", stopindex=tk.END, regexp=True)
        if not end:
            end = tk.END
        usertext.tag_add("string", start, end+"+1c")
        start = end

def tag_numbers(event):
    usertext.tag_configure("number", foreground=syntax_colors['number'])
    text_string = usertext.get("1.0", tk.END)
    for match in re.finditer(r"\b\d+\b", text_string):
        start, end = match.span()
        usertext.tag_add("number", f"1.0 + {start} chars", f"1.0 + {end} chars")


def tag_all(event=None):
    tag_keywords(event)
    tag_numbers(event)  # tag numbers
    tag_comments(event)  # comments should be tagged middle
    tag_strings(event)



def toggle_syntax_highlighting():
    global syntax_highlighting_enabled

    # Toggle the state of the syntax highlighting toggle.
    syntax_highlighting_enabled = not syntax_highlighting_enabled

    # If syntax highlighting is enabled, highlight the text in the text box.
    # Otherwise, un-highlight the text in the text box.
    if syntax_highlighting_enabled:
        usertext.bind('<Any-KeyRelease>', tag_all)
    else:
        tags = usertext.tag_names()
        # Remove all the tags from the text box.
        for tag in tags:
            usertext.tag_remove(tag, "1.0", "end")
        usertext.unbind('<Any-KeyRelease>')


#Mainloop
scratchpadwindow.mainloop()

