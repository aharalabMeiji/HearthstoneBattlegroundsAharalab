
from ..utils import *

BG_Refreshing_Anomaly=True ## (1)
BG_Sellemental=True ## (1)
BG_Bubblette=(Config.BG_VERSION>=2400 and Config.BG_VERSION<2420) ## (1) ## new 24.0 banned 24.2

BG_Molten_Rock=True ## (2)
BG_Party_Elemental=True ## (2)
BG26__Flourishing_Frostling=(Config.BG_VERSION>=2620)#(2)

BG_Crackling_Cyclone=True ## (3)
BG_Smogger=True ## (3)
BG_Stasis_Elemental=False ## (3) ## banned when?
BG25__Felemental=(Config.BG_VERSION>=2522)# 3/3/1 elemental/demon ## new 25.2.2

BG_Dazzling_Lightspawn=True ## (4)
BG_Recycling_Wraith=True # (4)
BG_Wildfire_Elemental=True # (4)
BG26__Upbeat_Upstart=(Config.BG_VERSION>=2620)#(4)
BG26__Dancing_Barnstormer=(Config.BG_VERSION>=2620)#(4)

BG_Tavern_Tempest=True # (5)
BG_Lil_Rag=True # (5)
BG25__Magmaloc=(Config.BG_VERSION>=2522)# (5/1/1) murloc ## new 25.2.2
BG26__Gusty_Trumpeter=(Config.BG_VERSION>=2620)#(5)

BG_Gentle_Djinni=True # (6)
BG_Lieutenant_Garr=True # (6)
BG26__Elemental_of_Surprise=(Config.BG_VERSION>=2620)#(6)
BG26__Rock_Rock=(Config.BG_VERSION>=2620)#(6)


BG_Minion_Elemental =[]
BG_PoolSet_Elemental=[]
BG_Elemental_Gold={}

#Refreshing Anomaly(1)  ### OK ###
if BG_Refreshing_Anomaly: # 
	BG_Minion_Elemental+=['BGS_116','TB_BaconUps_167']
	BG_PoolSet_Elemental.append('BGS_116')
	BG_Elemental_Gold['BGS_116']='TB_BaconUps_167'
class BGS_116:# <12>[1453] 
	""" Refreshing Anomaly
	[Battlecry:] Your next [Refresh] costs (0). """
	play = GetFreeRerole(CONTROLLER)
	pass
class TB_BaconUps_167:# <12>[1453]
	""" Refreshing Anomaly
	[Battlecry:] Your next two [Refreshes] cost (0). """
	play = GetFreeRerole(CONTROLLER) * 2
	pass


#Sellemental(1)  ### OK ###
if BG_Sellemental: # 
	BG_Minion_Elemental+=['BGS_115','BGS_115t','TB_BaconUps_156']
	BG_PoolSet_Elemental.append('BGS_115')
	BG_Elemental_Gold['BGS_115']='TB_BaconUps_156'
class BGS_115:# <12>[1453] ウレメンタル
	""" Sellemental
	When you sell this,add a 2/2 Elementalto your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BGS_115t'))
	pass
class BGS_115t:# <12>[1453] おつりちゃん
	""" Water Droplet  
	 """
	pass
class TB_BaconUps_156:# <12>[1453]
	""" Sellemental
	When you sell this,add two 2/2 Elementalsto your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BGS_115t') * 2)
	pass

if BG_Bubblette:
	BG_Minion_Elemental+=['BG_TID_713','BG_TID_713_G']
	BG_PoolSet_Elemental.append('BG_TID_713')
	BG_Elemental_Gold['BG_TID_713']='BG_TID_713_G'
class BG_TID_713:#あわわわ ## banned 24.2
	""" Bubblette
	After this minion takes  exactly one damage, destroy it. <i>(Pop!)</i>"""
	events = Damage(SELF, 1).on(Destroy(SELF))
