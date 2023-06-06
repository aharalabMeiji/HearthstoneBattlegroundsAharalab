from ast import If
from ..utils import *
from fireplace.battlegrounds.BG_battle import BG_Battle


Omega_Buster=True#Omega Buster(6)



BG_Micro_Mummy=(Config.BG_VERSION>=2522)#(1) <-> undead/mecha
BG_Pupbot=True#(1)

BG_Harvest_Golem=True#(2)
BG_Kaboom_Bot=(Config.BG_VERSION<2560)#(2)
BG_Metaltooth_Leaper=True#(2)
BG26__Lullabot=(Config.BG_VERSION>=2620)#(2)

BG_Deflect_o_Bot=True#(3)
BG_Replicating_Menace=True#(3)
BG_Screwjank_Clunker=False#(3)banned
BG_Iron_Sensei=(Config.BG_VERSION<2620)#(3) banned 26.2
BG26__Accord_o_Tron=(Config.BG_VERSION>=2620)#(3)

BG_Annoy_o_Module=True#(4)
BG_Mechano_Eg_g=(Config.BG_VERSION>=2504)#(4) banned  -> renew 25.0.4
BG_Mechano_Tank=(Config.BG_VERSION<2504)#(4) -> banned 25.0.4
BG_Wargear=(Config.BG_VERSION>=2360)#(4) # after 23.6
BG26__Scrap_Scraper=(Config.BG_VERSION>=2620)# (4)

BG_Holy_Mecherel=(Config.BG_VERSION<2620)#(5) banned 26.2
BG_Dr_Boombox=True#(5)
BG26__Utility_Drone=(Config.BG_VERSION>=2620)#(5/4/5)

BG_Foe_Reaper_4000=True#(6)
BG_Omega_Buster=True#(6)
BG_Grease_Bot=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2620)#(4->6) 23.6, 24.0.3 banned 26.2
BG26__Polarizing_Beatboxer=(Config.BG_VERSION>=2620) # (6/3/7)
	
BG_Minion_Mecha =[]
BG_PoolSet_Mecha = []
BG_Mecha_Gold={}

#25.2.2 -
#Micro Mummy 1/1/2/Mech, Undead	Reborn
#Micro Mummy(1) ### OK ###
if BG_Micro_Mummy:
	BG_Minion_Mecha+=['BG_ULD_217', 'ULD_217e','TB_BaconUps_250','TB_BaconUps_250e',]
	BG_PoolSet_Mecha.append('BG_ULD_217')
	BG_Mecha_Gold['BG_ULD_217']='TB_BaconUps_250'
class BG_ULD_217:
	"""
	[Reborn]At the end of your turn, giveanother random friendlyminion +1 Attack."""
	##<Tag enumID="2534" name="1" type="Int" value="1"/>(undead)
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'ULD_217e'))
	pass
