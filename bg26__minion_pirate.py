from ..utils import *

BG26_=[]


## Fleet Admiral Tethys (Pirate) (6)
BG26__Fleet_Admiral_Tethys=(Config.BG_VERSION>=2620)
if BG26__Fleet_Admiral_Tethys:# 
	BG_Minion_Pirate+=['BG26_766']
	BG_PoolSet_Pirate.append('BG26_766')
	BG_Pirate_Gold['BG26_766']=''
class BG26_766_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_766:# (minion)
	""" Fleet Admiral Tethys
	After you spend 8 Gold, get another random Pirate. <i>(@ Gold left!)</i> """
	#
	pass

	BG_Minion_Pirate+=['BG26_766_G']
class BG26_766_G:# (minion)
	""" Fleet Admiral Tethys
	After you spend 8 Gold, get 2 other random Pirates. <i>(@ Gold left!)</i> """
	#
	pass

