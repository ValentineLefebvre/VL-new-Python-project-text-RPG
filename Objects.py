
from random import randint
import os
from Map_and_descriptions import is_it_in_the_list
import time
armor_list = ["des gantelets", "des brassards", "des jambières","une cotte de mailles", "une cuirasse", "un casque"]
weapon_list = ["une épée courte en acier","un arc en bois","une épée longue en bronze céleste","un grand arc à flèches de bronze"]

Armor_informations = {
	"des gantelets" : {
		"stars" : 1
	},
	"des brassards" : {
		"stars" : 1
	},
	"des jambières" : {
		"stars" : 1
	},
	"une cotte de mailles" : {
		"stars" : 2
	},
	"une cuirasse" : {
		"stars" : 2
	},
	"un casque" : {
		"stars" : 2
	}
}
Weapon_informations = {
	"une épée courte en acier" : {
		"stars" : 2,
		"type" : "sword"
	},
	"un arc en bois" : {
		"stars" : 2,
		"type" : "bow"
	},
	"une épée longue en bronze céleste" : {
		"stars" : 3,
		"type" : "sword"
	},
	"un grand arc à flèches de bronze" : {
		"stars" : 3,
		"type" : "bow"
	},
}

def possible_loot(player):
	possible_armor = []
	possible_1star_armor = []
	possible_2stars_armor = []
	possible_weapons = []
	possible_swords = []
	possible_bows = []

	# possible armor
	for i in range(0,len(armor_list)) :
		if not is_it_in_the_list(armor_list[i],player.inventory["armor"]) :
			this_object = armor_list[i]
			possible_armor.append(this_object)
			if Armor_informations[this_object]["stars"] == 1:
				possible_1star_armor.append(this_object)
			else:
				possible_2stars_armor.append(this_object)
	# possible weapons
	for i in range(0,len(weapon_list)) :
		if not is_it_in_the_list(weapon_list[i],player.inventory["weapons"]) :
			this_object = weapon_list[i]
			possible_weapons.append(this_object)
			if Weapon_informations[this_object]["type"] == "sword" :
				possible_swords.append(this_object)
			else :
				possible_bows.append(this_object)
	return [possible_armor, possible_1star_armor, possible_2stars_armor, possible_weapons, possible_swords, possible_bows]


def loot_type(hero):
	available_loot = possible_loot(hero)
	available_armor = available_loot[0]
	available_weapons = available_loot[3]
	if available_armor == [] and available_weapons == [] :
		print("\nAucun objet à trouver : il doit rester quelque chose à corriger dans RPG ou Combat pour que la fonction loot ne soit pas appelée à ce moment-là.\n")
		weapon_or_armor = None
	else :
		if available_armor == [] :
			weapon_or_armor = "weapon"
		elif available_weapons == [] :
			weapon_or_armor = "armor"
		else :
			heads_or_tails = randint(0,1)
			if heads_or_tails == 0 :
				weapon_or_armor = "weapon"
			else :
				weapon_or_armor = "armor"
	return weapon_or_armor
		

def loot(player):		# This function calls the two previous ones and picks the loot for the player.
	what_type = loot_type(player)
	if what_type == None :
		print("Error : no loot type")
		return
	available_loot = possible_loot(player)
	# [possible_armor, possible_weapons, possible_swords, possible_bows]
	if what_type == "armor":
		armor_1star = available_loot[1]
		armor_2stars = available_loot[2]
		if armor_1star == [] and armor_2stars == []:
			print("erreur : liste vide")
		else :
			if armor_1star == [] :
				loot_list = armor_2stars
			elif armor_2stars == [] :
				loot_list = armor_1star
			else :
				rarity = randint(0,9)
				if rarity < 3 :
					loot_list = armor_2stars
				else :
					loot_list = armor_1star
			number = randint(0,len(loot_list)-1)
			obtained_loot = loot_list[number]
			print("\nOBTENU :", obtained_loot)
			player.inventory["armor"].append(obtained_loot)
			player.defense_boosted(obtained_loot)

	else :	# weapon
		swords = available_loot[4]
		bows = available_loot[5]
		if swords == [] and bows == [] :
			print("erreur : liste vide")
		else :
			# what type of weapon do we get ?
			if swords == [] :
				loot_list = bows
			elif bows == [] :
				loot_list = swords
			else :
				weapon_type = randint(0,1)
				if weapon_type == 0 :
					loot_list = bows

				else :
					loot_list = swords
			# now which weapon do we get exactly ?
			if loot_list == bows :
				# we only get the 3 stars weapons once we already have the 2 stars equivalent
				if is_it_in_the_list("un arc en bois", player.inventory["weapons"]):
					obtained_loot = "un grand arc à flèches de bronze"
				else :
					obtained_loot = "un arc en bois"
			else :
				# we only get the 3 stars weapons once we already have the 2 stars equivalent
				if is_it_in_the_list("une épée courte en acier", player.inventory["weapons"]):
					obtained_loot = "une épée longue en bronze céleste"
				else :
					obtained_loot = "une épée courte en acier"
			player.inventory["weapons"].append(obtained_loot)
			print("\nOBTENU :", obtained_loot)
			player.attack_boosted(obtained_loot)
	time.sleep(3)
	return