ULD_217e=buff(1,0)
class TB_BaconUps_250:# <5>[1453]
	""" Micro Mummy
	[Reborn]At the end of your turn, giveanother random friendly minion +2 Attack. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'TB_BaconUps_250e'))
	pass
TB_BaconUps_250e=buff(2,0)

#Pupbot(1) ### OK ###
if BG_Pupbot:
	BG_Minion_Mecha+=['BG21_022','BG21_022_G',]
	BG_PoolSet_Mecha.append('BG21_022')
	BG_Mecha_Gold['BG21_022']='BG21_022_G'
class BG21_022:# <12>[1453]
	""" Pupbot
	[Divine Shield] """
	#<Tag enumID="194" name="DIVINE_SHIELD" type="Int" value="1"/>
	pass
class BG21_022_G:# <12>[1453]
	""" Pupbot
	[Divine Shield] """
	pass

#Harvest Golem(2) ### OK ###
if BG_Harvest_Golem:
	BG_Minion_Mecha+=['BG_EX1_556', 'BG_EX1_556t','TB_BaconUps_006','TB_BaconUps_006t',]
	BG_PoolSet_Mecha.append('BG_EX1_556')
	BG_Mecha_Gold['BG_EX1_556']='TB_BaconUps_006'
class BG_EX1_556:
	"""
	[Deathrattle:] Summon a 2/1 Damaged Golem."""
	deathrattle = Summon(CONTROLLER, "BG_EX1_556t")
	pass
class BG_EX1_556t:
	"""
	"""
class TB_BaconUps_006:# <12>[1453]
	""" Harvest Golem
	[Deathrattle:] Summon a 4/2 Damaged Golem. """
	deathrattle = Summon(CONTROLLER, "TB_BaconUps_006t")
	pass
class TB_BaconUps_006t:# <12>[1453]
	""" Damaged Golem
	 """
	#
	pass

#Kaboom Bot(2)  ### OK ###
if BG_Kaboom_Bot:
	BG_Minion_Mecha+=['BG_BOT_606', 'TB_BaconUps_028',]
	BG_PoolSet_Mecha.append('BG_BOT_606')
	BG_Mecha_Gold['BG_BOT_606']='TB_BaconUps_028'
class BG_BOT_606:
	"""
	[Deathrattle:] Deal 4_damage to a random enemy minion. """
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 4)
	pass
class TB_BaconUps_028:# <12>[1453]
	""" Kaboom Bot
	[Deathrattle:] Deal 4_damage to a random enemy minion twice. """
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 4) * 2
	pass


#Metaltooth Leaper(2) ### OK ###
if BG_Metaltooth_Leaper:
	BG_Minion_Mecha+=['BG_GVG_048','GVG_048e','TB_BaconUps_066','TB_BaconUps_066e',]
	BG_PoolSet_Mecha.append('BG_GVG_048')
	BG_Mecha_Gold['BG_GVG_048']='TB_BaconUps_066'
class BG_GVG_048:
	"""
	[Battlecry:] Give your other Mechs +2 Attack."""
	play = Buff(FRIENDLY_MINIONS + MECH - SELF,'GVG_048e')
GVG_048e=buff(2,0)
class TB_BaconUps_066:# <3>[1453]
	""" Metaltooth Leaper
	[Battlecry:] Give your other Mechs +4 Attack. """
	play = Buff(FRIENDLY_MINIONS + MECH - SELF, 'TB_BaconUps_066e')
	pass
TB_BaconUps_066e=buff(4,0)



## Lullabot (Mecha) (2)
#BG26__Lullabot=(Config.BG_VERSION>=2620)#(2)
if BG26__Lullabot:# 
	BG_Minion_Mecha+=['BG26_146','BG26_146e','BG26_146e2']
	BG_Minion_Mecha+=['BG26_146_G','BG26_146_Ge','BG26_146_Ge2']
	BG_PoolSet_Mecha.append('BG26_146')
	BG_Mecha_Gold['BG26_146']='BG26_146_G'
class BG26_146_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_146:# (minion)
	""" Lullabot
	<b>Magnetic</b> At the end of your turn, gain +1/+1. """
	play = Magnetic(SELF, ['BG26_146e2'])
	events = OWN_TURN_END.on(Buff(SELF, 'BG26_146e'))
	pass
BG26_146e=buff(1,1)
class BG26_146e2:
	events = OWN_TURN_END.on(Buff(OWNER, 'BG26_146e'))
	pass
class BG26_146_G:# (minion)
	""" Lullabot
	<b>Magnetic</b> At the end of your turn, gain +2/+2. """
	play = Magnetic(SELF, ['BG26_146_Ge2'])
	events = OWN_TURN_END.on(Buff(SELF, 'BG26_146_Ge'))
	pass
BG26_146_Ge=buff(2,2)
class BG26_146_Ge2:
	events = OWN_TURN_END.on(Buff(OWNER, 'BG26_146_Ge'))
	pass



##### TIER 3 ####

#Deflect-o-Bot(3) ### OK ###
if BG_Deflect_o_Bot:
	BG_Minion_Mecha+=['BGS_071', 'BGS_071e', 'TB_BaconUps_123', 'TB_BaconUps_123e',]
	BG_PoolSet_Mecha.append('BGS_071')
	BG_Mecha_Gold['BGS_071']='TB_BaconUps_123'
class BGS_071_Action(TargetedAction):
	TARGET = ActionArg()#SELF
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if isinstance(target.game, BG_Battle):##during combat
			Buff(target, buff).trigger(target.controller)
			SetDivineShield(target).trigger(target.controller)
class BGS_071:# <12>[1453]
	""" Deflect-o-Bot
	[Divine Shield]Whenever you summon a Mech during combat, gain +2 Attackand [Divine Shield]. """
	tags = {GameTag.DIVINE_SHIELD:True, }
	events = Summon(CONTROLLER, MECH).on(BGS_071_Action(SELF, 'BGS_071e'))
	pass
BGS_071e=buff(2,0)
class TB_BaconUps_123:# <12>[1453]
	""" Deflect-o-Bot
	[Divine Shield]Whenever you summon a Mechduring combat, gain +4 Attackand [Divine Shield]. """
	events = Summon(CONTROLLER, MECH).on(BGS_071_Action(SELF, 'TB_BaconUps_123e'))
	pass
TB_BaconUps_123e=buff(4,0)



#Replicating Menace(3)  ### OK ###
if BG_Replicating_Menace:
	BG_Minion_Mecha+=['BG_BOT_312', 'BG_BOT_312e','BG_BOT_312t','TB_BaconUps_032','TB_BaconUps_032e','TB_BaconUps_032t',]
	BG_PoolSet_Mecha.append('BG_BOT_312')
	BG_Mecha_Gold['BG_BOT_312']='TB_BaconUps_032'
class BG_BOT_312:
	"""Replicating Menace
	[Magnetic][Deathrattle:] Summon three 1/1 Microbots."""
	if Config.BG_VERSION>=2600:
		option_tags={GameTag.ATK:3, GameTag.HEALTH:2}
	else:
		option_tags={GameTag.ATK:3, GameTag.HEALTH:1}
	play = Magnetic(SELF, ['BG_BOT_312e'])
	deathrattle = Summon(CONTROLLER, 'BG_BOT_312t' ) * 3
class BG_BOT_312e:
	"""Replicating Menace
	"""
	if Config.BG_VERSION>=2600:
		tags = {GameTag.DEATHRATTLE:True, 
			GameTag.ATK:3,
			GameTag.HEALTH:2}
	else:
		tags = {GameTag.DEATHRATTLE:True, 
			GameTag.ATK:3,
			GameTag.HEALTH:1}
	deathrattle = Summon(CONTROLLER, 'BG_BOT_312t' ) * 3
	pass
class BG_BOT_312t:
	""" Microbot
	"""
	pass
class TB_BaconUps_032:# <12>[1453]
	""" Replicating Menace
	[Magnetic][Deathrattle:] Summon three 2/2 Microbots. """
	if Config.BG_VERSION>=2600:
		option_tags={GameTag.ATK:3, GameTag.HEALTH:2}
	else:
		option_tags={GameTag.ATK:3, GameTag.HEALTH:1}
	play = Magnetic(SELF, ['TB_BaconUps_032e'])
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_032t' ) * 3
	pass
class TB_BaconUps_032e:
	if Config.BG_VERSION>=2600:
		tags = {GameTag.DEATHRATTLE:True, 
			GameTag.ATK:6,
			GameTag.HEALTH:4}
	else:
		tags = {GameTag.DEATHRATTLE:True, 
			GameTag.ATK:6,
			GameTag.HEALTH:2}
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_032t' ) * 3
	pass
class TB_BaconUps_032t:# <12>[1453]
	""" Microbot
	 """
	pass



#Screwjank Clunker(3) ### OK ###
if BG_Screwjank_Clunker:
	BG_Minion_Mecha+=['GVG_055', 'GVG_055e', 'TB_BaconUps_069','TB_BaconUps_069e',]
	BG_PoolSet_Mecha.append('GVG_055')
	BG_Mecha_Gold['GVG_055']='TB_BaconUps_069'
class GVG_055:
	""" Screwjank Clunker
	[Battlecry:] Give a friendly Mech +2/+2 """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MECHANICAL} 
	play = Buff(TARGET, 'GVG_055e')
	pass
GVG_055e=buff(2,2)
class TB_BaconUps_069:# <10>[1453]
	""" Screwjank Clunker
	[Battlecry:] Give a friendly Mech +4/+4. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MECHANICAL} 
	play = Buff(TARGET, 'TB_BaconUps_069e')
	pass