class BG_TID_713_G:#あわわわ
	""" Bubblette
	After this minion takes  exactly two damage, destroy it. <i>(Pop!)</i>"""
	events = Damage(SELF, 2).on(Destroy(SELF))


##### tavern tier 2


if BG_Molten_Rock: # 
#Molten Rock(2)  ### MAYBE ###
	BG_Minion_Elemental+=['BGS_127','BGS_127e','TB_Baconups_202','TB_Baconups_202e']
	BG_PoolSet_Elemental.append('BGS_127')
	BG_Elemental_Gold['BGS_127']='TB_Baconups_202'
class BGS_127:# <12>[1453] ようがん
	""" Molten Rock
	[Taunt]. After you play an Elemental, gain +1 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(SELF, 'BGS_127e'))
	pass
BGS_127e=buff(0,1)
class TB_Baconups_202:# <12>[1453]
	""" Molten Rock
	[Taunt]. After you play an Elemental, gain +2 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(SELF, 'TB_Baconups_202e'))
	pass
TB_Baconups_202e=buff(0,2)



if BG_Party_Elemental: # ## MAYBE ###
#Party Elemental(2)  #(2/4/2)
	BG_Minion_Elemental+=['BGS_120','BGS_120e','TB_BaconUps_160']
	BG_PoolSet_Elemental.append('BGS_120')
	BG_Elemental_Gold['BGS_120']='TB_BaconUps_160'
class BGS_120:# <12>[1453]
	""" Party Elemental
	After you play an Elemental, give another random friendly Elemental +1/+1. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(RANDOM(FRIENDLY_MINIONS + ELEMENTAL - SELF), 'BGS_120e'))
	pass
BGS_120e=buff(1,1)
class TB_BaconUps_160:# <12>[1453]
	""" Party Elemental
	After you play an Elemental, give another random friendly Elemental +1/+1 twice. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(RANDOM(FRIENDLY_MINIONS + ELEMENTAL - SELF), 'BGS_120e') * 2)
	pass



## Flourishing Frostling (Elemental) (2)
#BG26__Flourishing_Frostling=(Config.BG_VERSION>=2620)#(2)
if BG26__Flourishing_Frostling:# 
	BG_Minion_Elemental+=['BG26_537','BG26_537e','BG26_537pe']
	BG_Minion_Elemental+=['BG26_537_G']
	BG_PoolSet_Elemental.append('BG26_537')
	BG_Elemental_Gold['BG26_537']=''
class BG26_537_Action(GameAction):#
	AMOUNT=IntArg()
	def do(self, source,amount):# 
		source.controller.flourishing_frostling_powered_up += amount
		cards = [card for card in source.controller.field + source.controller.hand if isRaceCard(card, Race.ELEMENTAL)]
		for card in cards:
			Buff(card, 'BG26_537e', atk=source.controller.flourishing_frostling_powered_up).trigger(source)
		pass# 
class BG26_537:# (minion)
	""" Flourishing Frostling
	Has +1 Attack for each Elemental you played this ___game <i>(wherever this is)</i>. """
	play = BG26_537_Action(1)
	pass
class BG26_537e:
	pass
class BG26_537_G:# (minion)
	""" Flourishing Frostling
	Has +2 Attack for each Elemental you played this ___game <i>(wherever this is)</i>. """
	play = BG26_537_Action(2)
	pass



#### tavern tier 3


if BG_Crackling_Cyclone: # 
#Crackling Cyclone(3)   ### OK ###
	BG_Minion_Elemental+=['BGS_119','TB_BaconUps_159']
	BG_PoolSet_Elemental.append('BGS_119')
	BG_Elemental_Gold['BGS_119']='TB_BaconUps_159'
class BGS_119:# <12>[1453] ばりばり
	""" Crackling Cyclone
	[Divine Shield][Windfury] """
	pass
class TB_BaconUps_159:# <12>[1453]
	""" Crackling Cyclone
	[Divine Shield][Mega-Windfury] """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>
	pass


