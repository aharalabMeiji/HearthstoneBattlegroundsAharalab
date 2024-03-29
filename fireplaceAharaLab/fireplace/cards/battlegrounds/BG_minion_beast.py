from ..utils import *

BG_Alleycat=(Config.BG_VERSION<2620)#1/1/1 ## banned 26.2
BG_Scavenging_Hyena=True#1/2/2
BG26__Manasaber=(Config.BG_VERSION>=2620)#(1)

BG_Silverback_Patriarch=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2420)#new 23.6 banned 24.2 
BG_Leapfrogger=True#2/3/3
BG_Rabid_Saurolisk=(Config.BG_VERSION<2620) #2/3/2 ## banned 26.2
BG_Sewer_Rat=True#2/3/2
BG26__Humming_Bird=(Config.BG_VERSION>=2620)#(2)

BG_Monstrous_Macaw=(Config.BG_VERSION>=2622)#3/5/3
BG_Rat_Pack=True#3/2/2
BG26__Rylak_Metalhead=(Config.BG_VERSION>=2620)#(3)
BG26__Banana_Slamma=(Config.BG_VERSION>=2620)#(3)

BG_Cave_Hydra=(Config.BG_VERSION<2620)#4/2/4 ## banned 26.2
BG_Reanimating_Rattler=True#4/5/3
BG_Savannah_Highmane=(Config.BG_VERSION<2560) #4/6/5 banned 25.6
BG_Sly_Raptor=True#4/1/3

BG_Agamaggan_the_Great_Boar=(Config.BG_VERSION<2620)#5/6/6 ## banned 26.2
BG_Baby_Krush=(Config.BG_VERSION>=2320 and Config.BG_VERSION<2520)# 5  #new 23.2 banned 25.2
BG_Bonemare=(Config.BG_VERSION>=2560)#5/5/5 #new 25.6
BG_Mama_Bear=True#5/5/5
BG_Palescale_Crocolisk=(Config.BG_VERSION<2560 or Config.BG_VERSION>=2620)#5 banned 25.6 revive 26.2
#BG_Sinrunner_Blanchy=(Config.BG_VERSION>=2522) # 5/3/3 new 25.2.2 ## undead/beast

#BG25__Felstomper=(Config.BG_VERSION>=2522) ## 6/3/7 -> demon/beast
BG_Ghastcoiler=True#6/7/7
BG_Goldrinn_the_Great_Wolf=(Config.BG_VERSION<2620)#6/4/4 # banned 2620
BG_Maexxna=(Config.BG_VERSION<2320)## banned 23.2
BG26__Octosari_Wrap_God=(Config.BG_VERSION>=2620)## (6/6/7)


BG_Minion_Beast = []
BG_PoolSet_Beast = []
BG_Beast_Gold={}

BG_Beast_Gold['TB_BaconShop_HP_105t']='TB_BaconUps_307'
""" Fish of N'Zoth """

##Alleycat <beast> (1/1) ###  OK ###
if BG_Alleycat:
	BG_Minion_Beast += ['BG_CFM_315','BG_CFM_315t','TB_BaconUps_093','TB_BaconUps_093t',]#Alleycat
	BG_PoolSet_Beast.append('BG_CFM_315')
	BG_Beast_Gold['BG_CFM_315']='TB_BaconUps_093'
class BG_CFM_315:# <3>[25]   
	""" Alleycat <beast> (1/1)
	[Battlecry:] Summon a 1/1_Cat."""
	play = Summon(CONTROLLER, 'BG_CFM_315t')
	pass
class BG_CFM_315t:# <3>[25]
	""" Tabbycat <beast>, 	"""
	pass
class TB_BaconUps_093:#
	""" Alleycat <beast> (2/2)
	[Battlecry:] Summon a 2/2_Cat."""
	play = Summon(CONTROLLER, 'TB_BaconUps_093t')
	pass
class TB_BaconUps_093t:#
	""" Tabbycat <beast> (2/2),	"""



### Scavenging Hyena (1/2/2)  ### OK ### 
if BG_Scavenging_Hyena:
	BG_Minion_Beast += ['BG_EX1_531','EX1_531e','TB_BaconUps_043','TB_BaconUps_043e',]#Scavenging Hyena
	BG_PoolSet_Beast.append('BG_EX1_531')
	BG_Beast_Gold['BG_EX1_531']='TB_BaconUps_043'
