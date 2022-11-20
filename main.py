from tkinter import messagebox
from pytube import YouTube
from tkinter import *

def mp3_downloader():
    global video_entry, path_entry
    videolink = video_entry.get()
    path_access = path_entry.get()
    yt = YouTube(videolink)
    print(yt.streams.all())
    try:
        stream = yt.streams.get_by_itag(251)
    except:
        stream = yt.streams.get_by_itag(140)
    if path_access == None:
        stream.download()

    else:
        stream.download(output_path=path_access)
    messagebox.showinfo(title="MP3 Downloader", message="Téléchargement terminé !")

window = Tk()
window.title("MP3 Downloader")
window.geometry("512x512")
window.minsize(512, 512)
window.config(background="#7A66B1")

frame = Frame(window, bg="#7A66B1")

right_frame = Frame(frame, bg="#7A66B1")

label_title = Label(right_frame, text="Url de la vidéo :", font=("Helvetica", 20), bg="#7A66B1", fg="white")
label_title.pack()

video_entry = Entry(right_frame, font=("Helvetica", 20), bg="#7A66B1", fg="white")
video_entry.pack()

label_title = Label(right_frame, text="Chemin de l'enregistrement :", font=("Helvetica", 20), bg="#7A66B1", fg="white")
label_title.pack()

path_entry = Entry(right_frame, font=("Helvetica", 20), bg="#7A66B1", fg="white")
path_entry.pack()

download_button = Button(right_frame, text="Télécharger", font=("Helvetica", 20), bg="white", fg="#7A66B1", command=mp3_downloader)
download_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

window.mainloop()