if BG_Smogger: # 
#Smogger(3)   ### need check ###
	BG_Minion_Elemental+=['BG21_021','BG21_021e','BG21_021_G',]
	BG_PoolSet_Elemental.append('BG21_021')
	BG_Elemental_Gold['BG21_021']='BG21_021_G'
class BG21_021:# <12>[1453]
	""" Smogger
	[Battlecry:] Give a friendly Elemental stats equal to your Tavern Tier. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE:Race.ELEMENTAL,
		}
	def play(self):
		source = self
		target = self.target
		controller = self.controller
		tier = controller.tavern_tier
		if target:
			Buff(target, 'BG21_021e', atk=tier, max_health=tier).trigger(controller)
		pass
	pass
class BG21_021e:# <12>[1453]
	""" Smogged
	Increased stats. """
	pass
class BG21_021_G:# <12>[1453]
	""" Smogger
	[Battlecry:] Give a friendly Elemental stats equal to_your Tavern Tier twice. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE:Race.ELEMENTAL,
		}
	def play(self):
		source = self
		target = self.target
		controller = self.controller
		tier = controller.tavern_tier
		if target:
			Buff(target, 'BG21_021e', atk=tier, max_health=tier).trigger(controller)
			Buff(target, 'BG21_021e', atk=tier, max_health=tier).trigger(controller)
		pass



#Stasis Elemental(3)   ### OK ###
if BG_Stasis_Elemental: # 
	BG_Minion_Elemental+=['BGS_122','TB_BaconUps_161']
	BG_PoolSet_Elemental.append('BGS_122')
	BG_Elemental_Gold['BGS_122']='TB_BaconUps_161'
class BGS_122:# <12>[1453] ###
	""" Stasis Elemental 
	[Battlecry:] Add another random Elemental to Bob's Tavern and [Freeze] it. """
	def play(self):
		bartender = self.controller.opponent
		tier = self.controller.tavern_tier
		elementals = []
		for cardID in cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental:
			cardxml = cards.db.get(cardID)
			if cardxml!=None:
				cardtier = cardxml.tags.get(GameTag.TECH_LEVEL)
				if 1<=cardtier and cardtier<=tier:
					elementals.append(cardID) 
		if 'BGS_122' in elementals:
			elementals.remove('BGS_122')
		if len(elementals)>0:
			newcard_id = random.choice(elementals)
			newcard = Summon(bartender,newcard_id).trigger(self)
			if newcard[0]==[]:
				return
			newcard[0][0].frozen=True
	pass
class TB_BaconUps_161:# <12>[1453]
	""" Stasis Elemental
	[Battlecry:] Add two other random Elementals to Bob's Tavern and [Freeze] them. """
	def play(self):
		bartender = self.controller.opponent
		tier = self.controller.tavern_tier
		elementals = []
		for cardID in cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental:
			cardxml = cards.db.get(cardID)
			if cardxml!=None:
				cardtier = cardxml.tags.get(GameTag.TECH_LEVEL)
				if 1<=cardtier and cardtier<=tier:
					elementals.append(cardID) 
		if 'BGS_122' in elementals:
			elementals.remove('BGS_122')
		if len(elementals)>0:		
			newcard_id = random.choice(elementals)
			newcard = Summon(bartender,newcard_id).trigger(self)
			if newcard[0]==[]:
				return
			newcard[0][0].frozen=True
			newcard_id = random.choice(elementals)
			newcard = Summon(bartender,newcard_id).trigger(self)
			if newcard[0]==[]:
				return
			newcard[0][0].frozen=True
	pass


if BG25__Felemental:# 3/3/1 elemental/demon ## new 25.2.2 ##
	BG_Minion_Elemental+=['BG25_041','BG25_041_G','BG25_041e','BG25_041e2']
	BG_PoolSet_Elemental.append('BG25_041')
	BG_Elemental_Gold['BG25_041']='BG25_041_G'
