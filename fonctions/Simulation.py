from tkinter import *
import pygame
from fonctions import Carte
import sqlite3
import time

def simulation(emplacement,service):
    simu=Toplevel()
    simu.geometry("1300x680+70+40")
 
    if emplacement=="Intérieur":
        image=PhotoImage(file=r"images/simu/int.png")
        carte=PhotoImage(file=r"images/simu/int_carte.png")
        jean=PhotoImage(file=r"images/simu/int_music.png")
        livre=PhotoImage(file=r"images/simu/int_livre.png")
        x1,y1,x2,y2,x3,y3=991,257,630,424,12,536        
    else :
        if service=="Midi":
            image=PhotoImage(file=r"images/simu/terrasse_midi.png")
            carte=PhotoImage(file=r"images/simu/extjour_carte.png")
            jean=PhotoImage(file=r"images/simu/extjour_music.png")
            livre=PhotoImage(file=r"images/simu/extjour_livre.png")
            x1,y1,x2,y2,x3,y3=1057,108,666,413,22,425
        else :
            image=PhotoImage(file=r"images/simu/terrasse_nuit.png")
            carte=PhotoImage(file=r"images/simu/extnuit_carte.png")
            jean=PhotoImage(file=r"images/simu/extnuit_music.png")
            livre=PhotoImage(file=r"images/simu/extnuit_livre.png")
            x1,y1,x2,y2,x3,y3=1044,104,715,452,21,464
        
    canvas_simu = Canvas(simu,width=1300,height=680)
    canvas_simu.create_image(650,340,anchor="center",image=image)

    Pause = False
    def music_play(): 
        pygame.mixer.init()
        m1=r"musiques/french-waltz.mp3"
        pygame.mixer.music.load(m1)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
        b_music.configure(command=music_pause)
        
    def music_pause():
        pygame.mixer.music.pause()
        b_music.configure(command=music_unpause)
    def music_unpause():
        pygame.mixer.music.unpause()
        b_music.configure(command=music_pause)

     
    def quitter():
        simu.destroy()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)
        time.sleep(0.5)
        pygame.mixer.music.set_volume(0.3)
        time.sleep(0.5)
        pygame.mixer.music.set_volume(0.1)
        time.sleep(0.5)
        pygame.mixer.music.stop()

    bg = PhotoImage(file=r'images/ardoise.png')
    def note():
        fen = Toplevel()
        fen.geometry("400x300+400+100")
        fen.title("Déposer un avis")
        canvas = Canvas(fen,width=400,height=300)
        canvas.create_image(250,200,anchor="center",image=bg)
        l = Label(fen,text="Note :",width=20,bg="LightGoldenrod2",relief="ridge")
        l.place(x=20,y=20)
        c_note = ttk.Combobox(fen,values=[1,2,3,4,5],width=31,state="readonly")
        c_note.current(4)
        c_note.place(x=170,y=20)
        l1=Label(fen,text="Déposez un commentaire si vous le souhaitez",width=50,bg="LightGoldenrod2",relief="ridge")
        l1.place(x=20,y=50)
        text = Text(fen,width=44,height=10)
        text.place(x=20,y=85)

        def send():
            user_com=text.get("1.0","end-1c")
            conn=sqlite3.connect("GP211.db")
            c=conn.cursor()
            c.execute("INSERT INTO Avis (Notes,Commentaires) VALUES (?,?)",(c_note.get(),user_com))
            conn.commit()
            c.close()
            conn.close()
            messagebox.showinfo("Info","C'est noté, merci !")
                    
        
        def leave():
            fen.destroy()
            
        b=Button(fen,text="Envoyer",width=23,bg="LightGoldenrod2",command=send)
        b.place(x=205,y=260)
        b=Button(fen,text="Quitter",width=23,bg="red4",command=leave)
        b.place(x=20,y=260)
        
        canvas.pack()
        
    fond_carte = PhotoImage(file=r"images/fond_carte.png")
    carte1 = PhotoImage(file=r"images/carte1.png")
    carte2 = PhotoImage(file=r"images/carte2.png")
    carte3 = PhotoImage(file=r"images/carte3.png")
    oeil = PhotoImage(file=r"images/oeil.png")
    
    def carte_simu():
        Carte.carte(fond_carte,carte1,carte2,carte3,oeil)
        
    b_music = Button(canvas_simu, image=jean, borderwidth=0, highlightthickness=0, padx=0, pady=0,command=music_play)
    b_music.place(x=x1,y=y1)
    b_carte = Button(canvas_simu, image=carte, borderwidth=0, highlightthickness=0, padx=0, pady=0,command=carte_simu)
    b_carte.place(x=x2,y=y2)
    b_avis = Button(canvas_simu, image=livre, borderwidth=0, highlightthickness=0, padx=0, pady=0,command=note)
    b_avis.place(x=x3,y=y3)
    b_leave = Button(canvas_simu,text="Quitter",width=15, bg="red4", padx=0, pady=0,command=quitter)
    b_leave.place(x=1180,y=640)

    canvas_simu.pack()
    
    simu.mainloop()
