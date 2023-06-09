from ..utils import *

BG_Rockpool_Hunter=True ##(1) 
BG_Swampstriker=True ## (1)

BG_Murloc_Warleader=(Config.BG_VERSION<2620) ## (2) ## banned 26.2 
BG_Saltscale_Honcho=(Config.BG_VERSION>=2620) ## (2) banned when? revive 26.2
BG_Tad=True ## (2)
BG_Blazing_Skyfin=True ## (2/1/3)
BG26__Upbeat_Flutist=(Config.BG_VERSION>=2620)#(2)

BG_Coldlight_Seer=True ## (3)
BG_Felfin_Navigator=(Config.BG_VERSION<2620) ## (3) banned 26.2
BG_Swolefin=(Config.BG_VERSION<2620) ## (3) banned 26.2
BG26__Scourfin=(Config.BG_VERSION>=2620)#(3)

BG_Primalfin_Lookout=True ## (4)
BG26__Bream_Counter=(Config.BG_VERSION>=2620)# (4/4/4)
BG26__Bassgill=(Config.BG_VERSION>=2620) #(4/6/2)
BG26__Plagued_Tidewalker=(Config.BG_VERSION>=2620)#(4) undead/murloc

BG_King_Bagurgle=True ## (5)
BG_SI_Sefin=False ## (5) banned 4.2
BG26__Operatic_Belcher=(Config.BG_VERSION>=2620)#(5/5/2)

BG_Young_Murk_Eye=True ## (6) 
BG_Toxfin=(Config.BG_VERSION>=2420 and Config.BG_VERSION<2620) ##(4) new 24.2 -> (6) ## 25.2.2 (5) ## banned 26.2
BG26__Choral_Mrrrglr=(Config.BG_VERSION>=2620)#(6/6/6)


BG_Minion_Murloc =[]

BG_PoolSet_Murloc=[]

BG_Murloc_Gold={}


#Rockpool Hunter (1)  ## OK ##
if BG_Rockpool_Hunter:
	BG_Minion_Murloc+=['BG_UNG_073','UNG_073e','TB_BaconUps_061','TB_BaconUps_061e',]
	BG_PoolSet_Murloc.append('BG_UNG_073')
	BG_Murloc_Gold['BG_UNG_073']='TB_BaconUps_061'
class BG_UNG_073:
	""" >Rockpool Hunter
	[Battlecry:] Give a friendly Murloc +1/+1. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = Buff(TARGET, 'UNG_073e')
	pass
UNG_073e=buff(1,1)
class TB_BaconUps_061:# <12>[1453]
	""" Rockpool Hunter
	[Battlecry:] Give a friendly Murloc +2/+2. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = Buff(TARGET, 'TB_BaconUps_061e')
	pass
TB_BaconUps_061e=buff(2,2)


#Swampstriker (1)  ## OK ##
if BG_Swampstriker:
	BG_Minion_Murloc+=['BG22_401','BG22_401e','BG22_401_G','BG22_401_Ge',]
	BG_PoolSet_Murloc.append('BG22_401')
	BG_Murloc_Gold['BG22_401']='BG22_401_G'
class BG22_401:# <12>[1453]
	""" Swampstriker
	After you summon a Murloc, gain +1 Attack. """
	events = Summon(CONTROLLER, FRIENDLY + MURLOC).after(Buff(SELF, 'BG22_401e'))
	pass
BG22_401e=buff(1,0)
class BG22_401_G:# <12>[1453]
	""" Swampstriker
	After you summon a Murloc, gain +2 Attack. """
	events = Summon(CONTROLLER, FRIENDLY + MURLOC).after(Buff(SELF, 'BG22_401_Ge'))
	pass
BG22_401_Ge=buff(2,0)

#### TIER 2 ####

#Murloc Warleader (2)  ### maybe ### banned 26.2
if BG_Murloc_Warleader:
	BG_Minion_Murloc+=['BG_EX1_507','EX1_507e','TB_BaconUps_008','TB_BaconUps_008e',]
	BG_PoolSet_Murloc.append('BG_EX1_507')
	BG_Murloc_Gold['BG_EX1_507']='TB_BaconUps_008'
