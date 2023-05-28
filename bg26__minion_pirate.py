from ..utils import *

BG26_=[]


## Upbeat Impressionist (Pirate) (5)
BG26__Upbeat_Impressionist=(Config.BG_VERSION>=2620)
if BG26__Upbeat_Impressionist:# 
	BG_Minion_Pirate+=['BG26_124']
	BG_PoolSet_Pirate.append('BG26_124')
	BG_Pirate_Gold['BG26_124']=''
class BG26_124_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_124:# (minion)
	""" Upbeat Impressionist
	At the end of every 2 turns, make a random Pirate in your hand Golden. <i>({0} |4(turn, turns) left!)</i>@At the end of every 2 turns, make a random Pirate in your hand Golden. <i>(End of this turn!)</i> """
	#
	pass

	BG_Minion_Pirate+=['BG26_124_G']
class BG26_124_G:# (minion)
	""" Upbeat Impressionist
	At the end of every 2 turns, make 2 random Pirates in your hand Golden. <i>({0} |4(turn, turns) left!)</i>@At the end of every 2 turns, make 2 random Pirates in your hand Golden. <i>(End of this turn!)</i> """
	#
	pass

## Southsea Busker (Pirate) (1)
BG26__Southsea_Busker=(Config.BG_VERSION>=2620)
if BG26__Southsea_Busker:# 
	BG_Minion_Pirate+=['BG26_135']
	BG_PoolSet_Pirate.append('BG26_135')
	BG_Pirate_Gold['BG26_135']=''
class BG26_135_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_135:# (minion)
	""" Southsea Busker
	<b>Battlecry:</b> Gain 1 Gold next turn. """
	#
	pass

	BG_Minion_Pirate+=['BG26_135_G']
class BG26_135_G:# (minion)
	""" Southsea Busker
	<b>Battlecry:</b> Gain 2 Gold next turn. """
	#
	pass

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

## Gunpowder Courier (Pirate) (3)
BG26__Gunpowder_Courier=(Config.BG_VERSION>=2620)
if BG26__Gunpowder_Courier:# 
	BG_Minion_Pirate+=['BG26_810']
	BG_PoolSet_Pirate.append('BG26_810')
	BG_Pirate_Gold['BG26_810']=''
class BG26_810_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_810:# (minion)
	""" Gunpowder Courier
	After you spend 5 Gold, give your Pirates +1 Attack. <i>(@ Gold left!)</i> """
	#
	pass

	BG_Minion_Pirate+=['BG26_810_G']
class BG26_810_G:# (minion)
	""" Gunpowder Courier
	After you spend 5 Gold, give your Pirates +2 Attack. <i>(@ Gold left!)</i> """
	#
	pass

## Record Smuggler (Pirate) (5)
BG26__Record_Smuggler=(Config.BG_VERSION>=2620)
if BG26__Record_Smuggler:# 
	BG_Minion_Pirate+=['BG26_812']
	BG_PoolSet_Pirate.append('BG26_812')
	BG_Pirate_Gold['BG26_812']=''
class BG26_812_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_812:# (minion)
	""" Record Smuggler
	At the start of your turn, gain 1 Gold. Repeat for each other friendly Pirate. """
	#
	pass

	BG_Minion_Pirate+=['BG26_812_G']
class BG26_812_G:# (minion)
	""" Record Smuggler
	At the start of your turn, gain 2 Gold. Repeat for each other friendly Pirate. """
	#
	pass

## Lovesick Balladist (Pirate) (4)
BG26__Lovesick_Balladist=(Config.BG_VERSION>=2620)
if BG26__Lovesick_Balladist:# 
	BG_Minion_Pirate+=['BG26_814']
	BG_PoolSet_Pirate.append('BG26_814')
	BG_Pirate_Gold['BG26_814']=''
class BG26_814_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_814:# (minion)
	""" Lovesick Balladist
	<b>Battlecry:</b> Give a Pirate +1 Health for each Gold spent this turn. """
	#
	pass

	BG_Minion_Pirate+=['BG26_814_G']
class BG26_814_G:# (minion)
	""" Lovesick Balladist
	<b>Battlecry:</b> Give a Pirate +2 Health for each Gold spent this turn. """
	#
	pass

## Underhanded Dealer (Pirate) (5)
BG26__Underhanded_Dealer=(Config.BG_VERSION>=2620)
if BG26__Underhanded_Dealer:# 
	BG_Minion_Pirate+=['BG26_815']
	BG_PoolSet_Pirate.append('BG26_815')
	BG_Pirate_Gold['BG26_815']=''
class BG26_815_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_815:# (minion)
	""" Underhanded Dealer
	After you gain Gold, gain +1/+1. """
	#
	pass

	BG_Minion_Pirate+=['BG26_815_G']
class BG26_815_G:# (minion)
	""" Underhanded Dealer
	After you gain Gold, gain +2/+2. """
	#
	pass

## Blade Collector (Pirate) (4)
BG26__Blade_Collector=(Config.BG_VERSION>=2620)
if BG26__Blade_Collector:# 
	BG_Minion_Pirate+=['BG26_817']
	BG_PoolSet_Pirate.append('BG26_817')
	BG_Pirate_Gold['BG26_817']=''
class BG26_817_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_817:# (minion)
	""" Blade Collector
	Also damages the minions next to whomever this attacks. """
	#
	pass

	BG_Minion_Pirate+=['BG26_817_G']
class BG26_817_G:# (minion)
	""" Blade Collector
	Also damages the minions next to whomever this attacks. """
	#
	pass

