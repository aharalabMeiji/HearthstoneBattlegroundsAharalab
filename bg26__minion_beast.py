from ..utils import *

BG26_=[]


## Manasaber (Beast) (1)
BG26__Manasaber=(Config.BG_VERSION>=2620)
if BG26__Manasaber:# 
	BG_Minion_Beast+=['BG26_800']
	BG_PoolSet_Beast.append('BG26_800')
	BG_Beast_Gold['BG26_800']=''
class BG26_800_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_800:# (minion)
	""" Manasaber
	<b>Deathrattle:</b> Summon two 0/1 Cublings with <b>Taunt</b>. """
	#
	pass

	BG_Minion_Beast+=['BG26_800_G']
class BG26_800_G:# (minion)
	""" Manasaber
	<b>Deathrattle:</b> Summon two 0/2 Cublings with <b>Taunt</b>. """
	#
	pass

	BG_Minion_Beast+=['BG26_800_Gt']
class BG26_800_Gt:# (minion)
	""" Cubling
	<b>Taunt</b> """
	#
	pass

	BG_Minion_Beast+=['BG26_800t']
class BG26_800t:# (minion)
	""" Cubling
	<b>Taunt</b> """
	#
	pass

## Rylak Metalhead (Beast) (3)
BG26__Rylak_Metalhead=(Config.BG_VERSION>=2620)
if BG26__Rylak_Metalhead:# 
	BG_Minion_Beast+=['BG26_801']
	BG_PoolSet_Beast.append('BG26_801')
	BG_Beast_Gold['BG26_801']=''
class BG26_801_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_801:# (minion)
	""" Rylak Metalhead
	<b>Taunt</b> <b>Deathrattle:</b> Trigger the <b>Battlecries</b> of adjacent minions. """
	#
	pass

	BG_Minion_Beast+=['BG26_801_G']
class BG26_801_G:# (minion)
	""" Rylak Metalhead
	<b>Taunt</b> <b>Deathrattle:</b> Trigger the <b>Battlecries</b> of adjacent minions twice. """
	#
	pass

## Banana Slamma (Beast) (4)
BG26__Banana_Slamma=(Config.BG_VERSION>=2620)
if BG26__Banana_Slamma:# 
	BG_Minion_Beast+=['BG26_802']
	BG_PoolSet_Beast.append('BG26_802')
	BG_Beast_Gold['BG26_802']=''
class BG26_802_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_802:# (minion)
	""" Banana Slamma
	After you summon a Beast in combat, double its stats. """
	#
	pass

	BG_Minion_Beast+=['BG26_802_G']
class BG26_802_G:# (minion)
	""" Banana Slamma
	After you summon a Beast in combat, triple its stats. """
	#
	pass

## Tentacle of Octosari (Beast) (1)
BG26__Tentacle_of_Octosari=(Config.BG_VERSION>=2620)
if BG26__Tentacle_of_Octosari:# 
	BG_Minion_Beast+=['BG26_803_Gt']
	BG_PoolSet_Beast.append('BG26_803_Gt')
	BG_Beast_Gold['BG26_803_Gt']=''
class BG26_803_Gt_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_803_Gt:# (minion)
	""" Tentacle of Octosari
	 """
	#
	pass

## Tentacle of Octosari (Beast) (1)
BG26__Tentacle_of_Octosari=(Config.BG_VERSION>=2620)
if BG26__Tentacle_of_Octosari:# 
	BG_Minion_Beast+=['BG26_803t']
	BG_PoolSet_Beast.append('BG26_803t')
	BG_Beast_Gold['BG26_803t']=''
class BG26_803t_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_803t:# (minion)
	""" Tentacle of Octosari
	 """
	#
	pass

## Octosari, Wrap God (Beast) (6)
BG26__Octosari,_Wrap_God=(Config.BG_VERSION>=2620)
if BG26__Octosari,_Wrap_God:# 
	BG_Minion_Beast+=['BG26_804']
	BG_PoolSet_Beast.append('BG26_804')
	BG_Beast_Gold['BG26_804']=''
class BG26_804_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_804:# (minion)
	""" Octosari, Wrap God
	<b>Deathrattle:</b> Summon a @/@ Tentacle. <i>(It gains +2/+2  permanently after you summon a minion in combat!)</i> """
	#
	pass

	BG_Minion_Beast+=['BG26_804_G']
class BG26_804_G:# (minion)
	""" Octosari, Wrap God
	<b>Deathrattle:</b> Summon a @/@ Tentacle. <i>(It gains +4/+4  permanently after you summon a minion in combat!)</i> """
	#
	pass

## Humming Bird (Beast) (2)
BG26__Humming_Bird=(Config.BG_VERSION>=2620)
if BG26__Humming_Bird:# 
	BG_Minion_Beast+=['BG26_805']
	BG_PoolSet_Beast.append('BG26_805')
	BG_Beast_Gold['BG26_805']=''
class BG26_805_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_805:# (minion)
	""" Humming Bird
	Your other Beasts have +2 Attack. """
	#
	pass

	BG_Minion_Beast+=['BG26_805_G']
class BG26_805_G:# (minion)
	""" Humming Bird
	Your other Beasts have +4 Attack. """
	#
	pass

