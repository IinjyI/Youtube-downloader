from tkinter import *
from tkinter import filedialog
from pytube import Playlist, YouTube


def Widgets():

    link_label = Label(root, text="Link :", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Destination :", pady=5, padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)

    root.destinationText = Entry(
        root, width=27, textvariable=download_Path, font="Arial 14"
    )
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_B = Button(root, text="Browse", command=Browse, width=10, relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)

    Download_BP = Button(
        root,
        text="Download Playlist",
        command=DownloadPlaylist,
        width=20,
        pady=10,
        padx=15,
        relief=GROOVE,
        font="Georgia, 13",
    )
    Download_BP.grid(row=4, column=1, pady=10, padx=10)

    Download_BV = Button(
        root,
        text="Download Video",
        command=DownloadVideo,
        width=20,
        pady=10,
        padx=15,
        relief=GROOVE,
        font="Georgia, 13",
    )
    Download_BV.grid(row=5, column=1, pady=10, padx=10)


def Browse():

    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video"
    )

    download_Path.set(download_Directory)


def DownloadPlaylist():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    p = Playlist(Youtube_link)
    print(Youtube_link)
    for video in p.videos:
        print("downloading : {} with url : {}".format(video.title, video.watch_url))
        video.streams.filter(
            type="video", progressive=True, file_extension="mp4"
        ).order_by("resolution").desc().first().download(download_Folder)


def DownloadVideo():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    video = YouTube(Youtube_link)
    video.streams.filter(type="video", progressive=True, file_extension="mp4").order_by(
        "resolution"
    ).desc().first().download(download_Folder)


root = Tk()


root.geometry("520x250")
root.resizable(False, False)
root.title("YouTube Downloader")

video_Link = StringVar()
download_Path = StringVar()

Widgets()


root.mainloop()
