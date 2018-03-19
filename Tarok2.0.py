
from tkinter import *
import tkinter as tk
from tkinter import messagebox

global rows
rows = 4
global vse_igre
vse_igre = []

def glavna(col_sums):

	while len(rads) > pl_num:
		del rads[-1]
		del col_sums[-1]

	root.title("Glavna")
	root.geometry("675x400-200-150")
	root.resizable(width=True, height=True)
	
	if pl_num != 5:
		check = pl_num+1
		while check <=5:
			z = Label(c, text="", width=10, padx=10)
			z.grid(row=0, column=check)
			labels.append(z)
			check += 1
	
	z = Button(c, text="Vnesi igro", width = 10, command = lambda: vnesi_igro(root))
	z.grid(row=0, column=6, padx=10)
	labels.append(z)
	z = Button(c, text="Shrani igro", width = 10, command = lambda: shrani())
	z.grid(row=1, column=6, padx=10)
	labels.append(z)
	z = Button(c, text="Odpri igro", width = 10, command = lambda: odpri())
	z.grid(row=2, column=6, padx=10)
	labels.append(z)
	z = Button(c, text="Nastavitve", width = 10, command = lambda: nastavitve())
	z.grid(row=3, column=6, padx=10)
	labels.append(z)
	z = Button(c, text="Izhod", width=10, command = lambda: izhod())
	z.grid(row=4, column=6, padx=10)
	labels.append(z)

def vnesi_igro(root):

	global window
	window=Tk()
	window.title("Kaj se je zgodilo?")
	window.resizable(width=False,height=False)

	Button(window, text="ZMAGA", width = 8, borderwidth=2, command = lambda: game(True)).grid(row=0, column=0, padx=2, pady=2)
	Button(window, text="NI ZMAGE", width = 8, borderwidth=2, command = lambda: game(False)).grid(row=0, column=1, padx=2, pady=2)
	Button(window, text="KLOP", width=8, borderwidth=2, command= lambda: klop()).grid(row=1, column=0, padx=5, pady=2)
	Button(window, text="RENONS", width=8, borderwidth=2, command= lambda: renons()).grid(row=1, column=1, padx=5, pady=2)

def game(vict):

	window.destroy()
	global zmaga
	zmaga = vict
	w=Tk()
	w.title("Igra")
	
	igra=IntVar(w)
	t=IntVar(w)
	k=IntVar(w)
	zk=IntVar(w)
	zp=IntVar(w)
	v=IntVar(w)
	global kontra
	kontra=IntVar(w)
	kontra.set(1)

	if pl_num != 3:
		vseigre = [("3", 10), ("2", 20), ("1", 30), ("Solo 3", 40), ("Solo 2", 50),
		("Solo 1", 60), ("Berač", 70), ("Solo brez", 80), ("Odprti berač", 90), ("Barvni valat", 125)]
	else:
		vseigre = [("3", 10), ("2", 20), ("1", 30), ("Berač", 70), ("Odprti berač", 90), ("Barvni valat", 125)]
	
	i=0
	for text, val in vseigre:
		Radiobutton(w, text=text, value=val, variable=igra).grid(row=i, column=0)
		i+=1
	if zmaga == True:
		brez = -10
	else:
		brez = 10

	napovedi = [("Trula", 10, t, 1), ("Kralji", 10, k, 1), ("Zadnji pagat", 25, zp, 1), ("Zadnji kralj", 10, zk, 1), ("Brez trule", brez, t, 1),
	("Napovedana trula", 20, t, 2), ("Napovedani kralji", 20, k, 2), ("Napovedan z. pagat", 50, zp, 2),
	("Napovedan z. kralj", 20, zk, 2)]
	
	i=0
	for text, val, vari, col in napovedi:
		Radiobutton(w, text=text, value=val, variable=vari).grid(row=i, column=col)
		i += 1
		if i == 5:
			i=0
	
	if zmaga == True:
		valat = Radiobutton(w, text="Valat", value = 250, variable=v).grid(row=5, column=1)
		nvalat = Radiobutton(w, text="Napovedan valat", value = 500, variable=v).grid(row=5, column=2)
	kontre = [("Kontra", 2, kontra, 1), ("Sub-kontra", 8, kontra, 1), 
	("Re-kontra", 4, kontra, 2), ("Mord-kontra", 16, kontra, 2)]
	
	i=6
	for text, val, vari, col in kontre:
		Radiobutton(w, text=text, value=val, variable=vari).grid(row=i, column=col)
		i+=1
		if i == 8:
			i=6
	Button(w, text="POTRDI", command = lambda: sestej(w, zmaga)).grid(row=8, column=1)
	
	def sestej(w, zmaga):
		
		if igra.get()==0:
			messagebox.showerror(title="NAPAKA", message="Niste izbrali igre!")
			return
		
		global summa
		summa=0
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
		barvic = False
		
		if valat == 0:
			if vrIgre==125:
				li=[vrIgre]
				barvic = True
				kdo_je_igral(125, li, zmaga)
			
			elif vrIgre==70:
				li = [vrIgre]
				kdo_je_igral(70, li, zmaga)
			
			else:
				li = [vrIgre, trula, kralji, zkralj]
				for i in li:
					summa += i
				kdo_je_igral(summa, li, zmaga)
		
		elif valat != 0 and vrIgre==70:
			li=[vrIgre]
			kdo_je_igral(70, li, zmaga)
		
		else:
			li = [valat]
			kdo_je_igral(valat, li, zmaga)
		
		w.destroy()

