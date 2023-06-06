from ..utils import *

BG26_=[]


## Bristlebach (Quilboar) (6)
BG26__Bristlebach=(Config.BG_VERSION>=2620)
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
	events = Death(FRIENDLY).on(Avenge(SELF, 1, [GiveGem( FRIENDLY + QUILBOAR)]))#
	pass


class BG26_157_G:# (minion)
	""" Bristlebach
	<b>Avenge (1):</b> Play 2 <b>Blood Gems</b> on all your Quilboar. """
	events = Death(FRIENDLY).on(Avenge(SELF, 1, [GiveGem( FRIENDLY + QUILBOAR),GiveGem( FRIENDLY + QUILBOAR)]))
	pass

## Moon-Bacon Jazzer (Quilboar) (3)
BG26__Moon_Bacon_Jazzer=(Config.BG_VERSION>=2620)
if BG26__Moon_Bacon_Jazzer:# 
	BG_Minion_Quilboar+=['BG26_159']
	BG_Minion_Quilboar+=['BG26_159_G']
	BG_PoolSet_Quilboar.append('BG26_159')
	BG_Quilboar_Gold['BG26_159']='BG26_159_G'
class BG26_159_action(GameAction):
	AMOUNT=IntArg()
	def do(self, source, amount):
		source.controller.moon_bacon_jazzer_powered_up=amount
class BG26_159:# (minion)
	""" Moon-Bacon Jazzer
	<b>Battlecry:</b> For the rest of the game, your <b>Blood Gems</b> __give an extra +1 Health. """
	play = BG26_159_action(1)
	pass

	
class BG26_159_G:# (minion)
	""" Moon-Bacon Jazzer
	<b>Battlecry:</b> For the rest of the game, your <b>Blood Gems</b> __give an extra +2 Health. """
	play = BG26_159_action(2)#
	pass

## Prickly Piper (Quilboar) (4)
BG26__Prickly_Piper=(Config.BG_VERSION>=2620)
if BG26__Prickly_Piper:# 
	BG_Minion_Quilboar+=['BG26_160']
	BG_Minion_Quilboar+=['BG26_160_G']
	BG_PoolSet_Quilboar.append('BG26_160')
	BG_Quilboar_Gold['BG26_160']='BG26_160_G'
class BG26_160_Action(GameAction):#
	AMOUNT=IntArg()
	def do(self, source, amount):#
		source.controller.prickly_piper_powered_up=amount
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

## Bongo Bopper (Quilboar) (5)
BG26__Bongo_Bopper=(Config.BG_VERSION>=2620)
if BG26__Bongo_Bopper:# 
	BG_Minion_Quilboar+=['BG26_531']
	BG_PoolSet_Quilboar.append('BG26_531')
	BG_Quilboar_Gold['BG26_531']='BG26_531_G'
class BG26_531_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_531:# (minion)
	""" Bongo Bopper
	At the end of your turn, get a <b>Blood Gem</b> and play 2 more on this. """
	events = OWN_TURN_END.on((
		Give(CONTROLLER, 'BG_GEM'),
		PlayGem(SELF), PlayGem(SELF)))
	pass

	BG_Minion_Quilboar+=['BG26_531_G']
class BG26_531_G:# (minion)
	""" Bongo Bopper
	At the end of your turn, get 2 <b>Blood Gems</b> and play 4 more on this. """
	events = OWN_TURN_END.on((
		Give(CONTROLLER, 'BG_GEM'),Give(CONTROLLER, 'BG_GEM'),
		PlayGem(SELF), PlayGem(SELF), PlayGem(SELF), PlayGem(SELF)))
	pass

