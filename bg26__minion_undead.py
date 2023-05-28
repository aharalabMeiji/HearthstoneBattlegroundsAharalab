from ..utils import *

BG26_=[]


## Xylo-bones (Undead) (4)
BG26__Xylo_bones=(Config.BG_VERSION>=2620)
if BG26__Xylo_bones:# 
	BG_Minion_Undead+=['BG26_172']
	BG_PoolSet_Undead.append('BG26_172')
	BG_Undead_Gold['BG26_172']=''
class BG26_172_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_172:# (minion)
	""" Xylo-bones
	After you summon a minion in combat, gain +3 Health permanently. """
	#
	pass

	BG_Minion_Undead+=['BG26_172_G']
class BG26_172_G:# (minion)
	""" Xylo-bones
	After you summon a minion in combat, gain +6 Health permanently. """
	#
	pass

