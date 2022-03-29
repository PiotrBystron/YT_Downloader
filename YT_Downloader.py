#from tkinter import *
#from ast import Str
from tkinter import Entry, Label, CENTER, Text, Menu
import tkinter as tk
#from turtle import left
from pytube import YouTube
import keyboard
import youtube_dl


root = tk.Tk()
root.title("YouTube Downloader")
#root.geometry("310x190")
root.geometry("310x210")
root.resizable(False, False)

Entry1 = Text(root, font=("haveltica 15 bold"), bd=2)

quality = "360p" #Default quality
#download_folder = "D:\aaa" #Default download folder -> D:\aaa
download_folder = "" #Default download folder ( location of the .py file )

#------------------- right mouse context menu -------------------
def cut_text():
        Entry1.event_generate(("<<Cut>>"))

def copy_text():
        Entry1.event_generate(("<<Copy>>"))

def paste_text():
        Entry1.event_generate(("<<Paste>>"))

def paste_dl():
        Entry1.event_generate(("<<Paste>>"))
        keyboard.send("enter")

def select_all():
        Entry1.event_generate('<Control-a>')     

menu = Menu(root, tearoff = 0) 
menu.add_command(label="Paste & Download", command=paste_dl)
menu.add_command(label="Sellect All", command=select_all) 
menu.add_command(label="Cut", command=cut_text) 
menu.add_command(label="Copy", command=copy_text) 
menu.add_command(label="Paste", command=paste_text)
menu.add_separator()
menu.add_command(label="Exit", command=root.destroy)

# context menu on right button click 
def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()        
#-------------------------------------------------

def Submit(wideo):
    try:
        wideo = str(Entry1.get())
        print(wideo)
        Entry1.delete(0, "end")
        yt = YouTube(wideo)
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length//60, "min", yt.length%60, "sec")

        if quality == "opus":
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([wideo])

        else:    
            ys = yt.streams.get_by_resolution(resolution = quality)
            print("Downloading...")        
            ys.download(output_path = download_folder)

        print("Download completed!!")
        Label2.config(text = "Download completed!!")
        Label3.config(text = yt.title)

    except:
        print("Download ERROR!!")
        Label2.config(text = "Download ERROR!!")
        Label3.config(text = yt.title)

def ShowChoice():
    global quality 
    quality = v.get()
    print(quality)


Label1 = Label(root, text =
"""YouTube  LINK: 
(press Enter to download)""",)
Label1.pack()

Entry1 = Entry(root, bd=2, width=50, justify=CENTER,)
Entry1.focus()
Entry1.pack()
Entry1.bind('<Key-Return>', Submit)


v = tk.StringVar()
value = tk.StringVar()

YT_quality = [
    #("144p", "144p"),
    #("240p", "240p"),
    ("360p", "360p"),
    #("480p", "480p"),
    ("720p", "720p"),
    #("1080p", "1080p"),
    ("Audio", "opus"),
    ]

tk.Label(root, text =
"""Choose quality:""",
         pady = 5,).pack()

for YT_quality, val in YT_quality:
    tk.Radiobutton(root, 
                   text = YT_quality,
                   padx = 20,
                   width = 5, 
                   variable = v, 
                   command = ShowChoice,
                   indicatoron = 0,
                   value = val,
                   ).pack(anchor = CENTER)

v.set(quality)  # initializing the choice
value.set(quality) # initializing the choice

# Download completed / Download ERROR 
Label2 = Label(root, text = "", pady = 2,)
Label2.pack()

# title of the downloaded video
Label3 = Label(root, text = "", pady = 2,)
Label3.config(font = ("Arial", 8), anchor = "w")
Label3.pack()


root.bind("<Button-3>", context_menu)
root.mainloop()