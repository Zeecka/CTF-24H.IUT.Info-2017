# -*- coding: utf-8 -*-


# testé sous Python 3 !
# necessite le plugin PIL !

##############################
####    Code By Zeecka    ####
##############################
###    return(victoire)... ###
###       #equipe18        ###
###        IUT Vélizy      ###
##############################


import requests
from PIL import Image, ImageDraw

lienChall = "http://10.62.27.3/epreuve3/index.php" # Lien du formulaire de submit
lienImg = "http://10.62.27.3/epreuve3/images/code.php" # lien de l'image , c'est ce chargement qui set le session[captcha] / le timer
	filename = r"C:\Users\Alex\Desktop\temp.png" # Chemin de sauvegarde du captcha


def parseImage(url):
	""" Prend le chemin de l'image en param 
	retourne le nombre de lignes verticales et horizonales sous la form 57
	pour 5 lignes verticales et 7 horizonales """
	
	im = Image.open(url) # On ouvre l'image avec PIL
	pixels = list(im.getdata()) # On charge les pixels (liste 1d)
	width, height = im.size # On recup la taille de l'image
	pixels = [pixels[i * width:(i + 1) * width] for i in range(height)] # on convertit en liste 2d de pixels
	
	nbVerticaux = 0 # On initialise les nb de lignes/colonnes
	nbHorizontaux = 0
	
	for elt in pixels[0]: # On parcourt la premiere ligne
		if elt == 0: # Pour chaques pixels noirs sur la première ligne, si la valeure est noire
			nbVerticaux += 1 # alors on incrémente le nombre de lignes verticales
	
	for elt in pixels: # pour chaques lignes 
		if(elt[0] == 0): # si le premier pixel est noir
			nbHorizontaux += 1 # on incrémente le nombre de lignes horizonales
	
	return str(nbVerticaux)+str(nbHorizontaux)


# NOM ET PRENOMS POUR L'INSCRIPTION
nomstab = ["Jean","Charles","George","Louis","Simon","Constant"]
prenomtab = ["naej","selrahc","egroeg","siuol","nomis","tnatsnoc"]


s = requests.Session() # On initialise la session (important pour assurer le suivi des inscriptions)

for i in range(5): # Boucle de 5 comptes
	
	""" On recup l'image """
	
	response = s.get(lienImg);
	
	with open(filename, 'wb') as f: # On écrit l'image sous le chemin "filename"
		for chunk in response.iter_content(1024):
			f.write(chunk)
	
	# On set les valeurs du formulaire
	
	captcha = parseImage(filename) # résolution du captcha, voir parseImage()
	nom = nomstab[i]
	prenom = prenomtab[i]
	mail = prenom+"."+nom+"@gmail.com"
	formulaire = "1" # param présent avec la val 1 sur le site

	mondico = { # On construit le dictionnaire de param post
	'captcha':int(captcha),
	'nom':nom,
	'prenom':prenom,
	'email':mail,
	'formulaire':formulaire
	}
	
	# On inscrit le compte
	
	print("Inscription du compte :")
	print(mondico)
	print("\n\n")
	
	""" Construction de la requetes post """

	r = s.post(lienChall, data = mondico)
	
	# On recup la réponse
	
	rep = r.text
	rep = rep.split("<!-- Content -->")[1] # on prend le contenu dans <!-- content --> <!-- /content -->
	rep = rep.split("<!-- /content -->")[0]
	
	# On affiche la réponse
	print(rep)