TB_BaconUps_069e=buff(4,4)



## Iron Sensei (Mecha) (3) banned 26.2
if BG_Iron_Sensei:
	BG_Minion_Mecha+=['BG_GVG_027', 'GVG_027e', 'TB_BaconUps_044','TB_BaconUps_044e',]
	BG_PoolSet_Mecha.append('BG_GVG_027')
	BG_Mecha_Gold['BG_GVG_027']='TB_BaconUps_044'
class BG_GVG_027:
	"""Iron Sensei
	At the end of your turn, give another friendly Mech +2/+2."""
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS + MECH - SELF), "GVG_027e"))
GVG_027e = buff(+2, +2)
class TB_BaconUps_044:
	""" Iron Sensei
	At the end of your turn, give another friendly Mech +4/+4."""
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS + MECH - SELF), "TB_BaconUps_044e"))
TB_BaconUps_044e = buff(4,4)



## Accord-o-Tron (Mecha) (3)
#BG26__Accord_o_Tron=(Config.BG_VERSION>=2620)#(3)
if BG26__Accord_o_Tron:# 
	BG_Minion_Mecha+=['BG26_147','BG26_147e']
	BG_Minion_Mecha+=['BG26_147_G','BG26_147_Ge']
	BG_PoolSet_Mecha.append('BG26_147')
	BG_Mecha_Gold['BG26_147']='BG26_147_G'
