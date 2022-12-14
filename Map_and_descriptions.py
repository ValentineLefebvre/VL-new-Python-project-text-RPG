# Pour tester le jeu, c'est RPG.py qu'il faut lancer.

import time
from random import randint
from is_it_in_the_list import *


mountain_spots = [[0, 8], [1, 7], [1, 8], [2, 6], [2, 7], [2, 10], [2, 16], [3, 5], [3, 6], [3, 8], [3, 10], [3, 11], [3, 16], [3, 17], [4, 4], [4, 5], [4, 8], [4, 11], [4, 17], [5, 4], [5, 6], [5, 7], [5, 8], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15], [5, 16], [5, 17], [6, 4], [6, 6], [6, 16], [7, 1], [7, 2], [7, 3], [7, 4], [7, 6], [7, 9], [7, 10], [7, 16], [7, 17], [7, 18], [7, 19], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 16], [8, 19]]
mountain_fight_spots = [[2, 16], [5, 8], [7, 4], [7, 9], [7, 17]]
mountain_object_spots = [[2, 10], [3, 8], [7, 1], [7, 10], [8, 19]]
mountain_boss = [0, 8]                       # Zeus

forest_spots = [[9, 0], [9, 1], [9, 2], [9, 6], [9, 10], [9, 11], [9, 14], [9, 15], [9, 16], [9, 17], [9, 18], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [10, 14], [10, 15], [10, 16], [10, 17], [10, 18], [10, 19], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11], [11, 12], [11, 14], [11, 15], [11, 16], [11, 17], [11, 18], [11, 19], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [12, 15], [12, 16], [12, 17], [12, 18], [12, 19], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13], [13, 15], [13, 16], [13, 17], [13, 18], [13, 19], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [16, 7], [16, 8], [16, 9], [16, 10], [17, 6], [17, 7], [17, 8], [17, 9], [18, 7], [18, 8]]
dark_forest = [[9, 0], [9, 1], [9, 2], [9, 6], [9, 10], [9, 11], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11], [11, 12], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [16, 7], [16, 8], [16, 9], [16, 10], [17, 6], [17, 7], [17, 8], [17, 9], [18, 7], [18, 8]]
light_forest = [[9, 14], [9, 15], [9, 16], [9, 17], [9, 18], [10, 14], [10, 15], [10, 16], [10, 17], [10, 18], [10, 19], [11, 14], [11, 15], [11, 16], [11, 17], [11, 18], [11, 19], [12, 15], [12, 16], [12, 17], [12, 18], [12, 19], [13, 15], [13, 16], [13, 17], [13, 18], [13, 19]]

water_spots = [[1, 9], [2, 9], [3, 9], [4, 9], [4, 10], [5, 10], [6, 10], [6, 11], [7, 11], [7, 12], [8, 12], [9, 12], [9, 13], [10, 13], [11, 13], [12, 13], [12, 14], [13, 14], [14, 14], [15, 14], [15, 14], [15, 15], [15, 16], [15, 17], [15, 18], [15, 19], [16, 12], [16, 13], [16, 19], [17, 13], [17, 15], [17, 16], [17, 17], [17, 19], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 17], [18, 19], [19, 12], [19, 19], [20, 9], [20, 10], [20, 11], [20, 12], [20, 13], [20, 14], [20, 15], [20, 16], [20, 17], [20, 18], [20, 19]]
pont = [11, 13]
water_fight_spots = [[15, 18], [17, 13], [18, 10], [20, 11]]
water_object_spots = [[16, 12], [20, 9]]
water_boss = [18, 17]                # Pos??idon

hell_spots = [[11, 1], [12, 1], [13, 0], [13, 1], [13, 2], [14, 0], [14, 2], [14, 3], [14, 4], [14, 5], [15, 0], [15, 3], [15, 5], [16, 0], [16, 2], [16, 5], [17, 0], [17, 2], [17, 4], [18, 0], [18, 1], [18, 2], [18, 3], [18, 4], [19, 0], [19, 4], [19, 6], [20, 0], [20, 2], [20, 3], [20, 4], [20, 5], [20, 6]]
hell_fight_spots = [[13, 1], [15, 3], [20, 0]]
hell_object_spots = [[16, 5], [19, 6]]        # Had??s
hell_boss = [20, 2]

