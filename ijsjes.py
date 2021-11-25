opnieuw='y'
print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
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
def bakjeofhoorntje():
	while True:
		bakje = input(f'Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje?').lower()
		if bakje=='a':
			bakje = 'Hoorntje'
			return bakje
		elif bakje=='b':
			bakje = 'Bakje'
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
while opnieuw=='y':
	aantal = vraagbolljes()
	bakje = bakjeofhoorntje()
	opnieuw = again()
input("press enter to exit")