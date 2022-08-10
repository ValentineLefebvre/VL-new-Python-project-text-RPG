from is_it_in_the_list import *
from Attacks import *


Enemies_list = ["Harpie", "Cyclope", "Minotaure", "Cerbere", "Lamia", "Griffon", "Sirenes", "Sphinx", "Lion_de_Nemee", "Meduse", "Déesse Athéna", "Déesse Aphrodite", "Déesse Artémis", "Dieu Apollon", "Dieu Arès", "Dieu Dionysos", "Déesse Perséphone", "Dieu Hades", "Dieu Poséidon", "Dieu Zeus"]

class Enemy :
	def __init__(self, name):
		self.name = name
		if name == "Harpie" :
			self.level = 1
			self.max_hp = 100
			self.hp = self.max_hp
			self.atk = 60
			self.defense = 40
			self.xp_won = 50
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.4
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nEn quelques battements d'ailes, elle est devant vous. Les serres de la harpie raclent la pierre alors qu'elle se pose sur le rocher près de vous. Elle ne replie ses ailes qu'à demi et vous fixe de son regard perçant, prête à l'attaque.\n"
			self.victory_text = "\nLa harpie explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLa harpie transperce votre chair jusqu'à vous déchiqueter et vous mettre en pièce.\n"
			self.moves = {
				1 : "Bourrasque", 
				2 : "Serres acérées"
			}
		elif name == "Cyclope" :
			self.level = 1
			self.max_hp = 100
			self.hp = self.max_hp
			self.atk = 20
			self.defense = 70
			self.xp_won = 50
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.3
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nD'un pas lourd, le cyclope s'avance en détruisant tout sur son passage, ne laissant derrière lui que le chaos et la destruction.\n"
			self.victory_text = "\nLe cyclope explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLe cyclope vous arrache la tête, vous éventre de ses dents pointues et vous dévore.\n"
			self.moves = {
				1 : "Écrasement", 
				2 : "Chaudron"
			}
		elif name == "Minotaure" :
			self.level = 1
			self.max_hp = 80
			self.hp = self.max_hp
			self.atk = 50
			self.defense = 50
			self.xp_won = 50
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.2
			# possible popping spots: forest
			self.start_text = "\nUn corps d'homme surmonté d'une hideuse tête de taureau : le minotaure apparait entre les arbres et abaisse la tête, cornes en avant, prêt à charger.\n"
			self.victory_text = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLe minotaure ne vous laisse aucune chance de survie : il vous a chargé et vous a empallé sur ses cornes.\n"
			self.moves = {
				1 : "Plaquage", 
				2 : "Coup de corne"
			}
		elif name == "Cerbere" :
			self.level = 2
			self.max_hp = 150
			self.hp = self.max_hp
			self.atk = 85
			self.defense = 65
			self.xp_won = 75
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.3
			# possible popping spots: hell (random among [[15, 3], [20, 0]]) + forest
			self.start_text = "\nUn grondement sourd se fait entendre un instant avant que vous ne distinguiez le monstre. C'est un cerbère : un chien énorme, haut comme au moins trois hommes, et pourvu de trois têtes qui vous regardent toutes en salivant.\n"
			self.victory_text = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLe cerbère se jette sur vous et vous achève d'un coup de griffes avant que ses trois têtes se disputent pour vous dévorer.\n"
			self.moves = {
				1 : "Coup de griffes", 
				2 : "Morsure"
			}
		elif name == "Lamia" :
			self.level = 2
			self.max_hp = 200
			self.hp = self.max_hp
			self.atk = 60
			self.defense = 75
			self.xp_won = 75
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.25
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nLa lamia s'approche en faisant onduler son corps de serpent. Elle a un visage magnifique mais, lorsqu'elle sourit, elle dévoile ses longs crocs venimeux.\n"
			self.victory_text = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLa créature s'approche tout doucement de vous et plante profondément ses crocs dans votre chair, son venin agit instantanément. Vous êtes paralysé mais toujours conscient. Votre agonie ne fait que commencer.\n"
			self.moves = {
				1 : "Enserrement de queue de serpent", 
				2 : "Morsure venimeuse"
			}
		elif name == "Griffon" :
			self.level = 3
			self.max_hp = 225
			self.hp = self.max_hp
			self.atk = 125
			self.defense = 100
			self.xp_won = 100
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.4
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nMi-rapace, mi-lion, le griffon vous fait face. Il se dresse sur ses pattes arrières en battant des ailes et pousse un cri strident avant de se jeter sur vous.\n"
			self.victory_text = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLe griffon vous attaque de ses serres acérées et vous tue sur le coup.\n"
			self.moves = {
				1 : "Coup de griffes", 
				2 : "Serre d'aigle"
			}
		elif name == "Sirenes" :
			self.level = 2
			self.max_hp = 125
			self.hp = self.max_hp
			self.atk = 100
			self.defense = 50
			self.xp_won = 75
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.2
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nPar quelque étrange sortilège, le chant des sirènes est parfaitement audible malgré le bruit de la tempête, et menace de vous faire perdre de vue la réalité. Vous devez à tout prix rester lucide si vous tenez à la vie.\n"
			self.victory_text = "\nLes sirènes explosent en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nUn instant d'inattention a suffit à sceller votre sort. Vous vous êtes laissé envoûter et les sirènes en ont profité pour vous déchiqueter.\n"
			self.moves = {
				1 : "Chant ensorcelant", 
				2 : "Noyade"
			}
		elif name == "Sphinx" :
			self.level = 1
			self.max_hp = 100
			self.hp = self.max_hp
			self.atk = 30
			self.defense = 50
			self.xp_won = 50
			self.critical_bonus = 1.25
			self.proba_for_2nd_attack = 0.2
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nCorps de lion, ailes d'oiseau et tête de femme, le sphinx vous fait face. Il se dresse sur ses pattes arrières en battant des ailes et pousse un hurlement de rage avant de se jeter sur vous.\n"
			self.victory_text = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nVotre destin a été décidé lorsque vous n'avez pas su répondre à l'énigme du sphinx. Vous tombez sous les coups de griffes de ses énormes pattes de lion.\n"
			self.moves = {
				1 : "Coup de griffes", 
				2 : "Enigme mortelle"
			}
		elif name == "Lion_de_Nemee" :
			self.level = 1
			self.max_hp = 100
			self.hp = self.max_hp
			self.atk = 30
			self.defense = 70
			self.xp_won = 50
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.3
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nUn lion d'or émerge d'entre les arbres : le lion de Némée. Rien ne peut transpercer sa peau et ses griffes sont plus acérées que n’importe quel glaive. Il se tapit près du sol, prêt à l'attaque.\n"
			self.victory_text = "\nLe monstre explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLe lion de Némée parvient à vous plaquer au sol et vous déchiquette.\n"
			self.moves = {
				1 : "Peau d'acier", 
				2 : "Griffes d'acier"
			}
		elif name == "Meduse" :
			self.level = 3
			self.max_hp = 200
			self.hp = self.max_hp
			self.atk = 125
			self.defense = 100
			self.xp_won = 100
			self.critical_bonus = 1.25
			self.proba_for_2nd_attack = 0.2
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nUne femme s'avance entre les arbres. Vous ne distinguez pas encore ses traits mais sa chevelure semble s'agiter malgré l'absence de vent et un étrange sifflement se fait entendre. Lorsque vous comprenez que sa chevelure est faite de serpents, vous détournez au plus vite la tête. Vous ne devez en aucun cas croiser le regard de Méduse.\n"
			self.victory_text = "\nMéduse hurle et explose en un nuage de poussière après votre dernière attaque. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nVous avez eu le malheur d'ouvrir les yeux. Vous sentez votre corps se changer en pierre. Déjà vous ne pouvez plus lever le bras qui tient votre épée. Méduse s'approche en riant. Son rire sadique vous poursuivra jusque dans la mort.\n"
			self.moves = {
				1 : "Morsure de serpent", 
				2 : "Pétrification"
			}
		elif name == "Déesse Athéna" :
			self.level = 5
			self.max_hp = 450
			self.hp = self.max_hp
			self.atk = 255
			self.defense = 200
			self.xp_won = 150
			self.critical_bonus = 1.5
			self.proba_for_2nd_attack = 0.15
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Athéna, déesse de la guerre et de la sagesse.\n"
			self.victory_text = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nVous n'avez rien vu venir. Athéna a eu raison de vous à l'instant même où vous pensiez que la victoire était assurée.\n"
			self.moves = {
				1 : "Coup de bouquin", 
				2 : "Plan infaillible"
			}
		elif name == "Déesse Aphrodite" :
			self.level = 4
			self.max_hp = 400
			self.hp = self.max_hp
			self.atk = 150
			self.defense = 150
			self.xp_won = 125
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.4
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Aphrodite, déesse de la beauté.\n"
			self.victory_text = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nAphrodite vous a eu lâchement, mais, dans votre agonie, vous réalisez amèrement que l'honneur n'est d'aucun secours dans la mort.\n"
			self.moves = {
				1 : "Beauté fatale", 
				2 : "Tromperie"
			}
		elif name == "Déesse Artémis" :
			self.level = 6
			self.max_hp = 780
			self.hp = self.max_hp
			self.atk = 400
			self.defense = 350
			self.xp_won = 175
			self.critical_bonus = 1.25
			self.proba_for_2nd_attack = 0.3
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Artémis, déesse de la Lune et de la chasse.\n"
			self.victory_text = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nLa forêt est son territoire. Vous n'aviez aucune chance. Artémis s'est fondue parmi les arbres avant de vous abattre d'une flèche.\n"
			self.moves = {
				1 : "Tir critique", 
				2 : "Flèche de Lune"
			}
		elif name == "Dieu Apollon" :
			self.level = 6
			self.max_hp = 780
			self.hp = self.max_hp
			self.atk = 300
			self.defense = 400
			self.xp_won = 175
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.25
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais un dieu : Apollon, dieu du soleil et de la musique.\n"
			self.victory_text = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nVous aviez oublié qu'Apollon était aussi dieu de la guérison. Ses blessures disparaissaient en quelques instant, tandis que les vôtres ne faisaient que se multiplier. Vous n'aviez aucune chance de sortir vivant de ce combat.\n"
			self.moves = {
				1 : "Cacophonie", 
				2 : "Eclipse solaire", 
			}
		elif name == "Dieu Arès" :
			self.level = 8
			self.max_hp = 1500
			self.hp = self.max_hp
			self.atk = 900
			self.defense = 800
			self.xp_won = 225
			self.critical_bonus = 1.25
			self.proba_for_2nd_attack = 0.1
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais un dieu : Arès, dieu de la guerre.\n"
			self.victory_text = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nPenser vaincre le dieu de la guerre au combat était pure folie. Vous aurez l'éternité pour vous en repentir.\n"
			self.moves = {
				1 : "Coup d'estoc", 
				2 : "Berserk"
			}
		elif name == "Dieu Dionysos" :
			self.level = 3
			self.max_hp = 225
			self.hp = self.max_hp
			self.atk = 113
			self.defense = 113
			self.xp_won = 100
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.4
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais un dieu : Dyonisos, dieu du vin et de la folie.\n"
			self.victory_text = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nVous ne savez plus où vous êtes. La folie de Dyonisos a dû déteindre sur vous. Oui, vous devez être fou, ou vous ne verriez pas des nageoires à la place de vos bras. Avant de perdre définitivement toute pensée rationnelle, vous réalisez que le dieu ne vous a pas tué mais changé en dauphin. Et quelque part, au fond de vous, vous le remerciez de sa clémence.\n"
			self.moves = {
				1 : "Enserrement de vigne", 
				2 : "Supplice du tonneau"
			}
		elif name == "Déesse Perséphone" :
			self.level = 3
			self.max_hp = 225
			self.hp = self.max_hp
			self.atk = 125
			self.defense = 100
			self.xp_won = 100
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.25
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nVous déglutissez difficilement. Car ce n'est pas un monstre que vous avez en face de vous, mais une déesse : Perséphone, déesse du printemps et épouse d'Hadès.\n"
			self.victory_text = "\nLa déesse pousse un hurlement de rage. Elle émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, elle a disparu sans laisser de trace. Vous poussez un soupir de soulagement et prenez un peu de repos avant de poursuivre votre route.\n"
			self.loss_text = "\nVous n'atteindrez jamais le dieu des enfers. Sa femme était trop puissante pour vous. Vous mourez transpercé de toutes parts par les tiges des fleurs qu'elle a fait pousser par magie.\n"
			self.moves = {
				1 : "Allergies", 
				2 : "Floraison infernale"
			}
		elif name == "Dieu Hades" :
			self.level = 4
			self.max_hp = 366
			self.hp = self.max_hp
			self.atk = 166
			self.defense = 166
			self.xp_won = 125
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.3
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nHadès, dieu des morts et des enfers, apparait dans toute sa terrifiante splendeur. Il porte une armure noire.\nElle ne brille pas mais semble absorber toute la lumière environnante. Il se lève et son arme apparait dans sa main : une faux immense, plus grande encore que le dieux lui-même et dont l'énergie vous glace jusque dans votre âme.\n"
			self.victory_text = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous n'osez pas vous attarder sur les lieux.\nAu fond, derrière le trône, vous trouvez la barque de Charon qui gît abandonée. Vous décidez de l'emporter avec vous. Vous savez qu'après avoir vaincu Hadès, il vous faudra affronter ses frères. Et vous n'êtes pas encore prêt à faire face au seigneur des dieux.\n"
			self.loss_text = "\nVous êtes vaincu. Vous allez mourir, et vous savez que, pour l'avoir défié, Hadès ne vous réserve pas un sort favorable en son royaume.\n"
			self.moves = {
				1 : "Hantise", 
				2 : "Faux spectrale"
			}
		elif name == "Dieu Poséidon" :
			self.level = 7
			self.max_hp = 1222
			self.hp = self.max_hp
			self.atk = 555
			self.defense = 555
			self.xp_won = 200
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.25
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nPoséidon, dieu des océans, se tient devant vous. Et vous êtes sur son territoire. Il vous faudra plus que du courage pour espérer sortir victorieux de ce combat.\n"
			self.victory_text = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu, laissant une clé au fond de votre barque.\nDe l'objet émane une énergie phénoménale, presque effrayante, qui ne laisse aucun doute sur sa nature. Il s'agit de la clé qui ouvre les portes de l'Olympe. Il est temps pour vous maintenant d'affronter le plus puissant des dieux.\n"
			self.loss_text = "\nVous êtes soulevé dans les airs et votre barque rétrécit à vue d'oeil. Comment êtes-vous arrivé là-haut ?\nCe n'est qu'alors que vous remarquez que vous êtes empallé sur une des pointes du trident de Poséidon. Il vous en arrache et vous jette dans les flots déchaînés. Vous succombez heureusement rapidement, car les requins ne tardent pas à venir se disputer votre dépouille.\n"
			self.moves = {
				1 : "Coup de Trident", 
				2 : "Tsunami"
			}
		elif name == "Dieu Zeus" :
			self.level = 9
			self.max_hp = 2777
			self.hp = self.max_hp
			self.atk = 1717
			self.defense = 1111
			self.xp_won = 250
			self.critical_bonus = 1
			self.proba_for_2nd_attack = 0.3
			# possible popping spots: mountain (random among [[2, 16], [5, 8], [7, 9], [7, 17]]) + forest
			self.start_text = "\nZeus se tient là, devant vous, son immense éclair à la main. A la pensée de ce qu'il a pu faire à votre soeur, vous manquez perdre toute contenance, mais vous vous ressaisissez à temps.\nCe n'est pas le moment de vous laisser aller. La colère donne de la force mais obscurcit le jugement. Vous devez rester maître de vous-même si vous voulez la sauver."
			self.victory_text = "\nLe dieu pousse un hurlement de rage. Il émet soudain une lumière aveuglante, qui vous contraint à fermer les yeux. Quand vous les rouvrez, il a disparu sans laisser de trace. Vous poussez un soupir de soulagement.\n"
			self.loss_text = "\nVous êtes à terre, incapable de vous relever. Vous avez échoué. Vous aller mourir sans avoir pu sauver votre soeur.\nEt vous vous maudirez éternellement pour cela. Zeus lève son éclair haut au-dessus de sa tête puis l'abat dans votre direction. Vous ne voyez que la lumière aveuglante de l'attaque, et c'est fini.\n"
			self.moves = {
				1 : "30 millions de volts", 
				2 : "Barrage orageux"
			}
	def injured(self, damage) :
		if damage  > self.defense :
			actual_damage = damage - self.defense
			if actual_damage < self.hp :
				print("Vous infligez", actual_damage, "point(s) de dégât.")
				self.hp -= actual_damage
				print(self.name, "a encore", self.hp, "PV.")
			else :
				print(self.name, "perd tous ses PV.")
				self.hp = 0
		else :
			print(self.name, "ne subit aucun dégât.")
	
	def attack_damage(self, attack_number):
		attack_name = self.moves[attack_number]
		attack_power = all_attacks[attack_name]["power"]
		if attack_power == 0 :
			damage = 0
		else :
			damage = round(self.atk * attack_power)
		return damage





