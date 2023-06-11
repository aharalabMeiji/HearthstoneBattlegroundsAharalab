from ..utils import *


## NEW 23.2 -> quilboarDarkgaze_Elder=True



BG_Razorfen_Geomancer=True##	1
BG_Sun_Bacon_Relaxer=True##	1
BG25__Thorncaptain=(Config.BG_VERSION>=2522)# 1/4/2 quilboar ## new 25.2.2

BG_Roadboar=(Config.BG_VERSION<2620)##	2 ## banned 26.2
BG_Tough_Tusk=True##	2
BG_Thorncaller=True##	3->2(26.2)

BG_Bannerboar=True##	3
BG_Bristleback_Brute=(Config.BG_VERSION<2620)## Brute	3 ## banned 26.2
BG_Gemsplitter=(Config.BG_VERSION<2460)##	3 ### banned 24.6
BG_Bristlemane_Scrapsmith=(Config.BG_VERSION>=2460) ## 3 ## new 24.6 ### OK ###
BG26__Moon_Bacon_Jazzer=(Config.BG_VERSION>=2620) # (3)
BG25__Pufferquil=(Config.BG_VERSION>=2522)# 4/2/6, quilbour/naga, new 25.2.2 ## (4)->(3) new 2622

BG_Bonker=True##	4
BG_Dynamic_Duo=True##	4
BG_Groundshaker=(Config.BG_VERSION<2620)##	4 ## banned 26.2
BG_Necrolyte=True##	4
BG_Gem_Smuggler=(Config.BG_VERSION>=2560)
BG26__Prickly_Piper=(Config.BG_VERSION>=2620)#(4)

BG_Aggem_Thorncurse=True##	5
BG_Bristleback_Knight=True## 5 BG20_204
BG26__Bongo_Bopper=(Config.BG_VERSION>=2620)# (5/5/5)

BG_Captain_Flat_Tusk=False##	6 banned when?
BG_Charlga=True##	6
BG_Darkgaze_Elder=(Config.BG_VERSION>=2320 and Config.BG_VERSION<2620)## NEW 23.2 -> quilboar ## banned 26.2
BG26__Bristlebach=(Config.BG_VERSION>=2620)# (6/2/10)



BG_Minion_Quilboar=[]

BG_PoolSet_Quilboar=[]

BG_Quilboar_Gold={}


#Razorfen Geomancer	1 ### OK ###
if BG_Razorfen_Geomancer:
	BG_Minion_Quilboar += [ 'BG20_100','BG20_100_G',]#	
	BG_PoolSet_Quilboar.append('BG20_100')
	BG_Quilboar_Gold['BG20_100']='BG20_100_G'
class BG20_100:# <12>[1453]
	""" Razorfen Geomancer
	[Battlecry:] Gain a[Blood Gem](BG20_GEM). """
	play = Give(CONTROLLER, 'BG20_GEM')
	pass
class BG20_100_G:# <12>[1453]
	""" Razorfen Geomancer
	[Battlecry:] Gain 2[Blood Gems](BG20_GEM). """
	play = Give(CONTROLLER, 'BG20_GEM') * 2
	pass



#Sun-Bacon Relaxer	1 ### OK ###
if BG_Sun_Bacon_Relaxer:
	BG_Minion_Quilboar += [ 'BG20_301','BG20_301_G',]#	
	BG_PoolSet_Quilboar.append('BG20_301')
	BG_Quilboar_Gold['BG20_301']='BG20_301_G'
class BG20_301:# <12>[1453] コンガリ 
	""" Sun-Bacon Relaxer
	When you sell this, gain 2_[Blood Gems](BG20_GEM). """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BG20_GEM') * 2)
	pass
class BG20_301_G:# <12>[1453]
	""" Sun-Bacon Relaxer
	When you sell this, gain 4_[Blood Gems](BG20_GEM). """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BG20_GEM') * 4)
	pass


if BG25__Thorncaptain:# 1/4/2 quilboar/pirate ## new 25.2.2
	BG_Minion_Quilboar+=['BG25_045','BG25_045_G','BG25_045e','BG25_045e2']
	BG_PoolSet_Quilboar.append('BG25_045')
	BG_Quilboar_Gold['BG25_045']='BG25_045_G'
