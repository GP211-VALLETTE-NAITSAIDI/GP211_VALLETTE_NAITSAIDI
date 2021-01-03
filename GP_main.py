"""
Simulation de restaurant - GP211
Lakhdar Nait-Saidi & Renaud Vallette
2PA1 - 2020
"""
from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import Calendar, DateEntry
from fonctions import Carte,Statistiques,Coms,Notes,Recherche,Simulation,SaveRes
###################################################################################################################################################################################################


##FONCTIONS

def save():
    """
fonction de transition pour valider une réservation
    """
    SaveRes.save(nom.get(),prenom.get(),nb_personnes.get(),date_r.get(),service.get(),emplacement.get(),user_mail.get(),b6)

def clear():
    """
réinitialise l'interface de réservation
    """
    nom.delete(0,END)
    prenom.delete(0,END)
    nb_personnes.current(0)
    service.current(0)
    emplacement.current(0)
    user_mail.delete(0,END)
    mail_frame.place_forget()
    b6.place_forget()
        
def simu1():
    """
fonction de transition pouvant être appelée directement dans le bouton simulaion, car on ne peut appeler directement une fonction prenant des arguments
    """
    Simulation.simulation(emplacement.get(),service.get())

def carte():
    """
fonction de transition pour afficher la carte
    """
    Carte.carte(fond_carte,carte1,carte2,carte3,oeil)
    
def stats():
    """
fonction de transition pour afficher les stats
    """
    Statistiques.stats()


def avis():
    """
Ouvre une fenêtre donnant accès aux commentaires des utilisateurs et au graphique des notes des utilisateurs
    """
    root=Toplevel()
    root.geometry("220x150+600+200")
    root.resizable(False,False)
    canvas = Canvas(root,width=220,height=150)
    canvas.create_image(50,50,anchor="center",image=bg_reservation)
    def coms():
        Coms.avis_consult()
    def notes():
        Notes.notes_consult()
    def leave():
        root.destroy()
    b = Button(root,text="Consulter les commentaires",width=25,bg="LightGoldenrod2",command=coms)
    b.place(x=20,y=20)
    b1 = Button(root,text="Consulter les notes", width=25,bg="LightGoldenrod2",command=notes)
    b1.place(x=20,y=60)
    b2 = Button(root,text="Quitter",width=25,bg="red4",command=leave)
    b2.place(x=20,y=100)
    canvas.pack()

    
def checkvalue():
    if CheckVar2.get()==1:
        mail = Label(mail_frame, text="Adresse e-mail :", bg="LightGoldenrod2",width=22,relief="ridge")
        mail.place(x=5,y=5)        
        user_mail.place(x=185,y=5)
        mail_frame.place(x=30,y=400)
    if CheckVar2.get()==0:
        mail_frame.place_forget()

def recherche():
    Recherche.recherche(fenetre,bg_reservation)

    
        
##########################################################################################################################################################################################    