west_river_bank = [[1, 8], [3, 8], [4, 8], [7, 10], [9, 11], [10, 12], [12, 12]]
east_river_bank = [[2, 10], [3, 10], [4, 11], [5, 11], [9, 14], [10, 14], [12, 15]]
river = [[1, 9], [2, 9], [3, 9], [4, 9], [4, 10], [5, 10], [6, 10], [6, 11], [7, 11], [7, 12], [8, 12], [9, 12], [9, 13], [10, 13], [12, 13], [12, 14]]
# because the river mouths are the only access to the river, even after we get the "barque de charon"
west_river_mouth = [13, 13]
east_river_mouth = [13, 15]

def map(player):
	player_map = []
	reference_map = []
	i = 0
	while i < 21 :
		player_map.append("")
		reference_map.append([])
		j = 0
		while j < 20 :
			if player.position == [i, j]:
				player_map[i] = player_map[i] + " X"
				reference_map[i].append("J")
			elif is_it_in_the_list([i, j], forest_spots):
				player_map[i] = player_map[i] + " ^"
				reference_map[i].append("F")
			elif is_it_in_the_list([i, j], mountain_spots):
				player_map[i] = player_map[i] + " ."
				reference_map[i].append("M")
			elif is_it_in_the_list([i, j], water_spots):
				player_map[i] = player_map[i] + " ~"
				reference_map[i].append("R")
			elif is_it_in_the_list([i, j], hell_spots):
				player_map[i] = player_map[i] + " _"
				reference_map[i].append("E")
			else :
				player_map[i] = player_map[i] + "  "
				reference_map[i].append("V")          # empty
			j = j + 1
		i = i + 1
	return [player_map, reference_map]
	

def show_map(player):
	maps = map(player)
	map_to_show = maps[0]      # we don't use the 2nd map given by the map function
	print("L??gende : \n. : mountain \n^ : for??t \n_ : souterrain \n~ : eau \nX : votre position")
	print("Les zones noires ne sont pas accessibles.")
	print("________________________________________")
	i = 0
	while i < len(map_to_show) :
		print("|" + map_to_show[i] + "|")
		i = i + 1
	print("|________________________________________|")
	return "done"





def Move(player):
	maps = map(player)
	carte_de_reference = maps[1]    # we don't use the 1st map given by the map function
	ligne_j = int(player.position[0])
	colonne_j = int(player.position[1])
	directions_possibles = ["N", "S", "E", "O"]
	i = 0
	if ligne_j == 0 or (ligne_j > 0 and carte_de_reference[ligne_j - 1][colonne_j] == "V") :
		del directions_possibles[i]                 # North is blocked.
	elif player.position == [1, 8] and not is_it_in_the_list("Cl?? de l'Olympe", player.inventory["special"]) : # We can't see Zeus without the key.
		del directions_possibles[i]                 # North is blocked.
	elif player.position == [13, 14] or player.position == [11, 13] :
		# We can't go upstream on the river, or jump north from the bridge.
		del directions_possibles[i]                 # North is blocked.
	elif ligne_j > 0 and is_it_in_the_list([ligne_j - 1, colonne_j], river) :
		# We can't jump into the river towards the north when we're at a river's bend.
		del directions_possibles[i]                 # North is blocked.
	else :
		i = i + 1
	if ligne_j == 20 or (ligne_j < 20 and carte_de_reference[ligne_j + 1][colonne_j] == "V") :
		del directions_possibles[i]                 # South is blocked.
	elif player.position == [11, 13] :               # We can't jump south from the bridge.
		del directions_possibles[i]                 # South is blocked.
	elif ligne_j < 20 and is_it_in_the_list([ligne_j + 1, colonne_j], river) :
		# We can't jump into the river towards the south when we're at a river's bend.
		del directions_possibles[i]                 # South is blocked.
	else :
		i = i + 1
	if colonne_j == 19 or (colonne_j < 19 and carte_de_reference[ligne_j][colonne_j + 1] == "V") :
		del directions_possibles[i]                 # East is blocked.
	elif player.position == west_river_mouth and not is_it_in_the_list("Barque de Charon", player.inventory["special"]) :# We can't go onto the river without the "barque de charon".
		del directions_possibles[i]                 # L'Est est bloqu??.
	elif is_it_in_the_list(player.position, west_river_bank) :
		del directions_possibles[i]                 # East is blocked.
	else :
		i = i + 1
	if colonne_j == 0 or (colonne_j > 0 and carte_de_reference[ligne_j][colonne_j - 1] == "V") :
		del directions_possibles[i]                 # West is blocked.
	elif player.position == east_river_mouth and not is_it_in_the_list("Barque de Charon", player.inventory["special"]) : # We can't go onto the river without the "barque de charon".
		del directions_possibles[i]                 # West is blocked.
	elif is_it_in_the_list(player.position, east_river_bank) :
		del directions_possibles[i]                 # L'ouest est bloqu??.
	
	# We show the map with the Hero's position before asking where they want to go.
	show_map(player)
	print("O?? voulez-vous aller ? Les directions suivantes sont disponibles :", directions_possibles, "(N : nord, S : sud, E : est, O : ouest)")
	print("Vous pouvez aussi ouvrir votre inventaire en appuyant sur I ou voir les statistiques de votre personnage en appuyant sur P.")
	direction_choisie = input()
	direction_choisie = direction_choisie.upper()
	while not is_it_in_the_list(direction_choisie, directions_possibles) :
		if direction_choisie == "I":
			player.show_inventory()
		if direction_choisie == "P":
			player.show_stats()
		else :
			print("\nIl est impossible d'aller dans cette direction.\n")
			time.sleep(2)
		show_map(player)
		print("O?? voulez-vous aller ? Les directions suivantes sont disponibles :", directions_possibles, "(N : nord, S : sud, E : est, O : ouest)")
		print("Vous pouvez aussi ouvrir votre inventaire en appuyant sur I ou voir les statistiques de votre personnage en appuyant sur P.")
		direction_choisie = input()
		direction_choisie = direction_choisie.upper()
	if direction_choisie == "N" :
		ligne_j = ligne_j - 1
	elif direction_choisie == "S" :
		ligne_j = ligne_j + 1
	elif direction_choisie == "E" :
		colonne_j = colonne_j + 1
	elif direction_choisie == "O" :
		colonne_j = colonne_j - 1
	return [ligne_j, colonne_j]