class BG_EX1_531: #<3>[1637] 
	"""Scavenging Hyena (1/2/2)
	Whenever a friendly Beast dies, gain +2/+1."""
	events = Death(FRIENDLY + BEAST).on(Buff(SELF, "EX1_531e"))
	pass
EX1_531e=buff(2,1)
class TB_BaconUps_043: #<3>[1637]
	"""Scavenging Hyena (1/2/2)
	Whenever a friendly Beast dies, gain +4/+2."""
	events = Death(FRIENDLY + BEAST).on(Buff(SELF, "TB_BaconUps_043e"))
	pass
TB_BaconUps_043e=buff(4,2)


## Silverback Patriarch (1) new 23.6 banned 24.2 
if BG_Silverback_Patriarch:
	BG_Minion_Beast += ['BG_CS2_127','BG_CS2_127_G',]# Silverback Patriarch (1)
	BG_PoolSet_Beast.append('BG_CS2_127')
	BG_Beast_Gold['BG_CS2_127']='BG_CS2_127_G'
class BG_CS2_127:
	""" Silverback Patriarch
	[Taunt] """
class BG_CS2_127_G:
	""" Silverback Patriarch
	[Taunt] """
	pass

## Manasaber (Beast) (1)
#BG26__Manasaber=(Config.BG_VERSION>=2620)
if BG26__Manasaber:# 
	BG_Minion_Beast+=['BG26_800']
	BG_Minion_Beast+=['BG26_800_G']
	BG_Minion_Beast+=['BG26_800_Gt']
	BG_Minion_Beast+=['BG26_800t']
	BG_PoolSet_Beast.append('BG26_800')
	BG_Beast_Gold['BG26_800']='BG26_800_G'
class BG26_800:# (minion)
	""" Manasaber
	[Deathrattle:] Summon two 0/1 Cublings with [Taunt]. """
	deathrattle = DeathrattleSummon(CONTROLLER, 'BG26_800t') * 2
	pass

class BG26_800_G:# (minion)
	""" Manasaber
	[Deathrattle:] Summon two 0/2 Cublings with [Taunt]. """
	deathrattle = DeathrattleSummon(CONTROLLER, 'BG26_800_Gt') * 2
	pass

class BG26_800t:# (minion)
	""" Cubling
	[Taunt] """
	#
	pass
class BG26_800_Gt:# (minion)
	""" Cubling
	[Taunt] """
	#
	pass



#### TIER 2 ####

#Leapfrogger(2/3/3)  ###  need check ###
if BG_Leapfrogger:
	BG_Minion_Beast += ['BG21_000','BG21_000e','BG21_000_G','BG21_000_Ge',]#Leapfrogger(2)
	BG_PoolSet_Beast.append('BG21_000')
	BG_Beast_Gold['BG21_000']='BG21_000_G'
class BG21_000:# <12>[1453]  
	""" Leapfrogger(2/3/3)
	[Deathrattle:] Give a friendly Beast +1/+1 and this [Deathrattle]. """
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000e')
	pass
class BG21_000e:
	tags = {GameTag.DEATHRATTLE:True, GameTag.ATK:1, GameTag.HEALTH:1, }
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000e')
class BG21_000_G:# <12>[1453]
	""" Leapfrogger
	[Deathrattle:] Give a friendly Beast +2/+2 and this [Deathrattle]. """
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000_Ge')
	pass
class BG21_000_Ge:
	tags = {GameTag.DEATHRATTLE:True, GameTag.ATK:2, GameTag.HEALTH:2, }	
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000_Ge')



#Rabid Saurolisk (2/3/2)  ### maybe ### banned 26.2
if BG_Rabid_Saurolisk:
	BG_Minion_Beast += ['BGS_075','BGS_075e','TB_BaconUps_125','TB_BaconUps_125e',]#Rabid Saurolisk(2)
	BG_PoolSet_Beast.append('BGS_075')
	BG_Beast_Gold['BGS_075']='TB_BaconUps_125'
class BGS_075:# <3>[1453]  
	""" Rabid Saurolisk (2/3/2)
	After you play a minion with [Deathrattle], gain +1/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEATHRATTLE).after(Buff(SELF, 'BGS_075e'))
	pass
BGS_075e=buff(1,2)
class TB_BaconUps_125:# <3>[1453]
	""" Rabid Saurolisk
	After you play a minion with [Deathrattle], gain +2/+4. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEATHRATTLE).after(Buff(SELF, 'TB_BaconUps_125e'))
	pass
