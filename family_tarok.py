#!/usr/bin/env python
# -*- coding: utf-8 -*-
#DIAGRAM POTEKA V DOKUMENTACIJI
from tkinter import *
import tkinter as tk
#import tkMessageBox
#import ttk
#TODO: lepše uredi kodo: prazne vrstice vmes, bolj logični komentarji (če sploh bodo)
global rows
rows = 4 #definira vrstice

def glavna(col_sums):
	#oblika glavnega okna
	root.title("Glavna")
	root.geometry("675x400-200-150")
	root.resizable(width=True, height=True)
	
	#oznake stalnih vrstic
	Label(c, text="Igralci", font = (None, 15), padx=10).grid(row=0, column=0)
	Label(c, text="Radlci", font = (None, 15), padx=10).grid(row=1, column=0)
	Label(c, text="VSOTA", font = (None, 15), padx=10).grid(row=2, column=0)
	
	#seznam imen !!! bo iz nastavitev dobil spremenljivke
	global names
	names = ["A", "B", "C", "D", "E"]
	
	#spremenljivke, ki igralcem štejejo radlce
	rad1 = IntVar()
	rad2 = IntVar()
	rad3 = IntVar()
	rad4 = IntVar()
	rad5 = IntVar()
	global rads
	rads = [rad1,rad2,rad3,rad4,rad5]
	
	#stalna polja, kjer so imena, radlci in vsote posameznih igralcev
	for i in range(5): #5 bo nadomeščena s spremenljivko št. igralcev (v nastavitvah)
		Label(c, width = 10, text = names[i], relief=SUNKEN, borderwidth=4).grid(row=0,column=i+1, columnspan=1)
		Label(c, width = 10, text = rads[i].get(), relief=SUNKEN, borderwidth=4).grid(row=1,column=i+1, columnspan=1)
		Label(c, width = 10, text = col_sums[i].get(), relief=SUNKEN, borderwidth=4).grid(row=2,column=i+1, columnspan=1)
	Label(c, text=" ").grid(row=3, column=0) #prazna vrstica za estetiko. Mogoče črta-razišči
	
	#global rows
	#gumbi s funkcijami, TODO: nastavitve, shranjevanje
	Button(c, text="Vnesi igro", width = 10, command = lambda: vnesi_igro(root)).grid(row=0, column=6, padx=10)
	Button(c, text="!Nastavitve!", width = 10, command = lambda: nastavitve()).grid(row=2, column=6, padx=10)
	Button(c, text="!Shrani!", width = 10, command = lambda: shrani()).grid(row=1, column=6, padx=10)
	Button(c, text="Izhod", width=10, command = lambda: root.destroy()).grid(row=10, column=6, padx=10)
	
def vnesi_igro(root):
	#definira novo okno
	global window
	window=Tk()
	window.title("Zmaga?")
	window.resizable(width=False,height=False)
	#gumbi z izbiro zmaga DA/NE ali KLOP
	Button(window, text="DA", width = 8, borderwidth=2, command = lambda: game(True)).grid(row=0, column=0, padx=2, pady=2)
	Button(window, text="NE", width = 8, borderwidth=2, command = lambda: game(False)).grid(row=0, column=1, padx=2, pady=2)
	Button(window, text="KLOP", width=16, borderwidth=2, command= lambda: klop()).grid(row=1, columnspan=2, padx=5, pady=2)

