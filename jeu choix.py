import random


maxVal = 10
L5445 = random.choices(list(range(maxVal)), k = 5)
L4554 = random.choices(list(range(maxVal)), k = 5)



def Menu():
	jeu = int(input("Quel type de partie voulez-vous? \n - Normal - 1 \n - Attributs - 2\n - Completement barjo! - 3 \n - Règles - 4 \n"))
	if jeu == 1:
		dab = Equilibration(L5445,L4554) 
		CombatNormal(dab[0],dab[1])
	if jeu == 2:
		#dab = Equilibration(L5445,L4554) 
		#CombatAttribus(dab[0],dab[1])
		CombatAttribus([4,2,3,7,5],[1,1,1,1,1])
	if jeu == 4:
		print("Les règles de ce jeu sont simples: Deux joueurs ont chacun une liste de 5 nombres (dont la somme des nombres est égale). \n Il choisissent en même temps une nombre de leur liste (qui ne pourra plus être utilisé pour les futurs manchent). Le nombre le plus grand  gagne la manche, et le joueur avec le plus de manches gagné remporte la partie.") 
		Menu()


	return "m"

def Equilibration(L1,L2):
	somme1 = 0
	somme2 = 0
	for a in range (5):
		somme1 += L1[a]
		somme2 += L2[a]
	while somme1 != somme2:
		somme1 = 0
		somme2 = 0
		nombreRand = 0 
		for a in range(5):
			somme1 += L1[a]
			somme2 += L2[a]
		nombreRand = int(random.choices((list(range(5))), k = 1)[0])
		if somme1 > somme2:
			while L1[nombreRand] == 0:
				nombreRand = int(random.choices((list(range(5))), k = 1)[0])
			L1[nombreRand] = L1[nombreRand] - 1 
		elif somme2 > somme1:
			while L2[nombreRand] == 0:
				nombreRand = int(random.choices((list(range(5))), k = 1)[0])
			L2[nombreRand] = L2[nombreRand] - 1
				
	return (L1,L2)





def CombatNormal(L1,L2):
	print(L1,L2)
	pointJ1 = 0
	pointJ2 = 0 
	compteur = 0
	while compteur != 5:
		print("",L1, "\n", L2)
		choixJ1 = 0
		choixJ2 = 0
		choixJ1 = int(input("1er joueur, choissiez la position de votre choix: "))
		while choixJ1 > 5 or choixJ1 < 1 or L1[choixJ1-1] =="X":
			if choixJ1 > 5 or choixJ1 < 1 or L1[choixJ1-1] =="X":
				choixJ1 = int(input("Votre choix n'est pas valide. Réessayez. "))
		choixJ2 = int(input("2eme joueur, choissiez la position de votre choix: "))
		while choixJ2 > 5 or choixJ1 < 1 or L2[choixJ2-1] =="X":
			if choixJ2 > 5 or choixJ2 < 1 or L2[choixJ2-1] == "X":
				choixJ2 = int(input("Votre choix n'est pas valide. Réessayez. "))
		if L1[choixJ1-1] > L2[choixJ2-1]:
			pointJ1 +=  1
			print("Manche gagné par le Joueur 1! ", pointJ1 ," à ", pointJ2)
			L1[choixJ1-1] = "X"
			L2[choixJ2-1] = "X"
		elif L1[choixJ1-1] == L2[choixJ2-1]:
			if compteur == 4: 
				print("Egalité totale! Cette manche ne va à personne")
				compteur += 1
			else:
				print("Egalité! Manche à refaire")
			compteur -= 1
		else: 
			pointJ2 += 1
			print("Manche gagné par le Joueur 2! ", pointJ1 ," à ", pointJ2)
			L1[choixJ1-1] = "X"
			L2[choixJ2-1] = "X"
		compteur += 1
	if pointJ1 > pointJ2:
		print("Victoire du Joueur 1!")
	elif pointJ2 > pointJ1:
		print("Victoire du Joueur 2!")
	elif pointJ1 == pointJ2:
		print("Egalité! Personne ne gagne!")