def spot_description(player):
	if player.position == [11, 12] and player.previous_position != [11, 13] :
		print("Un pont de bois permet de traverser la gorge vers l'Est. Il a l'air solide.")
		time.sleep(2)
	elif player.position == [11, 14] and player.previous_position != [11, 13] :
		print("Un pont de bois permet de traverser la gorge vers l'Ouest. Il a l'air solide.")
		time.sleep(2)
	elif is_it_in_the_list(player.position, west_river_bank) and player.position[0] > 8 :
		# The second condition avoids showing the message in the mountains, because they kept popping up, which was bothersome.
		if is_it_in_the_list(player.previous_position, west_river_bank) :
			print("Vous longez la rive Ouest de la rivi??re. La gorge est trop profonde pour traverser.")
			time.sleep(3)
		else :
			print("Vous vous trouvez au bord d'une gorge au fond de laquelle coule une rivi??re. Elle vous coupe la route ?? l'Est tandis que l'eau s'??coule tranquillement vers le sud en scintillant sous le soleil. La for??t sur l'autre rive est plus lumineuse que celle o?? vous vous trouvez.")
			time.sleep(5)
	elif is_it_in_the_list(player.position, east_river_bank) and player.position[0] > 8 :
		# The second condition avoids showing the message in the mountains, because they kept popping up, which was bothersome.
		if is_it_in_the_list(player.previous_position, east_river_bank) :
			print("Vous longez la rive Est de la rivi??re. La gorge est trop profonde pour traverser.")
			time.sleep(5)
		else :
			print("Vous vous trouvez au bord d'une gorge au fond de laquelle coule une rivi??re. Elle vous coupe la route ?? l'Ouest tandis que l'eau s'??coule tranquillement vers le sud en scintillant sous le soleil. La for??t sur l'autre rive est plus sombre que celle o?? vous vous trouvez.")
			time.sleep(5)
	# west mountain // dark forest junction
	elif player.position == [8, 6] :
		if player.previous_position == [9, 6] :
			print("Vous vous engagez sur le chemin rocailleux de la plus haute mountain. L'ascension promet d'??tre longue.")
			time.sleep(3)
		else :
			print("Vous ??tes arriv??s au pied de la mountain. Devant vous s'??tend une for??t lugubre. Aucun sentier ne se dessine entre les arbres immenses.")
			time.sleep(5)
	elif player.position == [9, 6] :
		if player.previous_position == [8, 6] :
			print("Vous vous engagez dans la p??nombre inqui??tante de la for??t. La v??g??tation dense ne vous permet pas de voir tr??s loin. Le danger peut ??tre partout dor??navant.")
			time.sleep(5)
		else :
			print("Le sentier s'??claire devant vous. Vous ??tes arriv?? en bordure de la for??t. Devant vous, au Nord, commencent les contreforts de mountains imposantes, qui dressent leurs sommets d??chiquet??s vers le ciel.")
			time.sleep(5)
	# east mountain // light forest junction
	elif player.position == [8, 16] :
		if player.previous_position == [9, 16] :
			print("Vous entamez l'ascension de la mountain la plus proche par un chemin bord?? de fleurs qui s'??l??ve en pente douce vers le sommet.")
			time.sleep(4)
		else :
			print("Vous ??tes de retour au pied de la mountain. Devant vous s'??tend une for??t luxuriante, parcourue de nombreux sentiers et baign??e d'une douce lumi??re.")
			time.sleep(5)
	elif player.position == [9, 16] :
		if player.previous_position == [8, 16] :
			print("Vous vous engagez sous les frondaisons. L'air frais embaume et vous voyez des ??cureuils bondir dans les arbres au milieu des chants d'oiseaux.\nCependant, vous restez sur vos gardes : qui sait quels monstres peuvent se cacher dans la v??g??tation luxuriante ?")
			time.sleep(5)
		else :
			print("Vous parvenez ?? la lisi??re de la for??t. De majestueuses mountains s'??l??vent devant vous, au Nord.")
			time.sleep(3)
	elif player.position == [10, 1] :
		if player.previous_position == [11, 1] :
			print("Vous vous engagez dans la p??nombre inqui??tante de la for??t. La v??g??tation dense ne vous permet pas de voir tr??s loin. Le danger peut ??tre partout dor??navant.")
			time.sleep(5)
		else :
			print("L'entr??e d'une grotte se dessine soudain derri??re les arbres. Elle provoque chez vous une sensation de profond malaise qui ne permet aucun doute. Ce n'est pas une simple grotte. C'est l'entr??e du royaume des Enfers.")
			time.sleep(5)
	elif player.position == [11, 1] :
		if player.previous_position == [10, 1] :
			print("Vous p??n??trez dans la grotte. Le passage est d'abord ??troit et vous n'y voyez rien mais il s'??largit rapidement et s'??claire peu ?? peu de mousses bioluminescentes, diffusant une ??trange lueur verd??tre.\nBien qu'elles accentuent encore votre sensation de malaise, elles vous permettent au moins de voir ?? quelques pas.")
			time.sleep(5)
		else :
			print("Vous quittez enfin les enfers, mais votre soulagement est de courte dur??e. Devant vous s'??tend une for??t lugubre. Aucun sentier ne se dessine entre les arbres immenses.")
			time.sleep(5)
	elif player.position == [13, 14] :
		if player.previous_position == [14, 14] :
			print("Vous laissez derri??re vous le royaume de Pos??idon et retrouvez les eaux paisibles de la rivi??re.\nLes rives s'??l??vent rapidement et la rivi??re s'enfonce dans une gorge. Vous devez regagner la terre ferme maintenant.\nDeux for??ts encadrent le cours d'eau. Celle ?? l'Est est a??r??e et pleine de vie. Celle ?? l'Ouest est dense et t??n??breuse.")
			time.sleep(5)
		else :
			print("Vous mettez votre barque ?? l'eau ?? l'embouchure du fleuve. Au Sud, la mer semble s'??tendre ?? l'infini, miroitant sous le soleil.")
			time.sleep(4)
	elif player.position == [14, 14] :
		if player.previous_position == [13, 14] :
			print("?? l'instant o?? vous prenez le large, le vent se l??ve, les vagues se font plus violentes, et de lourds nuages noirs s'amoncellent ?? l'horizon.\nLe message est clair : Pos??idon sait que vous ??tes l??, et vous n'??tes pas le bienvenu en son royaume.")
			time.sleep(5)
		else :
			print("Alors que vous commenciez ?? d??sesp??rer de quitter un jour la mer d??cha??n??e, les vagues s'apaisent et vous apercevez enfin au Nord la c??te et l'embouchure de la rivi??re.")
			time.sleep(5)
	return "description finie"





