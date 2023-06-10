from ..utils import *

BG_Deck_Swabbie=(Config.BG_VERSION<2620) ## (1) ## banned 26.2
BG_Scallywag=True ##,1
BG26__Southsea_Busker=(Config.BG_VERSION>=2620)#(1)

BG_Freedealing_Gambler=True ##,2
BG_Southsea_Captain=(Config.BG_VERSION<2620) ##,2 ## banned 26.2
BG_Yo_Ho_Ogre=(Config.BG_VERSION<2522) ##,2 ## banned 25.2.2

BG_Briny_Bootlegger=(Config.BG_VERSION<2420) ##,3 banned 24.2
BG_Salty_Looter=(Config.BG_VERSION<2620) ##,3 ## banned 26.2
BG_Southsea_Strongarm=(Config.BG_VERSION<2620) ##,3 , ## banned 26.2
BG_First_Mate_Pip=(Config.BG_VERSION>=2420 and Config.BG_VERSION<2620) ##(3) new 24.2 ## banned 26.2
BG26__Gunpowder_Courier=(Config.BG_VERSION>=2620) # (3)
BGS_Bloodsail_Cannoneer=(Config.BG_VERSION>=2620) ## banned when? revive 26.2

BG_Goldgrubber=(Config.BG_VERSION<2620) ##,4 ## 26.2
BG_Peggy_Brittlebone=(Config.BG_VERSION<2522) ##,4  banned 25.2.2
BG25__Peggy_Sturdybone=(Config.BG_VERSION>=2522) ## ,4 new 25.2.2
BG_Ripsnarl_Captain=True ##,4
BG26__Lovesick_Balladist=(Config.BG_VERSION>=2620) # (4)
BG26__Blade_Collector=(Config.BG_VERSION>=2620) #(4)

BG_Cap_n_Hoggarr=(Config.BG_VERSION<2620) ##,5 ## banned 26.2
BG_Tony_Two_Tusk=(Config.BG_VERSION<2522) ##,5 ## banned 25.2.2
BG_Vanessa_VanCleef=(Config.BG_VERSION>=2460) ##, 5 ## new 24.6
BG26__Upbeat_Impressionist=(Config.BG_VERSION>=2620)#(5/8/4)
BG26__Record_Smuggler=(Config.BG_VERSION>=2620)#(5/7/6)
BG26__Underhanded_Dealer=(Config.BG_VERSION>=2620)#(4)->(5)

BG_Dread_Admiral_Eliza=(Config.BG_VERSION<2620) ##,6 ## banned 26.2
BG_Nosy_Looter=(Config.BG_VERSION<2460) ##,6 ### banned 24.6
BG26__Fleet_Admiral_Tethys=(Config.BG_VERSION>=2620)#(6/5/6)

BG_Minion_Pirate=[]

BG_PoolSet_Pirate=[]

BG_Pirate_Gold={}

## 25.2.2-
#Corpse Refiner 2/2/3/Pirate, Undead	Avenge (X)

#### TIER 1 ####

#Deck Swabbie,1,2,2,Pirate,Battlecry ### OK ### banned 26.2
if BG_Deck_Swabbie:
	BG_Minion_Pirate +=['BGS_055','TB_BaconUps_126']
	BG_PoolSet_Pirate.append('BGS_055')
	BG_Pirate_Gold['BGS_055']='TB_BaconUps_126'
class BGS_055:#
	""" Deck Swabbie <pirate>  (2/2)
	[Battlecry:] Reduce the cost of upgrading Bob's Tavern by (1). """
	play = ReduceTierUpCost(CONTROLLER,1)
	pass
class TB_BaconUps_126:
	""" Deck Swabbie <pirate>  (4/4)
	[Battlecry:] Reduce the cost of upgrading Bob's Tavern by (2). """
	play = ReduceTierUpCost(CONTROLLER,2)
	pass


#Scallywag,1,3,1,Pirate,Deathrattle  ### OK ###
if BG_Scallywag:
	BG_Minion_Pirate +=['BGS_061','BGS_061t','TB_BaconUps_141','TB_BaconUps_141t']
	BG_PoolSet_Pirate.append('BGS_061')
	BG_Pirate_Gold['BGS_061']='TB_BaconUps_141'
class BGS_061_Action(TargetedAction):
	TARGET=ActionArg()
	CARDID=ActionArg()
	def do(self, source, target, cardid):
		if getattr(source.game, 'this_is_battle', False):
			controller = target
			newcard=Summon(controller, cardid).trigger(controller)
			if newcard[0]==[]:
				return
			newcard=newcard[0][0]
			defenders = [card for card in newcard.attack_targets if card in controller.opponent.field]
			if len(defenders)>0:
				defender=random.choice(defenders)
				BG_Attack(newcard, defender).trigger(source)
				#source.game.process_deaths()#contained in BG_Attack
class BGS_061:# <12>[1453]
	""" Scallywag
	[Deathrattle:] Summon a 1/1 Pirate. It attacks immediately. """
	deathrattle = BGS_061_Action(CONTROLLER,'BGS_061t')
	#deathrattle = Summon(CONTROLLER, 'BGS_061t').then(BG_Attack(Summon.CARD,RANDOM_ENEMY_MINION))
	pass