def kdo_je_igral(summa, li, zmaga):
	
	novo = Tk()
	novo.title("Kdo je igral?")
	igralca=[]

	global igralec1
	igralec1=IntVar(novo)
	names2=names

	if pl_num == 5:
		global insert
		insert = names2.index(mesalec)
		for i in names2:
			h = names2.index(i)
			if h == insert:
				pass
			
			else:			
				Radiobutton(novo, text=i, value=h+1, variable=igralec1).grid(row=h, column = 0)

	else:
		for i in names2:
			h = names2.index(i)
			Radiobutton(novo, text=i, value=h+1, variable=igralec1).grid(row=h, column = 0)
	igralca.append(igralec1)
	
	if li[0] < 40 and pl_num != 3:
		global igralec2
		igralec2=IntVar(novo)
		igralca.append(igralec2)
		
		if pl_num == 5:
			for i in names2:
				h = names2.index(i)
				if h == insert:
					pass
				
				else:
					Radiobutton(novo, text=i, value=h+1, variable=igralec2).grid(row=h, column = 1)
		
		else:
			for i in names2:
				h = names2.index(i)
				Radiobutton(novo, text=i, value=h+1, variable=igralec2).grid(row=h, column = 1)

	b = Button(novo, text = "POTRDI", command = lambda: now_what(igralca, summa, zmaga)).grid(row=5, column=0)
	
	def now_what(igralca, summa, zmaga):
		
		i = igralca[0].get()
		j = igralca[-1].get()
		global players
		players = []
		
		if i==0 or j==0:
			messagebox.showerror(title="NAPAKA", message="Niste izbrali igralca!")
		
		else:
			players.append(i)
			players.append(j)
			if i==j:
				players.pop()
			novo.destroy()
			global pos
			if barvic==True or vrIgre==70:
				pos = False
				write_to_players(players, summa)
				
			else:
				pos = True
				razlika(summa, zmaga, players)
			
def razlika(summa, zmaga, players):
	
	okno = Tk()
	okno.title("Razlika")
	label = Label(okno, text="Razlika (absolutna vrednost, zaokrožena na 5)").pack()
	diferenca=IntVar(okno)
	ent = Entry(okno, textvariable=diferenca).pack()
	ok = Button(okno, text="POTRDI", command=lambda: checking(diferenca.get(), summa)).pack()

	def checking(raz, summa):
		
		if raz >= 36 or raz < 0 or str(raz)[-1] not in ["0", "5"]:
			messagebox.showerror(title="NAPAKA", message="Neveljavna vrednost za razliko!")
		
		else:
			summa += raz

			if zmaga == False:
				summa *= -1
			
			posebnosti(summa)
			okno.destroy()
			