class BG25_045:# (minion)
	""" Thorncaptain
	After a card is added to your hand, gain +1 Health until next turn. """
	events = [Give(CONTROLLER).after(Buff(SELF, 'BG25_045e')),
		   Buy(CONTROLLER).after(Buff(SELF, 'BG25_045e'))]
	pass
class BG25_045e:# (enchantment)
	""" Tis' the Captain
	+1 Health until next turn. """
	tags = {GameTag.TAG_ONE_TURN_EFFECT:1, GameTag.HEALTH:1 }
	pass
class BG25_045_G:# (minion)
	""" Thorncaptain
	After a card is added to your hand, gain +2 Health until next turn. """
	events = [Give(CONTROLLER).after(Buff(SELF, 'BG25_045e2')),
		   Buy(CONTROLLER).after(Buff(SELF, 'BG25_045e2'))]
	pass
class BG25_045e2:# (enchantment)
	""" Tis' the Captain
	+2 Health until next turn. """
	tags = {GameTag.TAG_ONE_TURN_EFFECT:1, GameTag.HEALTH:2 }
	pass



#Roadboar	2  ### OK ### banned 26.2
if BG_Roadboar:
	BG_Minion_Quilboar += [ 'BG20_101','BG20_101_G',]#	
	BG_PoolSet_Quilboar.append('BG20_101')
	BG_Quilboar_Gold['BG20_101']='BG20_101_G'
class BG20_101_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller=target.deepcopy_original
		Give(controller, card).trigger(controller)
class BG20_101:# <12>[1453] 
	""" Roadboar
	[Frenzy:] Gain a [Blood Gem]. """
	tags={GameTag.FRENZY:1, }
	#<ReferencedTag enumID="1637" name="FRENZY" type="Int" value="1"/>
	events = Damage(SELF).on(Frenzy(SELF,BG20_101_Action(CONTROLLER, 'BG20_GEM')))
	pass
class BG20_101_G:# <12>[1453]
	""" Roadboar
	[Frenzy:] Gain 2 [Blood Gems]. """
	tags={GameTag.FRENZY:1, }
	events = Damage(SELF).on(Frenzy(SELF,[BG20_101_Action(CONTROLLER, 'BG20_GEM'), BG20_101_Action(CONTROLLER, 'BG20_GEM')]))
	pass



#Tough Tusk	2 ### OK ###
if BG_Tough_Tusk:
	BG_Minion_Quilboar += [ 'BG20_102','BG20_102e','BG20_102_G','BG20_102_Ge',]#	
	BG_PoolSet_Quilboar.append('BG20_102')
	BG_Quilboar_Gold['BG20_102']='BG20_102_G'
class BG20_102:# <12>[1453]
	""" Tough Tusk
	After a [Blood Gem] is played on this, gain [Divine Shield] for the next combat. """
	events = ApplyGem(SELF).on(SetDivineShield(SELF), Buff(SELF,'BG20_102e'))
	pass
class BG20_102e:# <12>[1453]
	""" Toughened """
	events = BeginBar(CONTROLLER).on(SetDivineShield(OWNER, False),Destroy(SELF))
	pass
class BG20_102_G:# <12>[1453]
	""" Tough Tusk
	After a [Blood Gem] is played on this, gain[Divine Shield]. """
	events = ApplyGem(SELF).on(SetDivineShield(SELF),Buff(SELF,'BG20_102_Ge'))
	pass
class BG20_102_Ge:# <12>[1453]
	""" Real Tough
	[Divine Shield]. """
	events = BeginBar(CONTROLLER).on(SetDivineShield(OWNER, False),Destroy(SELF))
	pass



#Thorncaller	3->2  ### OK ###
if BG_Thorncaller:
	BG_Minion_Quilboar += [ 'BG20_105','BG20_105_G',]#	
	BG_PoolSet_Quilboar.append('BG20_105')
	BG_Quilboar_Gold['BG20_105']='BG20_105_G'
