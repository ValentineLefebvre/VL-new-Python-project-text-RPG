from random import randint
import os
import time
from is_it_in_the_list import *
from Attacks import *
from Objects import *

class Player:
	def __init__(self , godly_parent , player_name):
		self.name = player_name
		self.parent = godly_parent

		if godly_parent == "Zeus":
			self.max_hp = 100
			self.atk = 60
			self.defense = 50
			self.max_mana = 100
			self.bow_bonus = 1
			self.sword_bonus = 1
			self.critical_bonus = 1
			self.possible_spells = {
				2 : "Chataigne", 
				4 : "Coup de jus", 
				6 : "Eclair", 
				8 : "Orage", 
				10 : "Ouragan"
			}

		elif godly_parent == "Poséidon":
			self.max_hp = 100
			self.atk = 50
			self.defense = 50
			self.max_mana = 120
			self.bow_bonus = 0.8
			self.sword_bonus = 1.25
			self.critical_bonus = 1
			self.possible_spells = {
				2 : "De l'eau !", 
				4 : "Vague", 
				6 : "Attaque sous-marine", 
				8 : "Séisme", 
				10 : "Tsumani"
			}

		elif godly_parent == "Hadès":
			self.max_hp = 100
			self.atk = 70
			self.defense = 40
			self.max_mana = 100
			self.bow_bonus = 1
			self.sword_bonus = 1
			self.critical_bonus = 1
			self.possible_spells = {
				2 : None, 
				4 : None, 
				6 : "Attaque à travers les ombres", 
				8 : "Garde squelette", 
				10 : "Armée des morts-vivants"
			}

		elif godly_parent == "Athéna":
			self.max_hp = 100
			self.atk = 50
			self.defense = 50
			self.max_mana = 100
			self.bow_bonus = 1.2
			self.sword_bonus = 1.2
			self.critical_bonus = 1.25
			self.possible_spells = {
				2 : "Botte désarmante", 
				4 : "Casquette d'invisibilité", 
				6 : None, 
				8 : "Plan presque infaillible", 
				10 : None
			}

		elif godly_parent == "Arès":
			self.max_hp = 100
			self.atk = 70
			self.defense = 40
			self.max_mana = 100
			self.bow_bonus = 1
			self.sword_bonus = 1.5
			self.critical_bonus = 1
			self.possible_spells = {
				2 : "Botte désarmante", 
				4 : None, 
				6 : None, 
				8 : None, 
				10 : "Berserker"
			}

		elif godly_parent == "Apollon":
			self.max_hp = 120
			self.atk = 40
			self.defense = 60
			self.max_mana = 100
			self.bow_bonus = 1.5
			self.sword_bonus = 1
			self.critical_bonus = 1
			self.possible_spells = {
				2 : "Guérison mineure", 
				4 : "Flèche d'arc-lyre", 
				6 : "Michel Sardou à la Lyre", 
				8 : "Guérison majeure", 
				10 : "Flèche solaire"
			}

		elif godly_parent == "Hermès":
			self.max_hp = 120
			self.atk = 30
			self.defense = 60
			self.max_mana = 120
			self.bow_bonus = 1
			self.sword_bonus = 1
			self.critical_bonus = 1.25
			self.possible_spells = {
				2 : "Guérison mineure", 
				4 : "Trop de courrier", 
				6 : "Demi-guérison", 
				8 : "Attaque en traitre", 
				10 : "Guérison divine"
			}

		# initaializing common stats
		self.hp = self.max_hp
		self.mana = self.max_mana
		self.xp = 0
		self.level = 1
		self.inventory = {
			"potions" : {
				"remedies": 0, 
				"nectars" : 0
			}, 
			"armor" : [], 
			"weapons" : [], 
			"special" : []
		}
		self.basic_attacks = ["Attaquer à main nues", "Attaquer à l'épée", "Tir à l'arc"]
		self.known_spells = []
		self.previous_position = [12, 5]
		self.position = [12, 5]
	

	# functions about the hero
	def show_inventory(self):
		if self.inventory == {
			"potions" : {
				"remedies": 0, 
				"nectars" : 0
			}, 
			"armor" : [], 
			"weapons" : [], 
			"special" : []
		} :
			print("Votre inventaire est vide.")
		else :
			print("\n~INVENTAIRE~\n")
			if self.inventory["potions"]["remedies"] != 0 or self.inventory["potions"]["nectars"] != 0 :
				print("Potions (les remèdes restaurent les PV et les nectars restaurent le mana) :\n  *", self.inventory["potions"]["remedies"], " remède(s)\n  *", self.inventory["potions"]["nectars"], " nectar(s)")
			if self.inventory["armor"] != [] :
				print("Pièces d'armure (boostent votre défense) :")
				for i in range(len(self.inventory["armor"])) :
					print("  *", self.inventory["armor"][i])
			if self.inventory["weapons"] != [] :
				print("Armes (boostent votre attaque) :")
				for i in range(len(self.inventory["weapons"])) :
					print("  *", self.inventory["weapons"][i])
			if self.inventory["special"] != [] :
				print("Autres objets :")
				for i in range(len(self.inventory["special"])) :
					print("  *", self.inventory["special"][i])
		print("\n")
		time.sleep(2)
		pass

	def show_stats(self):
		print("\n~À PROPOS DE VOTRE PERSONNAGE~\n")
		text = "Vous vous appelez " + self.name + " et votre parent divin est " + self.parent + "." 
		print(text)
		time.sleep(1)
		print("\nStatistiques :")
		print("  * Niveau :", self.level)
		print("  * Points de vie :", self.max_hp)
		print("  * Attaque :", self.atk)
		print("  * Défense :", self.defense)
		print("  * Mana maximum :", self.max_mana)
		print("  * Bonus de coup critique :", self.critical_bonus)
		print("  * Bonus à l'épée :", self.sword_bonus)
		print("  * Mana au tir à l'arc :", self.bow_bonus)
		print("\n")
		time.sleep(6)
		pass

	# functions regarding the hero's growth

	def learn_a_spell(self):
		if is_it_in_the_list(self.level, [2, 4, 6, 8, 10]):
			new_spell = self.possible_spells[self.level]
			if not is_it_in_the_list(new_spell, self.known_spells): # to be sure we're not going to learn the spell twice
				self.known_spells.append(new_spell)
				if new_spell != None :
					print("Vous avez appris un nouveau sort : ", new_spell)
		else :
			return "Error: not supposed to learn a new spell at this level"
		pass

	def level_up(self):
		required_xp = 100 + (50 * (self.level - 1))
		if self.xp >= required_xp :
			self.xp -= required_xp
			self.level += 1
			print("Félicitations ! Vous venez de gagner un niveau !")
			print("Vous êtes maintenant au niveau ", self.level, ". Vos statistiques augmentent :")
			past_max_hp = self.max_hp
			self.max_hp = round(self.max_hp * 1.5)
			self.hp = self.max_hp
			print("  * Points de vie :", past_max_hp, "-->", self.max_hp)
			past_atk = self.atk
			self.atk = round(self.atk * 1.5)
			print("  * Attaque :", past_atk, "-->", self.atk)
			past_defense = self.defense
			self.defense = round(self.defense * 1.5)
			print("  * Défense :", past_defense, "-->", self.defense)
			past_max_mana = self.max_mana
			self.max_mana = round(self.max_mana * 2)
			self.mana = self.max_mana
			print("  * Mana maximum :", past_max_mana, "-->", self.max_mana)
			if is_it_in_the_list(self.level, [2, 4, 6, 8, 10]):
				self.learn_a_spell()
		else :
			message = "Il vous manque " + str(required_xp - self.xp) + " points d'expérience pour monter en niveau. Vous restez au niveau " + str(self.level) + "."
			print(message)
		pass

	# Recovery functions

	def heal(self, amount_in_percent):
		if amount_in_percent == 100 : # merely to avoid useless operations later
			recovery = self.max_hp - self.hp
		else :
			recovery = round(self.max_hp * amount_in_percent / 100)
			if recovery > self.max_hp - self.hp :
				recovery = self.max_hp - self.hp
		print("Vous regagnez ", recovery, " PV.")
		self.hp += recovery
		print("Vous avez à présent ", self.hp, "/", self.max_hp, " PV.")
		time.sleep(4)
	
	def recover_mana(self, amount_in_percent):
		if amount_in_percent == 100 : # merely to avoid useless operations later
			recovery = self.max_mana - self.mana
		else :
			recovery = round(self.max_mana * amount_in_percent / 100)
			if recovery > self.max_mana - self.mana :
				recovery = self.max_mana - self.mana
		print("Vous regagnez ", recovery, " points de mana.")
		self.mana += recovery
		print("Vous avez à présent ", self.mana, "/", self.max_mana, " points de mana.")
		time.sleep(4)
	
	# boost functions

	def defense_boosted(self, new_item):			 # We must call this function only when we're finding a new object, or else we're going to boost the character's defense infinitely. 
		if Armor_informations[new_item]["stars"] == 1 :
			former_defense = self.defense
			self.defense = round(self.defense * 1.1)
			print("Vous serez un peu mieux protégé(e) des attaques, à présent : ", former_defense, " --> ", self.defense)
		elif Armor_informations[new_item]["stars"] == 2 :
			former_defense = self.defense
			self.defense = round(self.defense * 1.2)
			print("Vous serez bien mieux mieux protégé(e) des attaques, à présent : ", former_defense, " --> ", self.defense)
		else :
			print("Erreur : objet inconnu")
	
	def attack_boosted(self, new_item):			 # We must call this function only when we're finding a new object, or else we're going to boost the character's attack infinitely.
		if Weapon_informations[new_item]["type"] == "sword" :
			if Weapon_informations[new_item]["stars"] == 2 :
				former_sword_bonus = self.sword_bonus
				self.sword_bonus = round(self.sword_bonus * 1.5)
				print("Votre attaque à l'épée infligera davantage de dégâts, à présent :")
				print("Bonus à l'épée : ", former_sword_bonus, " --> ", self.sword_bonus)
			elif Weapon_informations[new_item]["stars"] == 3 :
				former_sword_bonus = self.sword_bonus
				self.sword_bonus = round(self.sword_bonus * 2)
				print("Votre attaque à l'épée infligera davantage de dégâts, à présent :")
				print("Bonus à l'épée : ", former_sword_bonus, " --> ", self.sword_bonus)
				former_atk = self.atk
				self.atk = round(self.atk * 1.2)
				print("Cet objet augmente également votre attaque : ", former_atk, " --> ", self.atk)
			else :
				print("Erreur : objet inconnu")
		elif Weapon_informations[new_item]["type"] == "bow" :
			if Weapon_informations[new_item]["stars"] == 2 :
				former_bow_bonus = self.bow_bonus
				self.bow_bonus = round(self.bow_bonus * 1.5)
				print("Votre tir à l'arc infligera davantage de dégâts, à présent :")
				print("Bonus au tir à l'arc : ", former_bow_bonus, " --> ", self.bow_bonus)
			elif Weapon_informations[new_item]["stars"] == 3 :
				former_bow_bonus = self.bow_bonus
				self.bow_bonus = round(self.bow_bonus * 2)
				print("Votre tir à l'arc infligera davantage de dégâts, à présent :")
				print("Bonus au tir à l'arc : ", former_bow_bonus, " --> ", self.bow_bonus)
				former_atk = self.atk
				self.atk = round(self.atk * 1.2)
				print("Cet objet augmente votre attaque : ", former_atk, " --> ", self.atk)
			else :
				print("Erreur : objet inconnu")
		else :
			print("Erreur : objet inconnu")



	def injured(self, damage) :
		if damage  > self.defense :
			actual_damage = damage - self.defense
			if actual_damage < self.hp :
				print("Vous perdez", actual_damage, "PV.")
				self.hp -= actual_damage
				print("Il vous reste", self.hp, "PV.")
			else :
				print("Vous perdez tous vos PV.")
				self.hp = 0
		else :
			print("Vous ne subissez aucun dégât.")



	def attack_damage(self, attack_name):
		attack = all_attacks[attack_name]
		if attack["power"] == 0 :
			damage = 0
		else :
			damage = round(self.atk * attack["power"])
			if attack["sword bonus"] == True :
				damage = damage * self.sword_bonus
			if attack["bow bonus"] == True :
				damage = damage * self.bow_bonus
		return int(damage)

	def attack_description(self, attack_name) :
		if attack_name == None :
			Description = "Erreur : pas d'attaque"
		else :
			damage = self.attack_damage(attack_name)
			attack = all_attacks[attack_name]
			if attack["power"] == 0 :
				if attack["effect"] == None :
					Description = attack_name + " | soin : " + str(attack["heal"]) + " % | coût : " + str(attack["cost"]) + " points de mana"
					return Description
				else :
					Description = attack_name + " | soin :" + str(attack["heal"]) + " % | coût :" + str(attack["cost"]) + " points de mana |" + attack["effect"]
					return Description
			
			else :
				damage_to_show = str(int(damage))

				if attack["heal"] == 0 :
					if attack["effect"] == None :
						Description = attack_name + " | " + damage_to_show + " points de dégât | coût : " + str(attack["cost"]) + " points de mana"
						return Description
					else :
						Description = attack_name + " | " + damage_to_show + " points de dégât | coût : " + str(attack["cost"]) + " points de mana | " + attack["effect"]
						return Description
				else :
					if attack["effect"] == None :
						Description = attack_name + " | " + damage_to_show + " points de dégât | soin : " + str(attack["heal"]) + " % | coût : " + str(attack["cost"]) + " points de mana"
						return Description
					else :
						Description = attack_name + " | " + damage_to_show + " points de dégât | soin :" + str(attack["heal"]) + " % | coût : " + str(attack["cost"]) + " points de mana | " + attack["effect"]
						return Description

	# in-fight functions

	def attack_list(self):
		L = self.basic_attacks + self.known_spells
		print("Vous avez", self.mana, "points de mana.")
		print("Choisissez l'attaque à utiliser en entrant son numéro :")
		i = 0
		while i < len(L) :
			print("  *", i+1, ":", self.attack_description(L[i]))
			i += 1
		print("  * A : Annuler")
		return L

	def use_potion(self):
		if self.inventory["potions"] == {
				"remedies": 0, 
				"nectars" : 0
			} :
			print("Vous n'avez aucune potion à utiliser.")
			return 0
		elif self.hp == self.max_hp and self.mana == self.max_mana :
			print("Vous n'avez pas besoin de potion maintenant.")
			return 0
		else :
			# let's clarify the conditions
			remedy_possible = True
			if self.inventory["potions"]["remedies"] == 0 or self.hp == self.max_hp :
				remedy_possible = False
			nectar_possible = True
			if self.inventory["potions"]["nectars"] == 0 or self.mana == self.max_mana :
				nectar_possible = False
			# now onto the real thing
			if remedy_possible and nectar_possible :
				choice = ""
				while choice != "A" and choice != "B" and choice != "C" :
					print("Les remèdes restaurent les PV et les nectars restaurent le mana.\nChoisissez la potion à utiliser en entrant la lettre correspondante :\n  A-", self.inventory["potions"]["remedies"], " remède(s)\n  B-", self.inventory["potions"]["nectars"], " nectar(s)\n  C- Quitter")
					choice = input()				# choice of potion
					choice = choice.upper()			# just in case we answered in lowercase
					os.system("cls")
				if choice == "A" :
					self.heal(75)
					self.inventory["potions"]["remedies"] -= 1
					return 1
				elif choice == "B" :
					self.recover_mana(100) 			# we'll see whether we tone this down a bit.
					self.inventory["potions"]["nectars"] -= 1
					return 1
				else :
					return 0
			else :
				if remedy_possible :
					choice = ""
					while choice != "Y" and choice != "N" :
						print("Voulez-vous utiliser une potion pour retrouver quelques PV ? Entrez Y pour oui et N pour non")
						choice = input()
						choice = choice.upper()			# just in case we answered in lowercase
						os.system("cls")
					if choice == "Y" :
						self.heal(75)
						self.inventory["potions"]["remedies"] -= 1
						return 1
					else :
						return 0
				else :	# if nectar_possible
					choice = ""
					while choice != "Y" and choice != "N" :
						print("Voulez-vous utiliser un nectar pour régénérer votre mana ? Entrez Y pour oui et N pour non")
						choice = input()
						choice = choice.upper()			# just in case we answered in lowercase
						os.system("cls")
					if choice == "Y" :
						self.recover_mana(100)
						self.inventory["potions"]["nectars"] -= 1
						return 1
					else :
						return 0
