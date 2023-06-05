from ..utils import *

BG26_=[]


## Silent Swimmer (Naga) (4)
BG26__Silent_Swimmer=(Config.BG_VERSION>=2620)
if BG26__Silent_Swimmer:# 
	BG_Minion_Naga+=['BG26_171']
	BG_PoolSet_Naga.append('BG26_171')
	BG_Naga_Gold['BG26_171']=''
class BG26_171_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_171:# (minion)
	""" Silent Swimmer
	<b>Spellcraft:</b> Give a minion +3/+5 and <b>Stealth</b> until next turn. """
	#
	pass

	BG_Minion_Naga+=['BG26_171_G']
class BG26_171_G:# (minion)
	""" Silent Swimmer
	<b>Spellcraft:</b> Give a minion +6/+10 and <b>Stealth</b> until next turn. """
	#
	pass

## Deep Blue Crooner (Naga) (4)
BG26__Deep_Blue_Crooner=(Config.BG_VERSION>=2620)
if BG26__Deep_Blue_Crooner:# 
	BG_Minion_Naga+=['BG26_502']
	BG_PoolSet_Naga.append('BG26_502')
	BG_Naga_Gold['BG26_502']=''
class BG26_502_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_502:# (minion)
	""" Deep Blue Crooner
	<b>Spellcraft:</b> Give a minion +@/+@ until next turn. Improve your future Deep Blues. """
	#
	pass

	BG_Minion_Naga+=['BG26_502_G']
class BG26_502_G:# (minion)
	""" Deep Blue Crooner
	<b>Spellcraft:</b> Give a minion +@/+@ until next turn. Improve your future Deep Blues. """
	#
	pass