TB_BaconUps_125e=buff(2,4)



#Sewer Rat (2/3/2)  ### maybe ###
if BG_Sewer_Rat:
	BG_Minion_Beast += ['BG19_010','BG19_010t','BG19_010_G','BG19_010_Gt',]#Sewer Rat(2)
	BG_PoolSet_Beast.append('BG19_010')
	BG_Beast_Gold['BG19_010']='BG19_010_G'
class BG19_010:# <12>[1453]  
	""" Sewer Rat (2/3/2)
	[Deathrattle:] Summon a 2/3 Turtle with [Taunt]. """
	## <ReferencedTag enumID="217" name="DEATHRATTLE" type="Int" value="1"/>
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = DeathrattleSummon(CONTROLLER, 'BG19_010t')
	pass
class BG19_010t:# <12>[1453]
	""" Half-Shell
	[Taunt] """
	pass
class BG19_010_G:# <12>[1453]
	""" Sewer Rat
	[Deathrattle:] Summon a 4/6 Turtle with [Taunt]. """
	## <ReferencedTag enumID="217" name="DEATHRATTLE" type="Int" value="1"/>
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = DeathrattleSummon(CONTROLLER, 'BG19_010_Gt')
	pass
class BG19_010_Gt:# <12>[1453]
	""" Half-Shell
	[Taunt] """
	pass



## Humming Bird (Beast) (2)
#BG26__Humming_Bird=(Config.BG_VERSION>=2620)(2)
if BG26__Humming_Bird:# 
	BG_Minion_Beast+=['BG26_805','BG26_805e']
	BG_Minion_Beast+=['BG26_805_G','BG26_805_Ge']
	BG_PoolSet_Beast.append('BG26_805')
	BG_Beast_Gold['BG26_805']='BG26_805_G'
class BG26_805_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_805:# (minion)
	""" Humming Bird
	Your other Beasts have +2 Attack. """
	update = Refresh(FRIENDLY_MINIONS + BEAST, buff='BG26_805e')
	pass
BG26_805e=buff(2,0)
class BG26_805_G:# (minion)
	""" Humming Bird
	Your other Beasts have +4 Attack. """
	update = Refresh(FRIENDLY_MINIONS + BEAST, buff='BG26_805_Ge')
	pass
BG26_805_Ge=buff(2,0)



#### TIER 3 ####

# Monstrous Macaw (3/5/3)  #### need check ###
if BG_Monstrous_Macaw:
	BG_Minion_Beast += ['BGS_078','TB_BaconUps_135',]#Monstrous Macaw(3)
	BG_PoolSet_Beast.append('BGS_078')
	BG_Beast_Gold['BGS_078']='TB_BaconUps_135'
