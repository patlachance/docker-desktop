#!/usr/bin/env python

"""
Stop VNC server and exit Docker desktop
"""

try:
    import tkinter as tk
except:
    import Tkinter as tk


def clickLogout():
    import subprocess
    subprocess.call(['killall', 'startvnc.sh'])


app = tk.Tk()
app.title("Log out")
app.geometry("400x300+300+300")
app.configure(bg='light grey')

tk.Label(app, text="", height=3, bg='light grey').pack()
tk.Label(app, text="Are you sure you want to quit all\n" +
         "applications and log out now?", bg='light grey',
          font=("Sans-serif", 12, "bold"), height=3, width=100).pack()

tk.Label(app, text="Make sure you have saved all your data into a\n" +
         "shared or mounted folder before logging out.", bg='light grey',
         font=("Sans-serif", 10), height=0, width=100).pack()

button_shutdown = tk.Button(app, text="Log out",
                            width=20, command=clickLogout)

button_cancel = tk.Button(app, text="Cancel",
                          width=20, command=app.destroy)

button_cancel.pack(side='bottom', padx=20, pady=20)
button_shutdown.pack(side='bottom', padx=5, pady=5)

app.bind("<Escape>", lambda e: e.widget.quit())

app.mainloop()