class BG_EX1_507:
	"""Murloc Warleader 戦隊長
	"""
	update = Refresh(FRIENDLY_MINIONS + MURLOC - SELF, buff="EX1_507e")
	pass
EX1_507e=buff(2,0)
class TB_BaconUps_008:# <12>[1453]
	""" Murloc Warleader
	Your other Murlocs have +4 Attack. """
	update = Refresh(FRIENDLY_MINIONS + MURLOC - SELF, buff="TB_BaconUps_008e")
	pass
TB_BaconUps_008e=buff(4,0)# <12>[1453]
""" Mrgglaargl!,  +4 Attack from Murloc Warleader. """



#Saltscale Honcho (2) ### maybe ### revive 26.2
if BG_Saltscale_Honcho:
	BG_Minion_Murloc+=['BG21_008','BG21_008e','BG21_008_G','BG21_008_Ge',]
	BG_PoolSet_Murloc.append('BG21_008')
	BG_Murloc_Gold['BG21_008']='BG21_008_G'
class BG21_008:# <12>[1453] そるとすけいる
	""" Saltscale Honcho
	After you play a Murloc, give two other friendly Murlocs +1 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY + MURLOC).after(Buff(RANDOM(FRIENDLY_MINIONS + MURLOC - SELF),'BG21_008e') * 2)
	pass
BG21_008e=buff(0,1)# <12>[1453]
""" Salty, +1 Health. """
class BG21_008_G:# <12>[1453]
	""" Saltscale Honcho
	After you play a Murloc, give two other friendly Murlocs +2 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY+MURLOC).after(Buff(RANDOM(FRIENDLY_MINIONS + MURLOC - SELF),'BG21_008_Ge') * 2)
	pass
BG21_008_Ge=buff(0,2)# <12>[1453]
""" Extra Salty
+2 Health. """



#Tad (2) ### maybe ###
if BG_Tad:
	BG_Minion_Murloc+=['BG22_202','BG22_202_G',]
	BG_PoolSet_Murloc.append('BG22_202')
	BG_Murloc_Gold['BG22_202']='BG22_202_G'
class BG22_202:# <12>[1453]
	""" Tad
	When you sell this,add another random Murloc to your hand. """
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.ATK:2, GameTag.HEALTH:2}
	else:
		option_tags={GameTag.ATK:2, GameTag.HEALTH:4}
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, RandomBGMurloc(tech_level_less=TIER(CONTROLLER))))
	pass
class BG22_202_G:# <12>[1453]
	""" Tad
	When you sell this,add 2 other randomMurlocs to your hand. """
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:4}
	else:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:8}
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, RandomMurloc())*2)
	pass


### Blazing Skyfin (2/1/3) ## new 25.2.2
if BG_Blazing_Skyfin:
	BG_Minion_Murloc+=['BG25_040','BG25_040_G','BG25_040e','BG25_040_Ge']
	BG_PoolSet_Murloc.append('BG25_040')
	BG_Murloc_Gold['BG25_040']='BG25_040_G'
class BG25_040:
	""" Blazing Skyfin (2/1/3)
	After you play a [Battlecry] minion, gain +1/+1."""
	events = Play(CONTROLLER, FRIENDLY + BATTLECRY).after(Buff(SELF, 'BG25_040e'))
	pass
BG25_040e=buff(1,1)
class BG25_040_G:
	""" Blazing Skyfin (2/2/6)
	After you play a [Battlecry] minion, gain +2/+2."""
	events = Play(CONTROLLER, FRIENDLY + BATTLECRY).after(Buff(SELF, 'BG25_040_Ge'))
	pass
BG25_040_Ge=buff(2,2)



## Upbeat Flutist (Murloc) (2)
#BG26__Upbeat_Flutist=(Config.BG_VERSION>=2620)#(2)
if BG26__Upbeat_Flutist:# 
	BG_Minion_Murloc+=['BG26_352','BG26_352e']
	BG_Minion_Murloc+=['BG26_352_G','BG26_352_Ge']
	BG_PoolSet_Murloc.append('BG26_352')
	BG_Murloc_Gold['BG26_352']='BG26_352_G'