class BG26_147_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_147:# (minion)
	""" Accord-o-Tron
	<b>Magnetic</b> At the start of your turn, gain 1 extra Gold. """
	play = Magnetic(SELF, ['BG26_147e'])
	events = OWN_TURN_BEGIN.on(Give(CONTROLLER, 'GAME_005'))
	pass
class BG26_147e:
	""" """
	events = OWN_TURN_END.on(Give(CONTROLLER, 'GAME_005'))
	pass
class BG26_147_G:# (minion)
	""" Accord-o-Tron
	<b>Magnetic</b> At the start of your turn, gain 2 extra Gold. """
	play = Magnetic(SELF, ['BG26_147_Ge'])
	events = OWN_TURN_BEGIN.on((Give(CONTROLLER, 'GAME_005'), Give(CONTROLLER, 'GAME_005')))
	pass
class BG26_147_Ge:
	""" """
	events = OWN_TURN_BEGIN.on((Give(CONTROLLER, 'GAME_005'), Give(CONTROLLER, 'GAME_005')))
	pass


#### TIER 4 ####

#Annoy-o-Module(4) ### OK ###
if BG_Annoy_o_Module:
	BG_Minion_Mecha+=['BG_BOT_911', 'BG_BOT_911e', 'TB_BaconUps_099','TB_BaconUps_099e',]
	BG_PoolSet_Mecha.append('BG_BOT_911')
	BG_Mecha_Gold['BG_BOT_911']='TB_BaconUps_099'
class BG_BOT_911:
	"""
	[Magnetic][Divine Shield][Taunt]"""
	## divine shield is a consumable buff. taunt is not
	play = Magnetic(SELF, ['BOT_911e'])
	pass
class BG_BOT_911e:
	def apply(self,target):
		target.divine_shield=True
		target.taunt=True
		self.tags[GameTag.ATK] = 2
		self.tags[GameTag.HEALTH] = 4
	pass
class TB_BaconUps_099:# <5>[1453]
	""" Annoy-o-Module
	[Magnetic][Divine Shield][Taunt] """
	play = Magnetic(SELF, ['TB_BaconUps_099e'])
	pass
class TB_BaconUps_099e:
	def apply(self,target):
		target.divine_shield=True
		target.taunt=True
		self.tags[GameTag.ATK] = 4
		self.tags[GameTag.HEALTH] = 8
	pass