def write_to_players(players, summa):
	
	global kdo
	global rows
	points = []
	
	for i in range(pl_num):
		points.append(0)

	try:
		radl = rads[int(players[0])-1].get()
	except NameError:
		radl = rads[kdo].get()

	try: 	
		summa *= kontra.get()
	except NameError:
		pass

	if radl >=1:
		summa *= 2
		if summa >= 0:
			brisi_radlc(igralec1)
	
	if pos == True:
		pagat = zpagat*naredilzp.get()
		kdo = zadnjip.get()-1
		pradl = rads[kdo].get()
		if pradl >= 1 and pagat > 0:
			pagat *=2
			brisi_radlc(kdo)
		
		points[kdo] += pagat
		
		if mond.get() != (pl_num+1):
			points[mond.get()-1] -= 20
			
	try:
		kec.destroy()
	except TclError:
		pass
	except NameError:
		pass
	
	rows += 1    
	to_add = []
	z=Label(c, text="Igra " + str(rows-3), font = (None, 10))
	z.grid(row=rows, column=0) 
	labels.append(z)
	
	if barvic==True or vrIgre==70 or valat == 500:
		pisi_radlc()
	
	for j in players:
		points[j-1] += summa
	
	for i in range(pl_num):
		j = col_sums[i]
		k = points[i]
		j.set(j.get()+k)
		Label(c, width = 10, text=col_sums[i].get(), relief=SUNKEN, borderwidth=4).grid(row=2,column=i+1, columnspan=1)
	
	if pos == True:	
		if mond.get() != pl_num+1:
			points[mond.get()-1] = str(points[mond.get()-1])
			points[mond.get()-1] += " M"
	
	a=0
	for i in points:
		if len(players)==2:
			if a == (players[1]-1):
				i = str(i)
				i+=" X"
		
		a += 1
		to_add.append(str(i))
		z = Label(c, width=10, borderwidth=4, text=i, relief=SUNKEN)
		z.grid(row=rows, column=a)
		labels.append(z)
	
	root.update()
	f.config(scrollregion=f.bbox("all"))
	mesanje(rows-3, names)		
	vse_igre.append(to_add)


def mesanje(g, namesx):
	
	global nalepka
	try:
		nalepka.destroy()
	except NameError:
		pass
		
	while g >= pl_num:
		g -= pl_num
	
	global mix
	mix = g
	global mesalec
	mesalec = namesx[g]
	nalepka = Label(c, text="Meša: "+mesalec, font=(None, 15))
	nalepka.grid(row=5, column=6)
	return mesalec
	
	root.update()
	f.config(scrollregion=f.bbox("all"))

def pisi_radlc():
	
	k=0
	
	for i in rads:
		k += 1
		i.set(i.get()+1)
		Label(c, width = 10, text=i.get(),  relief=SUNKEN, borderwidth=4).grid(row=1,column=k, columnspan=1)

def brisi_radlc(komu):
	
	i = rads[komu.get()-1]
	i.set(i.get()-1)
	k=0
	
	for i in rads:
		Label(c, width = 10, text=i.get(),  relief=SUNKEN, borderwidth=4).grid(row=1,column=k+1, columnspan=1)
		k+=1

def posebnosti(summa):
	
	global kec
	kec = Tk()
	kec.title("Posebnosti")
	global mond
	mond=IntVar(kec)
	mond.set(pl_num+1)
	global zadnjip
	zadnjip=IntVar(kec)
	global naredilzp
	naredilzp=IntVar(kec)
	Label(kec, text="Izgubljen \nmond").grid(row=0,column=0)
	names.append("Nihče")
	x=0
	
	for i in names:
			x += 1
			Radiobutton(kec, text=i, value=x, variable=mond, width=10).grid(row=x, column=0, sticky=W)
	names.remove("Nihče")
	x=0
	
	if zpagat != 0:
		Label(kec, text="Zadnji \npagat").grid(row=x, column=1)
		
		for i in names:
			if x == insert:
				x += 1
			else:
				x+=1
				
				Radiobutton(kec, text=i, value=x, variable=zadnjip).grid(row=x, column=1)
		Label(kec, text="Ali je \nnaredil?").grid(row=0, column=2)
		Radiobutton(kec, text="DA", value=1, variable=naredilzp).grid(row=1, column=2)
		Radiobutton(kec, text="NE", value=-1, variable=naredilzp).grid(row=2, column=2)

	Button(kec, text="POTRDI", width=10, command=lambda: write_to_players(players, summa)).grid(row=3, column=2)

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
	
	global names2
	names2 = []
	
	for i in names:
		names2.append(i)
	
	idk = [pl1, pl2, pl3, pl4, pl5]
	
	if pl_num == 5:
		idk.remove(idk[mix])
		names2.remove(names2[mix])
	
	else:
		while len(idk) != pl_num:
			idk.remove(idk[-1])
	
	for i in range(len(idk)):
		Label(okno, text=names2[i]).grid(row=c, column=1)
		Entry(okno, textvariable=idk[i]).grid(row=c, column=2)
		c+=1
		
	Button(okno, text="POTRDI", command=lambda: pristej(okno)).grid(row=c, columnspan=2)


