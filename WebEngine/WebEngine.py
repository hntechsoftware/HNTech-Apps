#WebEngine Code

#IMPORTMODULES
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinterweb import HtmlFrame
from tkinter.colorchooser import askcolor


#INITIALIZEWINDOW
window = tk.Tk()
window.title("WebEngine")
window.geometry("1275x600")
window['background']='#c7e5fc'
window.resizable(True,True)

#INITIALIZE VARIABLES
previouslinks = ["https://skeptichn.github.io/skeptic/"]

#INITIALIZE CANVAS AS TKMENUBAR
C = Canvas(bg="white", height=50, width=1275)
C.grid(row=0,column=0,columnspan=2,sticky="EW")

#DEFINE GEO PARAMETERS
window.grid_columnconfigure(0, weight=1, minsize=1275)  #  is the minimum width
window.grid_rowconfigure(1, weight=1, minsize=500)     #  is the minimum height

#ADDIMAGE
logo = tk.PhotoImage(file="src/webenginelogo.png")
#Add the banner image
banner = tk.Label(image=logo, bg = "white")
banner.place(x=10,y=10)

#DEFINE THE WEB VIEWING FUNCTION
def openlink(event=None):
    url = userlink.get()
    webframe.load_website(url)
    previouslinks.append(url)
#DEFINE THE BACK FUNCTION
def oldlink():
    newurl = previouslinks.pop()
    userlink.delete(0,tk.END)
    userlink.insert(tk.END,newurl)
    webframe.load_website(newurl)
#DEFINE THE REFRESH FUNCTION
def refresh():
    lastlink = previouslinks[-1]
    webframe.load_website(lastlink)
#DEFINE THE HISTORY FUNCTION
def history():
    global previouslinks
    hist = Toplevel()
    hist.geometry("250x600")
    hist.title("History: WebEngine")
    previouslinks.reverse()
    oldstuff = tk.StringVar(value=previouslinks)
    listbox = tk.Listbox(
        hist,
        listvariable=oldstuff,
        height=6,
        selectmode=tk.EXTENDED)
    listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
    # link a scrollbar to a list
    scrollbar = ttk.Scrollbar(
        hist,
        orient=tk.VERTICAL,
        command=listbox.yview
    )
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)
    def reverselist():
        previouslinks.reverse()
        hist.destroy()
    hist.protocol("WM_DELETE_WINDOW", reverselist)
#DEFINE THE CUSTOMIZE BUTTON
def customize():
    colors = askcolor(title="Change menubar colour")
    C.configure(bg=colors[1])
#DEFINE THE FILE FUNCTION
def loadfile():
    file_dialog = tk.filedialog.askopenfile(title="Select an HTML file", filetypes=[("HTML files", "*.html")])
    if file_dialog is not None:
        webframe.load_file(file_dialog.name)
        userlink.insert(0,file_dialog.name)
        previouslinks.append(file_dialog.name)

#CODE FOR THE ACTIVELOAD OF WEBFRAME: FUNC1
def get_url():
    return webframe.get_url()
#CODE FOR THE ACTIVELOAD OF WEBFRAME: FUNC2
def copy_url():
    url = get_url()
    userlink.delete(0, tk.END)
    userlink.insert(0, url)
#CODE FOR CHANGE SIZE
def phonemode():
    window.config(width=400)


#CODE FOR ENTRYBOX
userlink = tk.Entry(
    width = "35",
    borderwidth = "3",
    fg = "#07328f",
    )
userlink.place(x=150,y=15)
linkfont = ("Arial",15)
userlink.configure(font = linkfont)
userlink.insert(0,"https://skeptichn.github.io/skeptic/")

#CODE FOR SEARCHBUTTON
searchbutton= tk.PhotoImage(file='src/search.png')
searchfilelabel= Label(image=searchbutton)
searchfilebutton= Button(window, image=searchbutton, command=openlink,
borderwidth=0, highlightthickness = 0,bd = 0,bg = "white",activebackground = "white")
searchfilebutton.place(x=560,y=7)

#CODE FOR REWINDBUTTON (USED IN SRC AS REWIND)
backbutton= tk.PhotoImage(file='src/rewind.png')
backfilelabel= Label(image=backbutton)
backfilebutton= Button(window, image=backbutton, command=oldlink,
borderwidth=0, highlightthickness = 0,bd = 0,bg = "white",activebackground = "white")
backfilebutton.place(x=660,y=9)

#CODE FOR REFRESHBUTTON
freshbutton= tk.PhotoImage(file='src/refresh.png')
freshfilelabel= Label(image=freshbutton)
freshfilebutton= Button(window, image=freshbutton, command=refresh,
borderwidth=0, highlightthickness = 0,bd = 0,bg = "white",activebackground = "white")
freshfilebutton.place(x=710,y=9)

#CODE FOR HISTORYBUTTON
historybutton= tk.PhotoImage(file='src/history.png')
historyfilelabel= Label(image=historybutton)
historyfilebutton= Button(window, image=historybutton, command=history,
borderwidth=0, highlightthickness = 0,bd = 0,bg = "white",activebackground = "white")
historyfilebutton.place(x=760,y=9)

#CODE FOR FILEBUTTON
filebutton= tk.PhotoImage(file='src/file.png')
filefilelabel= Label(image=filebutton)
filefilebutton= Button(window, image=filebutton, command=loadfile,
borderwidth=0, highlightthickness = 0,bd = 0,bg = "white",activebackground = "white")
filefilebutton.place(x=860,y=9)

#CODE FOR PHONEBUTTON
phonebutton= tk.PhotoImage(file='src/phone.png')
phonefilelabel= Label(image=phonebutton)
phonefilebutton= Button(window, image=phonebutton, command=phonemode,
borderwidth=0, highlightthickness = 0,bd = 0,bg = "white",activebackground = "white")


#CODE FOR PCBUTTON
pcbutton= tk.PhotoImage(file='src/pc.png')
pcfilelabel= Label(image=pcbutton)
pcfilebutton= Button(window, image=pcbutton, command=history,
borderwidth=0, highlightthickness = 0,bd = 0,bg = "white",activebackground = "white")





#CODE FOR CUSTOMIZE BUTTON
customize = tk.Button(
    text="Customize",
    fg="black",
    bg="white",
    height=1,
    width=10,
    command=customize,
    )
customize.place(x=1200,y=11)

#CODE FOR WEB FRAME
webframe = HtmlFrame(window,messages_enabled = False)
webframe.configure(width=250,height=450)
webframe.grid(row=1,column=0,sticky="NSEW")
#BIND THE CHANGEWEBFRAME TO COPYURL()
webframe.bind("Changed", copy_url)

#BIND ENTER KEY TO SEARCH
window.bind('<Return>', openlink)

#ADD DEFAULT WEBSITE
webframe.load_website("https://skeptichn.github.io/skeptic/")

#MAINLOOP
window.mainloop()