#Mechano-Egg(4) ### OK ### -> renew 25.0.4
if BG_Mechano_Eg_g:
	BG_Minion_Mecha+=['BOT_537', 'BOT_537t','TB_BaconUps_039', 'TB_BaconUps_039t',]
	BG_PoolSet_Mecha.append('BOT_537')
	BG_Mecha_Gold['BOT_537']='TB_BaconUps_039'
class BOT_537:
	"""
	[Deathrattle:] Summon an 8/8 Robosaur."""
	deathrattle = Summon(CONTROLLER, 'BOT_537t')
class BOT_537t:
	""" Robosaur """
	pass
class TB_BaconUps_039:# <5>[1453]
	""" Mechano-Egg
	[Deathrattle:] Summon a 16/16 Robosaur. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_039t')
	pass
class TB_BaconUps_039t:
	""" Robosaur 	"""



#Mechano-Tank(4)-> banned 25.0.4
if BG_Mechano_Tank:
	BG_Minion_Mecha+=['BG21_023', 'BG21_023_G',]
	BG_PoolSet_Mecha.append('BG21_023')
	BG_Mecha_Gold['BG21_023']='BG21_023_G'
class BG21_023:# <12>[1453]
	""" Mechano-Tank
	[Avenge (2):] Deal 5 damage to the highest Health enemy minion. """
	events = Death(FRIENDLY_MINIONS).on(Avenge(SELF, 2, [Hit(HIGHEST_HEALTH(ENEMY_MINIONS), 5)]))
	pass
class BG21_023_G:# <12>[1453]
	""" Mechano-Tank
	[Avenge (2):] Deal 5 damage to the highest Health enemy minion twice. """
	events = Death(FRIENDLY_MINIONS).on(Avenge(SELF, 2, [Hit(HIGHEST_HEALTH(ENEMY_MINIONS), 5), Hit(HIGHEST_HEALTH(ENEMY_MINIONS), 5)]))
	pass



##  Wargear (4) 23.6  ### OK ###
if BG_Wargear:
	BG_Minion_Mecha+=['BG_BOT_563','BG_BOT_563e','BG_BOT_563_G','BG_BOT_563_Ge',]
	BG_PoolSet_Mecha.append('BG_BOT_563')
	BG_Mecha_Gold['BG_BOT_563']='BG_BOT_563_G'
class BG_BOT_563:
	""" Wargear
	[Magnetic]"""
	if Config.BG_VERSION>=2600:
		option_tags={GameTag.ATK:6, GameTag.HEALTH:5}
	else:
		option_tags={GameTag.ATK:5, GameTag.HEALTH:5}
	play = Magnetic(SELF, ['BG_BOT_563e'])
	pass
if Config.BG_VERSION>=2600:
	BG_BOT_563e=buff(6,5)
else:
	BG_BOT_563e=buff(5,5)
class BG_BOT_563_G:
	if Config.BG_VERSION>=2600:
		option_tags={GameTag.ATK:12, GameTag.HEALTH:10}
	else:
		option_tags={GameTag.ATK:10, GameTag.HEALTH:10}
	play = Magnetic(SELF, ['BG_BOT_563_Ge'])
	pass
if Config.BG_VERSION>=2600:
	BG_BOT_563_Ge=buff(12,10)
else:
	BG_BOT_563_Ge=buff(10,10)


## Scrap Scraper (Mecha) (4)
#BG26__Scrap_Scraper=(Config.BG_VERSION>=2620)# (4)
if BG26__Scrap_Scraper:# 
	BG_Minion_Mecha+=['BG26_148']
	BG_Minion_Mecha+=['BG26_148_G']
	BG_PoolSet_Mecha.append('BG26_148')
	BG_Mecha_Gold['BG26_148']='BG26_148_G'
class BG26_148_Action(GameAction):# 
	def do(self, source):
		newcard=RandomBGMagnetic().evaluate(source)#
		newcard=get00(newcard)
		newcard.zone=Zone.SETASIDE
		newcard.controller.source.controller
		newcard.zone=Zone.HAND
		pass# 
class BG26_148:# (minion)
	""" Scrap Scraper
	<b>Avenge (4):</b> Get a random <b>Magnetic</b> Mech. """
	#magnetic = <Tag enumID="849" name="MAGNETIC" type="Int" value="1"/>
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [BG26_148_Action()]))
	pass
class BG26_148_G:# (minion)
	""" Scrap Scraper
	<b>Avenge (4):</b> Get 2 random <b>Magnetic</b> Mechs. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [BG26_148_Action(), BG26_148_Action()]))
	pass




