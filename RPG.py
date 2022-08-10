#C'est bien ce fichier qu'il faut lancer pour tester le jeu.
#Rappel des membres du groupe 17 (tous W1 groupe 2) : GUILLERD Victorien, JIN Loïc, LEFEBVRE Valentine, MOHAMED Mia

from random import randint
import os
from os import system
import time

from is_it_in_the_list import *
from Menu import *
from Fight import *
from Map_and_descriptions import *
from Class_player import *
from Class_enemies import *
from Objects import *

def game():
	running_game = 0
	token = 3
	a = menu(token) 
	if a == "Jeu" :     # New game
		if running_game == 0 :
			set_fighting_spots = [[2, 16], [5, 8], [7, 4], [7, 9], [7, 17], [15, 18], [17, 13], [18, 10], [20, 11], [13, 1], [15, 3], [20, 0], [18, 17], [20, 2]]  # Those are the spots, outside the forest, where a fight is supposed to start.
		#time.sleep(2)
		running_game = 1
		os.system("cls")
		print("...")
		#time.sleep(1)
		print("Fatigué...")
		#time.sleep(1)
		print("Vous êtes réveillé mais vous n'ouvrez pas tout de suite les yeux. Vous êtes allongé à même le sol couvert de feuilles mortes. Des racines vous labourent le dos et vous poussent à vous asseoir en vous frottant les yeux.")
		#time.sleep(5)
		print("Vous vous trouvez dans une forêt lugubre, au pied d'un arbre aux branches et au tronc distordus. Les arbres autour de vous, tous semblables, sont hauts et rapprochés. Leurs feuilles noires forment une canopée qui ne laisse presque aucune lumière filtrer. Il ne fait pas nuit mais l'heure est impossible à déterminer précisément.")
		#time.sleep(7)
		print("Qu'est-ce que vous faites là ? Vous ne vous souvenez de rien...")
		#time.sleep(3)
		print("Vous ne vous rappelez même pas de votre nom... Qu'est-ce que c'était déjà ?\n(Tapez votre nom.)")
		name = input()
		print("Ah oui.", name, ". C'est ça... Et vous êtes de sang mêlé : mi-dieu et mi-humain.")
		parent_letter = ""
		while not is_it_in_the_list(parent_letter, ["Z", "P", "H", "T", "R", "O", "E"]):
			print("Mais de quel dieu descendez-vous ? \n(Entrez Z pour Zeus, P pour Poséidon, H pour Hadès, T pour Athéna, R pour Arès, O pour Apollon ou E pour Hermès.)")
			parent_letter = input()
			parent_letter = parent_letter.upper()
		if parent_letter == "Z":
			Hero = Player("Zeus", name)
		elif parent_letter == "P":
			Hero = Player("Poséidon", name)
		elif parent_letter == "H":
			Hero = Player("Hadès", name)
		elif parent_letter == "T":
			Hero = Player("Athéna", name)
		elif parent_letter == "R":
			Hero = Player("Arès", name)
		elif parent_letter == "O":
			Hero = Player("Apollon", name)
		elif parent_letter == "E":
			Hero = Player("Hermès", name)
		else :
			return "Erreur : Dieu inconnu"
		sum_up = "Oui, c'est ça. Vous êtes " + Hero.name + ", enfant de " + Hero.parent +"."
		print(sum_up)
		time.sleep(1)
		print("Vous vous décidez finalement à vous lever et à explorer les environs. Rester inactif dans un endroit pareil vous met mal à l'aise.")
		#time.sleep(4)
		print("Une odeur nauséabonde flotte dans l'air. Vous hésitez à partir dans la direction opposée mais vous devez en avoir le coeur net.")
		#time.sleep(4)
		print("Quelle horreur ! Vous avez découvert un cadavre en décomposition. Vous vous couvrez le nez avec votre col. En observant les alentours plus attentivement, vous remarquez des traces de combat. Cette personne n'est pas morte de cause naturelle.")
		#time.sleep(6)
		print("Il vous en coûte d'agir ainsi mais, si ce qui l'a tué rode encore dans les parages, il faut que vous puissiez vous défendre. Vous lui volez donc ses armes.")
		#time.sleep(5)
		Hero.inventory["weapons"] = ["une épée rouillée", "un vieil arc tordu"]
		print("\nOBTENU : une épée rouillée et un vieil arc tordu")
		#time.sleep(2)
		print("\nEn vous penchant pour ramasser les armes, un pendentif est sorti de votre col et s'est balancé au bout de sa chaine. Vous n'aviez même pas remarqué que vous portiez ce bijou autour du cou.")
		#time.sleep(6)
		print("C'est un petit pendentif doré ovale. En l'ouvrant, vous découvrez le portrait d'une jeune fille souriante, et tous vos souvenirs reviennent brutalement, accompagnés d'une grande colère. Car il s'agit de votre soeur, et Zeus l'a enlevée.")
		#time.sleep(6)
		print("Vous vous rappelez le défi qu'il vous a lancé : vous devez le vaincre, ainsi que ses frères, et tous les monstres et dieux qui se trouveront sur votre route. Si vous y parvenez, elle vous sera rendue saine et sauve. Mais quel crédit accorder à la parole d'un dieu capable d'une telle félonie ? Il n'y a pas une seconde à perdre.")
		time.sleep(7)
		while running_game == 1 :
			Hero.previous_position = Hero.position
			Hero.position = Move(Hero)
			os.system("cls")
			# Some spots show descriptions to dive a little deeper into the game.
			spot_description(Hero)
			# This functions determines whether a fight begins, we find an object, or nothing happens.
			event = spot_event(Hero.position, set_fighting_spots)
			if event == "object":
				# When we find an object, There's an 80% chance that it's a remedy and 20% that it's a nectar.
				object = randint(1, 10)
				if object < 8 :
					Hero.inventory["potions"]["remedies"] += 1
					print("\nOBTENU : un remède. Vous pourrez le boire pour récupérer quelques points de vie en cas de besoin.\n")
					time.sleep(4)
				else :
					Hero.inventory["potions"]["nectars"] += 1
					print("\nOBTENU : un nectar. Vous pourrez le boire pour régénérer votre mana en cas de besoin.\n")
					time.sleep(4)
				pass
			elif event == "fight":
				# Depending on where we are on the map (forest, or specific spots in other areas), the enemys are not the same. This function returns the number of the enemy we have to fight.
				enemy_number = spot_enemy(Hero.position)
				enemy = Enemy(Enemies_list[enemy_number])		# We get all the informations on the enemy
				fight_result = fight(Hero, enemy, False, False)
				if fight_result == "game over" :
					print("~~~ FIN DU JEU ~~~ VOUS AVEZ PERDU ~~~")
					running_game = 0
				elif fight_result == "gagné" :
					if Hero.level != 10:
						print("Vous avez gagné", enemy.xp_won, "points d'expérience.")
						Hero.xp = Hero.xp + enemy.xp_won
						print("Vous avez en tout", Hero.xp, "points d'expérience.")
						Hero.level_up()
					if enemy_number == 17 :        # After the fight against Hadès.
						Hero.inventory["special"].append("Barque de Charon")
						print("\nOBTENU : Barque de Charon. Vous pouvez à présent rejoindre la mer depuis l'embouchure de la rivière.\n")
					elif enemy_number == 18 :      # After the fight against Poséidon.
						Hero.inventory["special"].append("Clé de l'Olympe")
						print("\nOBTENU : Clé de l'Olympe. Vous pouvez à présent atteindre le sommet de la plus haute montagne.\n")
					elif enemy_number == 19 :      # After the fight against Zeus, the game ends.
						os.system("cls")
						print("Un énorme bruit métallique retentit. Il vous fait penser à une grille, alors vous courrez dans sa direction. Après ce qui vous paraît une éternité, vous arrivez enfin devant un immense bâtiment de pierre.")
						time.sleep(6)
						print("À l'intérieur, d'innombrables cellules sont alignées, mais une seule est ouverte, et une jeune fille se tient dans l'entrée, sans oser sortir. Elle vous aperçoit, crie votre nom et court vers vous.")
						time.sleep(6)
						print("C'est votre soeur, terrifiée et amaigrie, mais vivante. Vous avez réussi. Vous allez enfin pouvoir rentrer chez vous.\n")
						time.sleep(4)
						print("~~~ FIN DU JEU ~~~ VOUS AVEZ GAGNÉ ~~~")
						running_game = 0
						time.sleep(4)
						credit(token)
					else :
						if possible_loot(Hero) != [[], [], [], [], [], []] :
							# Apart from the 3 great gods, we have 1 chance out of 4 of finding an item.
							loot_chance = randint(1, 4)
							if loot_chance == 1 :               
								loot(Hero)
					if set_fighting_spots.count == 1 :
						# avoids fighting twice on the same spot (when it's a path we have to travel both ways)
						set_fighting_spots.remove(Hero.position)
					time.sleep(3)
				elif fight_result == "fuite" :
					# If we escape, we're sent back to the previous spot. This avoids the fight starting automatically again on specific spots, as well as cheating by escaping a fight and going on our merry way.
					Hero.position = Hero.previous_position
	else :
		return game()

game()