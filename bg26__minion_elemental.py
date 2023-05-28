from ..utils import *

BG26_=[]


## Upbeat Upstart (Elemental) (4)
BG26__Upbeat_Upstart=(Config.BG_VERSION>=2620)
if BG26__Upbeat_Upstart:# 
	BG_Minion_Elemental+=['BG26_120']
	BG_PoolSet_Elemental.append('BG26_120')
	BG_Elemental_Gold['BG26_120']=''
class BG26_120_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_120:# (minion)
	""" Upbeat Upstart
	<b><b>Taunt</b>.</b> At the end of every 2 turns, set this minion's Health to the highest in your warband. <i>({0} |4(turn, turns) left!)</i>@<b><b>Taunt</b>.</b> At the end of every 2 turns, set this minion's Health to the highest in your warband. <i>(End of this turn!)</i> """
	#
	pass

	BG_Minion_Elemental+=['BG26_120_G']
class BG26_120_G:# (minion)
	""" Upbeat Upstart
	<b><b>Taunt</b>.</b> At the end of every 2 turns, set this minion's Health to double the highest in your warband. <i>({0} |4(turn, turns) left!)</i>@<b><b>Taunt</b>.</b> At the end of every 2 turns, set this minion's Health to double the highest in your ___warband. <i>(End of this turn!)</i> """
	#
	pass

## Dancing Barnstormer (Elemental) (4)
BG26__Dancing_Barnstormer=(Config.BG_VERSION>=2620)
if BG26__Dancing_Barnstormer:# 
	BG_Minion_Elemental+=['BG26_162']
	BG_PoolSet_Elemental.append('BG26_162')
	BG_Elemental_Gold['BG26_162']=''
class BG26_162_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_162:# (minion)
	""" Dancing Barnstormer
	<b>Deathrattle:</b> Elementals in Bob's Tavern have +3/+2 __for the rest of the game. """
	#
	pass

	BG_Minion_Elemental+=['BG26_162_G']
class BG26_162_G:# (minion)
	""" Dancing Barnstormer
	<b>Deathrattle:</b> Elementals in Bob's Tavern have +6/+4 __for the rest of the game. """
	#
	pass

## Elemental of Surprise (Elemental) (6)
BG26__Elemental_of_Surprise=(Config.BG_VERSION>=2620)
if BG26__Elemental_of_Surprise:# 
	BG_Minion_Elemental+=['BG26_175']
	BG_PoolSet_Elemental.append('BG26_175')
	BG_Elemental_Gold['BG26_175']=''
class BG26_175_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_175:# (minion)
	""" Elemental of Surprise
	<b>Divine Shield</b> This minion can triple with any Elemental. """
	#
	pass

	BG_Minion_Elemental+=['BG26_175_G']
class BG26_175_G:# (minion)
	""" Elemental of Surprise
	<b>Divine Shield</b> This minion can triple with any Elemental. """
	#
	pass

## Gusty Trumpeter (Elemental) (5)
BG26__Gusty_Trumpeter=(Config.BG_VERSION>=2620)
if BG26__Gusty_Trumpeter:# 
	BG_Minion_Elemental+=['BG26_534']
	BG_PoolSet_Elemental.append('BG26_534')
	BG_Elemental_Gold['BG26_534']=''
class BG26_534_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_534:# (minion)
	""" Gusty Trumpeter
	After you sell 5 Elementals, get another random Elemental. <i>(@ left!)</i> """
	#
	pass

	BG_Minion_Elemental+=['BG26_534_G']
class BG26_534_G:# (minion)
	""" Gusty Trumpeter
	After you sell 5 Elementals, get two other random Elementals. <i>(@ left!)</i> """
	#
	pass

## Rock Rock (Elemental) (6)
BG26__Rock_Rock=(Config.BG_VERSION>=2620)
if BG26__Rock_Rock:# 
	BG_Minion_Elemental+=['BG26_535']
	BG_PoolSet_Elemental.append('BG26_535')
	BG_Elemental_Gold['BG26_535']=''
class BG26_535_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_535:# (minion)
	""" Rock Rock
	After you play an Elemental, give your other minions +2 Attack. <i>(Swaps to Health next turn!)</i>@After you play an Elemental, give your other minions +2 Health. <i>(Swaps to Attack next turn!)</i> """
	#
	pass

	BG_Minion_Elemental+=['BG26_535_G']
class BG26_535_G:# (minion)
	""" Rock Rock
	After you play an Elemental, give your other minions +4 Attack. <i>(Swaps to Health next turn!)</i>@After you play an Elemental, give your other minions +4 Health. <i>(Swaps to Attack next turn!)</i> """
	#
	pass

## Flourishing Frostling (Elemental) (2)
BG26__Flourishing_Frostling=(Config.BG_VERSION>=2620)
if BG26__Flourishing_Frostling:# 
	BG_Minion_Elemental+=['BG26_537']
	BG_PoolSet_Elemental.append('BG26_537')
	BG_Elemental_Gold['BG26_537']=''
class BG26_537_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_537:# (minion)
	""" Flourishing Frostling
	Has +1 Attack for each Elemental you played this ___game <i>(wherever this is)</i>. """
	#
	pass

	BG_Minion_Elemental+=['BG26_537_G']
class BG26_537_G:# (minion)
	""" Flourishing Frostling
	Has +2 Attack for each Elemental you played this ___game <i>(wherever this is)</i>. """
	#
	pass