#### TIER 5 ####

#Holy Mecherel(5) banned 26.2
if BG_Holy_Mecherel:
	BG_Minion_Mecha+=['BG20_401', 'BG20_401_G',]
	BG_PoolSet_Mecha.append('BG20_401')
	BG_Mecha_Gold['BG20_401']='BG20_401_G'
class BG20_401:# <12>[1453]
	""" Holy Mecherel  さば
	After another friendly minion loses [Divine Shield], gain [Divine Shield]. """
	events = LoseDivineShield(FRIENDLY_MINIONS - SELF).after(SetDivineShield(SELF))
	pass
class BG20_401_G:# <12>[1453]
	""" Holy Mecherel
	After another friendly minion loses [Divine Shield], gain [Divine Shield]. """
	events = LoseDivineShield(FRIENDLY_MINIONS - SELF).after(SetDivineShield(SELF))
	pass


# Dr. Boombox (5)
if BG_Dr_Boombox:
	BG_Minion_Mecha+=['BG25_165', 'BG25_165_G',]
	BG_PoolSet_Mecha.append('BG25_165')
	BG_Mecha_Gold['BG25_165']='BG25_165_G'
class BG25_165_Action(GameAction):
	def do(self, source):
		if source in source.controller.field:
			index = 1.0*(source.controller.field.index(source))/(len(source.controller.field))
			newindex = int(index * len(source.controller.opponent.field))
			opp_len= len(source.controller.opponent.field)
			if newindex<opp_len and newindex>0:
				Hit(source.controller.opponent.field[newindex], 7).trigger(source)
				Hit(source.controller.opponent.field[newindex-1], 7).trigger(source)
			elif 1<opp_len and newindex==0:
				Hit(source.controller.opponent.field[newindex+1], 7).trigger(source)
				Hit(source.controller.opponent.field[newindex], 7).trigger(source)
			elif newindex<opp_len:
				Hit(source.controller.opponent.field[newindex], 7).trigger(source)
	pass
class BG25_165:
	""" Dr. Boombox
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 7 damage to the 2 nearest enemy minions."""
	if Config.BG_VERSION>=2602:
		option_tags = {GameTag.TECH_LEVEL:5}
	else:
		option_tags = {GameTag.TECH_LEVEL:4}
	deathrattle = BG25_165_Action()
class BG25_165_G_Action(GameAction):
	def do(self, source):
		if source in source.controller.field:
			index = 1.0*(source.controller.field.index(source))/(len(source.controller.field))
			newindex = int(index * len(source.controller.opponent.field))
			opp_len= len(source.controller.opponent.field)
			if newindex<opp_len and newindex>0:
				Hit(source.controller.opponent.field[newindex], 14).trigger(source)
				Hit(source.controller.opponent.field[newindex-1], 14).trigger(source)
			elif 1<opp_len and newindex==0:
				Hit(source.controller.opponent.field[newindex+1], 14).trigger(source)
				Hit(source.controller.opponent.field[newindex], 14).trigger(source)
			elif newindex<opp_len:
				Hit(source.controller.opponent.field[newindex], 14).trigger(source)
	pass
class BG25_165_G:
	""" Dr. Boombox
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 14 damage to the 2 nearest enemy minions."""
	if Config.BG_VERSION>=2602:
		option_tags = {GameTag.TECH_LEVEL:5}
	else:
		option_tags = {GameTag.TECH_LEVEL:4}
	deathrattle = BG25_165_G_Action()
	pass



