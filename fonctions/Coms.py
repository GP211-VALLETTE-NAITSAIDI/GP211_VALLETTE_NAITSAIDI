import tkinter as tk
from tkinter import ttk
import sqlite3

def avis_consult():
    root = tk.Tk()
    #root.geometry("500x300")
    root.resizable(False,False)
    container = ttk.Frame(root,width=500)
    canvas = tk.Canvas(container,width=500)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas,width=500)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    conn = sqlite3.connect("GP211.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Avis WHERE Commentaires != (?)",("",))
    com=c.fetchall()
    print(com)
    text=""
    for i in com:
        text = text+" Note : "+str(i[0])+"/5   -  "+i[1]+"\n\n"
        
    ttk.Label(scrollable_frame, text=text).pack()
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