def game(vict):
	#zapre prejšnje okno
	window.destroy()
	global zmaga
	zmaga = vict
	#novo okno
	w=Tk()
	w.title("Igra")
	
	#spremenljivke, ki shranjujejo izbrane vrednosti iger in napovedi
	igra=IntVar(w)
	t=IntVar(w)
	k=IntVar(w)
	zk=IntVar(w)
	zp=IntVar(w)
	v=IntVar(w)
	
	#seznam imen in vrednosti iger
	vseigre = [("3", 10), ("2", 20), ("1", 30), ("Solo 3", 40), ("Solo 2", 50),
	("Solo 1", 60), ("Berač", 70), ("Solo brez", 100), ("Barvni valat", 125)]
	i=0
	#ustvarjanje gumbov iz seznama
	for text, val in vseigre:
		Radiobutton(w, text=text, value=val, variable=igra).grid(row=i, column=0)
		i+=1
	#posebnost- brez trule mora biti z drugim predznakom glede na zmago
	if zmaga == True:
		brez = -10
	else:
		brez = 10

	#seznam imen in vrednosti napovedi
	napovedi = [("Trula", 10, t, 1), ("Kralji", 10, k, 1), ("Zadnji pagat", 25, zp, 1), ("Zadnji kralj", 10, zk, 1), ("Brez trule", brez, t, 1),
	("Napovedana trula", 20, t, 2), ("Napovedani kralji", 20, k, 2), ("Napovedan z. pagat", 50, zp, 2), ("Napovedan z. kralj", 20, zk, 2)]
	i=0
	#ustvarjanje gumbov iz seznama
	for text, val, vari, col in napovedi:
		Radiobutton(w, text=text, value=val, variable=vari).grid(row=i, column=col)
		i += 1
		if i == 5: #zato, da gredo v dva stolpca
			i=0
	
	if zmaga == True: #ponudi valat kot možnost le ob zmagi
		valat = Radiobutton(w, text="Valat", value = 250, variable=v).grid(row=5, column=1)
		nvalat = Radiobutton(w, text="Napovedan valat", value = 500, variable=v).grid(row=5, column=2)
	#gumb za nadaljevanje
	Button(w, text="POTRDI", command = lambda: sestej(w, zmaga)).grid(row=8, column=1)
	
	def sestej(w, zmaga):
		#preveri, ali je izbrana igra
		if igra.get()==0:
			tkMessageBox.showerror(title="NAPAKA", message="Niste izbrali igre!")
			return
		#spremenljivka, ki shrani vrednost vsote točk
		global summa
		summa=0
		#pridobivanje vrednosti iger in napovedi, shranjevanje v spremenljivke
		global vrIgre
		vrIgre= igra.get()
		trula= t.get()
		kralji= k.get()
		global zpagat
		zpagat= zp.get()
		zkralj= zk.get()
		global valat
		valat= v.get()
		global barvic
		barvic = False #ali se je igral barvni valat
		if valat == 0: #če ni bil valat
			li = [vrIgre, trula, kralji, zkralj]
			if vrIgre==125: #če je bil barvni valat
				li=[vrIgre]
				barvic = True
			elif vrIgre==70: #če je bil berač
				li = [vrIgre]
				kdo_je_igral(70, li, zmaga)
		else: #če je bil valat
			li = [valat]
			
		for i in li: #prišteje vse vrednosti iz seznama, k skupni vsoti
			summa += i
		kdo_je_igral(summa, li, zmaga)
		w.destroy() #zapre okno

def kdo_je_igral(summa, li, zmaga):
	#novo okno
	novo = Tk()
	novo.title("Kdo je igral?")
	igralca=[]
	"""if vrIgre != 70:
		if zmaga == False and li[1]==-10:
			summa += 20
			???
			"""
	
	global igralec1
	igralec1=IntVar(novo)
	#ustvari gumb za vsakega igralca
	i= 0
	while i < len(names):
		Radiobutton(novo, text=names[i], value=i+1, variable=igralec1).grid(row=i, column = 0)
		i+= 1
	igralca.append(igralec1)
	
	i=0
	if li[0] < 40: #če igralec ni igral sam, torej da ni šel solo3 ali več
		igralec2=IntVar(novo)
		igralca.append(igralec2)
		while i < len(names):
			b = Radiobutton(novo, text=names[i], value=i+1, variable=igralec2).grid(row=i, column = 1)
			i+= 1
	
	b = Button(novo, text = "POTRDI", command = lambda: now_what(igralca, summa, zmaga)).grid(row=5, column=0)
	
	def now_what(igralca, summa, zmaga):
		i = igralca[0].get()
		j = igralca[-1].get()
		global players
		players = []
		#preveri da sta oba igralca izbrana
		if i==0 or j==0:
			tkMessageBox.showerror(title="NAPAKA", message="Niste izbrali igralca!")
		else:
			players.append(i)
			players.append(j)
			if i==j:
				players.pop()
			novo.destroy() #uniči okno
			global pos
			if barvic==True or vrIgre==70:
				#print ("summa", summa)
				pos = False #ignoriraj rezultate posebnosti() - pomembno v write_to_players()
				write_to_players(players, summa)
				
			else:
				pos = True #upoštevaj rezultate posebnosti()
				razlika(summa, zmaga, players) #povprašaj za razliko
			
def razlika(summa, zmaga, players):
	#novo okno
	#global okno
	okno = Tk()
	okno.title("Razlika")
	label = Label(okno, text="Razlika (absolutna vrednost, zaokrožena na 5)").pack() #to bo v gumbu z navodili!
	diferenca=IntVar(okno)
	ent = Entry(okno, textvariable=diferenca).pack() #polje za vnos razlike
	ok = Button(okno, text="POTRDI", command=lambda: checking(diferenca.get(), summa)).pack() #gumb za nadaljevanje
	
	def checking(raz, summa):
		if raz >= 36 or raz < 0 or str(raz)[-1] not in ["0", "5"]: #preveri da razlika ustreza kriterijem
			tkMessageBox.showerror(title="NAPAKA", message="Neveljavna vrednost za razliko!")
		else:
			summa += raz #skupni vsoti doda razliko
			posebnosti(summa)
			okno.destroy()
			
