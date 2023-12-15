import tkinter as tk
import ttkbootstrap as tb
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import time

win = tb.Window()
win.title("google it!")
win.configure(bg="black")
mode = tk.IntVar()
mode.set("0")

def go_to_google():
    value = search.get("1.0", "end-1c")
    if value:
        try:
            if mode.get() == 0:
                webbrowser.open(f'https://www.google.com/search?q={value}&oq={value}&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIMCAEQIxgnGIAEGIoFMgcIAhAAGIAEMgcIAxAAGIAEMgYIBBBFGDwyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgxNjA0ajBqNKgCALACAA&sourceid=chrome&ie=UTF-8')
            elif mode.get() == 1:
                webbrowser.open(f'https://www.google.com/search?sca_esv=591053097&sxsrf=AM9HkKk8k10CLhl8V1LCUPW81QcYrNAb2w:1702615791590&q={value}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjphMmL0pCDAxXxTaQEHf-xBCUQ0pQJegQIFhAB&biw=1536&bih=738&dpr=1.25')
            elif mode.get() == 3:
                webbrowser.open(f'https://fa.wikipedia.org/wiki/{value}')
            else:
                webbrowser.open(f'https://www.google.com/search?q={value}&source=lmns&tbm=vid&bih=738&biw=1536&hl=fa&sa=X&ved=2ahUKEwjXvv6405CDAxXyrycCHUlBCPwQ0pQJKAJ6BAgBEAY')
        except:
            messagebox.showerror(title="Error", message="Connection Problem")
    else:
        messagebox.showerror(title="Error", message="the search box is empty")
search = tk.Text(win,font=("None",12), width=40, height=3)
search.pack(pady=(30,0))


style = tb.Style()
mode_frm = tk.Frame(win)
mode_frm.pack(pady=(40,0))

all = tk.Radiobutton(mode_frm, variable=mode, value="0", text="all", bg="white", fg="black", font=("None", 14), selectcolor="grey", indicatoron=0, cursor="hand2")
pictures_mode = tk.Radiobutton(mode_frm, variable=mode, value="1", text="pictures", bg="white", fg="black", font=("None", 14), selectcolor="grey", indicatoron=0, cursor="hand2")
videos_mode = tk.Radiobutton(mode_frm, variable=mode, value="2", text="videos", bg="white", fg="black", font=("None", 14), selectcolor="grey", indicatoron=0, cursor="hand2")
wiki_mode = tk.Radiobutton(mode_frm, variable=mode, value="3", text="wikipedia", bg="white", fg="black", font=("None", 14), selectcolor="grey", indicatoron=0, cursor="hand2")
pictures_mode.grid(row=0, column=0)
videos_mode.grid(row=0, column=1)
wiki_mode.grid(row=0, column=2)
all.grid(row=0, column=3)

style.configure('TButton', font=('Helvetica', 14))
btn = tb.Button(win, text="search", bootstyle="outline-success", cursor="hand2", command=go_to_google)
btn.pack(pady=(30,0))

win.minsize(600,300)
win.mainloop()