class BGS_078_Action(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		deathrattles = []
		for card in target.controller.field:
			if isinstance(card.deathrattles, list):
				for buffs in card.deathrattles:
					if isinstance(buffs, tuple):
						for buff in buffs:
							deathrattles.append(buff)
					else:
						deathrattles.append(buff)
		if len(deathrattles)>0:
			for repeat in range(amount):
				actionbuff = random.choice(deathrattles)
				actionbuff.trigger(source)
		pass
class BGS_078:# <12>[1453]  オウム
	""" Monstrous Macaw (3/5/3)
	After this attacks, trigger another friendly minion's [Deathrattle]. """
	events = BG_Attack(SELF).after(BGS_078_Action(SELF, 1))
	pass
class TB_BaconUps_135:
	""" Monstrous Macaw (3/10/6)
	[x]After this attacks, trigger another friendly minion's [Deathrattle] twice. """
	events = BG_Attack(SELF).after(BGS_078_Action(SELF, 2))
	pass


#Rat Pack (3/2/2)   ### maybe ###
if BG_Rat_Pack:
	BG_Minion_Beast += ['BG_CFM_316','CFM_316t','TB_BaconUps_027','TB_BaconUps_027t',]#Rat Pack(3)
	BG_PoolSet_Beast.append('BG_CFM_316')
	BG_Beast_Gold['BG_CFM_316']='TB_BaconUps_027'
class CFM_316:
	""" Rat Pack (3/2/2)
	[Deathrattle:] Summon a number of 1/1 Rats equal _to this minion's Attack."""
	deathrattle = DeathrattleSummon(CONTROLLER, 'CFM_316t') * ATK(SELF)#
	pass
class CFM_316t:
	""" Rat """
	pass
class TB_BaconUps_027:
	""" Rat Pack (3/4/4)
	[Deathrattle:] Summon a number of 2/2 Rats equal _to this minion's Attack."""
	deathrattle = DeathrattleSummon(CONTROLLER, 'TB_BaconUps_027t') * ATK(SELF)#
	pass
class TB_BaconUps_027t:
	""" Rat """
	pass

## Rylak Metalhead (Beast) (3)
#BG26__Rylak_Metalhead=(Config.BG_VERSION>=2620)
if BG26__Rylak_Metalhead:# 
	BG_Minion_Beast+=['BG26_801']
	BG_Minion_Beast+=['BG26_801_G']
	BG_PoolSet_Beast.append('BG26_801')
	BG_Beast_Gold['BG26_801']='BG26_801_G'
class BG26_801_Action(GameAction):# 
	def do(self, source):# 
		controller = source.controller
		if source in controller.field:
			index = controller.field.index(source)
			if index>0:
				adjacent=controller.field[index-1]
				PlayBattlecry(adjacent).trigger(source)
			if index<len(controller.field)-1:
				adjacent=controller.field[index+1]
				PlayBattlecry(adjacent).trigger(source)
		pass# 
class BG26_801:# (minion)
	""" Rylak Metalhead
	[Taunt] [Deathrattle:] Trigger the [Battlecries] of adjacent minions. """
	deathrattle = BG26_801_Action()
	pass
class BG26_801_G_Action(GameAction):# 
	def do(self, source):# 
		controller = source.controller
		if source in controller.field:
			index = controller.field.index(source)
			if index>0:
				adjacent=controller.field[index-1]
				PlayBattlecry(adjacent).trigger(source)
				PlayBattlecry(adjacent).trigger(source)
			if index<len(controller.field)-1:
				adjacent=controller.field[index+1]
				PlayBattlecry(adjacent).trigger(source)
				PlayBattlecry(adjacent).trigger(source)
		pass# 
class BG26_801_G:# (minion)
	""" Rylak Metalhead
	[Taunt] [Deathrattle:] Trigger the [Battlecries] of adjacent minions twice. """
	deathrattle = BG26_801_G_Action()
	pass

## Banana Slamma (Beast) (3)->(4)
#BG26__Banana_Slamma=(Config.BG_VERSION>=2620)
if BG26__Banana_Slamma:# 
	BG_Minion_Beast+=['BG26_802','BG26_802e']
	BG_Minion_Beast+=['BG26_802_G','BG26_802_Ge']
	BG_PoolSet_Beast.append('BG26_802')
	BG_Beast_Gold['BG26_802']='BG26_802_G'
class BG26_802_Action(TargetedAction):# 
	TARGET=ActionArg()
	def do(self, source, target):# 
		target=get00(target)
		if getattr(target, 'this_is_minion', False):
			atk=target.atk
			hlt=target.max_health
			Buff(target, 'BG26_802e', atk=atk, max_health=hlt).trigger(source)
		pass# 
class BG26_802:# (minion)
	""" Banana Slamma
	After you summon a Beast in combat, double its stats. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.TECH_LEVEL:4}
	elif Config.BG_VERSION>=2620:
		option_tags={GameTag.TECH_LEVEL:3}
	events = Summon(CONTROLLER).after(BG26_802_Action(Summon.CARD))
	pass
class BG26_802e:
	pass
class BG26_802_G_Action(TargetedAction):# 
	TARGET=ActionArg()
	def do(self, source, target):# 
		target=get00(target)
		atk=target.atk
		hlt=target.max_health
		Buff(target, 'BG26_802_Ge', atk=atk, max_health=hlt).trigger(source)
		pass# 
class BG26_802_G:# (minion)
	""" Banana Slamma
	After you summon a Beast in combat, triple its stats. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.TECH_LEVEL:4}
	elif Config.BG_VERSION>=2620:
		option_tags={GameTag.TECH_LEVEL:3}
	events = Summon(CONTROLLER).after(BG26_802_G_Action(Summon.CARD))
	pass
class BG26_802_Ge:
	pass


#### TIER 4 ####

##Cave Hydra (4/2/4) ### maybe ###
if BG_Cave_Hydra:
	BG_Minion_Beast += ['BG_LOOT_078','TB_BaconUps_151',]#Cave Hydra(4)
	BG_PoolSet_Beast.append('BG_LOOT_078')
	BG_Beast_Gold['BG_LOOT_078']='TB_BaconUps_151'
