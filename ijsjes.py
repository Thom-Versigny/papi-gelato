opnieuw='y'
bakjestellen='.'
toppingeidelijk=0
aantalhorentjes=0
aantalbakjes=0
aantaleindelijk=0
print("Welkom bij Papi Gelato")
def vraagbolljes():
	while True:
		aantal = int(input("Hoeveel bolletjes wilt u? "))
		if aantal == 1 or aantal == 2 or aantal == 3:
			return aantal
		elif aantal == 4 or aantal == 5 or aantal == 6 or aantal == 7 or aantal == 8:
			print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
			return aantal
		elif aantal > 8:
			print("Sorry, zulke grote bakken hebben we niet")
		else:
			print("Sorry dat snap ik niet...")
def smaakkiezen():
	Nbolletje = 1
	while Nbolletje <= aantal:
		smaak = input(f'Welke smaak wilt u voor bolletje nummer {Nbolletje}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?').lower()
		if smaak=='a' or smaak=='c' or smaak=='m' or smaak=='v':
			Nbolletje+=1
		else:
			print('Sorry dat snap ik niet...')
def bakjeofhoorntje():
	while True:
		bakje = input(f'Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje?').lower()
		if bakje=='a':
			global aantalhorentjes
			bakje = 'Hoorntje'
			aantalhorentjes+=1
			return bakje
		elif bakje=='b':
			global aantalbakjes
			bakje = 'Bakje'
			aantalbakjes+=1
			return bakje
		else:
			print("Sorry, dat snap ik niet...")
def topping():
	while True:
		toppingkeuze=input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?').lower()
		if toppingkeuze=='a':
			toppingkeuze=0
			return toppingkeuze
		elif toppingkeuze=='b':
			toppingkeuze=0.5
			return toppingkeuze
		elif toppingkeuze=='c':
			toppingkeuze=0.3
			return toppingkeuze
		elif toppingkeuze=='d':
			if bakje=='Hoorntje':
				toppingkeuze=0.6
				return toppingkeuze
			elif bakje=='Bakje':
				toppingkeuze=0.9
				return toppingkeuze
		else:
			print('Sorry dat snap ik niet...')
def again():
	while True:
		opnieuw = input(f'Hier is uw {bakje} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N)').lower()
		if opnieuw == 'y':
			return opnieuw
		elif opnieuw =='n':
			print('Bedankt en tot ziens!')
			return opnieuw
		else:
			print('Sorry, dat snap ik niet...')
def bonnnetje():
	if aantalbakjes>=1:
		totalbakje=f'Bakje     {aantalbakjes} x €0,75 = €{round(aantalbakjes*0.75, 2)}'
	else:
		totalbakje=''
	if aantalhorentjes>=1:
		totalhoorntje=f'hoorntje  {aantalhorentjes} x €1,25 = €{round(aantalhorentjes*1.25, 2)}'
	else:
		totalhoorntje=''
	if toppingeidelijk>=0.1:
		totaltopping=f'topping    1 x €{toppingeidelijk} = €{toppingeidelijk}'
	else:
		totaltopping=''
	totalbolletjes=f'Bolletjes {aantaleindelijk} x €1,10 = €{round(aantaleindelijk*1.10, 2)}'
	totaalmoney=f'Totaal                €{round(aantalbakjes*0.75, 2)+round(aantaleindelijk*1.10, 2)+round(aantalhorentjes*1.25, 2)+round(toppingeidelijk, 2)}'
	print(f"""---------["Papi Gelato"]---------

        {totalbolletjes}
        {totalhoorntje}
        {totalbakje}
        {totaltopping}
                              ------+
        {totaalmoney}""")
while opnieuw=='y':
	aantal = vraagbolljes()
	smaakkiezen()
	bakje = bakjeofhoorntje()
	toppingkeuze=topping()
	opnieuw = again()
	toppingeidelijk+=toppingkeuze
	aantaleindelijk+=aantal
bonnnetje()
input("press enter to exit")