class BG25_041_Action(GameAction):
	def do(self, source):
		source.controller.felemental_powered_up+=1
class BG25_041:# (minion)
	""" Felemental
	<b>Battlecry:</b> Minions in Bob's Tavern have +1/+1 __for the rest of the game. """
	play = BG25_041_Action()
	pass
class BG25_041_G_Action(GameAction):
	def do(self, source):
		source.controller.felemental_powered_up+=2
class BG25_041_G:# (minion)
	""" Felemental
	<b>Battlecry:</b> Minions in Bob's Tavern have +2/+2 __for the rest of the game. """
	play = BG25_041_G_Action()
	pass
class BG25_041e:# (enchantment)
	""" Felfire Player Enchant
	Increased stats. """
	pass
class BG25_041e2:# (enchantment)
	""" Felementality
	Increased stats. """
	pass



#### tavern tier 4



#Dazzling Lightspawn(4) ### OK ###
if BG_Dazzling_Lightspawn: # 
	BG_Minion_Elemental+=['BG21_020','BG21_020e','BG21_020pe','BG21_020_G']
	BG_PoolSet_Elemental.append('BG21_020')
	BG_Elemental_Gold['BG21_020']='BG21_020_G'
class BG21_020_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		controller.lightspawn_powered_up += amount
		#buffsize=controller.lightspawn_powered_up
		#BG21_020pe.atk = lambda self,i:i+buffsize
		#BG21_020pe.max_health= lambda self,i:i+buffsize
class BG21_020:# <12>[1453] ライトスポーン
	""" Dazzling Lightspawn
	[Avenge (2):] Elementals inBob's Tavern have +1/+1__for the rest of the game. """
	events = Death(FRIENDLY).on(Avenge(SELF, 2, [BG21_020_Action(CONTROLLER, 1)]))
	pass
class BG21_020e:# <12>[1453]
	""" Dazzled
	Increased stats. """
	pass
BG21_020pe=buff(1,1)# <12>[1453]
""" Dazzling Lightspawn Player Enchant
Increased stats. """
class BG21_020_G:# <12>[1453]
	""" Dazzling Lightspawn
	[Avenge (2):] Elementals inBob's Tavern have +2/+2__for the rest of the game. """
	events = Death(FRIENDLY).on(Avenge(SELF, 2, [BG21_020_Action(CONTROLLER, 2)]))
	pass


#Recycling Wraith(4)   ### maybe ###
if BG_Recycling_Wraith: # 
	BG_Minion_Elemental+=['BG21_040','BG21_040_G']
	BG_PoolSet_Elemental.append('BG21_040')
	BG_Elemental_Gold['BG21_040']='BG21_040_G'
class BG21_040:# <12>[1453] レイス
	""" Recycling Wraith
	After you play an Elemental, your next [Refresh] costs (1) less. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(GetFreeRerole(CONTROLLER))
	pass
class BG21_040_G:# <12>[1453]
	""" Recycling Wraith
	After you play anElemental, your next two[Refreshes] cost (1) less. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(GetFreeRerole(CONTROLLER)*2)
	pass



#Wildfire Elemental(4) ### OK ###
if BG_Wildfire_Elemental: # 
	BG_Minion_Elemental+=['BGS_126','TB_BaconUps_166']
	BG_PoolSet_Elemental.append('BGS_126')
	BG_Elemental_Gold['BGS_126']='TB_BaconUps_166'
class BGS_126_Action(TargetedAction):
	TARGET = ActionArg()
	LVL = IntArg()
	def do(self, source, target, lvl):
		attacker = source
		defender = target
		adjacents = defender.adjacent_minions
		amount = attacker.atk - defender.health
		if amount>0 and len(adjacents)>0:
			if lvl==1:
				Hit(random.choice(adjacents), amount).trigger(source.controller)
			else:
				for card in adjacents:
					Hit(card, amount).trigger(source.controller)