class LOOT_078:
	""" Cave Hydra (4/2/4)
	Also damages the minions next to whomever this attacks."""
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, ATK(SELF)))
	pass
class TB_BaconUps_151:
	""" Cave Hydra (4/4/8)
	Also damages the minions next to whomever this attacks."""
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, ATK(SELF)))
	pass



#Reanimating Rattler (4/5/3)  ### maybe ### 
if BG_Reanimating_Rattler:
	BG_Minion_Beast += ['BG21_003','BG21_003e','BG21_003_G',]#Reanimating Rattler(4)
	BG_PoolSet_Beast.append('BG21_003')
	BG_Beast_Gold['BG21_003']='BG21_003_G'
class BG21_003_Action2622(GameAction):
	def do(self, source):
		cards = [card for card in source.controller.field if isRaceCard(card, Race.BEAST)==True and card.reborn==False]
		if len(cards)>0:
			card = random.choice(cards)
			Buff(card, 'BG21_003e').trigger(source)
class BG21_003:# <12>[1453]
	""" Reanimating Rattler (4/5/3)
	At the end of your turn, give another friendly Beast Reborn.""" ## new 26.2.2	
	##[Battlecry:] Give a friendly Beast [Reborn]. 
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:3}
		events = OWN_TURN_END.on(BG21_003_Action2622())
		pass
	else:
		option_tags={GameTag.ATK:5, GameTag.HEALTH:3}
		requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST }
		play = Buff(TARGET,'BG21_003e')
	pass
BG21_003e=buff(reborn=True)
class BG21_003_G_Action2622(GameAction):
	def do(self, source):
		cards = [card for card in source.controller.field if isRaceCard(card, Race.BEAST)==True and card.reborn==False]
		if len(cards)>2:
			cards = random.sample(cards,2)
		for card in cards:
			Buff(card, 'BG21_003e').trigger(source)
class BG21_003_G:# <12>[1453]
	""" Reanimating Rattler (4/10/6)-> (4/8/6)
	At the end of your turn, give 2 other friendly Beasts [Reborn].""" ## new 26.2.2
	##[Battlecry:] Give a friendly Beast [Reborn]. 
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:8, GameTag.HEALTH:6}
		events = OWN_TURN_END.on(BG21_003_G_Action2622())
		pass
	else:
		option_tags={GameTag.ATK:10, GameTag.HEALTH:6}
		requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST }
		play = Buff(TARGET,'BG21_003e')
	pass




#Savannah Highmane (4/6/5) ### maybe ###
if BG_Savannah_Highmane:
	BG_Minion_Beast += ['BG_EX1_534','EX1_534t','TB_BaconUps_049','TB_BaconUps_049t',]#Savannah Highmane(4)
	BG_PoolSet_Beast.append('BG_EX1_534')
	BG_Beast_Gold['BG_EX1_534']='TB_BaconUps_049'
class BG_EX1_534: ## ハイメイン
	""" Savannah Highmane (4/6/5)
	[Deathrattle:] Summon two 2/2 Hyenas."""
	deathrattle = DeathrattleSummon(CONTROLLER, 'EX1_534t')
	pass
class BG_EX1_534t:
	""" Hyenta	"""
	pass
class TB_BaconUps_049:
	""" Savannah Highmane (4/12/10)
	[Deathrattle:] Summon two 4/4 Hyenas."""
	deathrattle = DeathrattleSummon(CONTROLLER, 'TB_BaconUps_049t')
	pass
class TB_BaconUps_049t:
	""" Hyenta	"""
	pass


# Sly Raptor #4/1/3 ## new 25.6
if BG_Sly_Raptor:#4/1/3
	BG_Minion_Beast += ['BG25_806','BG25_806_G',]#
	BG_PoolSet_Beast.append('BG25_806')
	BG_Beast_Gold['BG25_806']='BG25_806_G'
class BG25_806_Action(GameAction):
	def do(self, source):
		newcard = Summon(source.controller, RandomBGBeast()).trigger(source)
		newcard = get00(newcard)
		newcard.atk=7
		newcard.max_health=7
class BG25_806:
	""" Sly Raptor
	Deathrattle: Summon another random Beast. Set its stats to 7/7."""
	option_tags={GameTag.TECH_LEVEL:4}
	deathrattle = BG25_806_Action()
class BG25_806_Action(GameAction):
	def do(self, source):
		newcard = Summon(source.controller, RandomBGBeast()).trigger(source)
		newcard = get00(newcard)
		newcard.atk=14
		newcard.max_health=14
