from tkinter import *
from Stocks import main as mn

win = Tk()
win.geometry("700x350")
win.title("Aktier")
y, antal_entries, antal_text, y_värdetext = 0,0,0,0


namn = []
företag1 = {}
kör = False
företag = []
gammalt_v = []
nyaAktier = 0


def skapa_aktier():
    global  företag1, lista_namn,  gammalt_v
    lista_namn = []
    
    for loop in namn:
        företag1[loop] = 0
        lista_namn.append(loop)
        
    for loop in företag1:
        gammalt_v.append(0)
     
    #print (gammalt_v)
#stänga av programmet 
def stäng():
    global kör
    kör = False

    #print(plotAktie)
        

def på_start():
   global kör
   kör = True
  

def på_stopp():
   global kör
   kör = False

def konfimermation():
    
    global namn, antal_entries, nyaAktier
  
    for i in range(antal_entries):
        namn.append(skriv_rutor[i].get().upper())
    
    #    print(namn)
        skapa_aktier()
        
        nyaAktier +=1
    namn = list(dict.fromkeys(namn))
    #print(namn)

skriv_rutor = []
def lägg_till():
    global y, antal_entries

    if antal_entries <= 3:
        skriv_ruta = Entry(win)
        skriv_ruta.grid(row=y, column=0, pady=5, padx=5)
        skriv_rutor.append(skriv_ruta)
        antal_entries+=1 
        y+=1
    
    lägg_till_text()

text_rutor =[]
def lägg_till_text():
    global antal_text, y_värdetext
    if antal_text <= 3:
       text_ruta = Label(win)
       text_ruta.grid(row=y_värdetext, column=1, padx = 5, pady=5)
       text_rutor.append(text_ruta)
       antal_text+=1
       y_värdetext +=1 

def tabort():
    global antal_text, skriv_rutor, antal_entries
    if len(företag) >= 1:
        företag1.popitem()
        gammalt_v.pop(-1)
        företag.pop(-1)
        lista_namn.pop(-1)
        namn.pop(-1)
        
    
    text_rutor[-1].destroy()
    text_rutor.pop(-1)
    antal_entries-=1
    skriv_rutor[-1].destroy()
    skriv_rutor.pop(-1)
    antal_text-=1 


def print_text():
   global företag
  
   if kör:
        #själva programmet
        #print (företag1)
        for värde in range (len(företag1)):
            företag = mn(företag1)
        #    print (företag, 1 )
     
     #-------------------------------------
        #Jämförelse av priserna, via det gammla priset mot det nu varande
        #print (företag)
        #print (gammalt_v, "gammalt")
        for värde_f in range (len(namn)):
            """
            print (värde_f, "for, index ")
            print (företag[värde_f], "företag")
            print (gammalt_v[värde_f], "gammalt")
            print(text_rutor[värde_f], "text_rutor")
            """
            if företag[värde_f] > gammalt_v[värde_f]:
                text_rutor[värde_f].configure (text=f": {företag[värde_f]}$ ↑ +{round(företag[värde_f] - gammalt_v[värde_f],2 )}", fg= "green")
                
            
            elif företag[värde_f] < gammalt_v[värde_f]:
                text_rutor[värde_f].configure (text=f": {företag[värde_f]}$ ↓ -{round(gammalt_v[värde_f] - företag[värde_f], 2)}", fg= "red")
                
            else:
                text_rutor[värde_f].configure(text=f": {företag[värde_f]}$ 〃{round(gammalt_v[värde_f]- företag[värde_f], 2)}", fg="gray")
            gammalt_v.pop(värde_f)
            gammalt_v.insert(värde_f, företag[värde_f])
            

   win.after(1000, print_text)



x_värde = 210
start = Button(win, text="Start", command=på_start)
start.place(x=x_värde, y=150, anchor="center")

stopp_knapp = Button(win, text="Stop", command=på_stopp)
stopp_knapp.place(x=x_värde+40, y=150, anchor="center")

add_knapp = Button(win, text="Lägg till", command = lägg_till)
add_knapp.place(x=x_värde, y=190, anchor="center")

delete_knapp = Button(win, text="Ta bort", command=tabort)
delete_knapp.place(x = x_värde + 60, y=190, anchor="center")

confirm = Button(win, text= "Confirm", command=konfimermation)
confirm.place(x=x_värde, y=230, anchor="center")


win.after(1000, print_text)

win.mainloop()