## Utility Drone (Mecha) (5)
#BG26__Utility_Drone=(Config.BG_VERSION>=2620)#(5)
if BG26__Utility_Drone:# 
	BG_Minion_Mecha+=['BG26_152','BG26_152e']
	BG_Minion_Mecha+=['BG26_152_G','BG26_152_Ge']
	BG_PoolSet_Mecha.append('BG26_152')
	BG_Mecha_Gold['BG26_152']='BG26_152_G'
class BG26_152_Action(GameAction):# 
	def do(self, source):# 
		for card in source.controller.field:
			for buff in card.buffs:
				if getattr(buff, 'magnetic'):
					Buff(card, 'BG26_152e').trigger(source)
		pass# 
class BG26_152:# (minion)
	""" Utility Drone
	At the end of your turn, give your minions +1/+1 for each <b>Magnetization</b> they have. """
	events = OWN_TURN_END.on(BG26_152_Action())
	pass
BG26_152e=buff(1,1)
class BG26_152_G_Action(GameAction):# 
	def do(self, source):# 
		for card in source.controller.field:
			for buff in card.buffs:
				if getattr(buff, 'magnetic'):
					Buff(card, 'BG26_152_Ge').trigger(source)
		pass# 
class BG26_152_G:# (minion)
	""" Utility Drone
	At the end of your turn, give your minions +2/+2 for each <b>Magnetization</b> they have. """
	events = OWN_TURN_END.on(BG26_152_G_Action())
	pass
BG26_152_Ge=buff(1,1)



#### TIER 6 ####

#Foe Reaper 4000(6)
if BG_Foe_Reaper_4000:
	BG_Minion_Mecha+=['BG_GVG_113', 'TB_BaconUps_153',]
	BG_PoolSet_Mecha.append('BG_GVG_113')
	BG_Mecha_Gold['BG_GVG_113']='TB_BaconUps_153'
class BG_GVG_113:## エネリ
	""" Foe Reaper 4000
	Also damages the minions next to whomever it attacks. """
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, ATK(SELF)))
	pass
class TB_BaconUps_153:# <12>[1453]
	""" Foe Reaper 4000
	Also damages the minions next to whomever it attacks. """
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, ATK(SELF)))
	pass



#Omega Buster(6)
if BG_Omega_Buster:
	BG_Minion_Mecha+=['BG21_025','BG21_025e','BG21_025_G',]
	BG_PoolSet_Mecha.append('BG21_025')
	BG_Mecha_Gold['BG21_025']='BG21_025_G'
if Omega_Buster: #
	pass
class BG21_025_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source,target):
		controller = target
		summonnumber = 8-len(controller.field)# or 7-len(***) ?
		for repeat in range(summonnumber):
			yield Summon(CONTROLLER, 'BG_BOT_312t')
		if summonnumber<5:
			for repeat in range(5-summonnumber):
				yield Buff(FRIENDLY + MECH, 'BG21_025e')
class BG21_025:# <12>[1453] オメバス
	""" Omega Buster
	[Deathrattle:] Summon five 1/1 Microbots. For each that doesn't fit, give your Mechs +1/+1. """
	deathrattle = BG21_025_Action(CONTROLLER)
	pass
BG21_025e=buff(1,1)
class BG21_025_G:# <12>[1453]
	""" Omega Buster
	[Deathrattle:] Summon five 2/2 Microbots. For each that doesn't fit, give your Mechs +2/+2. """
	def do(self, source,target):
		controller = target
		summonnumber = 8-len(controller.field)# or 7-len(***) ?
		for repeat in range(summonnumber):
			yield Summon(CONTROLLER, 'TB_BaconUps_032t')
		if summonnumber<5:
			for repeat in range(5-summonnumber):
				yield Buff(FRIENDLY + MECH, 'BG21_025e2')
	pass
BG21_025e2=buff(2,2)
class TB_BaconUps_032t:
	""" Microbot (2/2)
	"""
	pass

#Grease Bot(4->6) 23.6
if BG_Grease_Bot:
	BG_Minion_Mecha+=['BG21_024', 'BG21_024e','BG21_024_G','BG21_024_Ge',]
	BG_PoolSet_Mecha.append('BG21_024')
	BG_Mecha_Gold['BG21_024']='BG21_024_G'