def CombatAttribus(L1,L2):
	print(L1)
	L1apres = [-1,-1,-1,-1,-1]
	L2apres = [-1,-1,-1,-1,-1]
	
	for i in range(5):
		
		print(L1[i])
		posi = int(input("Joueur 1, à quelle position voulez vous mettre le nombre ci dessus ?"))
		
		while posi > 5 or posi < 1 or L1apres[posi-1] !=-1:
			
			if posi > 5 or posi < 1 or L1apres[posi-1] !=-1:
				posi = int(input("La position choisie n'est pas valide, ou déjà occupée. Reessayez."))
		L1apres[posi - 1] = L1[i]
	
	for i in range(5):
			
		if L1[i] == 0:
			Lverif = Verif0(L1apres,i)
		if L1[i] == 1:
			Lverif = Verif1(L1apres,i)
		if L1[i] == 2:
			Lverif = Verif2(L1apres,i)
		if L1[i] == 3:
			Lverif = Verif3(L1apres,i)
		if L1[i] == 4:
			Lverif = Verif4(L1apres,i)
		if L1[i] == 5:
			Lverif = Verif5(L1apres,i)
		if L1[i] == 6:
			Lverif = Verif6(L1apres,i)
		if L1[i] == 7:
			Lverif = Verif7(L1apres,i)
		if L1[i] == 8:
			Lverif = Verif8(L1apres,i)
		if L1[i] == 9:
			Lverif = Verif9(L1apres,i)

		Lfinal1 = Lverif
	print("Votre liste final est ", Lfinal1)
		
	print(L2)	
		
	for i in range(5):
		print(L2[i])
		posi = int(input("Joueur 2, à quelle position voulez vous mettre le nombre ci dessus ?"))
		
		while posi > 5 or posi < 1 or L2[posi-1] ==-1:
			
			if posi > 5 or posi < 1 or L2[posi-1] ==-1:
				posi = int(input("La position choisie n'est pas valide, ou déjà occupée. Reessayez."))
		L2apres[posi - 1] = L2[i]
	
	
	for i in range(5):
			
		if L2[i] == 0:
			Lverif = Verif0(L2apres,i)
		if L2[i] == 1:
			Lverif = Verif1(L2apres,i)
		if L2[i] == 2:
			Lverif = Verif2(L2apres,i)
		if L2[i] == 3:
			Lverif = Verif3(L2apres,i)
		if L2[i] == 4:
			Lverif = Verif4(L2apres,i)
		if L2[i] == 5:
			Lverif = Verif5(L2apres,i)
		if L2[i] == 6:
			Lverif = Verif6(L2apres,i)
		if L2[i] == 7:
			Lverif = Verif7(L2apres,i)
		if L2[i] == 8:
			Lverif = Verif8(L2apres,i)
		if L2[i] == 9:
			Lverif = Verif9(L2apres,i)

		Lfinal2 = Lverif
		
	print("Votre liste final est ", Lfinal2)
	
	print(Lfinal1, Lfinal2)		
	pointJ1 = 0
	pointJ2 = 0 
	compteur = 0
	while compteur != 5:
		choixJ1 = 0
		choixJ2 = 0
		choixJ1 = int(input("1er joueur, choissiez la position de votre choix: "))
		while choixJ1 > 5 or choixJ1 < 1 or Lfinal1[choixJ1-1] =="X":
			if choixJ1 > 5 or choixJ1 < 1 or Lfinal1[choixJ1-1] =="X":
				choixJ1 = int(input("Votre choix n'est pas valide. Réessayez. "))
		choixJ2 = int(input("2eme joueur, choissiez la position de votre choix: "))
		while choixJ2 > 5 or choixJ1 < 1 or Lfinal2[choixJ2-1] =="X":
			if choixJ2 > 5 or choixJ2 < 1 or Lfinal2[choixJ2-1] == "X":
				choixJ2 = int(input("Votre choix n'est pas valide. Réessayez. "))
		if Lfinal1[choixJ1-1] > Lfinal2[choixJ2-1]:
			pointJ1 +=  1
			print("Manche gagné par le Joueur 1! ", pointJ1 ," à ", pointJ2)
			Lfinal1[choixJ1-1] = "X"
			Lfinal2[choixJ2-1] = "X"
		elif Lfinal1[choixJ1-1] == Lfinal2[choixJ2-1]:
			if compteur == 4: 
				print("Egalité totale! Cette manche ne va à personne")
				compteur += 1
			else:
				print("Egalité! Manche à refaire")
			compteur -= 1
		else: 
			pointJ2 += 1
			print("Manche gagné par le Joueur 2! ", pointJ1 ," à ", pointJ2)
			Lfinal1[choixJ1-1] = "X"
			Lfinal2[choixJ2-1] = "X"
		print("",Lfinal1, "\n", Lfinal2)
		compteur += 1
	if pointJ1 > pointJ2:
		print("Victoire du Joueur 1!")
	elif pointJ2 > pointJ1:
		print("Victoire du Joueur 2!")
	elif pointJ1 == pointJ2:
		print("Egalité! Personne ne gagne!")
		
		
		