class BGS_061t:# <7>[1453]
	""" Sky Pirate,	 """
class TB_BaconUps_141:# <12>[1453]
	""" Scallywag
	[Deathrattle:] Summon a 2/2 Pirate. It attacks immediately. """
	deathrattle = BGS_061_Action(CONTROLLER, 'TB_BaconUps_141t')
	pass
class TB_BaconUps_141t:# <7>[1453]
	""" Sky Pirate,	 """

from .BG_minion_quilboar import BG25__Thorncaptain
if BG25__Thorncaptain:# 1/4/2 quilboar/pirate ## new 25.2.2
	#BG_Minion_Pirate+=['BG25_045','BG25_045_G','BG25_045e','BG25_045e2']
	BG_PoolSet_Pirate.append('BG25_045')
	BG_Pirate_Gold['BG25_045']='BG25_045_G'



## Southsea Busker (Pirate) (1)
#BG26__Southsea_Busker=(Config.BG_VERSION>=2620)#(1)
if BG26__Southsea_Busker:# 
	BG_Minion_Pirate+=['BG26_135']
	BG_Minion_Pirate+=['BG26_135_G']
	BG_PoolSet_Pirate.append('BG26_135')
	BG_Pirate_Gold['BG26_135']='BG26_135_G'
class BG26_135_Action(GameAction):# 
	AMOUNT=IntArg()
	def do(self, source, amount):# 
		source.southsea_busker_powered_up=amount
		pass# 
class BG26_135:# (minion)
	""" Southsea Busker
	<b>Battlecry:</b> Gain 1 Gold next turn. """
	play = BG26_135_Action(1)
	pass

class BG26_135_G:# (minion)
	""" Southsea Busker
	<b>Battlecry:</b> Gain 2 Gold next turn. """
	play = BG26_135_Action(2)
	pass



#### tavern tier 2 ####

#Freedealing Gambler,2,3,3,Pirate,- ### OK ###
if BG_Freedealing_Gambler:
	BG_Minion_Pirate +=['BGS_049','TB_BaconUps_127']
	BG_PoolSet_Pirate.append('BGS_049')
	BG_Pirate_Gold['BGS_049']='TB_BaconUps_127'
class BGS_049:# <12>[1453]
	""" Freedealing Gambler
	This minion sells for 3 Gold. """
	#		<Tag enumID="1587" name="3" type="Int" value="3"/> # quiz tag
	pass
class TB_BaconUps_127:# <12>[1453]
	""" Freedealing Gambler
	This minion sells for 6 Gold. """
	#		<Tag enumID="1587" name="6" type="Int" value="6"/> #quiz tag
	pass



#Southsea Captain,2,3,3,Pirate,- ### OK ### banned 26.2
if BG_Southsea_Captain:
	BG_Minion_Pirate +=['BG_NEW1_027','NEW1_027e','TB_BaconUps_136','TB_BaconUps_136e']
	BG_PoolSet_Pirate.append('BG_NEW1_027')
	BG_Pirate_Gold['BG_NEW1_027']='TB_BaconUps_136'
class BG_NEW1_027:
	""" Southsea Captain
	Your other Pirates have +1/+1. """
	update = Refresh(FRIENDLY_MINIONS + PIRATE - SELF, buff="NEW1_027e")
	pass
NEW1_027e=buff(1,1)
class TB_BaconUps_136:
	""" Southsea Captain
	Your other Pirates have +2/+2. """
	update = Refresh(FRIENDLY_MINIONS + PIRATE - SELF, buff="TB_BaconUps_136e")
	pass
TB_BaconUps_136e = buff(+2, +2)



#Yo-Ho-Ogre,2/3/5,Pirate,Taunt  ### OK ###
if BG_Yo_Ho_Ogre:# 2/3/6 24.2.2
	BG_Minion_Pirate +=['BGS_060','TB_BaconUps_150']
	BG_PoolSet_Pirate.append('BGS_060')
	BG_Pirate_Gold['BGS_060']='TB_BaconUps_150'
class BGS_060_Action(GameAction):
	TARGET=ActionArg()# target=source
	def do(self, source):
		target=source
		##Deaths().trigger(source)## contained in BG_Attack.after
		if len(source.controller.opponent.field)>0 and target.alive:
			defender=random.choice(source.controller.opponent.field)
			print("%s attacks %s"%(target,defender))
			BG_Attack(target, defender).trigger(source.controller)
			##Deaths().trigger(source.controller)## contained in BG_Attack
class BGS_060:# <12>[1453]
	""" Yo-Ho-Ogre
	[Taunt]After this minion survives being attacked, attack immediately. """
	events = BG_Attack(ENEMY, SELF).after(BGS_060_Action())
	pass
class TB_BaconUps_150:# <12>[1453]
	""" Yo-Ho-Ogre (2/6/10)
	[Taunt]After this minion survives being attacked, attack immediately. """
	events = BG_Attack(ENEMY_MINIONS, SELF).after(BGS_060_Action()) 
	pass


