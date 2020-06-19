import sys
import threading
import tkinter as tk
import webbrowser

from tkmacosx import Button

from twitter_bot import tweet_devotional


def close(event):
    sys.exit()


def openweb(param):
    webbrowser.open_new(param)


class App(threading.Thread):

    def __init__(self, window):
        self.root = window
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        lines = tweet_devotional()
        frame = tk.Frame(window, pady=20)
        frame.pack()
        if len(lines) == 3:
            text = []
            for item in lines:
                if "http:" in item:
                    links = item.split("\n")
                    label.config(text=links[0], font=("Helvetica", 25, "bold"))

                    webpage = Button(master=frame, text="Devotional Page", borderless=1)
                    webpage.pack()
                    webpage.bind("<Button-1>", lambda e: webbrowser.open_new(links[1]))

                    soundcloud = Button(master=frame, text="Sound Cloud", borderless=1)
                    soundcloud.pack()
                    soundcloud.bind("<Button-1>", lambda e: webbrowser.open_new(links[2].split("Audio version: ")[1]))
                else:
                    text.append(item)
            body.config(text="\n\n".join(text),
                        wraplength=500,
                        justify="center",
                        padx=20,
                        pady=20)
            Button(master=frame, text="Quit", command=window.quit, borderless=1, padx=100).pack()
        error.config(text=lines[0],
                     wraplength=500,
                     justify="center",
                     bg="red",
                     padx=20,
                     pady=20)
        Button(master=frame, text="Quit", command=window.quit, borderless=1).pack()


window = tk.Tk()
window.title("Daily Devotional")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
app = App(window)
label = tk.Label(text="Publishing Latest Apostolic Faith Devotional to Twitter...",
                 wraplength=500,
                 justify="center",
                 padx=20,
                 pady=20)
label.pack()
body = tk.Label()
body.pack()
error = tk.Label()
error.pack()
window.bind('<Escape>', close)
window.after(60000, window.destroy)
window.mainloop()
