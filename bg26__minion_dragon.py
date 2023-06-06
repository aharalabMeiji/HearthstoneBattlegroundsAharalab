## Disco Shuffler (Dragon) (5)
BG26__Disco_Shuffler=(Config.BG_VERSION>=2620)
if BG26__Disco_Shuffler:# 
	BG_Minion_Dragon+=['BG26_355']
	BG_PoolSet_Dragon.append('BG26_355')
	BG_Dragon_Gold['BG26_355']='BG26_355_G'
class BG26_355_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_355:# (minion)
	""" Disco Shuffler
	<b>Choose One - </b>Trigger a friendly minion's <b>Battlecry</b>; or <b>Discover</b> a <b>Battlecry</b> minion. """
	#
	pass

	BG_Minion_Dragon+=['BG26_355_G']
class BG26_355_G:# (minion)
	""" Disco Shuffler
	<b>Choose One - </b>Trigger a friendly minion's <b>Battlecry</b> twice; or <b>Discover</b> 2 <b>Battlecry</b> minions. """
	#
	pass

## Sanctum Rester (Dragon) (5)
BG26__Sanctum_Rester=(Config.BG_VERSION>=2620)
if BG26__Sanctum_Rester:# 
	BG_Minion_Dragon+=['BG26_356']
	BG_PoolSet_Dragon.append('BG26_356')
	BG_Dragon_Gold['BG26_356']='BG26_356_G'
class BG26_356_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_356:# (minion)
	""" Sanctum Rester
	<b>Start of Combat:</b> Give your other Dragons +8 Health. """
	#
	pass

	BG_Minion_Dragon+=['BG26_356_G']
class BG26_356_G:# (minion)
	""" Sanctum Rester
	<b>Start of Combat:</b> Give your other Dragons +16 Health. """
	#
	pass
