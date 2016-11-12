#------------------------------------#
#  			 Arbre AVL 			     #
#------------------------------------#
# Auteurs : Kevin HOARAU 			 #
#------------------------------------#
# Date   : 09/2014                   #
# Lieu   : Universite de la Reunion  #
#------------------------------------#

#=====================================#
# Definition des classes  et methodes #
#=====================================#

#-------------------------#
# Debut de la classe AVL  #
#-------------------------#

class AVL:

	#---------------------------------------------------------------------------------------------------------
	# Constructeur : Creer un arbre AVL
	# Entree : 
	# 	- element (facultatif) : element a mettre a la racine de l'arbre 
	#	- droite (facultatif) : arbre AVL a mettre comme sous arbre droit de l'arbre 
	#	- gauche (facultatif) : arbre AVL a mettre comme sous arbre gauche de l'arbre 
	# Sortie : 
	#	- un arbre AVL avec element comme racine, droite comme sous arbre droit, gauche comme sous arbre gauche
	def __init__(self, element=None,droite=None,gauche=None):
		self.e = element							# Place element, droite et gauche dans l'arbre
		self.d = droite
		self.g = gauche
		self.hauteur =  0 							# Initialise la hauteur de l'arbre a 0
		
		if(droite!=None and gauche!=None):			# Calcul la hauteur de l'arbre en fonction
			if droite.hauteur>gauche.hauteur:		# des hauteur de droite et gauche
				self.hauteur=droite.hauteur+1
			else:
				self.hauteur=gauche.hauteur+1
		elif(droite!=None):
			self.hauteur=droite.hauteur+1
		elif(gauche!=None):
			self.hauteur=gauche.hauteur+1

	#---------------------------------------------------------------------------------------------------------
	# insere : Insere un element dans un arbre AVL
	# Entree : 
	#	- self : un arbre AVL
	# 	- e : element a inserer
	#	- req (facultatif) : Vrai si on souhaite reequilibrer l'arbre apres insertion, Faux sinon
	# Sortie : 
	#	- self qui reste un arbre AVL et dans lequel e a ete insere
	def insere(self, e, req=True):	
		# Si l'arbre ne contient pas d'element e devient racine de l'arbre
		if(self.e==None):								
			self.e=e 
		else:
			# Sinon, insere e dans le sous arbre droit ou gauche en fonction de la valeur de e									
			if(e>self.e):							# Si e > a la racine de l'arbre, insere a droite
				if(self.d==None):					
					self.d=AVL(e)
				else:								
					self.d=self.d.insere(e,req)
			else:									# Sinon insere a gauche
				if(self.g==None):
					self.g=AVL(e)
				else:
					self.g=self.g.insere(e,req)

			# Apres insertion, reequilibre l'arbre si necessaire
			if(req):
				self = self.reequilibre()

			# Calcul la nouvelle hauteur de l'arbre
			hfilsd=0 					 # Cherche la hauteur des sous arbres si ils existent
			hfilsg=0
			if(self.d!=None):
				hfilsd=self.d.hauteur
			if(self.g!=None):
				hfilsg=self.g.hauteur

			if(hfilsd>hfilsg):			# Si hauteur du sous arbre droit > hauteur sous arbre gauche
				self.hauteur=hfilsd+1 	# Hauteur de l'arbre vaut hauteur du sous arbre droit +1
			else:						# Sinon, hauteur de l'arbre vaut hauteur du sous arbre gauche +1
				self.hauteur=hfilsg+1

		return self						# Retourne l'arbre

	#---------------------------------------------------------------------------------------------------------
	# reequilibre : Reequilibre un arbre en effectuant la bonne rotation
	# Entree : 
	#	- self : un arbre desiquilibre
	# Sortie : 
	#	- self un arbre AVL
	def reequilibre(self):
		# Si le desequilibre vaut +2
		if(self.deseq()>1):
				if(self.g.deseq()>0):			# Si le desequilibre du ss arbre gauche vaut +1, RD
					self=self.rotation_droite()
				else:							# Sinon, RGD
					self=self.rotation_gauche_droite()
		else:
			# Si le desequilibre vaut -2
			if(self.deseq()<-1):
				if(self.d.deseq()<0):			# Si le desequilibre du ss arbre droit vaut -1, RG
					self=self.rotation_gauche()
				else:							# Sinon, RDG
					self=self.rotation_droite_gauche()
		# Si aucun des cas ne correspond l'arbre est equilibre
		return self
	
	#---------------------------------------------------------------------------------------------------------
	# reequilibre : Calcul le desequilibre d'un arbre
	# Entree : 
	#	- self : un arbre 
	# Sortie : 
	#	- Valeur du desequilibre de l'arbre
	def deseq(self):
		# Initialise la hauteur des sous arbre a -1 
		# Cela permet de differencier l'absence d'un sous arbre d'un sous arbre etant une feuille
		hfilsg=-1       
		hfilsd=-1		

		# Recupere les hauteurs des sous arbres si ils existent
		if(self.g!=None):
			hfilsg=self.g.hauteur
		if(self.d!=None):
			hfilsd=self.d.hauteur

		return hfilsg-hfilsd   # Renvois la valeur du desequilibre

	#---------------------------------------------------------------------------------------------------------
	# maj_hauteur : Recalcule les hauteurs d'un arbre et de ses sous arbres
	# Entree : 
	#	- self : un arbre 
	# Sortie : 
	#	- la hauteur de l'arbre recalcule
	def maj_hauteur(self):
		# Si l'arbre na aucun sous arbre, sa hauteur vaut 0
		if(self.d==None and self.g==None):
			self.hauteur=0
			return 0
		else:
			# Sinon on recalcul la hauteur de ses sous arbres si il existent
			hd=0
			hg=0
			if(self.d!=None):
				hd=self.d.maj_hauteur()
			if(self.g!=None):
				hg=self.g.maj_hauteur()

			# On compare les hauteurs des sous arbres
			# La hauteur de l'arbre vaut alors hauteur du plus haut sous arbre +1
			if(hd>hg):
				self.hauteur=hd+1
			else:
				self.hauteur=hg+1
			return self.hauteur 	# renvoi la valeur de la hauteur de l'arbre 

	#---------------------------------------------------------------------------------------------------------
	# printAVL : Affiche un arbre AVL sous forme hierarchique
	# Entree : 
	#	- self : un arbre 
	# Effet de bord : 
	#   - l'arbre est affiche a l'ecran
	def printAVL(self,n=0):
		if(self.d!=None):
			self.d.printAVL(n+1)		
		if(self.e!=None):
			espace=""
			for x in xrange(0,n):
				espace+="   |"
			#print(espace + "-->" + str(self.e) + "(h="+str(self.hauteur)+";d="+str(self.deseq())+")")
			print(espace + "-->" + str(self.e))
		if(self.g!=None):
			self.g.printAVL(n+1)

	#---------------------------------------------------------------------------------------------------------
	# rotation_droite : Effectue une rotation droite sur un aebre
	# Entree : 
	#	- self : un arbre 
	# Sortie : 
	#	- l'arbre ayant subit une rotation droite et qui est un AVL
	def rotation_droite(self):
		# Effectue la rotation
		Aux = self.g
		self.g = Aux.d
		Aux.d = self
		self = Aux
		# Met a jour les hateur de l'arbre
		self.maj_hauteur()
		return self

	#---------------------------------------------------------------------------------------------------------
	# rotation_gauche : Effectue une rotation gauche sur un aebre
	# Entree : 
	#	- self : un arbre 
	# Sortie : 
	#	- l'arbre ayant subit une rotation gauche et qui est un AVL
	def rotation_gauche(self):
		# Effectue la rotation
		Aux = self.d
		self.d = Aux.g
		Aux.g = self
		self = Aux
		# Met a jour les hateur de l'arbre
		self.maj_hauteur()
		return self

	#---------------------------------------------------------------------------------------------------------
	# rotation_gauche_droite : Effectue une rotation gauche droite sur un aebre
	# Entree : 
	#	- self : un arbre 
	# Sortie : 
	#	- l'arbre ayant subit une rotation gauche droite et qui est un AVL
	def rotation_gauche_droite(self):
		# Effectue la rotation
		Aux=self.g
		Aux2=Aux.d
		Aux.d=Aux2.g
		self.g=Aux2.d
		Aux2.g=Aux
		Aux2.d=self
		self=Aux2
		# Met a jour les hateur de l'arbre
		self.maj_hauteur()
		return self

	#---------------------------------------------------------------------------------------------------------
	# rotation_droite_gauche : Effectue une rotation droite gauche sur un aebre
	# Entree : 
	#	- self : un arbre 
	# Sortie : 
	#	- l'arbre ayant subit une rotation droite gauche et qui est un AVL
	def rotation_droite_gauche(self):
		# Effectue la rotation
		Aux = self.d
		Aux2 = Aux.g
		Aux.g = Aux2.d
		self.d = Aux2.g
		Aux2.d = Aux
		Aux2.g = self
		self = Aux2
		# Met a jour les hateur de l'arbre
		self.maj_hauteur()
		return self