def spot_event(spot, fighting_spot_list):
	# list in RPG.py, where we kept the fighting spots, to avoid fighting twice on the same spot
	if is_it_in_the_list(spot, fighting_spot_list):
		if is_it_in_the_list(spot, hell_fight_spots):
			print("\nDes bruits ??tranges r??sonnent dans le tunnel. Vous vous arr??tez pour tendre l'oreille. Le son se pr??cise et se rapproche.\nVous regardez f??brilement autour de vous ?? la recherche d'une cachette, mais il n'y en a aucune. Trop tard : l'ennemi est l??.")
			action = "fight"
		elif is_it_in_the_list(spot, water_fight_spots):
			print("\nLa temp??te fait rage. Vous faites de votre mieux pour maintenir le cap, conscient qu'une barque ordinaire aurait d??j?? chavir?? depuis longtemps.\nSoudain, un frisson vous parcourt l'??chine. Il vous a sembl?? entendre un rugissement qui n'??tait pas celui du vent. Alors que vous pensez l'avoir imagin??, vous atteignez la cr??te d'une vague, et votre ennemi appara??t.")
			action = "fight"
		elif is_it_in_the_list(spot, mountain_fight_spots):
			print("\nVous vous accroupissez derri??re un rocher, aux aguets. Des pierres ont boug?? ?? quelques pas de l??, vous en ??tes s??r.\nTrop tard : vous avez d?? ??tre rep??r?? car le bruit se rapproche. Vous vous relevez, pr??t ?? faire face. Le combat est ?? pr??sent in??vitable.")
			action = "fight"
		elif spot == hell_boss :
			print("\nSur le sol et les murs, la pierre brute a laiss?? la place ?? du marbre noir vein?? d'argent.\nLe passage s'??largit pour devenir une salle immense, dont les murs r??percutent le bruit de vos pas en ??chos inqui??tants. Les ombres semblent gagner du terrain. Devant vous, o?? il n'y avait rien un instant auparavant, se dessine ?? pr??sent un tr??ne de marbre noir plus haut que trois hommes. Le tr??ne semble empty mais votre instinct vous dit qu'il n'en est rien. En son centre, l'obscurit?? semble se solidifier.")
			action = "fight"
		elif spot == water_boss :
			print("\nLe vent s'arr??te brusquement, les vagues se calment, la mer devient d'huile, mais pas un rayon de soleil ne perce les nuages.\nLe silence se fait oppressant. ?? quelques m??tres ?? peine de votre embarcation, la mer se met ?? bouillonner. Une silhouette se forme au centre du ph??nom??ne : une ombre immense, arm??e d'un trident de bronze.")
			action = "fight"
	else :
		if is_it_in_the_list(spot, water_object_spots):
			print("\nAu milieu de la temp??te, une vague ??norme s'abat sur votre esquif. Lorsqu'elle se retire, vous d??couvrez un objet au fond de la coque.")
			action = "object"
		elif is_it_in_the_list(spot, hell_object_spots):
			print("\nLes tunnels se ressemblent tous, les m??mes moussent verd??tres, quelques cristaux color??s, parfois un trou dans un mur laisse entrevoir un filet de lave.\nMais quelque chose attire votre attention : quelque chose brille dans une anfractuosit?? de la roche.")
			action = "object"
		elif is_it_in_the_list(spot, mountain_object_spots):
			print("\nLes graviers qui couvrent le chemin roulent sous vos pieds, rendant l'ascension encore plus p??nible sous le soleil qui vous assome.\nLe sommet vous para??t encore tellement loin. Vous marchez sur quelque chose qui roule et vous tombez brutalement. Vous regardez de plus pr??s de quoi il s'agit car, cette fois, ce n'??tait pas un gravier.")
			action = "object"
		elif is_it_in_the_list(spot, dark_forest):
			chance = randint(1, 100)
			if chance > 85 :
				print("\nLe soleil s'appr??te ?? dispara??tre derri??re les arbres, plongeant encore un peu plus la for??t dans la p??nombre.\nTous vos nerfs sont ?? vifs, et les corbeaux de plus en plus nombreux dans les arbres environnants n'arrangent rien. Soudain, tous s'envolent en m??me temps. Un instant plus tard, une ombre se dessine entre les troncs distordus.")
				action = "fight"
			elif chance > 70 :
				print("\nLe jour se l??ve. Vous avez pass?? la nuit roul?? en boule entre les racines d'un arbre mort.\nVous ??tes fatigu?? et pensez ne jamais sortir de cette for??t. Mais vous reprenez un peu espoir en levant les yeux : le petit jour ??claire un objet dans un arbre creux en face de vous.")
				action = "object"
			else :
				action = "rien"
		elif is_it_in_the_list(spot, light_forest):
			chance = randint(1, 100)
			if chance > 85 :
				print("\nDepuis un moment, vous vous sentez comme un intrus au milieu de cette beaut?? luxuriante.\nVous ??cartez une liane qui pend en travers du passage et, brusquement, vous vous figez. Vous avez compris la source de votre malaise : la for??t s'est tue. Alors m??me que vous r??alisez ce que cela signifie, un bruit vous fait vous retourner.")
				action = "fight"
			elif chance > 70 :
				print("\nLe soleil est bas sur l'horizon lorsque vous trouvez enfin une clairi??re o?? passer la nuit.\nLa for??t vous a fourni tout ce dont vous pouviez avoir besoin : de l'eau, de la nourriture, et toutes les herbes m??dicinales n??cessaires ?? la pr??paration d'un rem??de, ou peut-??tre m??me d'un nectar.")
				action = "object"
			else :
				action = "rien"
		elif spot == mountain_boss :
			print("\nUn brouillard ??pais s'est install?? et vous ne voyez pas ?? plus de quelques pas devant vous.\nIl se dissipe peu ?? peu, r??v??lant une all??e de marbre blanc bord??e de colonnes. Le ciel au-dessus de vous est charg?? de lourds nuages noirs. Vous vous avancez entre les colonnes. Venu de nulle part, un ??clair frappe le sol quelques m??tres plus loin, ??clatant le marbre et soulevant un nuage de fum??e. Le coup de tonnerre est si puissant qu'il vous sonne et vous fait chuter ?? quatre pattes sur le sol. Alors que vous vous relevez avec difficult??, le ma??tre des lieux ??merge du nuage de poussi??re.")
			action = "fight"
		else :
			action = "rien"
	return action