from .BG_minion_undead import BG25__Corpse_Refiner
if BG25__Corpse_Refiner:# 2/2/3 undead/pirate ## new 25.2.2
	##BG_Minion_Pirate+=['BG25_033','BG25_033_G']  ## no need
	BG_PoolSet_Pirate+=['BG25_033']
	BG_Pirate_Gold['BG25_033']='BG25_033_G'



############ tavern tier 3

#Briny Bootlegger,3,4,4,Pirate,- ### OK ### banned 24.2
if BG_Briny_Bootlegger:
	BG_Minion_Pirate +=['BG21_017','BG21_017_G']
	BG_PoolSet_Pirate.append('BG21_017')
	BG_Pirate_Gold['BG21_017']='BG21_017_G'
class BG21_017_Action(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		controller = target.controller#
		field = controller.field
		for card in field:
			#if card != target and card.race==Race.PIRATE:
			if card != target and race_identity(card,Race.PIRATE):
				for repeat in range(amount):
					Give(controller, 'GAME_005').trigger(controller)
				return
class BG21_017:# <12>[1453]
	""" Briny Bootlegger
	At the end of your turn,if you have another Pirate,add a Gold Coin to your hand. """
	events = OWN_TURN_END.on(BG21_017_Action(SELF, 1))
	#events = OWN_TURN_END.on(Find(FRIENDLY_MINIONS - SELF + PIRATE) & Give(CONTROLLER, "GAME_005"))
	pass
class BG21_017_G:# <12>[1453]
	""" Briny Bootlegger
	At the end of your turn,if you have another Pirate,add 2 Gold Coins to your hand. """
	events = OWN_TURN_END.on(BG21_017_Action(SELF, 2))
	pass



#Salty Looter,3,4,5,Pirate,- ### OK ### banned 26.2
if BG_Salty_Looter:
	BG_Minion_Pirate +=['BGS_081','BGS_081e','TB_BaconUps_143','TB_BaconUps_143e']
	BG_PoolSet_Pirate.append('BGS_081')
	BG_Pirate_Gold['BGS_081']='TB_BaconUps_143'
class BGS_081:# <7>[1453]
	""" Salty Looter
	Whenever you play a Pirate, gain +1/+1. """
	events = BG_Play(CONTROLLER, PIRATE).on(Buff(SELF,'BGS_081e'))
	pass
BGS_081e=buff(1,1)
class TB_BaconUps_143:# <7>[1453]
	""" Salty Looter
	Whenever you play a Pirate, gain +2/+2. """
	events = BG_Play(CONTROLLER, PIRATE).on(Buff(SELF,'TB_BaconUps_143e'))
	pass
TB_BaconUps_143e=buff(2,2)



#Southsea Strongarm,3,4,3,Pirate,Battlecry  ### OK ### banned 26.2
if BG_Southsea_Strongarm:
	BG_Minion_Pirate +=['BGS_048','BGS_048e','TB_BaconUps_140','TB_BaconUps_140e']
	BG_PoolSet_Pirate.append('BGS_048')
	BG_Pirate_Gold['BGS_048']='TB_BaconUps_140'
class BGS_048:# <12>[1453]
	""" Southsea Strongarm
	[Battlecry:] Give a friendly Pirate +1/+1. Repeat foreach Pirate you bought this turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.PIRATE }
	def play(self):
		count=1
		log = self.controller.buy_this_turn_log()
		for card in log:
			if race_identity(card,Race.PIRATE):
				count += 1
		for repeat in range(count):
			Buff(self.target, 'BGS_048e').trigger(self.controller)
	pass
BGS_048e=buff(1,1)
class TB_BaconUps_140:# <12>[1453]
	""" Southsea Strongarm
	[Battlecry:] Give a friendly Pirate +2/+2. Repeat foreach Pirate you boughtthis turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.PIRATE }
	def play(self):
		count=1
		log = self.controller.buy_this_turn_log()
		for card in log:
			if race_identity(card,Race.PIRATE):
				count += 1
		for repeat in range(count):
			#yield Buff(TARGET, 'TB_BaconUps_140e')
			Buff(self.target, 'TB_BaconUps_140e').trigger(self.controller)
	pass
TB_BaconUps_140e=buff(2,2)


## First Mate Pip (3) ### BG23_192 ####### banned 26.2
if BG_First_Mate_Pip: ##(3) new 24.2
	BG_Minion_Pirate +=['BG23_192','BG23_192_G']
	BG_PoolSet_Pirate.append('BG23_192')
	BG_Pirate_Gold['BG23_192']='BG23_192_G'
class BG23_192:
	""" First Mate Pip (3)
	You only need 2 copies of this minion to make it Golden. """
	pass
class BG23_192_G:
	""" First Mate Pip (3)
	<i>(Only 2 copies of this minion were needed to make it Golden.)</i>"""
	pass



## Gunpowder Courier (Pirate) (3)
#BG26__Gunpowder_Courier=(Config.BG_VERSION>=2620) # (3)
if BG26__Gunpowder_Courier:# 
	BG_Minion_Pirate+=['BG26_810','BG26_810e']
	BG_Minion_Pirate+=['BG26_810_G','BG26_810_Ge']
	BG_PoolSet_Pirate.append('BG26_810')
	BG_Pirate_Gold['BG26_810']='BG26_810_G'