class GiveGemToOriginal(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		if target.deepcopy_original:
			Give(target.deepcopy_original,card).trigger(target.deepcopy_original)
class BG20_105:# <12>[1453] 荊使い
	""" Thorncaller
	[Deathrattle:] Gain a [Blood Gem]. """
	###[Battlecry and Deathrattle:] Gain a [Blood Gem]. """ <2620
	#<Tag enumID="217" name="DEATHRATTLE" type="Int" value="1"/>
	if Config.BG_VERSION>=2620:
		option_tags = {GameTag.TECH_LEVEL:2, GameTag.ATK:3, GameTag.HEALTH:2}
		pass
	else:
		option_tags = {GameTag.TECH_LEVEL:3, GameTag.ATK:4, GameTag.HEALTH:3}
		play = Give(CONTROLLER, 'BG20_GEM')
	deathrattle = GiveGemToOriginal(CONTROLLER, 'BG20_GEM')
	pass
class BG20_105_G:# <12>[1453]
	""" Thorncaller
	[Battlecry and Deathrattle:] Gain 2 [Blood Gems]. """
	if Config.BG_VERSION>=2620:
		option_tags = {GameTag.TECH_LEVEL:2, GameTag.ATK:6, GameTag.HEALTH:4}
		pass
	else:
		option_tags = {GameTag.TECH_LEVEL:3, GameTag.ATK:8, GameTag.HEALTH:6}
		play = Give(CONTROLLER, 'BG20_GEM')*2
	deathrattle = GiveGemToOriginal(CONTROLLER, 'BG20_GEM')*2
	pass



#### TIER 3 ####

#Bristlemane Scrapsmith (quilboar 3) (BG24_707)# ### OK ###
if BG_Bristlemane_Scrapsmith:
	BG_Minion_Quilboar += [ 'BG24_707','BG24_707_G',]#	
	BG_PoolSet_Quilboar.append('BG24_707')
	BG_Quilboar_Gold['BG24_707']='BG24_707_G'
class BG24_707_Action(TargetedAction):
	CONTROLLER=ActionArg()
	AMOUNT=ActionArg()
	def do(self, source, controller, amount):
		if source.game.this_is_battle==False:
			return
		controller=controller.deepcopy_original
		for repeat in range(amount):
			Give(controller, 'BG20_GEM').trigger(source)
		pass
class BG24_707:
	""" Bristlemane Scrapsmith (quilboar 3) (4/4)
	After a friendly [Taunt] minion dies, get a [Blood Gem]."""
	events = Death(FRIENDLY + TAUNT).on(BG24_707_Action(CONTROLLER, 1))
	pass
class BG24_707_G:
	"""
	After a friendly [Taunt] minion dies,get 2 [ Blood Gems]."""
	events = Death(FRIENDLY + TAUNT).on(BG24_707_Action(CONTROLLER, 2))
	pass


#Bannerboar	3  ### OK ###
if BG_Bannerboar:
	BG_Minion_Quilboar += [ 'BG20_201','BG20_201_G',]#	
	BG_PoolSet_Quilboar.append('BG20_201')
	BG_Quilboar_Gold['BG20_201']='BG20_201_G'
class BG20_201:# <12>[1453]
	""" Bannerboar
	At the end of your turn, play a [Blood Gem] on adjacent minions.
	"""
	events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENT, 'BG20_GEM'))
	##At the end of your turn, play a [Blood Gem] on adjacent Quilboar. 
	##events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENT + QUILBOAR, 'BG20_GEM'))
	pass
class BG20_201_G:# <12>[1453]
	""" Bannerboar
	At the end of your turn, play 2 [Blood Gems] on adjacent minions.
	 """
	events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENT, 'BG20_GEM'), ApplyGem(SELF_ADJACENT, 'BG20_GEM'))
	## At the end of your turn, play 2 [Blood Gems] on adjacent Quilboar.
	##events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENT + QUILBOAR, 'BG20_GEM'), ApplyGem(SELF_ADJACENT + QUILBOAR, 'BG20_GEM'))
	pass



#Bristleback Brute	3   ### OK ### banned 26.2
if BG_Bristleback_Brute:
	BG_Minion_Quilboar += [ 'BG20_103','BG20_103_G',]#	
	BG_PoolSet_Quilboar.append('BG20_103')
	BG_Quilboar_Gold['BG20_103']='BG20_103_G'
class GB20_103_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		if not target.gem_applied_thisturn:
			buff=target.buffs[-1]
			buff.atk+=amount
			buff.max_health+=amount
		pass
class BG20_103:# <12>[1453]
	""" Bristleback Brute
	The first [Blood Gem] played on this each turn gives an extra +3/+3. """
	events = ApplyGem(SELF).on(GB20_103_Action(SELF, 3))
	pass
