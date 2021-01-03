from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sqlite3
from tkinter import *


def notes_consult():
    conn = sqlite3.connect("GP211.db")
    c = conn.cursor()
    c.execute("SELECT Notes FROM Avis")
    notes = c.fetchall()            
    c.close()
    conn.close()
    print(notes)
    note_tot = 2.5
    tot=0
    un =0
    deux =0
    trois =0
    quatre =0
    cinq =0
    for i in notes:
        print(type(i[0]))
        if i[0]==1:
            un += 1
        elif i[0]==2:
            deux +=1
        elif i[0]==3:
            trois +=1
        elif i[0]==4:
            quatre +=1
        else :
            cinq +=1
        note_tot = note_tot + i[0]
    print(un,deux,trois,quatre,cinq)
    print(note_tot)
    tot = un + deux + trois + quatre + cinq
    moyenne =  round(note_tot/tot,2)      
    print(moyenne)

    p_un = (un/tot)*100
    p_deux = (deux/tot)*100
    p_trois = (trois/tot)*100
    p_quatre = (quatre/tot)*100
    p_cinq = (cinq/tot)*100
    fracs = [p_un,p_deux,p_trois,p_quatre,p_cinq]
    labels = ["1 étoile","2 étoiles","3 étoiles","4 étoiles","5 étoiles"]

    
    colors = ['lightskyblue', 'red', 'blue', 'green', 'gold']
    plt.pie(fracs, colors=colors, startangle=90, autopct='%.1f%%',explode=(0,0,0,0,0.1))
    plt.legend(labels,loc="best")
    plt.title("Notes des clients\nNote moyenne : "+str(moyenne)+"/5",bbox={'facecolor':'0.8', 'pad':5})
    plt.show()