class BG26_810_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_810_Action(GameAction):
	"""
	AMOUNT = IntArg() #
	"""
	AMOUNT = IntArg() #spent mana
	BUFF=ActionArg()
	def get_target_args(self, source):
		amount = self._args[1]
		bf = self._args[2]
		return [amount, bf]

	def do(self, source, amount, buff):
		triggeramount=5
		if amount==1:#buy a minion
			spent=source.controller.game.minionCost
		elif amount==2:# rerole
			spent=source.controller.game.reroleCost
		else:# upgrade
			spent=source.controller.tavern_tierup_cost
		source.sidequest_counter += spent
		source.script_data_num_1 = triggeramount - source.sidequest_counter
		if source.sidequest_counter>= triggeramount:
			## trigger action
			source.sidequest_counter -= triggeramount
			for card in source.controller.field:
				if isRaceCard(card, Race.PIRATE):
					Buff(card, buff).trigger(source)
class BG26_810:# (minion)
	""" Gunpowder Courier
	After you spend 5 Gold, give your Pirates +1 Attack. <i>(@ Gold left!)</i> """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="5"/>
	tags={GameTag.TAG_SCRIPT_DATA_NUM_1:5}
	events = [Buy(CONTROLLER).after(BG26_810_Action(1,'BG26_810e')), 
		   Rerole(CONTROLLER).after(BG26_810_Action(2,'BG26_810e')), 
		   UpgradeTier(CONTROLLER).after(BG26_810_Action(3,'BG26_810e'))]
	pass
BG26_810e=buff(1,0)
class BG26_810_G:# (minion)
	""" Gunpowder Courier
	After you spend 5 Gold, give your Pirates +2 Attack. <i>(@ Gold left!)</i> """
	#
	tags={GameTag.TAG_SCRIPT_DATA_NUM_1:5}
	events = [Buy(CONTROLLER).after(BG26_810_Action(1,'BG26_810_Ge')), 
		   Rerole(CONTROLLER).after(BG26_810_Action(2,'BG26_810_Ge')), 
		   UpgradeTier(CONTROLLER).after(BG26_810_Action(3,'BG26_810_Ge'))]	
	pass
BG26_810_Ge=buff(2,0)


## Bloodsail Cannoneer (pirate ) (3/4/3)
if BGS_Bloodsail_Cannoneer: ## banned when? revive 26.2
	BG_Minion_Pirate+=['BGS_053','BGS_053e']
	BG_Minion_Pirate+=['TB_BaconUps_138','TB_BaconUps_138e']
	BG_PoolSet_Pirate.append('BGS_053')
	BG_Pirate_Gold['BGS_053']='TB_BaconUps_138'
class BGS_053:
	""" Bloodsail Cannoneer
	&lt;b&gt;Battlecry&lt;/b&gt;: Give your other Pirates +3 Attack."""
	play = Buff(FRIENDLY_MINIONS + PIRATE, 'BGS_053e')
	pass
BGS_053e=buff(3,0)
class TB_BaconUps_138:
	""" Bloodsail Cannoneer
	&lt;b&gt;Battlecry&lt;/b&gt;: Give your other Pirates +6 Attack. """
	play = Buff(FRIENDLY_MINIONS + PIRATE, 'TB_BaconUps_138e')
	pass
TB_BaconUps_138e=buff(6,0)

#### TIER 4 ####


#Goldgrubber,4,4,4,Pirate,- 金ぴか ### OK ### banned 26.2
if BG_Goldgrubber:
	BG_Minion_Pirate +=['BGS_066','BGS_066e','TB_BaconUps_130','TB_BaconUps_130e']
	BG_PoolSet_Pirate.append('BGS_066')
	BG_Pirate_Gold['BGS_066']='TB_BaconUps_130'
class BGS_066_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target
		count=0
		for card in controller.field:
			if card.BG_is_gold:## that is, it is gold
				count += 1
		for repeat in range(count):
			Buff(source, buff).trigger(controller)
		pass
class BGS_066:# <12>[1453] 
	""" Goldgrubber
	At the end of your turn, gain +2/+2 for each friendly Golden minion. """
	events = OWN_TURN_END.on(BGS_066_Action(CONTROLLER, 'BGS_066e'))
	#events = OWN_TURN_END.on(Buff(SELF, 'BGS_066e')*Count(FRIENDLY + GOLDEN))
	pass
BGS_066e=buff(2,2)
class TB_BaconUps_130:# <12>[1453]
	""" Goldgrubber
	At the end of your turn, gain +4/+4 for each friendly Golden minion. """
	events = OWN_TURN_END.on(BGS_066_Action(CONTROLLER, 'TB_BaconUps_130e'))
	pass
TB_BaconUps_130e=buff(4,4)



#Peggy Brittlebone,4,6,5,Pirate,- ### OK ###
if BG_Peggy_Brittlebone:
	BG_Minion_Pirate +=['BG21_016','BG21_016e','BG21_016_G','BG21_016_Ge']
	BG_PoolSet_Pirate.append('BG21_016')
	BG_Pirate_Gold['BG21_016']='BG21_016_G'
