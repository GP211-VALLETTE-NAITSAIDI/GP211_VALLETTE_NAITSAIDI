from tkinter import *

def carte(fond_carte,carte1,carte2,carte3,oeil):
    fen_carte=Toplevel()
    fen_carte.title("Carte")
    fen_carte.geometry("1360x730+100+40")
    fen_carte.resizable(False,False)

    canvas1=Canvas(fen_carte,width=1560,height=800)
    
    canvas1.create_image(680,365, anchor="center", image=fond_carte)
    canvas1.create_image(620,365, anchor="center", image=carte1)

    def p1():
        canvas1.create_image(620,365,anchor="center",image=carte1)
        b1.place(x=480,y=90)
        b2.place(x=480,y=140)
        b3.place(x=480,y=192)
        b4.place(x=480,y=250)        
        b5.place(x=480,y=360)
        b6.place(x=480,y=415)
        b7.place(x=480,y=445)
        b8.place(x=480,y=520)
        b9.place(x=480,y=595)
        b10.place(x=480,y=620)
        b11.place(x=1065,y=115)
        b12.place(x=1065,y=200)
        b13.place(x=1065,y=280)
        b14.place(x=1065,y=350)
        b15.place(x=1065,y=420)
        b16.place(x=1065,y=520)
        
        b1.configure(command=ap1)
        b2.configure(command=ap2)
        b3.configure(command=ap3)
        b4.configure(command=ap4)
        b5.configure(command=ap5)
        b6.configure(command=ap6)
        b7.configure(command=ap7)
        b8.configure(command=ap8)
        b9.configure(command=ap9)
        b10.configure(command=ap10)
        b11.configure(command=ap11)
        b12.configure(command=ap12)
        b13.configure(command=ap13)
        b14.configure(command=ap14)
        b15.configure(command=ap15)
        b16.configure(command=ap16)
        
    def p2():
        canvas1.create_image(620,365,anchor="center",image=carte2)
        b1.place(x=480,y=80)
        b2.place(x=480,y=140)
        b3.place(x=480,y=197)
        b4.place(x=480,y=270)        
        b5.place(x=480,y=415)
        b6.place(x=480,y=460)
        b7.place(x=480,y=510)
        b8.place(x=480,y=560)
        b9.place(x=480,y=610)

        b10.place(x=1065,y=85)
        b11.place(x=1065,y=125)
        b12.place(x=1065,y=155)
        b13.place(x=1065,y=210)
        b14.place(x=1065,y=255)
        b15.place(x=1065,y=290)
        b16.place(x=1065,y=335)


        b1.configure(command=ap17)
        b2.configure(command=ap18)
        b3.configure(command=ap19)
        b4.configure(command=ap20)
        b5.configure(command=ap21)
        b6.configure(command=ap22)
        b7.configure(command=ap23)
        b8.configure(command=ap24)
        b9.configure(command=ap25)
        b10.configure(command=ap26)
        b11.configure(command=ap27)
        b12.configure(command=ap28)
        b13.configure(command=ap29)
        b14.configure(command=ap30)
        b15.configure(command=ap32)
        b16.configure(command=ap31)
        

        
    def p3():
        canvas1.create_image(620,365,anchor="center",image=carte3)
        b1.place_forget()
        b2.place_forget()
        b3.place_forget()
        b4.place_forget()        
        b5.place_forget()
        b6.place_forget()
        b7.place_forget()
        b8.place_forget()
        b9.place_forget()

        b10.place_forget()
        b11.place_forget()
        b12.place_forget()
        b13.place_forget()
        b14.place_forget()
        b15.place_forget()
        b16.place_forget()

        
    def leave():
        fen_carte.destroy()

    b = Button(fen_carte,text="Page 1",width=15,bg="LightGoldenrod2",command=p1)
    b.place(x=1215,y=300)
    b = Button(fen_carte,text="Page 2",width=15,bg="LightGoldenrod2",command=p2)
    b.place(x=1215,y=340)
    b = Button(fen_carte,text="Page 3",width=15,bg="LightGoldenrod2",command=p3)
    b.place(x=1215,y=380)
    b = Button(fen_carte,text="Quitter",width=15,bg="red4",command=leave)
    b.place(x=1215,y=420)


    def ok():
        print("ok")
        

    def ap(image):
        root = Toplevel()
        root.geometry("400x300+500+200")
        canvas=Canvas(root,width=400,height=300)
        canvas.create_image(200,150,anchor="center",image=image)
        def leave():
            root.destroy()
        b=Button(canvas,text="Fermer",bg="red4",width=8,command=leave)
        b.place(x=330,y=268)
        canvas.pack()
        root.mainloop()
        
    im1=PhotoImage(file=r"images/aperçus/Entrées/salade_chevre_chaud.png") 
    def ap1():
        ap(im1)
    im2=PhotoImage(file=r"images/aperçus/Entrées/gaspacho.png")
    def ap2():
        ap(im2)
    im3=PhotoImage(file=r"images/aperçus/Entrées/carpaccio_tomate.png")
    def ap3():
        ap(im3)
    im4=PhotoImage(file=r"images/aperçus/Entrées/terrine_avocat_crevette.png")
    def ap4():
        ap(im4)
    im5=PhotoImage(file=r"images/aperçus/Entrées/oeuf_mimosa.png")
    def ap5():
        ap(im5)
    im6=PhotoImage(file=r"images/aperçus/Entrées/veloute_blanc.png")
    def ap6():
        ap(im6)
    im7=PhotoImage(file=r"images/aperçus/Entrées/falafels.png")
    def ap7():
        ap(im7)
    im8=PhotoImage(file=r"images/aperçus/Entrées/salade_cesar.png")
    def ap8():
        ap(im8)
    im9=PhotoImage(file=r"images/aperçus/Entrées/tataki_thon_rouge.png")
    def ap9():
        ap(im9)
    im10=PhotoImage(file=r"images/aperçus/Entrées/bruschetta.png")
    def ap10():
        ap(im10)
        
    im11=PhotoImage(file=r"images/aperçus/Plats/plateau_du_boucher.png")
    def ap11():
        ap(im11)
    im12=PhotoImage(file=r"images/aperçus/Plats/burger_savoyard.png")
    def ap12():
        ap(im12)    
    im13=PhotoImage(file=r"images/aperçus/Plats/dinde_forestiere.png")
    def ap13():
        ap(im13)
    im14=PhotoImage(file=r"images/aperçus/Plats/poisson_provencale.png")
    def ap14():
        ap(im14)
    im15=PhotoImage(file=r"images/aperçus/Plats/seiche_plancha.png")
    def ap15():
        ap(im15)
    im16=PhotoImage(file=r"images/aperçus/Plats/spaghetti_fruits_de_mer.png")
    def ap16():
        ap(im16)
    im17=PhotoImage(file=r"images/aperçus/Plats/ratatouille.png")
    def ap17():
        ap(im17)
    im18=PhotoImage(file=r"images/aperçus/Plats/lasagnes_vege.png")
    def ap18():
        ap(im18)
    im19=PhotoImage(file=r"images/aperçus/Plats/risotto_truffe.png")
    def ap19():
        ap(im19)
    im20=PhotoImage(file=r"images/aperçus/Plats/assiette_friture.png")
    def ap20():
        ap(im20)
    im21=PhotoImage(file=r"images/aperçus/Desserts/tiramisu.png")
    def ap21():
        ap(im21)
    im22=PhotoImage(file=r"images/aperçus/Desserts/dame_blanche.png")
    def ap22():
        ap(im22)
    im23=PhotoImage(file=r"images/aperçus/Desserts/cafe_gourmand_choux.png")
    def ap23():
        ap(im23)
    im24=PhotoImage(file=r"images/aperçus/Desserts/fondant_choco.png")
    def ap24():
        ap(im24)
    im25=PhotoImage(file=r"images/aperçus/Desserts/panna_cotta.png")
    def ap25():
        ap(im25)
    im26=PhotoImage(file=r"images/aperçus/Desserts/creme_brulee.png")
    def ap26():
        ap(im26)
    im27=PhotoImage(file=r"images/aperçus/Desserts/browkie.png")
    def ap27():
        ap(im27)
    im28=PhotoImage(file=r"images/aperçus/Desserts/ile_flottante.png")
    def ap28():
        ap(im28)
    im29=PhotoImage(file=r"images/aperçus/Desserts/banana_split.png")
    def ap29():
        ap(im29)
    im30=PhotoImage(file=r"images/aperçus/Desserts/riz_au_lait.png")
    def ap30():
        ap(im30)
    im31=PhotoImage(file=r"images/aperçus/Desserts/cremeux_poire_speculoos.png")
    def ap31():
        ap(im31)
    im32=PhotoImage(file=r"images/aperçus/Desserts/mousse_choco.png")
    def ap32():
        ap(im32)

        
    b1 = Button(canvas1,image=oeil,bg="white",borderwidth=0.2,command=ap1)
    b1.place(x=480,y=90)
    b2 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap2)
    b2.place(x=480,y=140)
    b3 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap3)
    b3.place(x=480,y=192)
    b4 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap4)
    b4.place(x=480,y=250)
    b5 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap5)
    b5.place(x=480,y=300)
    b6 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap6)
    b6.place(x=480,y=340)
    b7 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap7)
    b7.place(x=480,y=415)
    b8 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap8)
    b8.place(x=480,y=480)
    b9 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap9)
    b9.place(x=480,y=555)
    b10 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap10)
    b10.place(x=480,y=620)

    b11 = Button(canvas1,image=oeil,bg="white",borderwidth=0.1,command=ap11)
    b11.place(x=1065,y=115)
    b12 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap12)
    b12.place(x=1065,y=200)
    b13= Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap13)
    b13.place(x=1065,y=280)
    b14 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap14)
    b14.place(x=1065,y=350)
    b15 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap15)
    b15.place(x=1065,y=420)
    b16 = Button(canvas1,image=oeil,bg="white",borderwidth=0,command=ap16)
    b16.place(x=1065,y=520)


    

    canvas1.pack()
    




