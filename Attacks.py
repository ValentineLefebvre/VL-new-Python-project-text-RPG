from is_it_in_the_list import *


all_attacks = {
	# For those who don't have a special attack (don't know if I'm gonna need it or not...)
	"None" : {
		"power" : 0,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	# Basic attacks that every hero has from the start
	"Attaquer à main nues" : {
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Attaquer à l'épée" : {
		"power" : 1.5,
		"cost" : 5,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : True,
		"bow bonus" : False
	},
	"Tir à l'arc" : {
		"power" : 1.5,
		"cost" : 5,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : True
	},



	# Attacks for Zeus' children
	"Chataigne" : {
		"power" : 2,
		"cost" : 20,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Coup de jus" : {
		"power" : 4,
		"cost" : 50,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Eclair" : {
		"power" : 6,
		"cost" : 100,
		"heal" : 0,
		"effect" : "Peut empêcher l'ennemi d'attaquer",		# 15% chance (see skip_turn in Combat.py)
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Orage" : {
		"power" : 8,
		"cost" : 200,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Ouragan" : {
		"power" : 10,
		"cost" : 500,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},



	# Attacks for "Poséidon"'s children
	"De l'eau !" : {
		"power" : 0,
		"cost" : 20,
		"heal" : 10,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Vague" : {
		"power" : 4,
		"cost" : 50,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Attaque sous-marine" : {
		"power" : 6,
		"cost" : 100,
		"heal" : 20,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Séisme" : {
		"power" : 8,
		"cost" : 200,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Tsumani" : {
		"power" : 10,
		"cost" : 500,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},



	# Attacks for Hades' children
	"Attaque à travers les ombres" : {
		"power" : 6,
		"cost" : 100,
		"heal" : 0,
		"effect" : "Impossible à esquiver",
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Garde squelette" : {
		"power" : 8,
		"cost" : 200,
		"heal" : 0,
		"effect" : "Peut empêcher l'ennemi d'attaquer",
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Armée des morts-vivants" : {
		"power" : 10,
		"cost" : 500,
		"heal" : 0,
		"effect" : "Peut empêcher l'ennemi d'attaquer",
		"sword bonus" : False,
		"bow bonus" : False
	},



	# Attacks for Athena's children
	"Botte désarmante" : {	# also for Arès' children
		"power" : 2,
		"cost" : 20,
		"heal" : 0,
		"effect" : "Peut empêcher l'ennemi d'attaquer",
		"sword bonus" : True,
		"bow bonus" : False
	},
	"Casquette d'invisibilité" : {
		"power" : 4,
		"cost" : 50,
		"heal" : 0,
		"effect" : "Impossible à esquiver",
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Plan presque infaillible" : {
		"power" : 8,
		"cost" : 200,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},



	# Attacks for Arès' children (see one in common with Athena's children)
	"Berserker" : {
		"power" : 12,
		"cost" : 500,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : True,
		"bow bonus" : False
	},



	# Attacks for Appolon's children
	"Guérison mineure" : {
		"power" : 0,
		"cost" : 20,
		"heal" : 10,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Flèche d'arc-lyre" : {
		"power" : 4,
		"cost" : 50,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : True
	},
	"Michel Sardou à la Lyre" : {
		"power" : 6,
		"cost" : 100,
		"heal" : 0,
		"effect" : "Peut empêcher l'ennemi d'attaquer",
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Guérison majeure" : {
		"power" : 0,
		"cost" : 200,
		"heal" : 70,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Flèche solaire" : {
		"power" : 10,
		"cost" : 500,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : True
	},



	# Attacks for "Hermès"'s children
	"Guérison mineure" : {
		"power" : 0,
		"cost" : 20,
		"heal" : 10,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Trop de courrier" : {
		"power" : 4,
		"cost" : 50,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Demi-guérison" : {
		"power" : 0,
		"cost" : 100,
		"heal" : 50,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Attaque en traitre" : {
		"power" : 8,
		"cost" : 200,
		"heal" : 0,
		"effect" : "Impossible à esquiver",
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Guérison divine" : {
		"power" : 0,
		"cost" : 500,
		"heal" : 100,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},



	# Now, attacks for enemies !
	"Bourrasque" : {					# Harpie
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Serres acérées" : {				# Harpie
		"power" : 2,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Écrasement" : {					# Cyclope
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Chaudron" : {						# Cyclope
		"power" : 3,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Plaquage" : {						# Minotaure
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Coup de corne" : {					# Minotaure
		"power" : 5,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Coup de griffes" : {				# Cerbère, Griffon, Sphinx
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Morsure" : {						# Cerbère
		"power" : 3,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Enserrement de queue de serpent" : {				# Lamia
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Morsure venimeuse" : {				# Lamia
		"power" : 4,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Serre d'aigle" : {					# Griffon
		"power" : 2,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Chant ensorcelant" : {				# Sirènes
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Noyade" : {						# Sirènes
		"power" : 5,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Enigme mortelle" : {				# Sphinx
		"power" : 5,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Peau d'acier" : {					# Lion de Némée
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Griffes d'acier" : {				# Lion de Némée
		"power" : 2,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Morsure de serpent" : {			# Méduse
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Pétrification" : {					# Méduse
		"power" : 5,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Coup de bouquin" : {				# Déesse Athéna
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Plan infaillible" : {
		"power" : 8,
		"cost" : 200,
		"heal" : 0,
		"effect" : "Impossible à esquiver",
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Beauté fatale" : {					# Déesse Aphrodite
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Tromperie" : {						# Déesse Aphrodite
		"power" : 2,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Tir critique" : {					# Déesse Artémis
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Flèche de Lune" : {				# Déesse Artémis
		"power" : 3,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Cacophonie" : {					# Dieu Apollon
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Eclipse solaire" : {				# Dieu Apollon
		"power" : 4,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Coup d'estoc" : {					# Dieu Arès
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Berserk" : {						# Dieu Arès
		"power" : 12,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : True,
		"bow bonus" : False
	},
	"Enserrement de vigne" : {			# Dieu Dionysos
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Supplice du tonneau" : {			# Dieu Dionysos
		"power" : 2,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Allergies" : {						# Déesse Perséphone
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Floraison infernale" : {			# Déesse Perséphone
		"power" : 4,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Hantise" : {						# Dieu Hades
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Faux spectrale" : {				# Dieu Hades
		"power" : 3,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Coup de Trident" : {				# Dieu Poséidon
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Tsunami" : {						# Dieu Poséidon
		"power" : 4,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"30 millions de volts" : {			# Dieu Zeus
		"power" : 1,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
	"Barrage orageux" : {				# Dieu Zeus
		"power" : 4,
		"cost" : 0,
		"heal" : 0,
		"effect" : None,
		"sword bonus" : False,
		"bow bonus" : False
	},
}





