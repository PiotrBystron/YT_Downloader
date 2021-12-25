#from tkinter import *
from tkinter import Entry, Label, CENTER
import tkinter as tk
from pytube import YouTube

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("350x250")
root.resizable(False, False)

#global Entry1
quality = "360p" # Domyślna jakość
#download_folder = "D:\Pobrane Pliki" # Domyślny folder pobierania
download_folder = "" # Domyślny folder pobierania ( tam gdzie plik .py )

def Submit(wideo):
    #print("Downloading...")
    #Label2.config(text="Downloading...")

    try:
        wideo = str(Entry1.get())
        print(wideo)
        Entry1.delete(0, "end")

        yt = YouTube(wideo)
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length//60, "min", yt.length%60, "sec")
        ys = yt.streams.get_by_resolution(resolution = quality)
        print("Downloading...")
        ##ys.download(output_path = "V:")
        ys.download(output_path = download_folder)
        print("Download completed!!")
        Label2.config(text = "Download completed!!")

    except:
        print("Download ERROR!!")
        Label2.config(text = "Download ERROR!!")
        
def ShowChoice():
    global quality 
    quality = v.get()
    print(quality)


Label1 = Label(root, 
            text =
"""YouTube  LINK: 
(press Enter to download)""",
            )
#Label1.pack(side = LEFT)
Label1.pack()

Entry1 = Entry(root,
            bd=5,
            width=52,
            )
#Entry1.pack(side = RIGHT)
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
    ]


tk.Label(root, 
         text =
"""Choose quality:""",
         #justify = tk.LEFT,
         pady = 15,
         ).pack()

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

Label2 = Label(root, 
            text = "",
            pady = 5,
            )
Label2.pack()

# L3 = Label( root, 
#             text="Location: ",
#             )
# L3.pack(side = LEFT)

# E2 = Entry( root,
#             bd =5,
#             width=50,
#             )
# E2.pack(side = RIGHT)
# E2.insert(0,"D:\Pobrane Pliki")

root.mainloop()