from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sqlite3
from tkinter import *

"""
statistiques :
    - service
    - emplacement
    - nombre de personnes
    - demande d'e-mail ou pas
"""
def stats():
    conn = sqlite3.connect("GP211.db")
    c =conn.cursor()
    l = c.execute("SELECT * FROM Reservation")

    #service :
    midi = 0
    soir = 0
    #emplacement
    inter = 0
    exter_fum = 0
    exter_nfum = 0
    #nombre de personnes
    un_deux = 0
    trois_quatre = 0
    cinq_six = 0
    sept_neuf = 0
    dix_douze = 0
    #e-mail ou pas
    mail_oui = 0
    mail_non = 0
    
    for i in l.fetchall():
        #nombre de personnes
        if 1 <= i[2] <= 2:
            un_deux += 1
        elif 3 <= i[2] <= 4:
            trois_quatre += 1
        elif 5 <= i[2] <= 6:
            cinq_six += 1
        elif 7 <= i[2] <= 9:
            sept_neuf += 1
        else :
            dix_douze += 1
        #service
        if i[4]=="Midi":
            midi += 1
        else :
            soir += 1
        #emplacement
        if i[5]=="Intérieur":
            inter += 1
        elif i[5]=="Terrasse-fumeur":
            exter_fum += 1
        else :
            exter_nfum += 1
        #email ou pas
        if i[7]!="":
            mail_oui += 1
        else :
            mail_non +=1

    bg = PhotoImage(file=r"images/fond_carte.png")
    stats = Toplevel()
    stats.geometry("860x720+200+70")
    stats.resizable(False,False)

    canvas = Canvas(stats,width=860,height=720)
    canvas.create_image(450,300,anchor="center",image=bg)
    
    
    
    #nombre de personnes
    tot_nb_pers = un_deux + trois_quatre + cinq_six + sept_neuf + dix_douze
    p_un_deux = (un_deux/tot_nb_pers)*100
    p_trois_qatre = (trois_quatre/tot_nb_pers)*100
    p_trois_qatre = (cinq_six/tot_nb_pers)*100
    p_sept_neuf = (sept_neuf/tot_nb_pers)*100
    p_dix_douze = (dix_douze/tot_nb_pers)*100

    lab_nbpers = ["1 ou 2","3 ou 4","5 ou 6","de 7 à 9","de 10 à 12"]
    frac_nbpers = [p_un_deux,p_trois_qatre,p_trois_qatre,p_sept_neuf,p_dix_douze]
    fig1 = Figure(figsize=(3.7,3))
    subplot1 = fig1.add_subplot(1,1,1)
    subplot1.pie(frac_nbpers,labels=lab_nbpers,autopct='%1.1f%%', shadow=True,textprops={'size': 'smaller'},explode=(0,0.1,0,0,0))
    pie1 = FigureCanvasTkAgg(fig1, canvas)
    pie1.get_tk_widget().place(x=40,y=30)
    
    #service
    tot_serv = midi + soir
    p_midi = (midi/tot_serv)*100
    p_soir = 100 - p_midi

    lab_serv = ["Midi","Soir"]
    frac_serv = [p_midi,p_soir]
    fig2 = Figure(figsize=(3.7,3))
    subplot2 = fig2.add_subplot(1,1,1)
    subplot2.pie(frac_serv,labels=lab_serv,autopct='%1.1f%%', shadow=True,textprops={'size': 'smaller'})
    pie2 = FigureCanvasTkAgg(fig2, canvas)
    pie2.get_tk_widget().place(x=450,y=30)

    
    #emplacement
    tot_loc = inter + exter_nfum + exter_fum
    p_inter = (inter/tot_loc)*100
    p_exter_nfum = (exter_nfum/tot_loc)*100
    p_exter_fum = 100 - p_inter - p_exter_nfum

    lab_loc = ["Intérieur","Terrasse\nnon-fumeur","Terrasse\nfumeur"]
    frac_loc = [p_inter,p_exter_nfum,p_exter_fum]
    fig3 = Figure(figsize=(3.7,3))
    subplot3 = fig3.add_subplot(1,1,1)
    subplot3.pie(frac_loc,labels=lab_loc,autopct='%1.1f%%', shadow=True,textprops={'size': 'smaller'})
    pie3 = FigureCanvasTkAgg(fig3, canvas)
    pie3.get_tk_widget().place(x=40,y=370)  

    
    #email ou pas
    tot_mail = mail_oui + mail_non
    p_mail_oui = (mail_oui/tot_mail)*100
    p_mail_non = (mail_non/tot_mail)*100
    
    lab_mail = ["Oui","Non"]
    frac_mail = [p_mail_oui,p_mail_non]
    fig4 = Figure(figsize=(3.7,3))
    subplot4 = fig4.add_subplot(1,1,1)
    subplot4.pie(frac_mail,labels=lab_mail,autopct='%1.1f%%', shadow=True,textprops={'size': 'smaller'})
    pie4 = FigureCanvasTkAgg(fig4, canvas)
    pie4.get_tk_widget().place(x=450,y=370) 

    fig1.set_facecolor("khaki")
    fig2.set_facecolor("khaki")
    fig3.set_facecolor("khaki")
    fig4.set_facecolor("khaki")

    title1 = Label(canvas,text="Nombre de personnes par réservation",fg="white",bg="gray21",relief="ridge",width=30)
    title1.place(x=110,y=40)
    title2 = Label(canvas,text="Heure de réservation",fg="white",bg="gray21",relief="ridge",width=30)
    title2.place(x=520,y=40)
    title3 = Label(canvas,text="Emplacement de la réservation",fg="white",bg="gray21",relief="ridge",width=30)
    title3.place(x=110,y=380)
    title4 = Label(canvas,text="Demande de récapitulatif par e-mail",fg="white",bg="gray21",relief="ridge",width=30)
    title4.place(x=520,y=380)

    def quitter():
        stats.destroy()
    b = Button(canvas,text="Quitter",bg="red4",width=110,command = quitter)
    b.place(x=40,y=680)
    
    canvas.pack()
    stats.mainloop()

    












        
