from ..utils import *

BG26_=[]


## Bream Counter (Murloc) (4)
BG26__Bream_Counter=(Config.BG_VERSION>=2620)
if BG26__Bream_Counter:# 
	BG_Minion_Murloc+=['BG26_137']
	BG_PoolSet_Murloc.append('BG26_137')
	BG_Murloc_Gold['BG26_137']=''
class BG26_137_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_137:# (minion)(murloc)
	""" Bream Counter
	While this is in your hand, after you play a Murloc, gain +3/+2. """
	#
	pass

	BG_Minion_Murloc+=['BG26_137_G']
class BG26_137_G:# (minion)(murloc)
	""" Bream Counter
	While this is in your hand, after you play a Murloc, gain +6/+4. """
	#
	pass

## Bassgill (Murloc) (4)
BG26__Bassgill=(Config.BG_VERSION>=2620)
if BG26__Bassgill:# 
	BG_Minion_Murloc+=['BG26_350']
	BG_PoolSet_Murloc.append('BG26_350')
	BG_Murloc_Gold['BG26_350']=''
class BG26_350_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_350:# (minion)(murloc)
	""" Bassgill
	<b>Deathrattle:</b> Summon the highest Health minion from your hand for this combat only. """
	#
	pass

	BG_Minion_Murloc+=['BG26_350_G']
class BG26_350_G:# (minion)(murloc)
	""" Bassgill
	<b>Deathrattle:</b> Summon the 2 highest Health minions from your hand for this combat only. """
	#
	pass

## Upbeat Flutist (Murloc) (2)
BG26__Upbeat_Flutist=(Config.BG_VERSION>=2620)
if BG26__Upbeat_Flutist:# 
	BG_Minion_Murloc+=['BG26_352']
	BG_PoolSet_Murloc.append('BG26_352')
	BG_Murloc_Gold['BG26_352']=''
class BG26_352_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_352:# (minion)(murloc)
	""" Upbeat Flutist
	At the end of every 2 turns, give a random minion in your hand +9 Health. <i>({0} |4(turn, turns) left!)</i>@At the end of every 2 turns, give a random minion in your hand +9 Health. <i>(End of this turn!)</i> """
	#
	pass

	BG_Minion_Murloc+=['BG26_352_G']
class BG26_352_G:# (minion)(murloc)
	""" Upbeat Flutist
	At the end of every 2 turns, give a random minion in your hand +18 Health. <i>({0} |4(turn, turns) left!)</i>@At the end of every 2 turns, give a random minion in your hand +18 Health. <i>(End of this turn!)</i> """
	#
	pass

## Choral Mrrrglr (Murloc) (6)
BG26__Choral_Mrrrglr=(Config.BG_VERSION>=2620)
if BG26__Choral_Mrrrglr:# 
	BG_Minion_Murloc+=['BG26_354']
	BG_PoolSet_Murloc.append('BG26_354')
	BG_Murloc_Gold['BG26_354']=''
class BG26_354_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_354:# (minion)(murloc)
	""" Choral Mrrrglr
	<b>Start of Combat:</b> Gain the stats of all the minions in your hand. """
	#
	pass

	BG_Minion_Murloc+=['BG26_354_G']
class BG26_354_G:# (minion)(murloc)
	""" Choral Mrrrglr
	<b>Start of Combat:</b> Gain the stats of all the minions in your hand twice. """
	#
	pass

## Scourfin (Murloc) (3)
BG26__Scourfin=(Config.BG_VERSION>=2620)
if BG26__Scourfin:# 
	BG_Minion_Murloc+=['BG26_360']
	BG_PoolSet_Murloc.append('BG26_360')
	BG_Murloc_Gold['BG26_360']=''
class BG26_360_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_360:# (minion)(murloc)
	""" Scourfin
	<b>Deathrattle:</b> Give a random minion in your hand +5/+5. """
	#
	pass

	BG_Minion_Murloc+=['BG26_360_G']
class BG26_360_G:# (minion)(murloc)
	""" Scourfin
	<b>Deathrattle:</b> Give a random minion in your hand +10/+10. """
	#
	pass

## Plagued Tidewalker (Murloc) (4)
BG26__Plagued_Tidewalker=(Config.BG_VERSION>=2620)
if BG26__Plagued_Tidewalker:# 
	BG_Minion_Murloc+=['BG26_361']
	BG_PoolSet_Murloc.append('BG26_361')
	BG_Murloc_Gold['BG26_361']=''
class BG26_361_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_361:# (minion)(murloc)
	""" Plagued Tidewalker
	<b>Venomous</b> """
	#
	pass

	BG_Minion_Murloc+=['BG26_361_G']
class BG26_361_G:# (minion)(murloc)
	""" Plagued Tidewalker
	<b>Venomous</b> """
	#
	pass

## Operatic Belcher (Murloc) (5)
BG26__Operatic_Belcher=(Config.BG_VERSION>=2620)
if BG26__Operatic_Belcher:# 
	BG_Minion_Murloc+=['BG26_888']
	BG_PoolSet_Murloc.append('BG26_888')
	BG_Murloc_Gold['BG26_888']=''
class BG26_888_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_888:# (minion)(murloc)
	""" Operatic Belcher
	<b>Venomous.</b> <b>Deathrattle:</b> Give a friendly Murloc <b>Venomous</b>. """
	#
	pass

	BG_Minion_Murloc+=['BG26_888_G']
class BG26_888_G:# (minion)(murloc)
	""" Operatic Belcher
	<b>Venomous.</b> <b>Deathrattle:</b> Give 2 friendly Murlocs <b>Venomous</b>. """
	#
	pass

