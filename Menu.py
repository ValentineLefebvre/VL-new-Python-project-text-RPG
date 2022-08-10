#Pour tester le jeu, c'est RPG.py qu'il faut lancer.


import os
import time
def credit(token) :
	if token > 0 :
		os.system("cls")
		print("CREDITS")
		token = token - 1
		print("\n~~~ Version améliorée : LEFEBVRE Valentine ~~~\n")
		print("Différences notables de cette nouvelle version :\n")
		time.sleep(2)
		print("  # Différences techniques :")
		print("    * Utilisation des dictionnaires, pour les objets et les attaques notemment")
		time.sleep(2)
		print("    * Utilisation des classes pour le personnage principal et les ennemis")
		time.sleep(2)
		print("  # Différences de gameplay :")
		print("    * Choix d'un parent divin pour le héros, influençant ses statistiques et attaques")
		time.sleep(2)
		print("    * Prise en compte de la défense directement dans les statistiques")
		time.sleep(2)
		print("    * Retrait de l'action 'Défendre' en combat")
		time.sleep(2)
		print("    * Ajouts d'effets particuliers sur certaines attaques")
		time.sleep(2)
		print("    * Rééquilibrage des statistiques du héros et des ennemis")
		time.sleep(2)
		print("    * Possibilité de visualiser l'inventaire et les statistiques du joueur en cours de partie")
		time.sleep(2)
		print("  # Différences secondaires :")
		print("    * Changements textuels : noms d'attaques notemment")
		time.sleep(3)
		# original credits
		print("\n~~~ Version d'origine ~~~\n")
		time.sleep(2)
		print("Création du héros : JIN Loïc")
		time.sleep(2)
		print("Création des ennemis : MOHAMED Mia")
		time.sleep(2)
		print("Système de combat : GUILLERD Victorien")
		time.sleep(2)
		print("Fans de Pokémon : GUILLERD Victorien, JIN Loïc")
		time.sleep(2)
		print("Arsenal : LEFEBVRE Valentine")
		time.sleep(2)
		print("Professionnel de l'esquive : GUILLERD Victorien")
		time.sleep(2)
		print("Coups critique ! : GUILLERD Victorien")
		time.sleep(2)
		print("Carte : LEFEBVRE Valentine")
		time.sleep(2)
		print("Création du menu : GUILLERD Victorien")
		time.sleep(2)
		print("Débug : JIN Loïc, LEFEBVRE Valentine, MOHAMED Mia")
		time.sleep(2)
		print("Créateur de bug : GUILLERD Victorien")
		time.sleep(2)
		print('"Scénario" : LEFEBVRE Valentine')
		time.sleep(2)
		print("Rédaction : LEFEBVRE Valentine")
		time.sleep(2)
		print("Adjointe de rédaction : MOHAMED Mia")
		time.sleep(2)
		print("Correctrice orthographique : LEFEBVRE Valentine")
		time.sleep(2)
		print("Musique : pas moi")
		time.sleep(2)
		print("Moteur graphique : Python")
		time.sleep(2)
		print("Graphisme : Consolas")
		time.sleep(2)
		print("Chef de projet : OUI")
		time.sleep(2)
		print("Une idée originale du groupe 17")
		time.sleep(2)
		print("Remerciments particuliers à JANIN Loïc, à la machine à café et à HETIC")
		time.sleep(5)
		return token, "credit"
	
	else :                      #La variable token diminue à chaque fois qu'on lance les crédits. Elle est à trois au début. Quand elle arrive à 0, ça affiche ce qui suit :
		os.system("cls")
		print("Sérieusement, vous avez lancé les crédits 3 fois ?")
		time.sleep(2)
		print("Il faut penser à lancer le jeu, maintenant !")
		time.sleep(2)
		print("Ou vous pouvez quitter...")
		time.sleep(2)
		print("Non ! Quittez pas ! Le jeu est bien, en vrai ! Testez-le, au moins !")
		time.sleep(4)
		token = 9999
		return token, "credit"
		
		
def menu(token) :
	os.system("cls")
	choice = str()
	while choice != "1" or choice != "nouveau jeu" or choice != "3" or choice != "quitter"  :
		print("Bienvenue, jeune dieu !")
		print("Es-tu prêt à te confronter à la vraie puissance ?")
		print("Choisis ce que tu veux : ")
		print("1) Nouveau jeu")
		print("2) Crédits ")
		print("3) Quitter")
		choice = input()
		choice = choice.lower()
		if choice == "1" or choice == "nouveau jeu" :
			print("Prépare-toi à affronter cette aventure !")
			return "Jeu"
		elif choice == "2" or choice == "crédit" or choice == "credit" or choice == "crédits" or choice == "credits" :
			os.system("cls")
			token, choice = credit(token)
		elif choice == "3" or choice == "quitter" :
			print("Déjà ? \nDommage... Au revoir.")
			return "Quitter"
		else :
			return menu(token)