if __name__ == "__main__":
    ##INTERFACE GRAPHIQUE
    fenetre = Tk()
    fenetre.geometry("900x630+200+70")
    fenetre.resizable(False,False)


        #IMAGES
    canvas = Canvas(fenetre,width=900,height=630)

    bg_reservation = PhotoImage(file=r'images/ardoise.png')
    canvas.create_image(420,295,anchor='center',image=bg_reservation)

    banniere_image = PhotoImage(file=r'images/bannière1.png')
    canvas.create_image(718,145, anchor="center", image=banniere_image)

    canvas.create_text(243,298,fill="white", text="/",font="Times 19 bold")
    canvas.create_text(293,298,fill="white", text="/",font="Times 19 bold")
    canvas.create_text(268,328,fill="white", text=":",font="Times 15 bold")

    canvas.pack()
    canvas.update

    fond_carte = PhotoImage(file=r"images/fond_carte.png")
    carte1 = PhotoImage(file=r"images/carte1.png")
    carte2 = PhotoImage(file=r"images/carte2.png")
    carte3 = PhotoImage(file=r"images/carte3.png")
    leave = PhotoImage(file=r"images/exit.png")
    oeil = PhotoImage(file=r"images/oeil.png")

    check = PhotoImage(file=r"images/check1.png")
    stats_image = PhotoImage(file=r"images/stats.png")
    loupe = PhotoImage(file=r"images/loupe.png")
    simu_b = PhotoImage(file=r"images/simulation_b.png")
    clear_b = PhotoImage(file=r"images/clear_b.png")
    carte_b = PhotoImage(file=r"images/carte_b.png")
    avis_b = PhotoImage(file=r"images/avis_b.png")
    
        #LABELS
    l1 = Label(fenetre, text="Nom :", padx=2, pady=2, width = 20, bg="LightGoldenrod2",relief="ridge")
    l1.place(x=30,y=200)
    l2 = Label(fenetre, text="Prénom :", padx=2, pady=2, width = 20, bg="LightGoldenrod2",relief="ridge")
    l2.place(x=30,y=230)
    l3 = Label(fenetre, text="Nombre de personnes :", padx=2, pady=2, width = 20, bg="LightGoldenrod2",relief="ridge")
    l3.place(x=30,y=260)
    l4 = Label(fenetre, text="Date :", padx=2, pady=2, width = 20, bg="LightGoldenrod2", relief="ridge")
    l4.place(x=30,y=290)
    l5 = Label(fenetre, text="Service :", padx=2, pady=2, width = 20, bg="LightGoldenrod2",relief="ridge")
    l5.place(x=30,y=320)
    l6 = Label(fenetre, text="Emplacement :", padx=2, pady=2, width = 20, bg="LightGoldenrod2",relief="ridge")
    l6.place(x=30,y=350)


        #COMBOBOX
    nb_personnes = ttk.Combobox(fenetre, values = [1,2,3,4,5,6,7,8,9,10,11,12],width=19, state="readonly")
    nb_personnes.current(0)
    nb_personnes.place(x=200,y=260)
    emplacement = ttk.Combobox(fenetre, values=["Intérieur","Terrasse-fumeur","Terrasse-non-fumeur"], width=19, state = "readonly")
    emplacement.current(0)
    emplacement.place(x=200,y=350)
    service = ttk.Combobox(fenetre, values=["Midi","Soir"],width=19, state = "readonly")
    service.current(0)
    service.place(x=200,y=320)

        #FRAMES
    mail_frame = Frame(fenetre, width=365,height=30)

        #ENTRIES
    nom = Entry(fenetre,width=22)
    nom.place(x=200,y=200)
    prenom = Entry(fenetre,width=22)
    prenom.place(x=200,y=230)
    date_r = DateEntry(fenetre, width=19, background='LightGoldenrod2',foreground='black', borderwidth=2,state="readonly")
    date_r.place(x=200,y=290)


    user_mail= Entry(mail_frame,width=25)


        #CHECKBOX
    CheckVar2 = IntVar()
    c_mail = ttk.Checkbutton(fenetre, text ="Je souhaite recevoir un récapitulatif de ma réservation par mail", width=57,variable = CheckVar2, onvalue = 1, offvalue = 0,command=checkvalue)
    c_mail.place(x=30,y=380)

        #BUTTONS
    b1 = Button(fenetre, text="Quitter", width = 15, bg="red4", command=fenetre.destroy)
    b1.place(x=30,y=580)
    b2 = Button(fenetre, text="Valider  ",padx=10, bg="forestgreen", command=save,image=check,compound=LEFT)
    b2.place(x=30,y=460)
    b3 = Button(fenetre, text="Carte  ", padx=12,image=carte_b,compound=LEFT,bg="LightGoldenrod2",command=carte)
    b3.place(x=360,y=580)
    b4 = Button(fenetre, text="Avis   ", bg="LightGoldenrod2",command=avis,image=avis_b,padx=5,compound=LEFT)
    b4.place(x=475,y=580)
    b5 = Button(fenetre,text="Réinitialiser  ",padx=5,image=clear_b,bg="LightGoldenrod2",command=clear,compound=LEFT)
    b5.place(x=287,y=460)
    b6 = Button(fenetre,text="Simulation",bg="LightGoldenrod2",command=simu1,image=simu_b,compound=LEFT,padx=5)
    b7 = Button(fenetre,text="Rechercher une réservation  ",bg="LightGoldenrod2",padx=5,command=recherche,image=loupe,compound=LEFT)
    b7.place(x=680,y=580)
    b8 = Button(fenetre,text="Statistiques  ",padx=5,command=stats,image=stats_image,compound=LEFT,bg="LightGoldenrod2")
    b8.place(x=240,y=580)

    fenetre.mainloop()

#####################################################################################################################################################################################################



