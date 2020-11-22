from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pytube
import time

win=Tk()
win.title('YOUTUBE-DOWNLOADER')
win.geometry('400x300')
win.resizable(False,False)
win.configure(bg='#527a7a')
win.iconbitmap('yt.ico')

yt_logo=ImageTk.PhotoImage(Image.open('youtube.png'))
logo=Label(win,image=yt_logo,borderwidth=8)
logo.place(x=160,y=60)

def download():
    global text
    link=text.get("1.0",'end-1c')

    if link=='':
        messagebox.showerror('YOUTUBE-DOWNLOADER','paste your link here...')

    else:
        yt=pytube.YouTube(link)
        stream=yt.streams.first()
        time.sleep(2)
        text=text.delete(1.0,'end')
        time.sleep(3)
        stream.download()
        messagebox.showinfo('YOUTUBE-DOWNLOADER','video has been downloaded succesfully')
        

text=Text(win,width=40,height=1,font=('arial',10,'bold'))
text.place(x=55,y=170)
text.insert('end','paste your link here...')


button=Button(win,text='DOWNLOAD',relief='ridge',font=('arial',10,'bold'),bg='red',fg='white',command=download)
button.place(x=150,y=200)





win.mainloop()
