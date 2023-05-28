from ..utils import *

BG26_=[]


## Lullabot (Mecha) (2)
BG26__Lullabot=(Config.BG_VERSION>=2620)
if BG26__Lullabot:# 
	BG_Minion_Mecha+=['BG26_146']
	BG_PoolSet_Mecha.append('BG26_146')
	BG_Mecha_Gold['BG26_146']=''
class BG26_146_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_146:# (minion)
	""" Lullabot
	<b>Magnetic</b> At the end of your turn, gain +1/+1. """
	#
	pass

	BG_Minion_Mecha+=['BG26_146_G']
class BG26_146_G:# (minion)
	""" Lullabot
	<b>Magnetic</b> At the end of your turn, gain +2/+2. """
	#
	pass

## Accord-o-Tron (Mecha) (3)
BG26__Accord_o_Tron=(Config.BG_VERSION>=2620)
if BG26__Accord_o_Tron:# 
	BG_Minion_Mecha+=['BG26_147']
	BG_PoolSet_Mecha.append('BG26_147')
	BG_Mecha_Gold['BG26_147']=''
class BG26_147_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_147:# (minion)
	""" Accord-o-Tron
	<b>Magnetic</b> At the start of your turn, gain 1 extra Gold. """
	#
	pass

	BG_Minion_Mecha+=['BG26_147_G']
class BG26_147_G:# (minion)
	""" Accord-o-Tron
	<b>Magnetic</b> At the start of your turn, gain 2 extra Gold. """
	#
	pass

## Scrap Scraper (Mecha) (4)
BG26__Scrap_Scraper=(Config.BG_VERSION>=2620)
if BG26__Scrap_Scraper:# 
	BG_Minion_Mecha+=['BG26_148']
	BG_PoolSet_Mecha.append('BG26_148')
	BG_Mecha_Gold['BG26_148']=''
class BG26_148_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_148:# (minion)
	""" Scrap Scraper
	<b>Avenge (4):</b> Get a random <b>Magnetic</b> Mech. """
	#
	pass

	BG_Minion_Mecha+=['BG26_148_G']
class BG26_148_G:# (minion)
	""" Scrap Scraper
	<b>Avenge (4):</b> Get 2 random <b>Magnetic</b> Mechs. """
	#
	pass

## Polarizing Beatboxer (Mecha) (6)
BG26__Polarizing_Beatboxer=(Config.BG_VERSION>=2620)
if BG26__Polarizing_Beatboxer:# 
	BG_Minion_Mecha+=['BG26_149']
	BG_PoolSet_Mecha.append('BG26_149')
	BG_Mecha_Gold['BG26_149']=''
class BG26_149_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_149:# (minion)
	""" Polarizing Beatboxer
	Whenever you <b>Magnetize</b> another minion, it also <b>Magnetizes</b> to this. """
	#
	pass

	BG_Minion_Mecha+=['BG26_149_G']
class BG26_149_G:# (minion)
	""" Polarizing Beatboxer
	Whenever you <b>Magnetize</b> another minion, it also _<b>Magnetizes</b> to this twice. """
	#
	pass

## Utility Drone (Mecha) (5)
BG26__Utility_Drone=(Config.BG_VERSION>=2620)
if BG26__Utility_Drone:# 
	BG_Minion_Mecha+=['BG26_152']
	BG_PoolSet_Mecha.append('BG26_152')
	BG_Mecha_Gold['BG26_152']=''
class BG26_152_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_152:# (minion)
	""" Utility Drone
	At the end of your turn, give your minions +1/+1 for each <b>Magnetization</b> they have. """
	#
	pass

	BG_Minion_Mecha+=['BG26_152_G']
class BG26_152_G:# (minion)
	""" Utility Drone
	At the end of your turn, give your minions +2/+2 for each <b>Magnetization</b> they have. """
	#
	pass