""" Attribus des nombres en jeu placé """

# - 0 - 

# - Si un joueur a 5 zeros APRES le placement des nombres, ses nombres deviennent tous des 8
# - Si il est placé sur la gauche de la liste:
#	- Tous les nombres pairs gagnent + 1 
#	- Tous les nombres impairs perdent - 1 
# - Si il est placé sur la droite de la liste:
#	- Tous les nombres pairs perdent - 1 
#	- Tous les nombres impairs gagnent + 1
# - Si il est placé au milieu de la liste rien ne se passe

# - 1 -

# - Tous les nombres à sa gauche perdent - 1
# - Tous les nombres à sa droite gagnent + 1 
# - Si il est en 5eme position, il gagne + 4

# - 2 -

# - Le nombre à sa droite est doublé
# - Le nombre à sa gauche est divisé par deux
# - Si il est en 5eme position, il gagne + 3

# - 3 - 

# - Si il est aux positions 1, 3 et 5, il gagne + 2 
# - Si il est aux positions 2 et 4 il perd - 2

# - 4 -

# - Si il est aux positions 1 ou 5, il gagne + 1
# - Si il est aux positions 2 ou 3 ou 4, il perd - 1

# - 5 - 

# - Il perd la moyenne des nombres à sa droite
# - Il gagne la moyenne des nombres à sa gauche

# - 6 -

# - Si il est en 4eme position, et que le total des 3eres positions est en dessous de 10, il gagne + 4
# - Si il n'est pas en 4eme position, il perd - 2

# - 7 - 

# - Si il est en 1ere position et que la 3eme position est au dessus de 5, il donne + 2 à la 3eme position
# - Si il n'est pas en 1ere position et que la 3eme position est au dessus de 5, il donne - 1 à toutes les positions

#  - 8 -

# - Si il est en 1ere position, il perd - 2 
# - Si il est en 2eme position, il perd - 1
# - Si il est en 4eme position, il gagne + 1
# - Si il est en 5eme position, il gagne + 2

# - 9 - 

# - Si il est en 1ere position:
#	- Tous les 9 perdent - 2
#	- Tous les 1 gagnent + 2
# - Si il est en 2eme position, il perd - 1
#	- Tous les 8 gagnent + 2
#	- Tous les 2 perdent - 2
# - Si il est en 3eme position, il gagne + 1
#	- Tous les 7 perdent - 2
#	- Tous les 3 gagnent + 2
# - Si il est en 5eme position, il gagne + 2
#	- Tous les 6 gagnent + 2
#	- Tous les 4 perdent - 2

""" Attribus des nombres en jeu placé """




""" Verification des attribus """ #Attention, les positions dans les descriptions sont une place plus haute que dans les fonctions

def Verif0(L, posi):
	LPlacePair = []
	LPlaceImpair = []
	for i in range (5):
		if pair(L[i]) == True:
			LPlacePair.append(i)
		elif pair(L[i]) == False:
			LPlaceImpair.append(i)	
	if posi == 0 or posi == 1:
		for i in range (len(LPlacePair)):
			L[LPlacePair[i]] += 1
			L[LPlaceImpair[i]] -= 1
	if posi == 3 or posi == 4:
		for i in range (len(LPlaceImpair)):
			L[LPlacePair[i]] -= 1		
			L[LPlacePair[i]] += 1
	return L
	
	