class BG25_806_G:
	""" Sly Raptor
	Deathrattle: Summon another random Beast. Set its stats to 14/14."""
	option_tags={GameTag.TECH_LEVEL:4}
	deathrattle = BG25_806_Action()



###### tier 5 ######

#Agamaggan, the Great Boar (5/6/6)   ### maybe ### banned 26.2
if BG_Agamaggan_the_Great_Boar:
	BG_Minion_Beast += ['BG20_205','BG20_205_G',]#Agamaggan, the Great Boar(5)
	BG_PoolSet_Beast.append('BG20_205')
	BG_Beast_Gold['BG20_205']='BG20_205_G'
class BG20_205:# <12>[1453] #
	""" Agamaggan, the Great Boar (5/6/6)
	Your [Blood Gems] give an extra +1/+1. """
	events = ApplyGem(SELF).on(Buff(SELF, 'BG20_GEMe'))
	pass
class BG20_205_G:# <12>[1453] #
	""" Agamaggan, the Great Boar (5/12/12)
	Your [Blood Gems] give an extra +2/+2. """
	events = ApplyGem(SELF).on(Buff(SELF, 'BG20_GEMe'), Buff(SELF, 'BG20_GEMe'))
	#
	pass



# Baby Krush (5/7/7)->(5/6/6) ### OK ### banned 25.2
if BG_Baby_Krush:
	BG_Minion_Beast += ['BG22_001','BG22_001t2','BG22_001_G','BG22_001t2_G',]#Baby Krush(5)
	BG_PoolSet_Beast.append('BG22_001')
	BG_Beast_Gold['BG22_001']='BG22_001_G'
class BG22_001_Action(TargetedAction):
	TARGET = ActionArg()# Attack.DEFENDER
	OTHER = ActionArg()# 'BG22_001t2'
	def do(self, source, target, other):
		controller = source.controller
		if len(controller.field)<7 and source in controller.field:
			index = controller.field.index(source)
			newcard = Summon(controller, other).trigger(controller)
			if newcard[0]==[]:
				return
			newcard = newcard[0][0]
			BG_Attack(newcard, target).trigger(controller)
class BG22_001:# <12>[1453]
	""" Baby Krush (5/7/7)->(5/6/6)
	Whenever this attacks,summon a 8/8 Devilsaur toattack the target first. """
	events = BG_Attack(SELF, ENEMY).on(BG22_001_Action(BG_Attack.OTHER, 'BG22_001t2'))
	pass
class BG22_001t2:
	pass
class BG22_001_G:# <12>[1453]
	""" Baby Krush (5/14/14)
	Whenever this attacks, summon an 16/16 Devilsaur to attack the target first. """
	events = BG_Attack(SELF, ENEMY).on(BG22_001_Action(BG_Attack.OTHER, 'BG22_001t2_G'))
	pass
class BG22_001t2_G:
	pass




# Bonemare (5/5/5) ### new 25.6 #99164
if BG_Bonemare:
	BG_Minion_Beast += ['BG26_ICC_705','BG26_ICC_705e', 'BG26_ICC_705_G','BG26_ICC_705_Ge',]#
	BG_PoolSet_Beast.append('BG26_ICC_705')
	BG_Beast_Gold['BG26_ICC_705']='BG26_ICC_705_G'
class BG26_ICC_705:
	"""
	Battlecry: Give a friendly minion +4/+4 and Taunt. """
	requirements = REQUIRE_FRIEND_MINION_TARGET
	play = Buff(TARGET, 'BG26_ICC_705e') 
BG26_ICC_705e=buff(4,4,taunt=True)
class BG26_ICC_705_G:
	"""
	Battlecry: Give a friendly minion +8/+8 and Taunt."""
	requirements = REQUIRE_FRIEND_MINION_TARGET
	play = Buff(TARGET, 'BG26_ICC_705_Ge') 
BG26_ICC_705_Ge=buff(8,8,taunt=True)



#Mama Bear (5/5/5) ### maybe ###
if BG_Mama_Bear:
	BG_Minion_Beast += ['BGS_021','BGS_021e','TB_BaconUps_090','TB_BaconUps_090e',]#Mama Bear(5)
	BG_PoolSet_Beast.append('BGS_021')
	BG_Beast_Gold['BGS_021']='TB_BaconUps_090'