class BG21_016:# <12>[1453] 義足
	""" Peggy Brittlebone
	After a card is added to your hand, give another friendly Pirate +1/+1. """
	events = [
		Buy(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG21_016e')),
		Give(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG21_016e')),
		]
	pass
BG21_016e=buff(1,1)
class BG21_016_G:# <12>[1453]
	""" Peggy Brittlebone
	After a card is added to your hand, give another friendly Pirate +2/+2. """
	events = [
		Buy(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG21_016_Ge')),
		Give(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG21_016_Ge')),
		]
	pass
BG21_016_Ge=buff(2,2)



if BG25__Peggy_Sturdybone:# 
	BG_Minion_Pirate+=['BG25_032','BG25_032_G','BG25_032_Ge','BG25_032e']
	BG_PoolSet_Pirate.append('BG25_032')
	BG_Pirate_Gold['BG25_032']='BG25_032_G'
class BG25_032:# (minion) 4/6/5 -> 4/4/2
	""" Peggy Sturdybone
	After a card is added to your hand, give another friendly Pirate +1/+1. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:2}
	else:
		option_tags={GameTag.ATK:6, GameTag.HEALTH:5}

	events = [
		Buy(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG25_032e')),
		Give(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG25_032e')),
		]
	pass
BG25_032e=buff(1,1)# (enchantment)
""" Loot Get	+1/+1. """
class BG25_032_G:# (minion)
	""" Peggy Sturdybone
	After a card is added to your hand, give another friendly Pirate +2/+2. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:8, GameTag.HEALTH:4}
	else:
		option_tags={GameTag.ATK:12, GameTag.HEALTH:10}
	events = [
		Buy(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG25_032_Ge')),
		Give(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS + PIRATE - SELF), 'BG25_032_Ge')),
		]
	pass
BG25_032_Ge=buff(2,2)# (enchantment)
""" Loot Get	+2/+2. """


#Ripsnarl Captain,4,4,6,Pirate,- ### OK ###
if BG_Ripsnarl_Captain:
	BG_Minion_Pirate +=['BGS_056','BGS_056e','TB_BaconUps_139','TB_BaconUps_139e']
	BG_PoolSet_Pirate.append('BGS_056')
	BG_Pirate_Gold['BGS_056']='TB_BaconUps_139'
class BGS_056:# <12>[1453] ギリガルル
	""" Ripsnarl Captain
	Whenever a friendly Pirate attacks, give it +3 Attack.""" ### new 2620
	##Whenever another friendly Pirate attacks, give it +3/+3. ## renew 2522
	##Whenever another friendly Pirate attacks, give it +2/+2. """ ## very old
	if Config.BG_VERSION>=2620:
		events = BG_Attack(FRIENDLY + PIRATE).on(Buff(BG_Attack.TARGET,'BGS_056e'))
	else:
		events = BG_Attack(FRIENDLY + PIRATE - SELF).on(Buff(BG_Attack.TARGET,'BGS_056e'))
	pass
if Config.BG_VERSION>=2620:
	BGS_056e=buff(3,0)
elif Config.BG_VERSION>=2522:
	BGS_056e=buff(3,3)
else:
	BGS_056e=buff(2,2)
class TB_BaconUps_139:# <12>[1453]
	""" Ripsnarl Captain
	Whenever another friendly Pirate attacks, give it +4/+4. """
	if Config.BG_VERSION>=2620:
		events = BG_Attack(FRIENDLY + PIRATE).on(Buff(BG_Attack.TARGET,'TB_BaconUps_139e'))
	else:
		events = BG_Attack(FRIENDLY + PIRATE - SELF).on(Buff(BG_Attack.TARGET,'TB_BaconUps_139e'))
	pass
if Config.BG_VERSION>=2620:
	TB_BaconUps_139e=buff(6,0)
elif Config.BG_VERSION>=2522:
	TB_BaconUps_139e=buff(6,6)
else:
	TB_BaconUps_139e=buff(4,4)


## Lovesick Balladist (Pirate) (4)
#BG26__Lovesick_Balladist=(Config.BG_VERSION>=2620) # (4)
if BG26__Lovesick_Balladist:# 
	BG_Minion_Pirate+=['BG26_814','BG26_814e']
	BG_Minion_Pirate+=['BG26_814_G']
	BG_PoolSet_Pirate.append('BG26_814')
	BG_Pirate_Gold['BG26_814']='BG26_814_G'
class BG26_814_Action(TargetedAction):# 
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):# 
		if target!=None and getattr(target, 'this_is_minion'):
			amount = source.controller.spentmoney_in_this_turn * amount
			for card in source.controller.field:
				if isRaceCard(card, Race.PIRATE):
					Buff(card, 'BG26_814e', atk=amount).trigger(source)
		pass# 
class BG26_814:# (minion)
	""" Lovesick Balladist
	<b>Battlecry:</b> Give a Pirate +1 Health for each Gold spent this turn. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = BG26_814_Action(TARGET, 1)
	pass
class BG26_814e:
	""" """
	pass
class BG26_814_G:# (minion)
	""" Lovesick Balladist
	<b>Battlecry:</b> Give a Pirate +2 Health for each Gold spent this turn. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = BG26_814_Action(TARGET, 2)
	pass



## Blade Collector (Pirate) (4)
#BG26__Blade_Collector=(Config.BG_VERSION>=2620) #(4)
if BG26__Blade_Collector:# 
	BG_Minion_Pirate+=['BG26_817']
	BG_Minion_Pirate+=['BG26_817_G']
	BG_PoolSet_Pirate.append('BG26_817')
	BG_Pirate_Gold['BG26_817']='BG26_817_G'
class BG26_817_Action(TargetedAction):# 
	TARGET=ActionArg()
	def do(self, source, target):# 
		enemy_field=source.controller.opponent.field
		if target in enemy_field:
			amount = source.atk
			index=enemy_field.index(target)
			if index>0:
				Hit(enemy_field[index-1], amount)
			if index<len(enemy_field)-1:
				Hit(enemy_field[index+1], amount)
		pass# 
class BG26_817:# (minion)
	""" Blade Collector
	Also damages the minions next to whomever this attacks. """
	events = BG_Attack(SELF).on(BG26_817_Action(BG_Attack.OTHER))
	pass
class BG26_817_G:# (minion)
	""" Blade Collector
	Also damages the minions next to whomever this attacks. """
	events = BG_Attack(SELF).on(BG26_817_Action(BG_Attack.OTHER))
	pass




#### TIER 5 ####

#Cap'n Hoggarr,5,6,6,Pirate,- ### OK ### banned 26.2
if BG_Cap_n_Hoggarr:
	BG_Minion_Pirate +=['BGS_072','TB_BaconUps_133']
	BG_PoolSet_Pirate.append('BGS_072')
	BG_Pirate_Gold['BGS_072']='TB_BaconUps_133'
class BGS_072:# <12>[1453] ホガァ
	""" Cap'n Hoggarr
	Whenever you buy a Pirate,gain 1 Gold this turn only. """
	events = Buy(CONTROLLER, MINION + PIRATE).on(ManaThisTurn(CONTROLLER, 1))
	pass
class TB_BaconUps_133:# <12>[1453]
	""" Cap'n Hoggarr
	Whenever you buy a Pirate, gain 2 Gold this turn only. """
	events = Buy(CONTROLLER, MINION + PIRATE).on(ManaThisTurn(CONTROLLER, 2))
	pass



#Tony Two-Tusk,5,4,6,Pirate,Avenge (X) ### OK ###
if BG_Tony_Two_Tusk:
	BG_Minion_Pirate +=['BG21_031','BG21_031_G']
	BG_PoolSet_Pirate.append('BG21_031')
	BG_Pirate_Gold['BG21_031']='BG21_031_G'
class BG21_031_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		for repeat in range(amount):
			friendly_pirates=[]
			for card in controller.field:
				#if card.race==Race.PIRATE:
				if race_identity(card,Race.PIRATE):
					if hasattr(card, 'gold_card') and card.gold_card != 0 and card != source:
						friendly_pirates.append(card)
			if len(friendly_pirates)>0:
				card = random.choice(friendly_pirates)
				original_card = card.deepcopy_original
				new_card = controller.game.BG_morph_gold(card)
				new_original_card = original_card.controller.game.BG_morph_gold(original_card)
		pass
class BG21_031:# <12>[1453]
	""" Tony Two-Tusk
	[Avenge (4):] Make another friendly Pirate Golden permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [BG21_031_Action(CONTROLLER, 1)]))
	pass
class BG21_031_G:# <12>[1453]
	""" Tony Two-Tusk
	[Avenge (4):] Make 2 other friendly Pirates Golden permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [BG21_031_Action(CONTROLLER, 2)]))
	pass