class BG20_103_G:# <12>[1453]
	""" Bristleback Brute
	The first [Blood Gem] played on this each turn gives an extra +6/+6. """
	events = ApplyGem(SELF).on(GB20_103_Action(SELF, 6))
	pass



#Gemsplitter	3 ### OK ### banned 24.6
if BG_Gemsplitter:
	BG_Minion_Quilboar += [ 'BG21_037','BG21_037_G',]#	
	BG_PoolSet_Quilboar.append('BG21_037')
	BG_Quilboar_Gold['BG21_037']='BG21_037_G'
class BG21_037_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller=target.deepcopy_original
		Give(controller, card).trigger(controller)
class BG21_037:# <12>[1453] 宝石割
	""" Gemsplitter
	After a friendly minion loses [Divine Shield], gain a_[Blood Gem]. """
	events = LoseDivineShield(FRIENDLY).on(GiveInBattle(CONTROLLER, 'BG20_GEM'))
	pass
class BG21_037_G:# <12>[1453]
	""" Gemsplitter
	After a friendly minion loses [Divine Shield], gain 2_[Blood Gems]. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(GiveInBattle(CONTROLLER, 'BG20_GEM')*2)
	pass




## Moon-Bacon Jazzer (Quilboar) (3)
#BG26__Moon_Bacon_Jazzer=(Config.BG_VERSION>=2620) # (3)
if BG26__Moon_Bacon_Jazzer:# 
	BG_Minion_Quilboar+=['BG26_159','BG26_159pe',]
	BG_Minion_Quilboar+=['BG26_159_G']
	BG_PoolSet_Quilboar.append('BG26_159')
	BG_Quilboar_Gold['BG26_159']='BG26_159_G'
class BG26_159_action(GameAction):
	AMOUNT=IntArg()
	def do(self, source, amount):
		source.controller.moon_bacon_jazzer_powered_up+=amount
class BG26_159:# (minion)
	""" Moon-Bacon Jazzer
	<b>Battlecry:</b> For the rest of the game, your <b>Blood Gems</b> __give an extra +1 Health. """
	play = BG26_159_action(1)
	pass
class BG26_159pe:
	pass
class BG26_159_G:# (minion)
	""" Moon-Bacon Jazzer
	<b>Battlecry:</b> For the rest of the game, your <b>Blood Gems</b> __give an extra +2 Health. """
	play = BG26_159_action(2)#
	pass

if BG25__Pufferquil:# 4/2/6, quilbour/naga (4)->(3) new 2622
	BG_Minion_Quilboar+=['BG25_039','BG25_039_G','BG25_039_Ge','BG25_039e']
	BG_PoolSet_Quilboar.append('BG25_039')
	BG_Quilboar_Gold['BG25_039']='BG25_039_G'
class BG25_039_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if target==source:
			Buff(target, 'BG25_039e').trigger(source)
class BG25_039:# (minion)
	""" Pufferquil
	After a spell is played on this, gain Venomous until end of turn.""" ## new 26.2
	##After a spell is played on this, gain <b>Poisonous</b> until next turn. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.TECH_LEVEL:3}
	else:
		option_tags={GameTag.TECH_LEVEL:4}
	events = BG_Play(CONTROLLER).after(BG25_039_Action(Play.TARGET))
	pass
class BG25_039e:# (enchantment)
	""" Puffed Up
	<b>Poisonous</b> until next turn. """
	if Config.BG_VERSION>=2620:
		tags = {GameTag.TAG_ONE_TURN_EFFECT:1, GameTag.VENOMOUS:1 }
	else:
		tags = {GameTag.TAG_ONE_TURN_EFFECT:1, GameTag.POISONOUS:1 }
	pass
class BG25_039_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if target==source:
			Buff(target, 'BG25_039_Ge').trigger(source)
class BG25_039_G:# (minion)
	""" Pufferquil
	After a spell is played on this, gain <b>Poisonous</b>. """
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.TECH_LEVEL:3}
	else:
		option_tags={GameTag.TECH_LEVEL:4}
	events = BG_Play(CONTROLLER).after(BG25_039_G_Action(Play.TARGET))
	pass
if Config.BG_VERSION>=2620:
	BG25_039_Ge=buff(venomous=True)# (enchantment)
else:
	BG25_039_Ge=buff(poisonous=True)# (enchantment)
""" Puffed Full	<b>Poisonous</b>. """



#### tavern tier 4 ####

#Bonker	4  ### OK ###
if BG_Bonker:
	BG_Minion_Quilboar += [ 'BG20_104','BG20_104_G',]#	
	BG_PoolSet_Quilboar.append('BG20_104')
	BG_Quilboar_Gold['BG20_104']='BG20_104_G'
class BG20_104:# <12>[1453]
	""" Bonker
	[Windfury]After this attacks, gain a [Blood Gem]. """
	events = Attack(SELF).after(GiveGemToOriginal(CONTROLLER, 'BG20_GEM'))
	pass
class BG20_104_G:# <12>[1453]
	""" Bonker
	[Mega-Windfury]After this attacks, gain a [Blood Gem]. """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>
	events = Attack(SELF).after(GiveGemToOriginal(CONTROLLER, 'BG20_GEM'))
	pass



#Dynamic Duo	4 ### OK ###
if BG_Dynamic_Duo:
	BG_Minion_Quilboar += [ 'BG20_207','BG20_207e','BG20_207_G','BG20_207_Ge',]#	
	BG_PoolSet_Quilboar.append('BG20_207')
	BG_Quilboar_Gold['BG20_207']='BG20_207_G'
class BG20_207:# <12>[1453]
	""" Dynamic Duo
	[[Taunt].] After a [Blood Gem]is played on another Quilboar, gain +1/+1. """
	events = ApplyGem(FRIENDLY_MINIONS - SELF).on(Buff(SELF, 'BG20_207e'))
	pass
BG20_207e=buff(1,1)# <12>[1453]
""" Boar's Favor,+1/+1. """
class BG20_207_G:# <12>[1453]
	""" Dynamic Duo
	[[Taunt].] After a [Blood Gem]is played on anotherQuilboar, gain +2/+2. """
	events = ApplyGem(FRIENDLY_MINIONS - SELF).on(Buff(SELF, 'BG20_207_Ge'))
	pass