def write_to_players(players, summa):
	#seznam s točkami posameznih igralcev
	points = [0,0,0,0,0]
	
	if zmaga == False: #v primeru poraza da vsoto v minus
		summa *= -1
		
	radl = rads[igralec1.get()-1].get()
	if radl >=1 and zmaga == True: #če ima tisti, ki je igral radlc in je zmagal
		summa *= 2 #podvoji vsoto
		brisi_radlc(igralec1) #igralcu briše radlc
	if pos == True: #če so posebnosti res (torej je zadnji pagat možen)
		pagat = zpagat*naredilzp.get() #vrednost (25/50) * naredil(1/-1)
		kdo = zadnjip.get()-1	#mestu igralca, ki je naredil v seznamu points
		pradl = rads[kdo].get() #število radlcev tega igralca
		
		if pradl >= 1 and pagat > 0: #če ima radlc in je naredil
			pagat *=2 #podvoji vrednost
			brisi_radlc(kdo) #izbriši 1 radlc temu igralcu
		
		points[kdo] += pagat #prištej točkam igralca zadnjega pagata
		
		if mond.get() != 6: #če je monda kdo izgubil
			points[mond.get()-1] -= 20 #odštej 20 (kazen za izgubljenega monda
			
		z.destroy() #uniči okno od posebnosti()
	global rows
	Label(c, text="Igra " + str(rows-3), font = (None, 10)).grid(row=rows, column=0) #oznaka z zap. številko igre
	
	if barvic==True or vrIgre==70 or valat == 500: #v katerem primeru pisati radlce
		pisi_radlc()
	
	for j in players: #vsakemu od igralcev (tistih, ki so igrali) prišteje vsoto
		points[j-1] += summa
	
	for i in range(5): #5 bo nadomestilo št. igralcev iz nastavitev
		j = col_sums[i]
		k = points[i]
		j.set(j.get()+k) #nastavi vrednost vsote stolpcev na novo vrednost in jo zapiše v stolpce
		Label(c, width = 10, text=col_sums[i].get(), relief=SUNKEN, borderwidth=4).grid(row=2,column=i+1, columnspan=1)
	
	
	if pos == True:	
		if mond.get() != 6: #če je kdo izgubil monda
			points[mond.get()-1] = str(points[mond.get()-1])
			points[mond.get()-1] += "☽" #pripiše lunico, da se ve, da je izgubil monda
	
	a=0
	for i in points:
		if len(players)==2: #če ni igral sam
			if a == (players[1]-1):
				i = str(i)
				i+="●" #pripiše pikico tistemu, ki ni igral
		a += 1 #napiše točke posameznih igralcev v vrstico v tabeli
		Label(c, width=10, borderwidth=4, text=i, relief=SUNKEN).grid(row=rows, column=a)
	rows += 1 #doda še eno vrstico

			
			
# obvezno zadnja stvar, ki se zgodi v programu - da se osveži scrollbar (PREVOD?!?!?!?)
	root.update()
	f.config(scrollregion=f.bbox("all"))
	

def pisi_radlc():
	k=0
	for i in rads: #vsaki spremenljivki za radlce
		k += 1
		i.set(i.get()+1) #prištej ena in prepiši vrednost v tabelo v vrstico RADLCI
		Label(c, width = 10, text=i.get(),  relief=SUNKEN, borderwidth=4).grid(row=1,column=k, columnspan=1)

def brisi_radlc(komu): #briše radlc igralcu, ki ga podamo v argumentu
	i = rads[komu.get()-1] #v seznamu radlcev poišče igralca
	i.set(i.get()-1) #odšteje 1 radlc
	k=0
	for i in rads: #prepiše vrednosti za radlce v tabelo
		Label(c, width = 10, text=i.get(),  relief=SUNKEN, borderwidth=4).grid(row=1,column=k+1, columnspan=1)
		k+=1