class BG26_352_Action(GameAction):# 
	BUFF=ActionArg()
	def do(self, source, buff):# 
		if len(source.controller.hand):
			Buff(source.controller.hand[0], buff)
		pass# 
class BG26_352:# (minion)(murloc)
	""" Upbeat Flutist
	At the end of every 2 turns, give a random minion in your hand +9 Health. <i>({0} |4(turn, turns) left!)</i>@At the end of every 2 turns, give a random minion in your hand +9 Health. <i>(End of this turn!)</i> """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 2,[BG26_352_Action('BG26_352e')]))
	pass
BG26_352e=buff(0,9)
class BG26_352_G:# (minion)(murloc)
	""" Upbeat Flutist
	At the end of every 2 turns, give a random minion in your hand +18 Health. <i>({0} |4(turn, turns) left!)</i>@At the end of every 2 turns, give a random minion in your hand +18 Health. <i>(End of this turn!)</i> """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 2,[BG26_352_Action('BG26_352_Ge')]))
	pass
BG26_352_Ge=buff(0,18)


###### tavern tier 3

#Coldlight Seer (3)
if BG_Coldlight_Seer:
	BG_Minion_Murloc+=['BG_EX1_103','EX1_103e','TB_BaconUps_064','TB_BaconUps_064e',]
	BG_PoolSet_Murloc.append('BG_EX1_103')
	BG_Murloc_Gold['BG_EX1_103']='TB_BaconUps_064'
class BG_EX1_103:
	""" Coldlight Seer
	[Battlecry:] Give your other Murlocs +2 Health. """
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'EX1_103e')
	pass
EX1_103e=buff(0,2)
class TB_BaconUps_064:# <12>[1453]
	""" Coldlight Seer
	[Battlecry:] Give your other Murlocs +4 Health. """
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'TB_BaconUps_064e')
	pass
TB_BaconUps_064e=buff(0,4)



#Felfin Navigator (3) ### maybe ### banned 26.2
if BG_Felfin_Navigator:
	BG_Minion_Murloc+=['BG_BT_010','BT_010e','TB_BaconUps_124','TB_BaconUps_124e',]
	BG_PoolSet_Murloc.append('BG_BT_010')
	BG_Murloc_Gold['BG_BT_010']='TB_BaconUps_124'
class BG_BT_010:
	""" Felfin Navigator
	[Battlecry:] Give your other Murlocs +1/+1. """
	play =  Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'BT_010e')
BT_010e=buff(1,1)
class TB_BaconUps_124:# <12>[1453]
	""" Felfin Navigator
	[Battlecry:] Give your other Murlocs +2/+2. """
	play =  Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'TB_BaconUps_124e')
	pass
TB_BaconUps_124e=buff(2,2)



#Swolefin (3) ### need check ### banned 26.2
if BG_Swolefin:
	BG_Minion_Murloc+=['BG21_010','BG21_010e','BG21_010_G','BG21_010_Ge',]
	BG_PoolSet_Murloc.append('BG21_010')
	BG_Murloc_Gold['BG21_010']='BG21_010_G'
class BG21_010:# <12>[1453] ムキムキ
	""" Swolefin
	[Battlecry:] Gain +2/+1 for each other friendly Murloc. """
	play = Buff(SELF, 'BG21_010e') * Count(FRIENDLY_MINIONS + MURLOC - SELF)
	pass
BG21_010e=buff(2,1)# <12>[1453]
""" Swole
+2/+1. """
class BG21_010_G:# <12>[1453]
	""" Swolefin
	[Battlecry:] Gain +4/+2 foreach other friendly Murloc. """
	play = Buff(SELF, 'BG21_010_Ge') * Count(FRIENDLY_MINIONS + MURLOC - SELF)
	pass
BG21_010_Ge=buff(4,2)# <12>[1453]
""" Swoler
+4/+2. """