class BGS_126:# <12>[1453]
	""" Wildfire Elemental
	After this attacks and kills a minion, deal excess damage to a random adjacent minion. """
	events = Attack(SELF, ENEMY_MINIONS).on(BGS_126_Action(Attack.DEFENDER, 1))
	pass
class TB_BaconUps_166:# <12>[1453]
	""" Wildfire Elemental
	After this attacks and killsa minion, deal excess damage to both adjacent minions. """
	events = Attack(SELF, ENEMY_MINIONS).on(BGS_126_Action(Attack.DEFENDER, 2))
	pass



## Upbeat Upstart (Elemental) (4)
#BG26__Upbeat_Upstart=(Config.BG_VERSION>=2620)#(4)
if BG26__Upbeat_Upstart:# 
	BG_Minion_Elemental+=['BG26_120','BG26_120e']
	BG_Minion_Elemental+=['BG26_120_G','BG26_120_Ge']
	BG_PoolSet_Elemental.append('BG26_120')
	BG_Elemental_Gold['BG26_120']='BG26_120_G'
class BG26_120_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		amount= max([card.max_health for card in controller.field])
		amount -= source.max_health
		if amount>0:
			Buff(source, 'BG26_120e').trigger(source)
		pass# 
class BG26_120:# (minion)
	""" Upbeat Upstart
	<b><b>Taunt</b>.</b> At the end of every 2 turns, set this minion's Health to the highest in your warband. <i>({0} |4(turn, turns) left!)</i>@"""
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="2"/>
	events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_120_Action()]))
	pass
class BG26_120e:
	""" """
	pass
class BG26_120_G_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		amount= max([card.max_health for card in controller.field])*2
		amount -= source.max_health
		if amount>0:
			Buff(source, 'BG26_120_Ge').trigger(source)
		pass# 
class BG26_120_G:# (minion)
	""" Upbeat Upstart
	<b><b>Taunt</b>.</b> At the end of every 2 turns, set this minion's Health to double the highest in your warband. <i>({0} |4(turn, turns) left!)</i></i> """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_120_G_Action()]))
	#
	pass
class BG26_120_Ge:
	""" """
	pass



## Dancing Barnstormer (Elemental) (4)
if BG26__Dancing_Barnstormer:# 
	BG_Minion_Elemental+=['BG26_162','BG26_162e','BG26_162pe']
	BG_Minion_Elemental+=['BG26_162_G']
	BG_PoolSet_Elemental.append('BG26_162')
	BG_Elemental_Gold['BG26_162']='BG26_162_G'
class BG26_162_Action(GameAction):# 
	AMOUNT=IntArg()
	def do(self, source, amount):#
		source.controller.dancing_barnstormer_powered_up += amount
		if source.controller.deepcopy_original!=None:
			source.controller.deepcopy_original.dancing_barnstormer_powered_up += amount
		pass# 
class BG26_162:# (minion)
	""" Dancing Barnstormer
	<b>Deathrattle:</b> Elementals in Bob's Tavern have +3/+2 __for the rest of the game. """
	deathrattle = BG26_162_Action(1)
	pass
class BG26_162e:
	pass
class BG26_162_G:# (minion)
	""" Dancing Barnstormer
	<b>Deathrattle:</b> Elementals in Bob's Tavern have +6/+4 __for the rest of the game. """
	deathrattle = BG26_162_Action(2)
	pass


#### tavern tier 5

#Tavern Tempest(5)   ### need check ###
if BG_Tavern_Tempest: # 
	BG_Minion_Elemental+=['BGS_123','TB_BaconUps_162']
	BG_PoolSet_Elemental.append('BGS_123')
	BG_Elemental_Gold['BGS_123']='TB_BaconUps_162'
