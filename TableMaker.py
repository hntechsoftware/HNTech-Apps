import tkinter as tk
from PIL import ImageGrab
from PIL import Image
import pyautogui
import pygetwindow
import os
import time




def capture_window():
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = window.winfo_height()    #get details about window
    takescreenshot = ImageGrab.grab(bbox=(x, y, width, height))
    takescreenshot.save("Tablemaker.png")
    message.grid(row = rows + 2,column = 0)
    message2.grid(row = rows + 3,column = 0)
    message3.grid(row = rows + 4, column = 0)

def saveImage():
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    height = rows * 9
    width = columns * length
    height2 = window.winfo_screenheight()
    width2 = window.winfo_screenwidth()
    print(height, width)
    print(height2, width2)
    img = ImageGrab.grab(bbox=(x,y,x + width2,y + height2))
    img.show()

def imagesave():
    download_folder = os.path.expanduser("~")+"/Downloads/table.png"
    path = download_folder
    title = pygetwindow.getWindowsWithTitle("TableMaker by HNTech: " + name)[0]
    left, top = title.topleft
    right, bottom = title.bottomright
    pyautogui.screenshot(path)
    im = Image.open(path)
    im = im.crop((left+10, top+50, right-160, bottom-50))
    im.save(path)
    Thanks = tk.Label(
    text="downloaded",
    foreground="green", 
    background="white" 
    )
    window.rowconfigure(index=0, weight=1)
    window.rowconfigure(index=rows+2,weight=10)
    Thanks.grid(row=rows+2, column = columns)
    
            

print("Welcome to the INSTANT TABLE MAKER!")
rows = int(input("Specify the number of rows:"))
columns = int(input("Specify the number of columns:"))
length = int(input("How long should each text box be?"))
name = input("Name your table:")

        


window = tk.Tk()
window.title("TableMaker by HNTech: " + name)
textbox = tk.Entry(fg="black", bg="white", width=length)



for i in range(rows):
            for j in range(columns):
                 
                box = tk.Entry(window, width=length, fg='black',
                               font=('Arial',9,'bold'))
                 
                box.grid(row=i, column=j)

            

message = tk.Label(
    text="Table saved in",
    foreground="green", 
    background="white" 
)
message2 = tk.Label(
    text="same folder as",
    foreground="green", 
    background="white" 
)
message3 = tk.Label(
    text="the app file",
    foreground="green", 
    background="white" 
)

                
download = tk.Button(
    text="Download",
    width=10,
    height=1,
    bg="black",
    fg="white",
    command= imagesave,
)
download.grid(row=rows + 1,column= columns)
 



window.mainloop()