## Scourfin (Murloc) (3)
#BG26__Scourfin=(Config.BG_VERSION>=2620)#(3)
if BG26__Scourfin:# 
	BG_Minion_Murloc+=['BG26_360','BG26_360e']
	BG_Minion_Murloc+=['BG26_360_G','BG26_360_Ge']
	BG_PoolSet_Murloc.append('BG26_360')
	BG_Murloc_Gold['BG26_360']='BG26_360_G'
class BG26_360_Action(GameAction):# 
	BUFF=ActionArg()
	def do(self, source, buff):# 
		original_controller = getattr(source.controller,'deepcopy_original')
		if original_controller != None:
			if len(original_controller.hand):
				card=random.choice(original_controller.hand)
				Buff(card, buff).trigger(source)
		pass# 
class BG26_360:# (minion)(murloc)
	""" Scourfin
	<b>Deathrattle:</b> Give a random minion in your hand +5/+5. """
	#New: 3 Attack, 3 Health
	#Old: 6 Attack, 3 Health
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:3, GameTag.HEALTH:3}
	else:
		option_tags={GameTag.ATK:6, GameTag.HEALTH:3}

	deathrattle = BG26_360_Action('BG26_360e')
	pass
BG26_360e=buff(5,5)
class BG26_360_G:# (minion)(murloc)
	""" Scourfin
	<b>Deathrattle:</b> Give a random minion in your hand +10/+10. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:6, GameTag.HEALTH:6}
	else:
		option_tags={GameTag.ATK:12, GameTag.HEALTH:6}
	deathrattle = BG26_360_Action('BG26_360_Ge')
	pass
BG26_360_Ge=buff(10,10)



#### TIER 4 ####

#Primalfin Lookout (4) ### maybe ###
if BG_Primalfin_Lookout:
	BG_Minion_Murloc+=['BGS_020','TB_BaconUps_089',]
	BG_PoolSet_Murloc.append('BGS_020')
	BG_Murloc_Gold['BGS_020']='TB_BaconUps_089'
class BGS_020_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		pass
class BGS_020_Action(GameAction):
	def do(self, source):
		controller=source.controller
		#cards=[card for card in controller.field if card!=source and card.type==CardType.MINION and card.race==Race.MURLOC]
		cards=[card for card in controller.field if card!=source and race_identity(card,Race.MURLOC)]
		if len(cards):
			BGS_020_Choice(controller, RandomBGMurloc(tech_level_less=TIER(CONTROLLER))*3).trigger(source)
class BGS_020:# <12>[1453] 見張り番
	""" Primalfin Lookout
	[Battlecry:] If you control another Murloc, [Discover] a_Murloc. """
	play = BGS_020_Action()
	pass
class BGS_020_Choice2(Choice):
	def choose(self, card):
		card.zone=Zone.HAND
		self.source.sidequest_counter+=1
		if self.source.sidequest_counter==1:
			self.next_choice=self
		else:
			self.next_choice=None
		super().choose(card)
		pass
class BGS_020_Action2(GameAction):
	def do(self, source):
		controller=source.controller
		#cards=[card for card in controller.field if card!=source and card.type==CardType.MINION and card.race==Race.MURLOC]
		cards=[card for card in controller.field if card!=source and race_identity(card,Race.MURLOC)]
		if len(cards):
			BGS_020_Choice2(controller, RandomBGMurloc(tech_level_less=TIER(CONTROLLER))*3).trigger(source)
class TB_BaconUps_089:# <12>[1453]
	""" Primalfin Lookout
	[Battlecry:] If you control another Murloc, [Discover] two_Murlocs. """
	play = BGS_020_Action2()
	pass





## Bream Counter (Murloc) (4)
#BG26__Bream_Counter=(Config.BG_VERSION>=2620)# (4)
if BG26__Bream_Counter:# 
	BG_Minion_Murloc+=['BG26_137','BG26_137e']
	BG_Minion_Murloc+=['BG26_137_G','BG26_137_Ge']
	BG_PoolSet_Murloc.append('BG26_137')
	BG_Murloc_Gold['BG26_137']='BG26_137_G'
class BG26_137_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_137:# (minion)(murloc)
	""" Bream Counter
	While this is in your hand, after you play a Murloc, gain +3/+2. """
	class Hand:
		events = BG_Play(CONTROLLER, FRIENDLY + MINION + MURLOC).after(Buff(SELF, 'BG26_137e'))
	pass
BG26_137e=buff(3,2)
class BG26_137_G:# (minion)(murloc)
	""" Bream Counter
	While this is in your hand, after you play a Murloc, gain +6/+4. """
	class Hand:
		events = BG_Play(CONTROLLER, FRIENDLY + MINION + MURLOC).after(Buff(SELF, 'BG26_137e'))
	pass
BG26_137_Ge=buff(6,4)



## Bassgill (Murloc) (4)
#BG26__Bassgill=(Config.BG_VERSION>=2620) #(4)
if BG26__Bassgill:# 
	BG_Minion_Murloc+=['BG26_350','BG26_350e2']
	BG_Minion_Murloc+=['BG26_350_G']
	BG_PoolSet_Murloc.append('BG26_350')
	BG_Murloc_Gold['BG26_350']='BG26_350_G'
class BG26_350_Action(GameAction):# 
	def do(self, source):# 
		cards=[]
		if len(source.controller.hand):
			for card in source.controller.hand:
				if card.type==CardType.MINION:
					if cards==[]:
						cards=[card]
					elif cards[0].max_health<card.max_health:
						cards=[card]
					elif cards[0].max_health==card.max_health:
						cards.append(card)
		if len(cards):
			card = random.choice(cards)
			Summon(source.controller, card.id).trigger(source) 
		pass# 
class BG26_350:# (minion)(murloc)
	""" Bassgill
	<b>Deathrattle:</b> Summon the highest Health minion from your hand for this combat only. """
	deathrattle = BG26_350_Action()
	pass
class BG26_350_G_Action(GameAction):# 
	def do(self, source):# 
		cards=[]
		if len(source.controller.hand):
			for card in source.controller.hand:
				if card.type==CardType.MINION:
					if cards==[]:
						cards=[card]
					elif cards[0].max_health<card.max_health:
						cards=[card]
					elif cards[0].max_health==card.max_health:
						cards.append(card)
		if len(cards)>=2:
			cards = random.sample(cards,2)
			Summon(source.controller, cards[0].id).trigger(source) 
			Summon(source.controller, cards[1].id).trigger(source) 
		elif len(cards)==1:
			Summon(source.controller, cards[0].id).trigger(source) 
			Summon(source.controller, cards[0].id).trigger(source) 
		pass# 
class BG26_350_G:# (minion)(murloc)
	""" Bassgill
	<b>Deathrattle:</b> Summon the 2 highest Health minions from your hand for this combat only. """
	deathrattle = BG26_350_G_Action()
	pass



## Plagued Tidewalker (Murloc) (4)
#BG26__Plagued_Tidewalker=(Config.BG_VERSION>=2620)#(4)
if BG26__Plagued_Tidewalker:# 
	BG_Minion_Murloc+=['BG26_361']
	BG_Minion_Murloc+=['BG26_361_G']
	BG_PoolSet_Murloc.append('BG26_361')
	BG_Murloc_Gold['BG26_361']='BG26_361_G'
class BG26_361_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_361:# (minion)(murloc)
	""" Plagued Tidewalker
	<b>Venomous</b> """
	#<Tag enumID="2853" name="VENOMOUS" type="Int" value="1"/>
	pass
class BG26_361_G:# (minion)(murloc)
	""" Plagued Tidewalker
	<b>Venomous</b> """
	#<Tag enumID="2853" name="VENOMOUS" type="Int" value="1"/>
	pass




#### TIER 5 ####

#King Bagurgle (5) ### OK ###
if BG_King_Bagurgle:
	BG_Minion_Murloc+=['BGS_030','BGS_030e','TB_BaconUps_100','TB_BaconUps_100e',]
	BG_PoolSet_Murloc.append('BGS_030')
	BG_Murloc_Gold['BGS_030']='TB_BaconUps_100'
class BGS_030:# <12>[1453] バガァグル
	""" King Bagurgle
	[Battlecry and Deathrattle:] Give your other Murlocs +2/+2. """
	play = Buff(FRIENDLY_MINIONS + MURLOC, 'BGS_030e')
	deathrattle = Buff(FRIENDLY_MINIONS + MURLOC, 'BGS_030e')
	pass
BGS_030e=buff(2,2)
class TB_BaconUps_100:# <12>[1453]
	""" King Bagurgle
	[Battlecry and Deathrattle:] Give your other Murlocs +4/+4. """
	play = Buff(FRIENDLY_MINIONS + MURLOC, 'TB_BaconUps_100e')
	deathrattle = Buff(FRIENDLY_MINIONS + MURLOC, 'TB_BaconUps_100e')
	pass
TB_BaconUps_100e=buff(4,4)



#SI:Sefin (5)  ### maybe ### banned 24.2
if BG_SI_Sefin:
	BG_Minion_Murloc+=['BG21_009','BG21_009e','BG21_009_G',]
	BG_PoolSet_Murloc.append('BG21_009')
	BG_Murloc_Gold['BG21_009']='BG21_009_G'
class BG21_009:# <12>[1453] セブリ
	""" SI:Sefin
	[Avenge (3):] Give a friendly Murloc [Poisonous] permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(RANDOM(FRIENDLY_MINIONS + MURLOC), 'BG21_009e')])) #
	pass