class BGS_021:# <12>[1453]
	""" Mama Bear (5/5/5)
	Whenever you summon a Beast, give it +4/+4.""" ##new 26.2.2
	##Whenever you summon a Beast, give it +5/+5. 
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:4}
	else:
		option_tags={GameTag.ATK:5, GameTag.HEALTH:5}
	events = Summon(CONTROLLER, BEAST).on(Buff(Summon.CARD, 'BGS_021e'))
	pass
if Config.BG_VERSION>=2622:
	BGS_021e=buff(4,4)
else:
	BGS_021e=buff(5,5)
class TB_BaconUps_090:# <12>[1453]
	""" Mama Bear (5/10/10)
	Whenever you summon a Beast, give it +10/+10. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:8, GameTag.HEALTH:8}
	else:
		option_tags={GameTag.ATK:10, GameTag.HEALTH:10}
	events = Summon(CONTROLLER, BEAST).on(Buff(Summon.CARD, 'TB_BaconUps_090e'))
	pass
if Config.BG_VERSION>=2622:
	TB_BaconUps_090e=buff(8,8)
else:
	TB_BaconUps_090e=buff(10,10)



#Palescale Crocolisk(5/4/5) ### maybe OK ### banned 25.6 revive 26.2
if BG_Palescale_Crocolisk:
	BG_Minion_Beast += ['BG21_001','BG21_001e','BG21_001_G','BG21_001e2',]#Palescale Crocolisk(5)
	BG_PoolSet_Beast.append('BG21_001')
	BG_Beast_Gold['BG21_001']='BG21_001_G'
class BG21_001:# <12>[1453] クロコリスク
	""" Palescale Crocolisk(5/4/5)
	[Avenge (2) and Deathrattle:] Give another friendly Beast +6/+6. """
	#<Tag enumID="2129" name="AVENGE" type="Int" value="1"/>
	#<Tag enumID="451" name="SCORE_VALUE_1" type="Int" value="2"/>
	events = Death(FRIENDLY).on(Avenge(SELF, 2, [Buff(RANDOM(FRIENDLY_MINIONS + BEAST - SELF), 'BG21_001e')]))
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST - SELF), 'BG21_001e')
	pass
BG21_001e=buff(6,6)
class BG21_001_G:# <12>[1453]
	""" Palescale Crocolisk(5/8/10)
	[Avenge (2) and Deathrattle:] Give another friendly Beast +12/+12. """
	events = Death(FRIENDLY).on(Avenge(SELF, 2, [Buff(RANDOM(FRIENDLY_MINIONS + BEAST - SELF), 'BG21_001e2')]))
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST - SELF), 'BG21_001e2')
	pass
BG21_001e2=buff(12,12)


#Sinrunner Blanchy 5/3/3  Beast/Undead	Reborn ## new 25.2.2
from .BG_minion_undead import BG24__Sinrunner_Blanchy
if BG24__Sinrunner_Blanchy:
	##BG_Minion_Beast += ['BG24_005','BG24_005_G']## no need
	BG_PoolSet_Beast+=['BG24_005']
	BG_Beast_Gold['BG24_005']='BG24_005_G'


########### tavern tier 6


from .BG_minion_demon import BG25__Felstomper
#Felstomper
if BG25__Felstomper:# 6/3/7 demon/beast ## new 25.2.2 ### need check##############
	##BG_Minion_Beast+=['BG25_042','BG25_042_G','BG25_042_Ge','BG25_042e']
	BG_PoolSet_Beast.append('BG25_042')
	BG_Beast_Gold['BG25_042']='BG25_042_G'




#Ghastcoiler (6/7/7) ### maybe OK ###
if BG_Ghastcoiler:
	BG_Minion_Beast += ['BGS_008','TB_BaconUps_057',]#Ghastcoiler(6)
	BG_PoolSet_Beast.append('BGS_008')
	BG_Beast_Gold['BGS_008']='TB_BaconUps_057'
class BGS_008:# <6>[1453]
	""" Ghastcoiler (6/7/7)
	[Deathrattle:] Summon 2 random [Deathrattle] minions. """
	deathrattle = DeathrattleSummon(CONTROLLER, RandomCollectible(deathrattle=True)) * 2
	pass
class TB_BaconUps_057:# <6>[1453]
	""" Ghastcoiler (6/14/14)
	[Deathrattle:] Summon 4 random [Deathrattle] minions. """
	deathrattle = DeathrattleSummon(CONTROLLER, RandomCollectible(deathrattle=True)) * 4
	pass



# Goldrinn, the Great Wolf (6/4/4)  ### maybe OK ###
if BG_Goldrinn_the_Great_Wolf:
	BG_Minion_Beast += ['BGS_018','BGS_018e','TB_BaconUps_085','TB_BaconUps_085e']#Goldrinn, the Great Wolf(6)
	BG_PoolSet_Beast.append('BGS_018')
	BG_Beast_Gold['BGS_018']='TB_BaconUps_085'
class BGS_018:# <12>[1453]
	""" Goldrinn, the Great Wolf (6/4/4)
	[Deathrattle:] Give your Beasts +5/+5. """
	deathrattle = Buff(FRIENDLY_MINIONS + BEAST, 'BGS_018e')
	pass
BGS_018e=buff(5,5)
class TB_BaconUps_085:# <12>[1453]
	""" Goldrinn, the Great Wolf (6/8/8)
	[Deathrattle:] Give your Beasts +10/+10. """
	deathrattle = Buff(FRIENDLY_MINIONS + BEAST, 'TB_BaconUps_085e')
	pass
TB_BaconUps_085e=buff(10,10)


#Maexxna (BAN)   ### I'M WAITING  ###
if BG_Maexxna:
	BG_Minion_Beast += ['FP1_010','TB_BaconUps_155',]# Maexxna (BAN)(6)
	BG_PoolSet_Beast.append('FP1_010')
	BG_Beast_Gold['FP1_010']='TB_BaconUps_155'
class FP1_010:
	""" Maexxna (BAN)
	[Poisonous] """
	pass
class TB_BaconUps_155:
	""" Maexxna (BAN)
	[Poisonous] """
	pass

from .BG_minion_demon import BG25__Felstomper
if BG25__Felstomper:# 6/3/7 demon/beast ## new 25.2.2 ##
	##BG_Minion_Beast+=['BG25_042','BG25_042_G','BG25_042_Ge','BG25_042e'] ## no need
	BG_PoolSet_Beast.append('BG25_042')
	BG_Beast_Gold['BG25_042']='BG25_042_G'

## Octosari, Wrap God (Beast) (6)
#BG26__Octosari_Wrap_God=(Config.BG_VERSION>=2620)
if BG26__Octosari_Wrap_God:# 
	BG_Minion_Beast+=['BG26_804']
	BG_Minion_Beast+=['BG26_804_G']
	BG_Minion_Beast+=['BG26_803t']
	BG_Minion_Beast+=['BG26_803_Gt']
	BG_PoolSet_Beast.append('BG26_804')
	BG_Beast_Gold['BG26_804']='BG26_804_G'
class BG26_804_Action(GameAction):# 
	CARDID=ActionArg()
	def do(self, source, cardid):# 
		newcard=Summon(source.controller, cardid).trigger(source)
		newcard=get00(newcard)
		newcard.atk=source.script_data_num_1
		newcard.max_health=source.script_data_num_1
		pass# 
class BG26_804_Action2(TargetedAction):# 
	CARD=CardArg()
	def do(self, source, card):# 
		if hasattr(source.controller.game,'this_is_battle') and source.controller.game.this_is_battle:
			source.script_data_num_1 += 2
class BG26_804:# (minion)
	""" Octosari, Wrap God
	[Deathrattle:] Summon a @/@ Tentacle. <i>(It gains +2/+2  permanently after you summon a minion in combat!)</i> """
	##<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="2"/>
	deathrattle = BG26_804_Action('BG26_803t')
	events = Summon(CONTROLLER).after(BG26_804_Action2(Summon.CARD))
	pass
class BG26_803t:# (minion)
	""" Tentacle of Octosari
	"""
	#
class BG26_804_G_Action2(TargetedAction):# 
	CARDID=ActionArg()
	def do(self, source, cardid):# 
		if hasattr(source.controller.game,'this_is_battle') and source.controller.game.this_is_battle:
			source.script_data_num_1 += 4
class BG26_804_G:# (minion)
	""" Octosari, Wrap God
	[Deathrattle:] Summon a @/@ Tentacle. <i>(It gains +4/+4  permanently after you summon a minion in combat!)</i> """
	deathrattle = BG26_804_Action('BG26_803t')
	##<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="4"/>
	events = Summon(CONTROLLER).after(BG26_804_G_Action2(Summon.CARD))
	pass
class BG26_803_Gt:# (minion)
	""" Tentacle of Octosari
	"""
	#
