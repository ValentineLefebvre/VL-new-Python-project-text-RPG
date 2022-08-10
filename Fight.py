# Pour tester le jeu, c'est RPG.py qu'il faut lancer.


from asyncio.windows_events import NULL
from random import randint
import os
from is_it_in_the_list import *
import time
from Class_player import *
from Class_enemies import *


def player_escape() : 		# When the player chooses to escape, we check wether he succeeds or not
	escape = randint(0, 9)
	if escape <= 8 :
		escape_result = "fuite"
		os.system("cls")
		print("Vous réussissez à fuir.")
		time.sleep(1)
	else :					# 1 "chance" out of ten that we fail to escape
		escape_result = "fail"
		os.system("cls")
		print("Vous n'arrivez pas à fuir.")
		time.sleep(1)
	return escape_result


def critical_hit(attack_power, who) :		# function used both for the player and the enemies
	chance = randint(1, 100)
	if is_it_in_the_list(who.name, Enemies_list) : # testing if it's the player or the enemy
		name = who.name
		if chance > 90 :
			attack_power = attack_power * 2 
			print(name, "fait un coup critique.")
	else :
		chance = chance * who.critical_bonus
		if chance > 90 :
			attack_power = attack_power * 2 
			print("Vous faites un coup critique.")
	return attack_power

def dodge(attack_power, who, effect=None):		# Function used both for the player and the enemies
	if effect == "Impossible à esquiver" :
		return attack_power
	if is_it_in_the_list(who.name, Enemies_list) : 	# testing if it's the player or the enemy
		name = who.name
		message = name + " esquive."
	else :
		message = "Vous esquivez."
	chance = randint(1, 100)
	if chance > 90 :
		print(message)
		return 0
	else :
		return attack_power


def player_attacks(player, enemy) :
	first_try = True
	L = player.attack_list()
	L2 = []
	for i in range(1, len(L)+1):					# just the possible entries for the input
		L2.append(str(i))
	choice = -1
	chosen_attack_details = {"name":None, "cost":1000000000}
	# the while and if/elif below ar for dealing with possible input errors
	while (not is_it_in_the_list(choice, L2)) or chosen_attack_details["cost"] > player.mana :
		if not is_it_in_the_list(choice, L2) :
			if not first_try :
				if choice.upper() == "A" :
					return "Quit"
				print("Choix non valide. Veuillez entrer le numéro de l'attaque souhaitée.")
				player.attack_list()
			first_try = False
			choice = input()								# The player chooses which attack to use.
			if is_it_in_the_list(choice, L2) :	# if i don't check that and we enter something random, it will crash
				chosen_attack_name = L[int(choice) - 1]
				chosen_attack_details = all_attacks[chosen_attack_name]
			# else :
			# 	choice = -1
		elif chosen_attack_details["cost"] > player.mana :
			print("Vous n'avez pas assez de mana pour utiliser cette attaque.")
			L = player.attack_list()
			choice = input()								# The player chooses which attack to use.
			chosen_attack_name = L[int(choice) - 1]
			chosen_attack_details = all_attacks[chosen_attack_name]
	os.system("cls")
	damage = player.attack_damage(chosen_attack_name)
	text = "Vous utilisez '" + chosen_attack_name + "'."
	print(text)
	player.mana -= chosen_attack_details["cost"]
	if damage != 0 :
		effective_damage = dodge(damage, enemy, chosen_attack_details["effect"])
		if effective_damage > 0 :
			effective_damage = critical_hit(effective_damage, player) # useless if the enemy avoided the attack
		enemy.injured(effective_damage)
	if chosen_attack_details["effect"] == "Peut empêcher l'ennemi d'attaquer" :
		return True
	else :
		return False


def enemy_attacks(enemy, player) :
	number = randint(1, 10)
	if number < enemy.proba_for_2nd_attack * 10 :
		attack_number = 2
	else :
		attack_number = 1
	attack_name = enemy.moves[attack_number]
	attack_effect = all_attacks[attack_name]["effect"]
	os.system("cls")
	damage = enemy.attack_damage(attack_number)
	text = enemy.name + " utilise '" + attack_name + "'."
	print(text)
	if damage != 0 :
		effective_damage = dodge(damage, player, attack_effect)
		if effective_damage > 0 :
			effective_damage = critical_hit(effective_damage, enemy) # useless if the player avoided the attack
		player.injured(effective_damage)


def fight(player, enemy, ongoing, skip_turn):
	if not ongoing :
		print(enemy.start_text)
		if player.level < enemy.level :
			# Some enemies pop randomly, so we warn the player when one is too dangerous.
			print("\nCet ennemi est meilleur que vous ! La fuite est fortement conseillée !\n")
		print("\n", "Vous avez", player.hp, "point(s) de vie.\n")
		print("\n", enemy.name, "a", enemy.hp, "point(s) de vie.\n")

	while enemy.hp > 0 and player.hp > 0 :
		turn = "player"
		escape= str()
		action = 0
		while not is_it_in_the_list(action, ["1", "2", "3"]):
			print("Que voulez-vous faire ? (Entrez le numéro de l'action.)")
			print("1.attaquer")
			print("2.utiliser un objet")
			print("3.fuir")
			action = input()
			os.system("cls")
		if action == "1" :							# player chooses to attack
			skip_turn = player_attacks(player, enemy)
			if skip_turn == "Quit" :
				# if, in the end, the player didn't attack, it's his turn again.
				os.system("cls")
				fight(player, enemy, True, False)
			turn = "enemy"
			time.sleep(5)
			
		elif action == "2" :						# player chooses to use a potion
			potion = player.use_potion()
			if potion == 0:
				# if, in the end, the player didn't use a potion, it's his turn again.
				fight(player, enemy, True, False)
		
		elif action == "3" :						# player chooses to escape.
			escape = player_escape()
		else :
			fight(player, enemy, True, False)
		if escape == "fuite" :						# if escape succeeded.
			player.mana = player.max_mana
			player.hp = player.max_hp
			enemy.hp = enemy.max_hp
			return "fuite"
		else :
			turn = "enemy"
		while turn == "enemy" :
			if enemy.hp == 0 :
				print(enemy.victory_text)
				time.sleep(4)
				player.mana = player.max_mana
				player.hp = player.max_hp
				enemy.hp = enemy.max_hp			# Some enemies can pop several times so we need to heal them.
				return "gagné"					# The enemy is dead. The player can move again.
			if skip_turn :
				chance = randint(1, 100)
				if chance <= 15 :
					print("Votre dernière attaque a empêché l'ennemi d'attaquer ! Profitez-en !")
				else :
					enemy_attacks(enemy, player)
			else :
				enemy_attacks(enemy, player)
			time.sleep(4)
			turn = "player"
		if player.hp != 0 :
			os.system("cls")
			print("Il vous reste", player.hp, "pv.")
			print("L'adversaire a ", enemy.hp, "pv.")

	
	if enemy.hp == 0 :
		print(enemy.victory_text)
		time.sleep(4)
		player.mana = player.max_mana
		player.hp = player.max_hp
		enemy.hp = enemy.max_hp				# Some enemies can pop several times so we need to heal them.
		return "gagné"                      # The enemy is dead. The player can move again.

	elif player.hp == 0 :                   # The player is dead. Game over.
		print(enemy.loss_text)
		time.sleep(4)
		return "game over"
