opnieuw='y'
bakjestellen='.'
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
	bolletjesgeld=aantaleindelijk*1.10
	hoorentjesgeld=aantalhorentjes*1.25
	bakjesgeld=aantalbakjes*0.75
	if bakje=='Hoorntje'and aantalbakjes<1:	
		print(f"""---------["Papi Gelato"]---------

		Bolletjes {aantaleindelijk} x €1,10 = €{round(bolletjesgeld, 2)}
		hoorntje  {aantalhorentjes} x €1,25 = €{round(hoorentjesgeld, 2)}
                                    ------+
		Totaal                €{round(bolletjesgeld+hoorentjesgeld, 2)}""")
	elif bakje=='Bakje'and aantalhorentjes<1:	
		print(f"""---------["Papi Gelato"]---------

		Bolletjes {aantaleindelijk} x €1,10 = €{round(bolletjesgeld, 2)}
		Bakje     {aantalbakjes} x €0,75 = €{round(bakjesgeld, 2)}
                                     ------+
		Totaal                €{round(bolletjesgeld+bakjesgeld, 2)}""")
	else:
		print(f"""---------["Papi Gelato"]---------

		Bolletjes {aantaleindelijk} x €1,10 = €{round(bolletjesgeld, 2)}
		hoorntje  {aantalhorentjes} x €1,25 = €{round(hoorentjesgeld, 2)}
		Bakje     {aantalbakjes} x €0,75 = €{round(bakjesgeld, 2)}
                                      ------+
		Totaal                €{round(bolletjesgeld+hoorentjesgeld+bakjesgeld, 2)}""")

while opnieuw=='y':
	aantal = vraagbolljes()
	smaakkiezen()
	bakje = bakjeofhoorntje()
	opnieuw = again()
	aantaleindelijk+=aantal
bonnnetje()
input("press enter to exit")