#========================#
# 	Programme Principal	 #
#========================#


#------------Test rotation droite-------------------------------------

print("\n| Test de rotation droite |\n===========================")
# Cree un AVL avec une forme adapte a cette rotation 
A=AVL()
for x in ["D","F","B","A","C"]:
	A.insere(x,False)

# Affiche l'arbre AVL avant et apres la rotation
print("\nAvant :\n-------\n")
A.printAVL()

A = A.rotation_droite()
print("\nApres :\n-------\n")
A.printAVL()

#------------Test rotation gauche-------------------------------------

print("\n| Test de rotation gauche |\n===========================")
# Cree un AVL avec une forme adapte a cette rotation
A=AVL()
for x in ["B","A","D","C","F"]:
	A.insere(x,False)

# Affiche l'arbre AVL avant et apres la rotation
print("\nAvant :\n-------\n")
A.printAVL()
A = A.rotation_gauche()

print("\nApres :\n-------\n")
A.printAVL()

#------------Test rotation gauche droite-------------------------------

print("\n| Test de rotation gauche droite |\n==================================")
# Cree un AVL avec une forme adapte a cette rotation
A=AVL()
for x in ["F","B","A","D","C","E","G"]:
	A.insere(x,False)

# Affiche l'arbre AVL avant et apres la rotation
print("\nAvant :\n-------\n")
A.printAVL()
A = A.rotation_gauche_droite()

print("\nApres :\n-------\n")
A.printAVL()

#------------Test rotation droite gauche-------------------------------

print("\n| Test de rotation droite gauche |\n==================================")
# Cree un AVL avec une forme adapte a cette rotation
A=AVL()
for x in ["B","A","F","D","C","E","G"]:
	A.insere(x,False)

# Affiche l'arbre AVL avant et apres la rotation
print("\nAvant :\n-------\n")
A.printAVL()
A = A.rotation_droite_gauche()

print("\nApres :\n-------\n")
A.printAVL()

#------------Test d'insertion dans un AVL-------------------------------

print("\n| Test d'insertion |\n====================")

A=AVL() 							# Cree un AVL vide

for x in map(chr, range(65, 91)):	# Cree une liste de A-Z
	A = A.insere(x)					# Insere tout les element de la liste dans AVL

A.printAVL()						# Affiche l'arbre AVL