BG20_207_Ge=buff(2,2)# <12>[1453]
""" Boar's Favor,+2/+2. """



#Groundshaker	4  ## OK ### banned 26.2
## 2543
#Old: 2 Attack, 6 Health.
#New: 3 Attack, 8 Health.
if BG_Groundshaker:
	BG_Minion_Quilboar += [ 'BG20_106','BG20_106e','BG20_106_G',]#	
	BG_PoolSet_Quilboar.append('BG20_106')
	BG_Quilboar_Gold['BG20_106']='BG20_106_G'
class BG20_106:# <12>[1453]
	""" Groundshaker
	After a [Blood Gem] is played on this, give your other minions +2 Attack for next combat only. """
	if Config.BG_VERSION>=2543:
		option_tags={GameTag.ATK:3, GameTag.HEALTH:8}
	else:
		option_tags={GameTag.ATK:2, GameTag.HEALTH:6}
	events = ApplyGem(SELF).on(Buff(FRIENDLY_MINIONS - SELF, 'BG20_106e'))
	pass
class BG20_106e:# <12>[1453]
	""" Groundshook,	+@ Attack. """
	tags = {GameTag.ATK:2, }
	events = EndBattle(CONTROLLER).on(Destroy(SELF))
class BG20_106_G:# <12>[1453]
	""" Groundshaker
	After a [Blood Gem] is played on this, give your other minions +4 Attack for next combat only. """
	if Config.BG_VERSION>=2543:
		option_tags={GameTag.ATK:6, GameTag.HEALTH:16}
	else:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:12}
	events = ApplyGem(SELF).on(
		Buff(FRIENDLY_MINIONS - SELF, 'BG20_106e'), 
		Buff(FRIENDLY_MINIONS - SELF, 'BG20_106e'))
	pass



#Necrolyte	4  ### OK ###
if BG_Necrolyte:
	BG_Minion_Quilboar += [ 'BG20_202','BG20_202_G',]#	
	BG_PoolSet_Quilboar.append('BG20_202')
	BG_Quilboar_Gold['BG20_202']='BG20_202_G'
class BG20_202:# <12>[1453]
	""" Necrolyte
	[Battlecry:] Play 2 [BloodGems] on a friendly minion. It steals all [Blood Gems]from its neighbors. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,}
	play = ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		StealGem(TARGET, TARGET_ADJACENT)
	pass
class BG20_202_G:# <12>[1453]
	""" Necrolyte
	[Battlecry:] Play 4 [BloodGems] on a friendly minion.It steals all [Blood Gems]from its neighbors. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,}
	play = ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		StealGem(TARGET, TARGET_ADJACENT)
	pass




