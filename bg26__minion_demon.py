
## Tichondrius (Demon) (5)
BG26__Tichondrius=(Config.BG_VERSION>=2620)
if BG26__Tichondrius:# 
	BG_Minion_Demon+=['BG26_523']
	BG_PoolSet_Demon.append('BG26_523')
	BG_Demon_Gold['BG26_523']=''
class BG26_523_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_523:# (minion)(demon)
	""" Tichondrius
	After your hero takes damage, give your other Demons +1/+1. """
	#
	pass

	BG_Minion_Demon+=['BG26_523_G']
class BG26_523_G:# (minion)(demon)
	""" Tichondrius
	After your hero takes damage, give your other Demons +2/+2. """
	#
	pass

## Malchezaar, Prince of Dance (Demon) (3)
BG26__Malchezaar,_Prince_of_Dance=(Config.BG_VERSION>=2620)
if BG26__Malchezaar,_Prince_of_Dance:# 
	BG_Minion_Demon+=['BG26_524']
	BG_PoolSet_Demon.append('BG26_524')
	BG_Demon_Gold['BG26_524']=''
class BG26_524_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_524:# (minion)(demon)
	""" Malchezaar, Prince of Dance
	2 Refreshes each turn cost Health instead of Gold. <i>(@ left!)</i> """
	#
	pass

	BG_Minion_Demon+=['BG26_524_G']
class BG26_524_G:# (minion)(demon)
	""" Malchezaar, Prince of Dance
	4 Refreshes each turn cost Health instead of Gold. <i>(@ left!)</i> """
	#
	pass

## Imposing Percussionist (Demon) (5)
BG26__Imposing_Percussionist=(Config.BG_VERSION>=2620)
if BG26__Imposing_Percussionist:# 
	BG_Minion_Demon+=['BG26_525']
	BG_PoolSet_Demon.append('BG26_525')
	BG_Demon_Gold['BG26_525']=''
class BG26_525_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_525:# (minion)(demon)
	""" Imposing Percussionist
	<b>Battlecry: Discover</b> a Demon. Deal damage to your hero equal to its Tier._ """
	#
	pass

	BG_Minion_Demon+=['BG26_525_G']
class BG26_525_G:# (minion)(demon)
	""" Imposing Percussionist
	<b>Battlecry: Discover</b> 2 Demons. Deal damage to your hero equal to their Tiers._ """
	#
	pass