def Verif1(L, posi):
	if posi == 0:
		L[1] += 1 
		L[2] += 1
		L[3] += 1
		L[4] += 1
	if posi == 1:
		L[0] -= 1 
		L[2] += 1
		L[3] += 1
		L[4] += 1
	if posi == 2:
		L[1] -= 1 
		L[0] -= 1
		L[3] += 1
		L[4] += 1
	if posi == 3:
		L[1] -= 1 
		L[2] -= 1
		L[0] -= 1
		L[4] += 1
	if posi == 4:
		L[1] -= 1 
		L[2] -= 1
		L[3] -= 1
		L[0] -= 1
		L[4] += 4
	return L
	
def Verif2(L, posi):
	print(posi)
	if posi != 4:
		L[posi + 1] *= 2
	elif posi != 0:
		L[posi - 1] /= 2
	if posi == 4:
		L[posi] += 4
	return L
	
def Verif3(L, posi):
	if posi == 0 or posi == 2 or posi == 4:
		L[posi] += 2
	elif posi == 1 or posi == 3:
		L[posi] -= 2
	return L
	
def Verif4(L,posi):
	if posi == 0 or posi == 4:
		L[posi] += 1
	elif posi == 1 or posi == 2 or posi == 3:
		L[posi] -= 1
	return L
	
def Verif5(L,posi):
	if posi == 0:
		L[posi] -= (L[posi + 1] + L[posi + 2] + L[posi + 3] + L[posi + 4]) / 4
	if posi == 1:
		L[posi] -= (L[posi + 1] + L[posi + 2] + L[posi + 3]) / 3
		L[posi] += L[posi - 1]
	if posi == 2:
		L[posi] -= (L[posi + 1] + L[posi + 2]) / 2
		L[posi] += (L[posi - 1] + L[posi - 2]) / 2
	if posi == 3:
		L[posi] -= L[posi + 1]
		L[posi] += (L[posi - 1] + L[posi - 2] + L[posi - 3]) / 3
	if posi == 1:
		L[posi] += (L[posi - 1] + L[posi - 2] + L[posi - 3] + L[posi - 4]) / 4
	return L
		

def Verif6(L,posi):
	if posi == 3:
		if L[0] + L[1] + L[2] < 10:
			L[posi] += 4
	else:
		L[posi] -= 2
	return L
	
def Verif7(L,posi):
	if posi == 0:
		if L[2] > 5:
			L[2] += 2
	if posi != 0 and L[2] > 5:
		for i in range(5):
			L[i] -= 1
	return L		
			
def Verif8(L,posi):
	if posi == 0:
		L[posi] -= 2
	if posi == 1:
		L[posi] -= 1
	if posi == 3:
		L[posi] += 1
	if posi == 4:
		L[posi] += 2
	return L
		
def Verif9(L,posi):
	if posi == 0:
		for i in range(5):
			if L[i] == 9:
				L[i] -= 2
			if L[i] == 1:
				L[i] += 2
	if posi == 1:
		for i in range(5):
			if L[i] == 8:
				L[i] += 2
			if L[i] == 2:
				L[i] -= 2
	if posi == 3:
		for i in range(5):
			if L[i] == 7:
				L[i] -= 2
			if L[i] == 3:
				L[i] += 2
	if posi == 4:
		for i in range(5):
			if L[i] == 6:
				L[i] += 2
			if L[i] == 4:
				L[i] -= 2
	return L
			
	
def pair(elt):
	pair = False
	if elt % 2 == 0:
		pair == True
	return pair

""" Verification des attribus """ 


#dab = Equilibration(L5445,L4554) 
#Combat(dab[0],dab[1])

#dab = Equilibration(L5445,L4554) 
#CombatAttribus(dab[0],dab[1])

Menu()