class BGS_123:# <12>[1453] 逆巻き風
	""" Tavern Tempest
	[Battlecry:] Add another random Elemental to your hand. """
	def play(self):
		controller = self.controller
		tier = self.controller.tavern_tier
		elementals = []
		for cardID in cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental:
			cardxml = cards.db.get(cardID)
			if cardxml!=None:
				cardtier = cardxml.tags.get(GameTag.TECH_LEVEL)
				if 1<=cardtier and cardtier<=tier:
					elementals.append(cardID) 
		if 'BGS_123' in elementals:
			elementals.remove('BGS_123')
		if len(elementals):
			newcard_id = random.choice(elementals)
			Give(controller,newcard_id).trigger(self)
	pass
class TB_BaconUps_162:# <12>[1453]
	""" Tavern Tempest
	[Battlecry:] Add two other random Elementals to your hand. """
	def play(self):
		controller = self.controller
		tier = self.controller.tavern_tier
		elementals = []
		for cardID in cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental:
			cardxml = cards.db.get(cardID)
			if cardxml!=None:
				cardtier = cardxml.tags.get(GameTag.TECH_LEVEL)
				if 1<=cardtier and cardtier<=tier:
					elementals.append(cardID) 
		if 'BGS_123' in elementals:
			elementals.remove('BGS_123')
		if len(elementals):
			newcard_id = random.choice(elementals)
			Give(controller,newcard_id).trigger(self)
			newcard_id = random.choice(elementals)
			Give(controller,newcard_id).trigger(self)
	pass



#Lil' Rag (6->5, 24.0.3)   ### OK ###
if BG_Lil_Rag: # 
	BG_Minion_Elemental+=['BGS_100','BGS_100e','TB_BaconUps_200']
	BG_PoolSet_Elemental.append('BGS_100')
	BG_Elemental_Gold['BGS_100']='TB_BaconUps_200'
class BGS_100_Action(TargetedAction):
	TARGET = ActionArg()
	CARDS = CardArg()
	def do(self, source, target, cards):
		if not isinstance(cards, list):
			cards = [cards]
		controller = target
		tier = cards[0].tech_level
		if controller.field != []:
			card = random.choice(controller.field)
			Buff(card, 'BGS_100e', atk=tier, max_health=tier).trigger(source)
			pass
class BGS_100:# <12>[1453] チビラグ
	""" Lil' Rag
	After you play an Elemental,give a friendly minion stats equal to the Elemental's Tavern Tier. """
	if Config.BG_VERSION>=2403:
		option_tags={GameTag.TECH_LEVEL:5}
	else:
		option_tags={GameTag.TECH_LEVEL:6}
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_100_Action(CONTROLLER, BG_Play.CARD))
	pass
class BGS_100e:
	pass
class TB_BaconUps_200:# <12>[1453]
	""" Lil' Rag
	After you play an Elemental,give a friendly minion statsequal to the Elemental'sTavern Tier twice. """
	if Config.BG_VERSION>=2403:
		option_tags={GameTag.TECH_LEVEL:5}
	else:
		option_tags={GameTag.TECH_LEVEL:6}
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_100_Action(CONTROLLER, BG_Play.CARD)*2)
	pass



if BG25__Magmaloc:# 5/1/1 murloc ## new 25.2.2
	BG_Minion_Elemental+=['BG25_046','BG25_046e','BG25_046_G','BG25_046_Ge']
	BG_PoolSet_Elemental.append('BG25_046')
	BG_Elemental_Gold['BG25_046']='BG25_046_G'
class BG25_046_Action(GameAction):
	def do(self, source):
		amount = len([log for log in  source.controller._play_log if log.card.type==CardType.MINION and log.turn==source.controller.game.turn ])
		Buff(source, 'BG25_046e', atk=amount+1, max_health=amount+1).trigger(source)
class BG25_046:# (minion)(murloc)
	""" Magmaloc
	At the end of your turn, gain +1/+1. Repeat for each minion you played this turn. """
	events = OWN_TURN_END.on(BG25_046_Action())
	pass
class BG25_046e:# (enchantment)
	""" Magma!
	+1/+1. """
	#
	pass