BG21_009e=buff(poisonous=True)# <12>[1453]
""" SI:7 Training
[Poisonous] """
class BG21_009_G:# <12>[1453]
	""" SI:Sefin
	[Avenge (3):] Give 2 friendly Murlocs [Poisonous] permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(RANDOM(FRIENDLY_MINIONS + MURLOC), 'BG21_009e'), BuffPermanently(RANDOM(FRIENDLY_MINIONS + MURLOC - SELF), 'BG21_009e')])) #
	pass



## Operatic Belcher (Murloc) (5)
#BG26__Operatic_Belcher=(Config.BG_VERSION>=2620)#(5)
if BG26__Operatic_Belcher:# 
	BG_Minion_Murloc+=['BG26_888']
	BG_Minion_Murloc+=['BG26_888_G']
	BG_PoolSet_Murloc.append('BG26_888')
	BG_Murloc_Gold['BG26_888']='BG26_888_G'
class BG26_888_Action(GameAction):# 
	def do(self, source):# 
		cards=[card for card in source.controller.field if card.race==Race.MURLOC]
		if len(cards):
			card = random.choice(cards)
			card.venomous=True
		pass# 
class BG26_888:# (minion)(murloc)
	""" Operatic Belcher
	<b>Venomous.</b> <b>Deathrattle:</b> Give a friendly Murloc <b>Venomous</b>. """
	deathrattle = BG26_888_Action()
	pass
class BG26_888_G_Action(GameAction):# 
	def do(self, source):# 
		cards=[card for card in source.controller.field if card.Race==Race.MURLOC]
		if len(cards)==1:
			card = random.choice(cards)
			card.venomous=True
		elif len(cards)>1:
			cards=random.sample(cards, 2)
			for card in cards:
				card.venomous=True
		pass# 
class BG26_888_G:# (minion)(murloc)
	""" Operatic Belcher
	<b>Venomous.</b> <b>Deathrattle:</b> Give 2 friendly Murlocs <b>Venomous</b>. """
	deathrattle = BG26_888_G_Action()
	pass




#### TIER 6 ####

## Young Murk-Eye (6) 
if BG_Young_Murk_Eye:
	BG_Minion_Murloc+=['BG22_403','BG22_403_G']
	BG_PoolSet_Murloc.append('BG22_403')
	BG_Murloc_Gold['BG22_403']='BG22_403_G'
class BG22_403_Action(GameAction):
	def do(self, source):
		index = source.controller.field.index(source)
		if index>0 :
			card = source.controller.field[index-1]
			if card.has_battlecry:
				PlayBattlecry(card).trigger(source)
class BG22_403:
	""" Young Murk-Eye (6) 
	At the end of your turn, the minion to the left of this triggers its Battlecry."""
	##	At the end of your turn, the Murloc to the left of this triggers its [Battlecry].""" old, <2620
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.ATK:7, GameTag.HEALTH:4}
	else:
		option_tags={GameTag.ATK:8, GameTag.HEALTH:5}
	events = OWN_TURN_END.on(BG22_403_Action())
	pass