def posebnosti(summa):
	global z #novo okno
	z = Tk()
	z.title("Posebnosti")
	global mond #spremenljivke za izgubljenega monda in zadnjega pagata- ker se piše igralcu, ne pa ekipi
	mond=IntVar(z)
	mond.set(6) #privzeto vrednost za igubljenega monda nastavi na "Nihče"
	global zadnjip
	zadnjip=IntVar(z)
	global naredilzp
	naredilzp=IntVar(z)
	Label(z, text="Izgubljen \nmond").grid(row=0,column=0)
	names.append("Nihče")
	x=0
	for i in names: #ustvari gumbe za izbor igralca, ki je izgubil monda
		x+=1
		Radiobutton(z, text=i, value=x, variable=mond).grid(row=x, column=0, sticky=W)
	names.remove("Nihče")
	x=0
	if zpagat != 0: #v primeru da se je igral zadnji pagat
		Label(z, text="Zadnji \npagat").grid(row=x, column=1)
		for i in names: #ustvari gumbe za izbor igralca, ki je delal zadnjega pagata
			x+=1
			Radiobutton(z, text=i, value=x, variable=zadnjip).grid(row=x, column=1)
		Label(z, text="Ali je \nnaredil?").grid(row=0, column=2) #izbor možnosti, ali je naredil
		Radiobutton(z, text="DA", value=1, variable=naredilzp).grid(row=1, column=2)
		Radiobutton(z, text="NE", value=-1, variable=naredilzp).grid(row=2, column=2)
	
	
	#gumb za nadaljevanje
	Button(z, text="POTRDI", width=10, command=lambda: write_to_players(players, summa)).grid(row=3, column=2)



def klop():
	window.destroy()
	okno = Tk()
	okno.title("Klop")
	c=0
	global pl1
	pl1 = IntVar(okno)
	global pl2
	pl2 = IntVar(okno)
	global pl3
	pl3 = IntVar(okno)
	global pl4
	pl4 = IntVar(okno)
	global pl5
	pl5 = IntVar(okno)
	
	idk = [("A", pl1),("B", pl2),("C", pl3),("D", pl4),("E", pl5)]
	for i, j in idk:
		Label(okno, text=i).grid(row=c, column=1)
		Entry(okno, textvariable=j).grid(row=c, column=2)
		c+=1
		
	Button(okno, text="POTRDI", command=lambda: pristej(okno)).grid(row=c, columnspan=2)


def pristej(okno):
	global rows
	scores = [pl1.get()*-1,pl2.get()*-1,pl3.get()*-1,pl4.get()*-1,pl5.get()*-1]
	vsota = 0
	for i in scores:
		vsota += i*-1
		if str(i)[-1] not in ["0","5"]:
			tkMessageBox.showerror(title="NAPAKA", message="Napačne vrednosti!")
			return
	#print ( "points", scores)
	b=70
	points=[0,0,0,0,0]
	pl = IntVar()
	for i in range(5):
		if scores[i] == 0:
			points[i]=70
			
		elif scores[i] <= -36:
			points[i]=-70
		else:
			for j in points:
				if j == 70 or j == -70:
					break
				else:
					points[i]=scores[i]
	
	prazni = 0
	polni = 0
	if 70 in points or -70 in points:
		for i in range(5):
			if points[i] != 70 and points[i] != -70:
				points[i] = 0
			elif points[i] == 70:
				prazni += 1
			elif points[i] == -70:
				polni += 1
	if prazni > 3 or polni > 1 or vsota != 70:
		tkMessageBox.showerror(title="NAPAKA", message="Napačne vrednosti!")
		return
	for a in range(5):
		radl = rads[a].get()
		if radl >=1 :
			points[a] *= 2
			if points[a] > 0:
				#print "rads" ,rads[i].get()
				pl.set(a+1)
				#print "pl", pl.get()
				brisi_radlc(pl)
		Label(c, width=10, borderwidth=4, text=points[a], relief=SUNKEN).grid(row=rows, column=a+1)
	rows += 1
	#print points
	okno.destroy()
	for i in range(5):
		j = col_sums[i]
		k = points[i]
		j.set(j.get()+k)
		Label(c, width = 10, text=col_sums[i].get(), relief=SUNKEN, borderwidth=4).grid(row=2,column=i+1, columnspan=1)
	pisi_radlc()
#zadnja stvar, ki se zgodi
	root.update()
	f.config(scrollregion=f.bbox("all"))




























#DO NOT GO BELOW THIS LINE!

root=tk.Tk()
global vscrollbar
vscrollbar = tk.Scrollbar(root)

f= tk.Canvas(root,yscrollcommand=vscrollbar.set)
c=tk.Frame(f)
f.pack(side=LEFT,expand=True,fill=BOTH)
f.create_window(0,0,window=c, anchor='nw')
vscrollbar.config(command=f.yview)
vscrollbar.pack(side=RIGHT,fill=Y)
	
	
	
root.update()
f.config(scrollregion=f.bbox("all"))

col1 = IntVar(root)
col2 = IntVar(root)
col3 = IntVar(root)
col4 = IntVar(root)
col5 = IntVar(root)
global col_sums
col_sums = [col1, col2, col3, col4, col5]

glavna(col_sums)
root.mainloop()