class BG25_046_G_Action(GameAction):
	def do(self, source):
		amount = len([log for log in  source.controller._play_log if log.type==CardType.MINION and log.turn==source.controller.game.turn ])
		Buff(source, 'BG25_046_Ge', atk=2*amount+2, max_health=2*amount+2).trigger(source)
class BG25_046_G:# (minion)(murloc)
	""" Magmaloc
	At the end of your turn, gain +2/+2. Repeat for each minion you played this turn. """
	events = OWN_TURN_END.on(BG25_046_G_Action())
	pass
class BG25_046_Ge:# (enchantment)
	""" Magma!
	+2/+2. """
	#
	pass



## Gusty Trumpeter (Elemental) (5)
#BG26__Gusty_Trumpeter=(Config.BG_VERSION>=2620)#(5)
if BG26__Gusty_Trumpeter:# 
	BG_Minion_Elemental+=['BG26_534']
	BG_PoolSet_Elemental.append('BG26_534')
	BG_Elemental_Gold['BG26_534']=''
class BG26_534_Action(TargetedAction):# 
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):#
		if isRaceCard(target, Race.ELEMENTAL):
			source.script_data_num_1 -= 1
			if source.script_data_num_1==0:
				for repeat in range(amount):
					newcard=RandomBGElemental(tech_level_less=source.controller.tavern_tier).evaluate(source)
					newcard=get00(newcard)
					newcard.zone=Zone.SETASIDE
					newcard.controller=source.controller
					newcard.zone=Zone.HAND
				source.script_data_num_1=5
		pass# 
class BG26_534:# (minion)
	""" Gusty Trumpeter
	After you sell 5 Elementals, get another random Elemental. <i>(@ left!)</i> """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="5"/>
	events = Sell(CONTROLLER).after(BG26_534_Action(Sell.CARD, 1))
	pass

	BG_Minion_Elemental+=['BG26_534_G']
class BG26_534_G:# (minion)
	""" Gusty Trumpeter
	After you sell 5 Elementals, get two other random Elementals. <i>(@ left!)</i> """
	events = Sell(CONTROLLER).after(BG26_534_Action(Sell.CARD, 2))
	pass




#### tavern tier 6

#Gentle Djinni(6)   ### OK ###
if BG_Gentle_Djinni: # 
	BG_Minion_Elemental+=['BGS_121','TB_BaconUps_165']
	BG_PoolSet_Elemental.append('BGS_121')
	BG_Elemental_Gold['BGS_121']='TB_BaconUps_165'
class BGS_121_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		tier = controller.tavern_tier
		elementals = []
		for cardID in cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental:
			cardxml = cards.db.get(cardID)
			if cardxml!=None:
				cardtier = cardxml.tags.get(GameTag.TECH_LEVEL)
				if 1<=cardtier and cardtier<=tier:
					elementals.append(cardID) 
		if 'BGS_121' in elementals:
			elementals.remove('BGS_121')
		if len(elementals):
			for repeat in range(amount):
				newcard_id = random.choice(elementals)
				Summon(controller,newcard_id).trigger(source)
				if controller.deepcopy_original!=None:
					Give(controller.deepcopy_original, newcard_id).trigger(source)
	pass
class BGS_121:# <12>[1453] ランプの精
	""" Gentle Djinni
	[Taunt]. [Deathrattle:] Summon another random Elemental and add a copy of it to your hand. """
	deathrattle = BGS_121_Action(CONTROLLER, 1)
	pass
class TB_BaconUps_165:# <12>[1453]
	""" Gentle Djinni
	[Taunt]. [Deathrattle:] Summon two other random Elementals and add copies of them to your hand. """
	deathrattle = BGS_121_Action(CONTROLLER, 2)
	pass