class BG22_403_G_Action(GameAction):
	def do(self, source):
		index = source.controller.field.index(source)
		if index>0 :
			card = source.controller.field[index-1]
			if card.has_battlecry:
				PlayBattlecry(card).trigger(source)
		if index<len(source.controller.field)-1 :
			card = source.controller.field[index+1]
			if card.has_battlecry:
				PlayBattlecry(card).trigger(source)
class BG22_403_G:
	""" (6) 
	At the end of your turn, adjacent Murlocs trigger their [Battlecries]."""
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.ATK:14, GameTag.HEALTH:8}
	else:
		option_tags={GameTag.ATK:16, GameTag.HEALTH:10}
	events = OWN_TURN_END.on(BG22_403_G_Action())
	pass



## Toxfin (6)
if BG_Toxfin: ##(4) new 24.2 -> (6) 25.0.4
	BG_Minion_Murloc+=['BG_DAL_077','TB_BaconUps_152']
	BG_PoolSet_Murloc.append('BG_DAL_077')
	BG_Murloc_Gold['BG_DAL_077']='TB_BaconUps_152'
class BG_DAL_077:
	""" Toxfin (4)-> (6) 25.0.4
	[Battlecry:] Give a friendly Murloc [Poisonous].""" 
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.MURLOC }	
	if Config.BG_VERSION>=2504:
		option_tags={GameTag.TECH_LEVEL:6}
	else:
		option_tags={GameTag.TECH_LEVEL:4}
	play = SetTag(TARGET, (GameTag.POISONOUS,))
