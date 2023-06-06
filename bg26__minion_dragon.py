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

## Electric Synthesizer (Dragon) (4)
BG26__Electric_Synthesizer=(Config.BG_VERSION>=2620)
if BG26__Electric_Synthesizer:# 
	BG_Minion_Dragon+=['BG26_963']
	BG_PoolSet_Dragon.append('BG26_963')
	BG_Dragon_Gold['BG26_963']='BG26_963_G'
class BG26_963_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_963:# (minion)
	""" Electric Synthesizer
	<b>Battlecry:</b> Give your other Dragons +3 Attack. """
	#
	pass

	BG_Minion_Dragon+=['BG26_963_G']
class BG26_963_G:# (minion)
	""" Electric Synthesizer
	<b>Battlecry:</b> Give your other Dragons +6 Attack. """
	#
	pass

## Stormbringer (Dragon) (4)
BG26__Stormbringer=(Config.BG_VERSION>=2620)
if BG26__Stormbringer:# 
	BG_Minion_Dragon+=['BG26_966']
	BG_PoolSet_Dragon.append('BG26_966')
	BG_Dragon_Gold['BG26_966']='BG26_966_G'
class BG26_966_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_966:# (minion)
	""" Stormbringer
	After a different friendly Dragon gains Attack, this also gains it. """
	#
	pass

	BG_Minion_Dragon+=['BG26_966_G']
class BG26_966_G:# (minion)
	""" Stormbringer
	After a different friendly Dragon gains Attack, this also gains it twice. """
	#
	pass