# Lieutenant Garr (6)(8/8) ### HP OK ###
if BG_Lieutenant_Garr: # 
	BG_Minion_Elemental+=['BGS_124','BGS_124e','TB_BaconUps_163','TB_BaconUps_163e']
	BG_PoolSet_Elemental.append('BGS_124')
	BG_Elemental_Gold['BGS_124']='TB_BaconUps_163'
class BGS_124_Action(TargetedAction):
	TARGET = ActionArg()# SELF
	BUFF = ActionArg()#'BGS_124e'
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		#count = len([card for card in source.controller.field if card.race==Race.ELEMENTAL])
		count = len([card for card in source.controller.field if race_identity(card, Race.ELEMENTAL)])
		Buff(target, buff, max_health=count*amount).trigger(source)
class BGS_124: #
	""" Lieutenant Garr
	[Taunt]. After you play an Elemental, gain +1 Health for each Elemental you have """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).after(BGS_124_Action(SELF, 'BGS_124e', 1))
	pass
class BGS_124e:
	pass
class TB_BaconUps_163:
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).after(BGS_124_Action(SELF, 'TB_BaconUps_163e', 2))
	pass
class TB_BaconUps_163e:
	pass



## Elemental of Surprise (Elemental) (6)
#BG26__Elemental_of_Surprise=(Config.BG_VERSION>=2620)#(6)
if BG26__Elemental_of_Surprise:# 
	BG_Minion_Elemental+=['BG26_175']
	BG_Minion_Elemental+=['BG26_175_G']
	BG_PoolSet_Elemental.append('BG26_175')
	BG_Elemental_Gold['BG26_175']='BG26_175_G'
class BG26_175:# (minion)
	""" Elemental of Surprise
	<b>Divine Shield</b> This minion can triple with any Elemental. """
	#
	pass
class BG26_175_G:# (minion)
	""" Elemental of Surprise
	<b>Divine Shield</b> This minion can triple with any Elemental. """
	#
	pass



## Rock Rock (Elemental) (6)
#BG26__Rock_Rock=(Config.BG_VERSION>=2620)#(6)
if BG26__Rock_Rock:# 
	BG_Minion_Elemental+=['BG26_535','BG26_535e','BG26_535e2']
	BG_Minion_Elemental+=['BG26_535_G','BG26_535_Ge','BG26_535_Ge2']
	BG_PoolSet_Elemental.append('BG26_535')
	BG_Elemental_Gold['BG26_535']=''
class BG26_535_Action(GameAction):# 
	def do(self, source):# 
		if source.script_data_num_1!=0:
			source.script_data_num_1=0
			for card in source.controller.field:
				if card!=source:
					Buff(card, 'BG26_535e2').trigger(source)
		else:
			source.script_data_num_1=1
			for card in source.controller.field:
				if card!=source:
					Buff(card, 'BG26_535e').trigger(source)
		pass# 
class BG26_535:# (minion)
	""" Rock Rock
	After you play an Elemental, give your other minions +2 Attack. <i>(Swaps to Health next turn!)</i> """
	events = BG_Play(CONTROLLER, FRIENDLY+MINION+ELEMENTAL).after(BG26_535_Action())
	pass
BG26_535e=buff(2,0)
BG26_535e2=buff(0,2)
class BG26_535_G_Action(GameAction):# 
	def do(self, source):# 
		if source.script_data_num_1!=0:
			source.script_data_num_1=0
			for card in source.controller.field:
				if card!=source:
					Buff(card, 'BG26_535_Ge2').trigger(source)
		else:
			source.script_data_num_1=1
			for card in source.controller.field:
				if card!=source:
					Buff(card, 'BG26_535_Ge').trigger(source)
		pass# 
class BG26_535_G:# (minion)
	""" Rock Rock
	After you play an Elemental, give your other minions +4 Attack. <i>(Swaps to Health next turn!)</i> """
	events = BG_Play(CONTROLLER, FRIENDLY+MINION+ELEMENTAL).after(BG26_535_Action())
	pass
BG26_535_Ge=buff(4,0)
BG26_535_Ge2=buff(0,4)

