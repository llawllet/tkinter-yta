from tkinter import *
from tkinter import messagebox
from yt_dlp import YoutubeDL

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("YouTube Audio Downloader")
root.configure(bg="#f2eee3")

link = StringVar()

def download():
    url = str(link.get())
    if ('http' and 'yout' not in url):
        return messagebox.showerror('Error', 'Enter a valid youtube url.')
    try:
        opts = {'format': 'bestaudio[ext=m4a]'}
        with YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio = ydl.prepare_filename(info)
            ydl.process_info(info)
        title = info['title']
        messagebox.showinfo('Alert', f'Downloaded "{title}" successfully.')
        link.set('')
    except Exception as e:
        link.set('')
        return messagebox.showerror('Error', str(e))

HEADER = Label(root, text='Paste the YouTube link here:', font='consolas 15', bg='#f2eee3').place(x=85, y=60)
ENTRY = Entry(root, width=50, textvariable=link, font='consolas 10', relief=FLAT).place(x=50, y=90)
DOWNLOAD = Button(root, text='Download MP3', font='consolas 15', bg='#526a9c', padx=2, command=download, relief=FLAT, fg="white").place(x=175, y=180)

root.mainloop()