def pristej(okno):
	
	global rows
	scores = [pl1.get()*-1,pl2.get()*-1,pl3.get()*-1,pl4.get()*-1,pl5.get()*-1]
	vsota = 0
	
	for i in scores:
		vsota += i*-1
		if str(i)[-1] not in ["0","5"]:
			messagebox.showerror(title="NAPAKA", message="Napačne vrednosti!")
			return
	
	b=70
	points=[]
	
	for i in range(pl_num):
		points.append(0)
	pl = IntVar()
	i = 0
	
	for i in range(pl_num):
		if i == mix:
			pass
		
		else:
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
		for i in range(pl_num):
			if points[i] != 70 and points[i] != -70:
				points[i] = 0
			
			elif points[i] == 70:
				prazni += 1
			
			elif points[i] == -70:
				polni += 1
	
	if prazni > 3 or polni > 1 or vsota != 70:
		messagebox.showerror(title="NAPAKA", message="Napačne vrednosti!")
		return
	
	rows += 1
	z = Label(c, width=10, borderwidth=4, text="Igra " + str(rows-3), font = (None, 10))
	z.grid(row=rows, column=0)
	labels.append(z)
	to_add = []
	
	for a in range(pl_num):
		radl = rads[a].get()
		
		if radl >=1 :
			points[a] *= 2
			if points[a] > 0:
				pl.set(a+1)
				brisi_radlc(pl)
		
		z = Label(c, width=10, borderwidth=4, text=points[a], relief=SUNKEN)
		z.grid(row=rows, column=a+1)
		labels.append(z)
		to_add.append(str(points[a]))
	
	vse_igre.append(to_add)
	okno.destroy()
	
	for i in range(pl_num):
		j = col_sums[i]
		k = points[i]
		j.set(j.get()+k)
		z = Label(c, width = 10, text=col_sums[i].get(), relief=SUNKEN, borderwidth=4)
		z.grid(row=2,column=i+1, columnspan=1)
		labels.append(z)
	
	pisi_radlc()
	mesanje(rows-3, names)

	root.update()
	f.config(scrollregion=f.bbox("all"))

def renons():
	
	window.destroy()
	global ha
	ha = Tk()
	ha.title("Renons")	
	global ren
	ren = StringVar(ha)
	ren.set(0)
	
	for i in range(pl_num):
		Radiobutton(ha, text=str(names[i]), variable = ren, value = i).grid(row=i, column=0)
	
	Button(ha, text="POTRDI", width = 10, command = lambda: dalje(ren)).grid(row=pl_num+1, column=0)

def dalje(ren):
	
	ha.destroy()
	global kdo
	kdo = int(ren.get())
	global jeRenons
	jeRenons = True
	global pos
	pos = False
	global barvic
	barvic = False
	global vrIgre
	vrIgre = 0
	global valat
	valat = 0
	write_to_players([kdo+1], -70)

def shrani():
	
	global w
	w=Tk()
	w.title("Izberi igro")
	w.geometry("300x300")
	global izbrana
	izbrana=IntVar(w)
	global novo_ime
	novo_ime=StringVar(w)
	j=0
	
	for i in datoteke:
		Radiobutton(w, text=i, width=10, value=j, variable=izbrana).grid(row=j, column=0)
		j+=1
	
	a = Radiobutton(w, text="                ", width=10, value=j, variable=izbrana)
	a.grid(row=j, column=0)
	Entry(a, width=8, textvariable=novo_ime).pack()
	Button(w, text="POTRDI", command=lambda: write_to_file(j)).grid(row=j+1, column=0)
	
def write_to_file(j):
	
	w.destroy()
	a = izbrana.get()
	if a == j:
		ime=novo_ime.get()
		ime+=".txt"
		global datoteke
		datoteke.append(ime)
		datoteke=sorted(datoteke)
	
	else:
		ime=datoteke[a]
	
	with open(ime, "a+") as s:
		s.truncate(0)
		for i in names:
			s.write(i)
			s.write(",")
		s.write("\n")
		
		for i in rads:
			s.write(str(i.get()))
			s.write(",")
		s.write("\n")
		
		for i in col_sums:
			s.write(str(i.get()))
			s.write(",")
		s.write("\n")
		mesanje(rows-4, names)
		s.write(mesalec)
		
		for i in vse_igre:
			s.write("\n")
			for j in i:
				s.write(j)
				s.write(",")			
	
	glavna(col_sums)

def nastavitve():
	
	x=Tk()
	x.title("Nastavitve")
	name1=StringVar(x)
	name2=StringVar(x)
	name3=StringVar(x)
	name4=StringVar(x)
	name5=StringVar(x)
	global imena
	imena=[name1, name2, name3, name4, name5]
	j=0
	
	for i in imena:
		Label(x, text="Ime "+str(j+1), width=10).grid(row=j, column=0, padx=10)
		Entry(x, text=i.get(), textvariable=i).grid(row=j, column=1, padx=10)
		j+=1
	Button(x, text="POTRDI", width=10, command=lambda: naprej(x)).grid(row=j+1, column=1, padx=10)