class TB_BaconUps_152:
	""" Toxfin
	[Battlecry:] Give a friendly Murloc [Poisonous]."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.MURLOC }
	if Config.BG_VERSION>=2504:
		option_tags={GameTag.TECH_LEVEL:6}
	else:
		option_tags={GameTag.TECH_LEVEL:4}
	play = SetTag(TARGET, (GameTag.POISONOUS,))



## Choral Mrrrglr (Murloc) (6)
#BG26__Choral_Mrrrglr=(Config.BG_VERSION>=2620)#(6)
if BG26__Choral_Mrrrglr:# 
	BG_Minion_Murloc+=['BG26_354','BG26_354e']
	BG_Minion_Murloc+=['BG26_354_G']
	BG_PoolSet_Murloc.append('BG26_354')
	BG_Murloc_Gold['BG26_354']='BG26_354_G'
class BG26_354_Action(GameAction):#
	AMOUNT=IntArg()
	def do(self, source, amount):# 
		if len(source.controller.hand):
			atk=0
			hlt=0
			for card in source.controller.hand:
				if getattr(card, 'this_is_minion', False):
					atk += (card.atk*amount)
					hlt += (card.max_health*amount)
			if atk>0 or hlt>0:
				Buff(source, 'BG26_354e', atk=atk, max_health=hlt).trigger(source)
		pass# 
class BG26_354:# (minion)(murloc)
	""" Choral Mrrrglr
	<b>Start of Combat:</b> Gain the stats of all the minions in your hand. """
	events = BeginBattle(CONTROLLER).on(BG26_354_Action(1))
	pass
class BG26_354_G:# (minion)(murloc)
	""" Choral Mrrrglr
	<b>Start of Combat:</b> Gain the stats of all the minions in your hand twice. """
	events = BeginBattle(CONTROLLER).on(BG26_354_Action(2))
	pass