def spot_enemy(spot):      # sends back the enemy's index in Enemies_list (Ennemies.py)
	if spot == water_boss :
		return 18   # "Pos??idon"
	elif spot == hell_boss :
		return 17   # "Had??s"
	elif spot == mountain_boss :
		return 19   # "Zeus"
	elif spot == [7, 4] :
		return 14   # "Ar??s"
	elif spot == [15, 18] :
		return 15   # "Dyonisos"
	elif spot == [13, 1] :
		return 16   # "Pers??phone"
	elif is_it_in_the_list(spot, [[2, 16], [5, 8], [7, 9], [7, 17]]) :		# random in the mountain
		random_monster = randint(1, 7)
		if random_monster <= 2 :
			return 0    # "Harpie"
		elif random_monster <= 4 :
			return 1    # "Cyclope"
		elif random_monster <= 6 :
			return 5    # "Gryffon"
		else :
			return 13   # "Apollon"
	elif is_it_in_the_list(spot, [[15, 3], [20, 0]]) :					# random in hell
		random_monster = randint(1, 3)
		if random_monster <= 2 :
			return 3    # "Cerb??re"
		else :
			return 7    # "Sphinx"    
	elif is_it_in_the_list(spot, [[17, 13], [18, 10], [20, 11]]) :		# random in the sea
		random_monster = randint(1, 6)
		if random_monster <= 2 :
			return 4    # "Lamia"
		elif random_monster <= 5 :
			return 6    # "Sir??nes"
		else :
			return 11   # "Aphrodite"
	elif is_it_in_the_list(spot, dark_forest) or is_it_in_the_list(spot, light_forest) :
		monster_or_god = randint(0, 5)
		if monster_or_god == 0 : 					# gods
			random_god = randint(0, 3)
			if random_god == 0:
				return 10   # "Ath??na"
			elif random_god == 1:
				return 11   # "Aphrodite"
			elif random_god == 2:
				return 12   # "Art??mis"
			else:
				return 13   # "Apollon"
		else : 										# monsters
			random_monster = randint(1, 14)
			# Level 1 & 2 monsters pop up more often, to help gain levels in the beginning
			if random_monster <= 2 :
				return 0    # "Harpie"
			elif random_monster <= 4 :
				return 1    # "Cyclope"
			elif random_monster <= 6 :
				return 2    # "Minotaure"
			elif random_monster <= 8 :
				return 3    # "Cerb??re"
			elif random_monster <= 10 :
				return 4    # "Lamia"
			elif random_monster == 11 :
				return 5    # "Griffon"
			elif random_monster == 12 :
				return 7    # "Sphinx"
			elif random_monster == 13 :
				return 8    # "Lion de N??m??e"
			else :
				return 9    # "M??duse"
		