def naprej(x):
	
	x.destroy()
	global names
	names=[]
	count = 0
	
	for i in imena:
		if len(i.get()) != 0:
			names.append(i.get())
		
		count += 1
	global pl_num
	pl_num = len(names)
	mesanje(rows-4, names)
	napisi(names)

def odpri():
	
	for k in labels:
		k.pack_forget()
		k.destroy()
	
	global w
	w=Tk()
	w.title("Izberi igro")
	w.geometry("150x200")
	global car
	car = False
	global izbrana
	izbrana=IntVar(w)
	j=0
	names = []
	
	for i in datoteke:
		Radiobutton(w, text=i, width=10, value=j, variable=izbrana).grid(row=j, column=0)
		j+=1
	
	Button(w, text="POTRDI", width=10, command=lambda: napisi(names)).grid(row=j+1, column=0)
	Button(w, text="NOVA IGRA", width=10, command=lambda: nova_igra()).grid(row=j+2, column=0)
	
def napisi(namesx):
	
	glavna(col_sums)
	try:
		w.destroy()		
	except TclError:
		pass
	
	if car == False:
		ime=datoteke[izbrana.get()]
	
	else:
		ime="nova_igra.txt"
	count = 0
	global rows
	rows=0
	
	with open(ime) as s:
		global vrste
		vrste = s.readlines()
		
		for l in vrste:
			line = l.split(",")
			line.pop()
			
			while len(line) > pl_num:
				del line[-1]
			
			if rows == 0:
				z = Label(c, text="Igralci", font=(None, 15), padx=10)
				z.grid(row=rows, column=0)
				labels.append(z)
				
				if car == False:
					global names
					names = line
				
				for i in names:
					count+=1
					z = Label(c, text=i, borderwidth=4, relief=SUNKEN, width=10)
					z.grid(row=rows, column=count)
					labels.append(z)
				count = 0
				rows += 1
			
			elif rows == 1:
				z = Label(c, text="Radlci", font=(None, 15), padx=10)
				z.grid(row=rows, column=0)
				labels.append(z)
				
				for i in line:
					rads[count].set(i)
					count+=1
				count = 0
				
				for i in rads:
					count+=1
					z = Label(c, text=i.get(), borderwidth=4, relief=SUNKEN, width=10)
					z.grid(row=rows, column=count)
					labels.append(z)
				count = 0
				rows += 1
			
			elif rows == 2:
				z = Label(c, text="VSOTA", font=(None, 15), padx=10)
				z.grid(row=rows, column=0)
				labels.append(z)
				
				for i in line:
					col_sums[count].set(i)
					count+=1
				count = 0
				
				for i in col_sums:
					count+=1
					z = Label(c, text=i.get(), borderwidth=4, relief=SUNKEN, width=10)
					z.grid(row=rows, column=count)
					labels.append(z)
				
				count = 0
				rows += 1
				z = Label(c, text=" ")
				z.grid(row=rows, column=0)
				labels.append(z)
			
			elif rows == 3:
				mesanje(len(vrste)-4, names)
				rows += 1
			
			else:
				vse_igre.append(line)
				z = Label(c, text="Igra "+str(rows-3), font=(None, 10), padx=10)
				z.grid(row=rows, column=0)
				labels.append(z)
				
				for i in line:
					count+=1
					z = Label(c, text=i, borderwidth=4, relief=SUNKEN, width=10)
					z.grid(row=rows, column=count)
					labels.append(z)
				
				count = 0
				rows += 1
		
		s.close()
	glavna(col_sums)

def nova_igra():
	
	for i in labels:
		i.destroy()
	
	global car
	car = True
	nastavitve()	

def izhod():
	
	with open("config.txt", "a") as conf:
		conf.truncate(0)
		
		for i in datoteke:
			conf.write(i)
			conf.write(" ")

	root.destroy()

def zagon():
	
	with open("config.txt") as conf:
			i = conf.readline().rstrip()
			global datoteke
			datoteke = i.split()			
	odpri()



##################################################

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

global labels
labels = []

col1 = IntVar(root)
col2 = IntVar(root)
col3 = IntVar(root)
col4 = IntVar(root)
col5 = IntVar(root)
global col_sums
col_sums = [col1, col2, col3, col4, col5]

rad1 = IntVar()
rad2 = IntVar()
rad3 = IntVar()
rad4 = IntVar()
rad5 = IntVar()
global rads
rads = [rad1,rad2,rad3,rad4,rad5]

zagon()
root.mainloop()