#Vanessa VanCleef( parate 5, BG24_708)### OK ###
if BG_Vanessa_VanCleef:
	BG_Minion_Pirate +=['BG24_708','BG24_708e','BG24_708_G','BG24_708e_G']
	BG_PoolSet_Pirate.append('BG24_708')
	BG_Pirate_Gold['BG24_708']='BG24_708_G'
class BG24_708:
	""" Vanessa VanCleef (3/7)
	Whenever this attacks, give your Pirates +2/+1 permanently.""" ##new 26.2
	#Whenever this attacks, give your Pirates +2/+2 permanently.
	events = Attack(SELF, ENEMY).on(BuffPermanently(FRIENDLY_MINIONS + PIRATE, 'BG24_708e'))
	pass
if Config.BG_VERSION>=2620:
	BG24_708e=buff(2,1)
else:
	BG24_708e=buff(2,2)
class BG24_708_G:
	""" Vanessa VanCleef
	Whenever this attacks, give your Pirates +4/+2 permanently."""
	events = Attack(SELF, ENEMY).on(BuffPermanently(FRIENDLY_MINIONS + PIRATE, 'BG24_708e_G'))
if Config.BG_VERSION>=2620:
	BG24_708e_G=buff(4,2)
else:
	BG24_708e_G=buff(2,2)



## Upbeat Impressionist (Pirate) (5)
#BG26__Upbeat_Impressionist=(Config.BG_VERSION>=2620)#(5)
if BG26__Upbeat_Impressionist:# 
	BG_Minion_Pirate+=['BG26_124']
	BG_Minion_Pirate+=['BG26_124_G']
	BG_PoolSet_Pirate.append('BG26_124')
	BG_Pirate_Gold['BG26_124']='BG26_124_G'