#Gem Smuggler
if BG_Gem_Smuggler:
	BG_Minion_Quilboar += [ 'BG25_155','BG25_155_G']#	
	BG_PoolSet_Quilboar.append('BG25_155')
	BG_Quilboar_Gold['BG25_155']='BG25_155_G'
class BG25_155_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.field if isRaceCard(card, Race.QUILBOAR)==True and card!=source]
		for card in cards:
			ApplyGem(card, 'BG20_GEM').trigger(source)
class BG25_155:
	""" Gem Smuggler
	Battlecry: Play a Blood Gem on all your other Quilboar."""
	#[Tavern Tier 4, Quilboar] 3 Attack, 4 Health. Battlecry: Play a Blood Gem on all your other Quilboar.
	option_tags={GameTag.TECH_LEVEL:4}
	play = BG25_155_Action()
	pass
class BG25_155_G_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.field if isRaceCard(card, Race.QUILBOAR)==True and card!=source]
		for card in cards:
			ApplyGem(card, 'BG20_GEM').trigger(source)
			ApplyGem(card, 'BG20_GEM').trigger(source)
class BG25_155_G:
	""" Gem Smuggler
	Battlecry: Play 2 Blood Gems on all your other Quilboar."""
	option_tags={GameTag.TECH_LEVEL:4}
	play = BG25_155_G_Action()
	pass



## Prickly Piper (Quilboar) (4)
#BG26__Prickly_Piper=(Config.BG_VERSION>=2620)#(4)
if BG26__Prickly_Piper:# 
	BG_Minion_Quilboar+=['BG26_160']
	BG_Minion_Quilboar+=['BG26_160_G']
	BG_PoolSet_Quilboar.append('BG26_160')
	BG_Quilboar_Gold['BG26_160']='BG26_160_G'
class BG26_160_Action(GameAction):#
	AMOUNT=IntArg()
	def do(self, source, amount):#
		if hasattr(source.controller,'deepcopy_original'):
			source.controller.deepcopy_original.prickly_piper_powered_up+=amount
		pass# 
class BG26_160:# (minion)
	""" Prickly Piper
	<b>Deathrattle:</b> For the rest of the game, your <b>Blood Gems</b> __give an extra +1 Attack. """
	deathrattle = BG26_160_Action(1)
	pass
class BG26_160_G:# (minion)
	""" Prickly Piper
	<b>Deathrattle:</b> For the rest of the game, your <b>Blood Gems</b> __give an extra +2 Attack. """
	deathrattle = BG26_160_Action(2)#
	pass
@custom_card
class BG26_160e:
	tags = {
		GameTag.CARDNAME: "ZZZZ",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}



#### tavern tier 5 3333

#Aggem Thorncurse	5  ### OK ###
if BG_Aggem_Thorncurse:
	BG_Minion_Quilboar += [ 'BG20_302','BG20_302e','BG20_302_G','BG20_302_Ge',]#	
	BG_PoolSet_Quilboar.append('BG20_302')
	BG_Quilboar_Gold['BG20_302']='BG20_302_G'
class BG20_302_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		controller = target
		field = controller.field
		flag = [0] * len(field)
		ret = []
		while True:
			if sum(flag)==len(field):
				break
			c =random.choice(field)
			addOK=True
			for d in ret:
				if c.race == d.race:
					flag[field.index(c)]=1
					addOK=False
					continue
			if addOK:
				flag[field.index(c)]=1
				if c.race != Race.INVALID:
					ret.append(c)
			pass
		for c in ret:
			Buff(c,buff).trigger(source)
class BG20_302:# <12>[1453] そーんかーす
	""" Aggem Thorncurse
	After a [Blood Gem] is played on this, give a friendly minion of each minion type +1/+1. """
	events = ApplyGem(SELF).on(BG20_302_Action(CONTROLLER, 'BG20_302e'))
	pass
BG20_302e=buff(1,1)# <12>[1453]
""" Thorncursed
+1/+1 """
class BG20_302_G:# <12>[1453]
	""" Aggem Thorncurse
	After a [Blood Gem] is played on this, give a friendly minion of each minion type +2/+2. """
	events = ApplyGem(SELF).on(BG20_302_Action(CONTROLLER, 'BG20_302_Ge'))
	pass