class BG21_024:# <12>[1453]
	""" Grease Bot
	After a friendly minion loses [Divine Shield], give it +2/+2_permanently. """
	if Config.BG_VERSION>=2360:
		option_tags={GameTag.TECH_LEVEL:6}
	else:
		option_tags={GameTag.TECH_LEVEL:4}
	events = LoseDivineShield(FRIENDLY_MINIONS).on(BuffPermanently(LoseDivineShield.TARGET, 'BG21_024e'))
	pass
BG21_024e=buff(2,2)#24.0.3
#BG21_024e=buff(3,2)# until 23.6
class BG21_024_G:# <12>[1453]
	""" Grease Bot
	After a friendly minion loses [Divine Shield], give it +4/+4_permanently. """
	if Config.BG_VERSION>=2360:
		option_tags={GameTag.TECH_LEVEL:6}
	else:
		option_tags={GameTag.TECH_LEVEL:4}
	events = LoseDivineShield(FRIENDLY_MINIONS).on(BuffPermanently(LoseDivineShield.TARGET, 'BG21_024_Ge'))
	pass
BG21_024_Ge=buff(4,4)# 24.0.3
#BG21_024_Ge=buff(6,4)# until 23.6

from .BG_minion_demon import BG25__Mecha_Jaraxxus
if BG25__Mecha_Jaraxxus:# 6/3/15 MECH/DEMON ## new 25.2.2 ##
	##BG_Minion_Mecha+=['BG25_807','BG25_807_G','BG25_807e','BG25_807e2','BG25_807e3']
	##BG_Minion_Mecha+=['BG25_807t','BG25_807t_G','BG25_807t2','BG25_807t2_G','BG25_807t3','BG25_807t3_G']
	BG_PoolSet_Mecha.append('BG25_807')
	BG_Mecha_Gold['BG25_807']='BG25_807_G'
	BG_Mecha_Gold['BG25_807t']='BG25_807t_G'
	BG_Mecha_Gold['BG25_807t2']='BG25_807t2_G'
	BG_Mecha_Gold['BG25_807t3']='BG25_807t3_G'



## Polarizing Beatboxer (Mecha) (6)
#BG26__Polarizing_Beatboxer=(Config.BG_VERSION>=2620) # (6)
if BG26__Polarizing_Beatboxer:# 
	BG_Minion_Mecha+=['BG26_149']
	BG_Minion_Mecha+=['BG26_149_G']
	BG_PoolSet_Mecha.append('BG26_149')
	BG_Mecha_Gold['BG26_149']='BG26_149_G'
class BG26_149_Action(TargetedAction):#
	TARGET=ActionArg()
	def do(self, source, target):#target = buffs
		for buff in target:
			if getattr(buff, 'this_is_enchantment'):
				Buff(source, buff.id).trigger(source)
			elif isinstance(buff, str):
				Buff(source, buff).trigger(source)
		pass# 
class BG26_149:# (minion)
	""" Polarizing Beatboxer
	Whenever you <b>Magnetize</b> another minion, it also <b>Magnetizes</b> to this. """
	events = Magnetic(FRIENDLY + MINION - SELF).after(BG26_149_Action(Magnetic.BUFFS))
	pass
class BG26_149_G_Action(TargetedAction):#
	TARGET=ActionArg()
	def do(self, source, target):#target = buffs
		for buff in target:
			if getattr(buff, 'this_is_enchantment'):
				Buff(source, buff.id).trigger(source)
				Buff(source, buff.id).trigger(source)
			elif isinstance(buff, str):
				Buff(source, buff).trigger(source)
				Buff(source, buff).trigger(source)
		pass# 
class BG26_149_G:# (minion)
	""" Polarizing Beatboxer
	Whenever you <b>Magnetize</b> another minion, it also _<b>Magnetizes</b> to this twice. """
	events = Magnetic(FRIENDLY + MINION - SELF).after(BG26_149_G_Action(Magnetic.BUFFS))
	pass