class BG26_124_Action(GameAction):# 
	amount=IntArg()
	def do(self, source, amount):# 
		cards=[card for card in source.controller.hand if isRaceCard(card, Race.PIRATE) and not card.BG_is_gold]
		if len(cards)==1 and amount==2:
			amount=1
		if len(cards)>=amount:
			cards = random.sample(cards, amount)
			controller=source.controller
			for card in cards:
				index = controller.hand.index(card)
				gold_id = controller.game.parent.BG_Gold[card.id]
				if not gold_id:
					return
				buffs=[]
				for buff in card.buffs:## inferit buffs
					buffs.append(buff)
				card.zone=Zone.GRAVEYARD
				newcard = controller.card(gold_id)
				for buff in buffs:## inferit buffs
					buff.apply(newcard)
				newcard._summon_index=index
				newcard.zone = Zone.HAND #
				newcard.gold_original = card
		pass# 
class BG26_124:# (minion)
	""" Upbeat ImpressionistGame_005
	At the end of every 2 turns, make a random Pirate in your hand Golden. <i>({0} |4(turn, turns) left!)</i>@
	At the end of every 2 turns, make a random Pirate in your hand Golden. <i>(End of this turn!)</i> """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_124_Action(1)]))
	pass
class BG26_124_G:# (minion)
	""" Upbeat Impressionist
	At the end of every 2 turns, make 2 random Pirates in your hand Golden. <i>({0} |4(turn, turns) left!)</i>@
	At the end of every 2 turns, make 2 random Pirates in your hand Golden. <i>(End of this turn!)</i> """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_124_Action(2)]))#
	pass



## Record Smuggler (Pirate) (5)
#BG26__Record_Smuggler=(Config.BG_VERSION>=2620)#(5)
if BG26__Record_Smuggler:# 
	BG_Minion_Pirate+=['BG26_812']
	BG_Minion_Pirate+=['BG26_812_G']
	BG_PoolSet_Pirate.append('BG26_812')
	BG_Pirate_Gold['BG26_812']='BG26_812_G'
class BG26_812_Action(GameAction):# 
	AMOUNT=IntArg()
	def do(self, source, amount):# 
		cards = [card for card in source.controller.field if isRaceCard(card, Race.PIRATE)]
		for repeat in range(len(cards)*amount):
			Give(source.controller, 'GAME_005').trigger(source)
		pass# 
class BG26_812:# (minion)
	""" Record Smuggler
	At the start of your turn, gain 1 Gold. Repeat for each other friendly Pirate. """
	if Config.BG_VERSION>=2622:	
		option_tags={GameTag.ATK:5, GameTag.HEALTH:4}
	else:
		option_tags={GameTag.ATK:7, GameTag.HEALTH:6}

	events = BeginBar(CONTROLLER).on(BG26_812_Action(1))
	pass
class BG26_812_G:# (minion)
	""" Record Smuggler
	At the start of your turn, gain 2 Gold. Repeat for each other friendly Pirate. """
	if Config.BG_VERSION>=2622:	
		option_tags={GameTag.ATK:10, GameTag.HEALTH:8}
	else:
		option_tags={GameTag.ATK:14, GameTag.HEALTH:12}
	events = BeginBar(CONTROLLER).on(BG26_812_Action(2))
	pass


## Underhanded Dealer (Pirate) (4)->(5)
#BG26__Underhanded_Dealer=(Config.BG_VERSION>=2620)#(4)->(5)
if BG26__Underhanded_Dealer:# 
	BG_Minion_Pirate+=['BG26_815','BG26_815e']
	BG_Minion_Pirate+=['BG26_815_G','BG26_815_Ge']
	BG_PoolSet_Pirate.append('BG26_815')
	BG_Pirate_Gold['BG26_815']='BG26_815_G'
class BG26_815:# (minion)
	""" Underhanded Dealer
	After you gain Gold, gain +1/+1. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.TECH_LEVEL:5, GameTag.ATK:4, GameTag.HEALTH:4}
	elif Config.BG_VERSION>=2620:
		option_tags={GameTag.TECH_LEVEL:4, GameTag.ATK:2, GameTag.HEALTH:2}
	events = Give(CONTROLLER, ID('GAME_005')).on(Buff(SELF, 'BG26_815e'))
	pass
BG26_815e=buff(1,1)
class BG26_815_G:# (minion)
	""" Underhanded Dealer
	After you gain Gold, gain +2/+2. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.TECH_LEVEL:5, GameTag.ATK:8, GameTag.HEALTH:8}
	elif Config.BG_VERSION>=2620:
		option_tags={GameTag.TECH_LEVEL:4, GameTag.ATK:4, GameTag.HEALTH:4}
	events = Give(CONTROLLER, ID('GAME_005')).on(Buff(SELF, 'BG26_815_Ge'))
	pass
BG26_815_Ge=buff(2,2)


###### TIER 6 ######