BG20_302_Ge=buff(2,2)# <12>[1453]
""" Thorncursed
+2/+2 """



###BG_Bristleback_Knight (5)
if BG_Bristleback_Knight:
	BG_Minion_Quilboar += [ 'BG20_204','BG20_302e','BG20_302_G','BG20_302_Ge',]#	
	BG_PoolSet_Quilboar.append('BG20_204')
	BG_Quilboar_Gold['BG20_204']='BG20_302_G'
class BG20_204:
	"""Bristleback_Knight
	[Windfury], [Divine Shield] [Frenzy:] Gain [Divine Shield]."""
	events = Damage(SELF).on(Frenzy(SELF,SetDivineShield(SELF, True)))
	#<Tag enumID="189" name="WINDFURY" type="Int" value="1"/>
	pass
class BG20_204_G:
	"""Bristleback_Knight
	[Mega-Windfury], [[Divine Shield].] [Frenzy:] Gain [Divine Shield]."""
	events = Damage(SELF).on(Frenzy(SELF,SetDivineShield(SELF, True)))
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>
	pass


	
## Bongo Bopper (Quilboar) (5)
#BG26__Bongo_Bopper=(Config.BG_VERSION>=2620)# (5)
if BG26__Bongo_Bopper:# 
	BG_Minion_Quilboar+=['BG26_531']
	BG_PoolSet_Quilboar.append('BG26_531')
	BG_Quilboar_Gold['BG26_531']='BG26_531_G'
class BG26_531:# (minion)
	""" Bongo Bopper
	At the end of your turn, get a <b>Blood Gem</b> and play 2 more on this. """
	events = OWN_TURN_END.on((
		Give(CONTROLLER, 'BG20_GEM'),
		ApplyGem(SELF, 'BG20_GEM'), ApplyGem(SELF, 'BG20_GEM')))
	pass

	BG_Minion_Quilboar+=['BG26_531_G']
class BG26_531_G:# (minion)
	""" Bongo Bopper
	At the end of your turn, get 2 <b>Blood Gems</b> and play 4 more on this. """
	events = OWN_TURN_END.on((
		Give(CONTROLLER, 'BG20_GEM'),Give(CONTROLLER, 'BG20_GEM'),
		ApplyGem(SELF, 'BG20_GEM'),ApplyGem(SELF, 'BG20_GEM'),ApplyGem(SELF, 'BG20_GEM'),ApplyGem(SELF, 'BG20_GEM')))
	pass



#### TIER 6


#Captain Flat Tusk	6  ### OK ###
if BG_Captain_Flat_Tusk:
	BG_Minion_Quilboar += [ 'BG20_206','BG20_206_G',]#	
	BG_PoolSet_Quilboar.append('BG20_206')
	BG_Quilboar_Gold['BG20_206']='BG20_206_G'
class BG20_206_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		if controller.spentmoney_in_this_turn>=4:
			for repeat in range(amount):
				Give(controller,'BG20_GEM').trigger(source)
			controller.spentmoney_in_this_turn -= 4
class BG20_206:# <12>[1453]
	""" Captain Flat Tusk
	After you spend 4 Gold, gain a [Blood Gem].<i>(@ Gold left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_206_Action(CONTROLLER, 1)),
		Rerole(CONTROLLER).on(BG20_206_Action(CONTROLLER, 1)),
		UpgradeTier(CONTROLLER).on(BG20_206_Action(CONTROLLER, 1)),
		]
	pass
class BG20_206_G:# <12>[1453]
	""" Captain Flat Tusk
	After you spend 4 Gold,gain 2 [Blood Gems].<i>(@ Gold left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_206_Action(CONTROLLER, 2)),
		Rerole(CONTROLLER).on(BG20_206_Action(CONTROLLER, 2)),
		UpgradeTier(CONTROLLER).on(BG20_206_Action(CONTROLLER, 2)),
		]
	pass


#Charlga	6 ### OK ###
if BG_Charlga:
	BG_Minion_Quilboar += [ 'BG20_303','BG20_303_G',]#	
	BG_PoolSet_Quilboar.append('BG20_303')
	BG_Quilboar_Gold['BG20_303']='BG20_303_G'
