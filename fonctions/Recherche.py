import sqlite3
from tkinter import *
from fonctions import Simulation


def recherche(root,image):
    search_frame = LabelFrame(root,text="Rechercher une réservation",width=350,height=230,bg="LightGoldenrod2")
    search_frame.place(x=525,y=300)
    search_canvas = Canvas(search_frame,width=340,height=220,borderwidth=0)
    search_canvas.create_image(170,95,anchor="center",image=image)
    search_canvas.pack()
    l1 = Label(search_frame,text="Nom :",width=15,bg="LightGoldenrod2",relief="ridge")
    l1.place(x=15,y=10)
    l2 = Label(search_frame,text="Prénom :",width=15,bg="LightGoldenrod2",relief="ridge")
    l2.place(x=15,y=35)
    l3 = Label(search_frame,text="N° de réservation :",width=15,bg="LightGoldenrod2",relief="ridge")
    l3.place(x=15,y=60)

    search_nom = Entry(search_frame,width=30)
    search_nom.place(x=140,y=10)
    search_prenom = Entry(search_frame,width=30)
    search_prenom.place(x=140,y=35)
    num_res = Entry(search_frame,width=30)
    num_res.place(x=140,y=60)

    def quitter():
        search_nom.delete(0,END)
        search_prenom.delete(0,END)
        num_res.delete(0,END)
        search_frame.place_forget()       

    def search_table():
        def simu2():
            Simulation.simulation(result[5],result[4])
        def clear():
            search_nom.delete(0,END)
            search_prenom.delete(0,END)
            num_res.delete(0,END)
            res.place_forget()
            b9.place_forget() 
            
        try:
            nom = search_nom.get().rstrip(" ")
            prenom = search_prenom.get().rstrip(" ")
            num = num_res.get()
            conn = sqlite3.connect("GP211.db")
            c = conn.cursor()
            c.execute("SELECT * FROM Reservation WHERE Nom=? AND Prénom=? AND n°_de_reservation=?",(nom,prenom,num))
            result = c.fetchone()
            print(result)
            c.close()
            conn.close()

            if result[4]=="Midi":
                search_service = "Midi" 
                repas="déjeuner"
            else :
                search_service = "Soir"
                repas="dîner"
            if result[5]=="Intérieur":
                search_emplacement = "Intérieur"
                loc="intérieur"
            elif result[5]=="Terrasse-fumeur":
                search_emplacement = "Terrasse-fumeur"
                loc="terrasse (coin fumeur)"
            else :
                search_emplacement = "Terrasse-non-fumeur"
                loc="terrasse (coin non-fumeur)"
                
            text="Bonjour "+nom+" "+prenom+",\nvous avez réservé une table pour "+str(result[2])+" personnes \nle "+str(result[3])+" pour un "+repas+" en "+loc
            res = Label(search_frame,text=text,width=44,height=4,bg="white",relief="ridge")
            res.place(x=13,y=118)
            
            b9 = Button(search_frame,text="Simulation",width=12,bg="LightGoldenrod2",command=simu2)
            b9.place(x=125,y=190)
            b11 = Button(search_frame,text="Réinitialiser",width=12,bg="LightGoldenrod2",command=clear)
            b11.place(x=15,y=190)  

        except :
            messagebox.showwarning("Erreur","Données éronnées, peut-être n'avez vous pas encore validé votre réservation chez nous !")

    b8 = Button(search_frame,text="Rechercher",width=43,bg="LightGoldenrod2",command=search_table)
    b8.place(x=15,y=85)
    b10 = Button(search_frame,text="Fermer", width=12,bg="red4",command=quitter)
    b10.place(x=234,y=190)