#Dread Admiral Eliza,6,6,7,Pirate,- ### OK ### banned 26.2
if BG_Dread_Admiral_Eliza:
	BG_Minion_Pirate +=['BGS_047','BGS_047e','TB_BaconUps_134','TB_BaconUps_134e']
	BG_PoolSet_Pirate.append('BGS_047')
	BG_Pirate_Gold['BGS_047']='TB_BaconUps_134'
class BGS_047:# <12>[1453]  イライザ
	""" Dread Admiral Eliza
	Whenever a friendly Pirate attacks, give all friendly minions +2/+1. """
	events = Attack(FRIENDLY + PIRATE).on(Buff(FRIENDLY_MINIONS,'BGS_047e'))
	pass
BGS_047e=buff(2,1)
class TB_BaconUps_134:# <12>[1453]
	""" Dread Admiral Eliza
	Whenever a friendly Pirate attacks, give all friendly minions +4/+2. """
	events = Attack(FRIENDLY + PIRATE).on(Buff(FRIENDLY_MINIONS,'TB_BaconUps_134e'))
	pass
TB_BaconUps_134e=buff(4,2)




#Nosy Looter,6,9,8,Pirate,-  ### OK ### banned 24.6
if BG_Nosy_Looter:
	BG_Minion_Pirate +=['BG21_019','BG21_019_G']
	BG_PoolSet_Pirate.append('BG21_019')
	BG_Pirate_Gold['BG21_019']='BG21_019_G'
class BG21_019_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		decks = controller.game.parent.BG_decks
		dk=[]
		for i in range(1, controller.tavern_tier+1):
			dk += decks[i]
		for repeat in range(amount):
			cardID = random.choice(dk)
			controller.game.BG_deal_gold(cardID)
		pass
class BG21_019:# <12>[1453] 戦利品詮索屋
	""" Nosy Looter
	Every two turns,add a random Golden minion to your hand.<i>(@ |4(turn, turns) left!)</i> """
	events = BeginBar(CONTROLLER).on(SidequestCounter(SELF, 2, [BG21_019_Action(CONTROLLER,1)]))
	pass
class BG21_019_G:# <12>[1453]
	""" Nosy Looter
	At the start of your turn,add a random Golden minion to your hand. """
	events = BeginBar(CONTROLLER).on(SidequestCounter(SELF, 2, [BG21_019_Action(CONTROLLER,2)]))
	pass

from .BG_minion_naga import BG25__Greta_Gold_Gun
if BG25__Greta_Gold_Gun:# 6/2/9 naga/pirate ## new 25.2.2### banned 26.2
	#BG_Minion_Pirate+=['BG25_044','BG25_044_G','BG25_044e2','BG25_044t']
	BG_PoolSet_Pirate.append('BG25_044')
	BG_Pirate_Gold['BG25_044']='BG25_044_G'

	
## Fleet Admiral Tethys (Pirate) (6)
#BG26__Fleet_Admiral_Tethys=(Config.BG_VERSION>=2620)#(6)
if BG26__Fleet_Admiral_Tethys:# 
	BG_Minion_Pirate+=['BG26_766']
	BG_Minion_Pirate+=['BG26_766_G']
	BG_PoolSet_Pirate.append('BG26_766')
	BG_Pirate_Gold['BG26_766']='BG26_766_G'
class BG26_766_Action(GameAction):
	"""
	AMOUNT = IntArg() #
	"""
	AMOUNT = IntArg() #spent mana
	REPEAT = IntArg()
	def do(self, source, amount, repeat):
		triggeramount=8
		if amount==1:#buy a minion
			spent=source.controller.game.minionCost
		elif amount==2:# rerole
			spent=source.controller.game.reroleCost
		else:# upgrade
			spent=source.controller.tavern_tierup_cost
		source.sidequest_counter += spent
		source.script_data_num_1 = triggeramount - source.sidequest_counter
		if source.sidequest_counter>= triggeramount:
			## trigger action
			source.sidequest_counter -= triggeramount
			for i in range(repeat):
				newcard=RandomBGPirate().evaluate(source)	
				newcard=get00(newcard)
				newcard.zone=Zone.SETASIDE
				newcard.controller=source.controller
				newcard.zone=Zone.HAND
class BG26_766:# (minion)
	""" Fleet Admiral Tethys
	After you spend 8 Gold, get another random Pirate. <i>(@ Gold left!)</i> """
	tags={GameTag.TAG_SCRIPT_DATA_NUM_1:8}
	events = [Buy(CONTROLLER).after(BG26_810_Action(1,1)), 
		   Rerole(CONTROLLER).after(BG26_810_Action(2,1)), 
		   UpgradeTier(CONTROLLER).after(BG26_810_Action(3,1))]
	pass
class BG26_766_G:# (minion)
	""" Fleet Admiral Tethys
	After you spend 8 Gold, get 2 other random Pirates. <i>(@ Gold left!)</i> """
	tags={GameTag.TAG_SCRIPT_DATA_NUM_1:8}
	events = [Buy(CONTROLLER).after(BG26_810_Action(1,2)), 
		   Rerole(CONTROLLER).after(BG26_810_Action(2,2)), 
		   UpgradeTier(CONTROLLER).after(BG26_810_Action(3,2))]
	#
	pass