class BG20_303:# <12>[1453] ちゃるが
	""" Charlga
	At the end of your turn, play a Blood Gem on your other minions.""" ##new 26.2
	##At the end of your turn, play a [Blood Gem] on all friendly minions. 
	if Config.BG_VERSION>=2620:
		events = OWN_TURN_END.on(ApplyGem(FRIENDLY_MINIONS - SELF, 'BG20_GEM'))
	else:
		events = OWN_TURN_END.on(ApplyGem(FRIENDLY_MINIONS, 'BG20_GEM'))
	pass

class BG20_303_G:# <12>[1453]
	""" Charlga
	At the end of your turn, play 2 [Blood Gems] on all friendly minions. """
	if Config.BG_VERSION>=2620:
		events = OWN_TURN_END.on(ApplyGem(FRIENDLY_MINIONS - SELF, 'BG20_GEM')*2)
	else:
		events = OWN_TURN_END.on(ApplyGem(FRIENDLY_MINIONS, 'BG20_GEM')*2)
	pass


if BG_Darkgaze_Elder:## Darkgaze Elder (6) (quilboar)  ### maybe OK ### NEW 23.2 ## banned 26.2
	BG_Minion_Quilboar += ['BG23_018','BG23_018t','BG23_018_G', ]#	
	BG_PoolSet_Quilboar.append('BG23_018')
	BG_Quilboar_Gold['BG23_018']='BG23_018_G'
	# Darkgaze Elder 6 NEW 23.2
	pass
class BG23_018_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		source.script_data_num_1 = 5-controller.spentmoney_in_this_turn
		if controller.spentmoney_in_this_turn>=5:
			quilboars=[]
			for card in controller.field:
				#if card.race==Race.QUILBOAR:
				if race_identity(card,Race.QUILBOAR):
					quilboars.append(card)
			if len(quilboars)>4:
				quilboars=random.select(quilboars,4)
			for card in quilboars:
				for repeat in range(amount):
					ApplyGem(card,'BG20_GEM').trigger(source)
			controller.spentmoney_in_this_turn -= 5
			source.script_data_num_1 = 5-controller.spentmoney_in_this_turn
class BG23_018:# <12>[1453]
	""" Darkgaze Elder (6)
	After you spend 5 Gold, play a [Blood Gem] on four friendly Quilboar. <i>(@ Gold left!)</i>"""
	events = [
		Buy(CONTROLLER).on(BG23_018_Action(CONTROLLER, 1)),
		Rerole(CONTROLLER).on(BG23_018_Action(CONTROLLER, 1)),
		UpgradeTier(CONTROLLER).on(BG23_018_Action(CONTROLLER, 1)),
		]
	pass
class BG23_018_G:# <12>[1453]
	"""
	After you spend 4 Gold, play a [Blood Gem] on four friendly Quilboar twice. <i>(@ Gold left!)</i>"""
	events = [
		Buy(CONTROLLER).on(BG23_018_Action(CONTROLLER, 2)),
		Rerole(CONTROLLER).on(BG23_018_Action(CONTROLLER, 2)),
		UpgradeTier(CONTROLLER).on(BG23_018_Action(CONTROLLER, 2)),
		]
	pass
class BG23_018t:# <12>[1453]
	pass



## Bristlebach (Quilboar) (6)
#BG26__Bristlebach=(Config.BG_VERSION>=2620)# (6)
if BG26__Bristlebach:# 
	BG_Minion_Quilboar+=['BG26_157']
	BG_Minion_Quilboar+=['BG26_157_G']
	BG_PoolSet_Quilboar.append('BG26_157')
	BG_Quilboar_Gold['BG26_157']='BG26_157_G'
class BG26_157_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_157:# (minion)
	""" Bristlebach
	<b>Avenge (1):</b> Play a <b>Blood Gem</b> on all your Quilboar. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 1, [ApplyGem( FRIENDLY_MINIONS + QUILBOAR, 'BG20_GEM')]))#
	pass
class BG26_157_G:# (minion)
	""" Bristlebach
	<b>Avenge (1):</b> Play 2 <b>Blood Gems</b> on all your Quilboar. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 1, [
		ApplyGem( FRIENDLY_MINIONS + QUILBOAR, 'BG20_GEM'),
		ApplyGem( FRIENDLY_MINIONS + QUILBOAR, 'BG20_GEM')]
											 ))
	pass



#####################