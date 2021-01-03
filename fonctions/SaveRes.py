from tkinter import *
import sqlite3
import smtplib   #py -m pip install py-smtp
from email.mime.multipart import MIMEMultipart #py -m pip install email-to
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkcalendar import Calendar, DateEntry
from time import strptime, struct_time, localtime


def save(nom,prenom,nb_personnes,date_r,service,emplacement,user_mail,b6):
    """
    Enregistre les données de la réservation dans la table Reservation
    """
    try :
        systemDate = struct_time(localtime())
        userDate = strptime(date_r, '%m/%d/%y')
        assert userDate > systemDate    #vérifie que la date est valide        
        
        conn = sqlite3.connect("GP211.db")
        c = conn.cursor()
        c.execute("INSERT INTO Reservation (Nom,Prénom,Nb_personnes,Date,Heure,Emplacement,email) VALUES (?, ?, ?, ?, ?, ?, ?)",(nom, prenom, nb_personnes, date_r, service, emplacement,user_mail))
        conn.commit()
        n=nom
        p=prenom
        c.execute("SELECT n°_de_reservation FROM Reservation WHERE Nom=? AND Prénom=?",(n,p))
        num = c.fetchone()
        c.close()
        conn.close()
                  
        messagebox.showinfo("Réservation","Votre réservation est bien enregistrée !\n Votre numéro de réservation est le {}".format(num[0]))
                  
    except :
        messagebox.showwarning("Erreur","Date invalide !")

    if user_mail!="":
        try :
            email_user = 'chezjean.desproduitsdujardin@gmail.com'  #email de départ
            email_password = 'gp2112020!'                    #destinataire
            email_send = user_mail            

            subject = 'Votre réservation'     #objet

            msg = MIMEMultipart()   #creation du message
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            filename=r"images/Carte.pdf"     
            attachment=open(filename,'rb')                                  #ouverture du fichier

            body = prenom+" "+nom+", rendez-vous  le "+date_r+" dans notre restaurant !\nVotre numéro de réservation est le "+str(num[0])+"\nA très bientôt !"
            msg.attach(MIMEText(body,'plain'))                              #on attache le texte au message

            part = MIMEBase('application','octet-stream')   
            part.set_payload((attachment).read())
            encoders.encode_base64(part)                                    #Encodage de la piece en base64
            part.add_header('Content-Disposition',"attachment; filename= "+filename)
            msg.attach(part)        #on attache la piece au message
            
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)                     #connexion au serveur sortant (nom et port)
            server.starttls()                                               #spécification de la sécurisation du serveur
            server.login(email_user,email_password)                         #authentification

            server.sendmail(email_user,email_send,text)     #envoi
            server.quit()                                   #deconnexion

            messagebox.showinfo("Info","e-mail bien envoyé !")

        except:
            messagebox.showwarning("Erreur","Adresse e-mail invalide")
            
    b6.place(x=155,y=460)
