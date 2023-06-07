from ..utils import *

BG_Dozy_Whelp=(Config.BG_VERSION>=2460) #(1) new 24.6 ### OK ###
BG_Evolving_Chromawing=(Config.BG_VERSION<2360 or (Config.BG_VERSION>=2400 and Config.BG_VERSION<2620))##(1) banned 23.6, revive 24.0, revised 24.0.3 ## banned 26.2
BG_Red_Whelp=(Config.BG_VERSION<2620) ## ##(1) ## banned 26.2
BG26__Upbeat_Frontdrake=(Config.BG_VERSION>=2620) # (1)

#BG_Blazing_Sklyfin=True ## (2/1/3) -> dragon/murloc
BG_Glyph_Guardian=(Config.BG_VERSION<2560) ## ##(2) ###banned 25.?
BG_Steward_of_Time=(Config.BG_VERSION<2420) ####(2) ##banned 24.2
BG_Twilight_Emissary=True ##(2/3/3)
BG26__Low_Flier=(Config.BG_VERSION>=2620) # (2)

BG24__Amber_Guardian=(Config.BG_VERSION>=2420)# (3) new 24.2
BG_Bronze_Warden=True ##(3)
BG_Drakonid_Enforcer=False ##(3) ## banned when?
BG24__Nether_Drake=(Config.BG_VERSION>=2420 and Config.BG_VERSION<2620)# (3) new 24.2 (2)->(3) ## banned 26.2

BG_Atramedes=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2620) ## (4)  23.6 ##OK## banned 26.2
BG25__Chronormu=(Config.BG_VERSION<2562)# 4/4/4 dragon ## 25.2.2
BG_Cobalt_Scalebane=(Config.BG_VERSION<2420) ##(4) banned 24.2
BG25__General_Drakkisath=(Config.BG_VERSION>=2522)# 4/2/8 DRAGON ## new 25.2.2
BG_Prestor_s_Pyrospawn=False ## (4) banned
BG_Prized_Promo_Drake=True ##(4)
BG_Tarecgosa=True ##(3)->(4)
BG26__Electric_Synthesizer=(Config.BG_VERSION>=2620) #(4)
BG26__Stormbringer=(Config.BG_VERSION>=2620) #(4/1/7)


BG_Murozond=True ##(5)
BG_Razorgore_the_Untamed=(Config.BG_VERSION>=2562 and Config.BG_VERSION<2620) ## (5) ## banned when? ## revive 25.6.2 ## banned 26.2
BG25__Cyborg_Drake=(Config.BG_VERSION>=2522 and Config.BG_VERSION<2620)# 5/2/8 dragon ## new 25.2.2 ## banned 26.2
BG26__Disco_Shuffler=(Config.BG_VERSION>=2620)# (5/4/3)
BG26__Sanctum_Rester=(Config.BG_VERSION>=2620)# (5/5/5)

BG_Kalecgos_Arcane_Aspect=True ## (6)

BG_Minion_Dragon =[]

BG_PoolSet_Dragon=[]

BG_Dragon_Gold={}

if BG_Evolving_Chromawing:#Evolving Chromawing(1) ## banned 23.6, revive 26.0 banned 26.2
	BG_Minion_Dragon+=['BG21_027','BG21_027e','BG21_027_G','BG21_027_Ge',]#
	BG_PoolSet_Dragon.append('BG21_027')
	BG_Dragon_Gold['BG21_027']='BG21_027_G' #	
#Evolving Chromawing(1)  ### OK ###
class BG21_027_Buff(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, buff, amount):
		count=0#>= 26.0
		for card in target.controller.field:#>= 24.0
			#if card.race==Race.DRAGON:#>= 24.0
			if race_identity(card,Race.DRAGON):#>= 24.0
				count += 1#>= 24.0
		Buff(target, buff, atk=count*amount).trigger(source)#>= 24.0.3
		#Buff(target, buff, atk=count*amount, max_health=count*amount).trigger(source)#>= 24.0
class BG21_027:# <12>[1453]
	""" Evolving Chromawing
	After you upgrade your Tavern Tier, gain +1 Attack __for each friendly Dragon.."""  #>= 24.0.3
	##After you upgrade your Tavern Tier, gain +1/+1 for each friendly Dragon."""  #>= 24.0
	##After you upgrade your Tavern Tier, double this minion's Attack. """ #<= 23.4
	events = UpgradeTier(CONTROLLER).after(BG21_027_Buff(SELF, 'BG21_027e',1 ))
	pass
class BG21_027e:
	pass
class BG21_027_G:# <12>[1453]
	""" Evolving Chromawing
	After you upgrade your Tavern Tier, gain +2 Attack __for each friendly Dragon. """
	events = UpgradeTier(CONTROLLER).after(BG21_027_Buff(SELF, 'BG21_027_Ge', 2))
	pass
class BG21_027_Ge:
	pass


#Red Whelp(1) ### need check ### banned 26.2
if BG_Red_Whelp:
	BG_Minion_Dragon+=['BGS_019','TB_BaconUps_102']#
	BG_PoolSet_Dragon.append('BGS_019')
	BG_Dragon_Gold['BGS_019']='TB_BaconUps_102' #	
class BGS_019_Action(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		controller=target
		if len(controller.opponent.field)==0:
			return 
		count=0
		for card in controller.field:
			#if card.race==Race.DRAGON:
			if race_identity(card,Race.DRAGON):
				count += 1
		for i in range(amount):
			if len(controller.opponent.field):
				target = random.choice(controller.opponent.field)
				Hit(target, count).trigger(source)
				##controller.game.process_deaths()## contained in Hit
class BGS_019:# <12>[1453]
	""" Red Whelp
	[Start of Combat:] Deal1 damage per friendly Dragon to one random enemy minion. """
	events = BeginBattle(CONTROLLER).on(BGS_019_Action(CONTROLLER, 1))
	pass
class TB_BaconUps_102:# <12>[1453]
	""" Red Whelp
	[Start of Combat:] Deal1 damage per friendlyDragon to one randomenemy minion twice. """
	events = BeginBattle(CONTROLLER).on(BGS_019_Action(CONTROLLER, 2))
	pass


#Dozy Whelp（dragon 1）(BG24_300) ### OK ###
if BG_Dozy_Whelp:
	BG_Minion_Dragon+=['BG24_300','BG24_300e','BG24_300_G','BG24_300_Ge']#
	BG_PoolSet_Dragon.append('BG24_300')
	BG_Dragon_Gold['BG24_300']='BG24_300_G' #	
class BG24_300_Target(TargetedAction):
	CARD=ActionArg()
	BUFF=ActionArg()
	def do(self, source, card, buff):
		assert source.game.this_is_battle==True, 'This is a battle.'
		Buff(card, buff).trigger(source)
		if card.deepcopy_original!=None:
			Buff(card.deepcopy_original, buff).trigger(source)
class BG24_300:
	""" Dozy Whelp (1) (0/3)
	[[Taunt].] Whenever this is attacked, gain +1 Attack permanently."""
	events = Attack(ENEMY, SELF).on(BG24_300_Target(SELF, 'BG24_300e'))
	pass
BG24_300e=buff(1,0)
class BG24_300_G:
	events = Attack(ENEMY, SELF).on(BG24_300_Target(SELF, 'BG24_300_Ge'))
	pass
BG24_300_Ge=buff(2,0)


## Upbeat Frontdrake (Dragon) (1)
#BG26__Upbeat_Frontdrake=(Config.BG_VERSION>=2620) # (1)
if BG26__Upbeat_Frontdrake:# 
	BG_Minion_Dragon+=['BG26_529']
	BG_Minion_Dragon+=['BG26_529_G']
	BG_PoolSet_Dragon.append('BG26_529')
	BG_Dragon_Gold['BG26_529']='BG26_529_G'
class BG26_529_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_529:# (minion)
	""" Upbeat Frontdrake
	At the end of every 3 turns, get another random Dragon. <i>({0} |4(turn, turns) left!)</i>@At the end of every 3 turns, get another random Dragon. <i>(End of this turn!)</i> """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 3, [Give(CONTROLLER, RandomBGDragon(tech_level_less=TIER(CONTROLLER)))]))
	pass
class BG26_529_G:# (minion)
	""" Upbeat Frontdrake
	At the end of every 3 turns, get 2 other random Dragons. <i>({0} |4(turn, turns) left!)</i>@At the end of every 3 turns, get 2 other random Dragons. <i>(End of this turn!)</i> """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 3, [
		Give(CONTROLLER, RandomBGDragon(tech_level_less=TIER(CONTROLLER))),
		Give(CONTROLLER, RandomBGDragon(tech_level_less=TIER(CONTROLLER)))]))
	pass


#### TIER 2 ###

#Glyph Guardian(2)   ### need check ###
if BG_Glyph_Guardian:
	BG_Minion_Dragon+=['BGS_045','BGS_045e','TB_BaconUps_115','TB_BaconUps_115e']#
	BG_PoolSet_Dragon.append('BGS_045')
	BG_Dragon_Gold['BGS_045']='TB_BaconUps_115' #	
class BGS_045_Buff(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, buff, amount):
		Buff(target, buff, atk=target.atk*amount).trigger(source)
class BGS_045:# <4>[1453]
	""" Glyph Guardian
	Whenever this attacks, double its Attack. """
	events = BG_Attack(SELF).on(BGS_045_Buff(SELF,'BGS_045e',1))
	pass
class BGS_045e:
	pass
class TB_BaconUps_115:# <4>[1453]
	""" Glyph Guardian
	Whenever this attacks, triple its Attack. """
	events = BG_Attack(SELF).on(BGS_045_Buff(SELF,'TB_BaconUps_115e',2))
	pass
class TB_BaconUps_115e:
	pass


#Steward of Time(2) ### OK ### ### banned 24.2
if BG_Steward_of_Time:
	BG_Minion_Dragon+=['BGS_037','BGS_037e','TB_BaconUps_107','TB_BaconUps_107e']#
	BG_PoolSet_Dragon.append('BGS_037')
	BG_Dragon_Gold['BGS_037']='TB_BaconUps_107' #	
class BGS_037:
	""" Steward of Time
	When you sell this minion, give all minions in Bob's Tavern +2/+1."""
	events = Sell(CONTROLLER, FRIENDLY + ID('BGS_037')).on(Buff(ENEMY_MINIONS, 'BGS_037e'))
BGS_037e=buff(2,1)
class TB_BaconUps_107:
	""" Steward of Time
	When you sell this minion, give all minions in Bob's Tavern +4/+2."""
	events = Sell(CONTROLLER, FRIENDLY + ID('TB_BaconUps_107')).on(Buff(ENEMY_MINIONS, 'TB_BaconUps_107e'))
TB_BaconUps_107e=buff(4,2)


from .BG_minion_murloc import BG_Blazing_Skyfin
### Blazing Skyfin (2/1/3) ## new 25.2.2
if BG_Blazing_Skyfin:
	##BG_Minion_Dragon+=['BG25_040','BG25_040_G','BG25_040e','BG25_040_Ge']
	BG_PoolSet_Dragon.append('BG25_040')
	BG_Dragon_Gold['BG25_040']='BG25_040_G'




## Low-Flier (Dragon) (2)
#BG26__Low_Flier=(Config.BG_VERSION>=2620) # (2)
if BG26__Low_Flier:# 
	BG_Minion_Dragon+=['BG26_969','BG26_969e']
	BG_Minion_Dragon+=['BG26_969_G','BG26_969_Ge']
	BG_PoolSet_Dragon.append('BG26_969')
	BG_Dragon_Gold['BG26_969']='BG26_969_G'
class BG26_969_Action(GameAction):# 
	BUFF=ActionArg()
	def do(self, source, buff):# 
		amount = source.atk
		for card in source.controller.field:
			if card.atk<amount:
				Buff(card, buff).trigger(source)
		pass# 
class BG26_969:# (minion)
	""" Low-Flier
	At the end of your turn, give +1 Attack to your minions ___with less Attack than this. """
	events = OWN_TURN_END.on(BG26_969_Action('BG26_969e'))
	pass
BG26_969e=buff(1,0)
class BG26_969_G:# (minion)
	""" Low-Flier
	At the end of your turn, give +2 Attack to your minions ___with less Attack than this. """
	events = OWN_TURN_END.on(BG26_969_Action('BG26_969_Ge'))
	pass
BG26_969_Ge=buff(2,0)



#### TIER 3 #########



if BG24__Nether_Drake:# (3)  new 24.2 ### visually OK ## banned 26.2
	BG_Minion_Dragon+=['BG24_003','BG24_003e','BG24_003_G','BG24_003_Ge']
	BG_PoolSet_Dragon.append('BG24_003')
	BG_Dragon_Gold['BG24_003']='BG24_003_G'
class BG24_003:# (minion) (2/0/4)
	""" Nether Drake
	At the end of your turn, give your Dragons +1 Attack. """
	events = OWN_TURN_END.on(Buff(FRIENDLY_MINIONS + DRAGON, 'BG24_003e'))
	pass
BG24_003e=buff(1,0)
class BG24_003_G:# (minion)
	""" Nether Drake
	At the end of your turn, give your Dragons +2 Attack. """
	events = OWN_TURN_END.on(Buff(FRIENDLY_MINIONS + DRAGON, 'BG24_003_Ge'))
	pass
BG24_003_Ge=buff(2,0)



#Bronze Warden(3)  ### OK ###
if BG_Bronze_Warden:
	BG_Minion_Dragon+=['BGS_034','TB_BaconUps_149']#
	BG_PoolSet_Dragon.append('BGS_034')
	BG_Dragon_Gold['BGS_034']='TB_BaconUps_149' #	
class BGS_034:# <12>[1453]
	""" Bronze Warden
	[Divine Shield][Reborn] """
	#<Tag enumID="194" name="DIVINE_SHIELD" type="Int" value="1"/>
	#<Tag enumID="1085" name="REBORN" type="Int" value="1"/>
	pass
class TB_BaconUps_149:# <12>[1453]
	""" Bronze Warden
	[Divine Shield][Reborn] """
	pass




#Drakonid Enforcer(4)  ### OK ## (3)->(4)
if BG_Drakonid_Enforcer:
	BG_Minion_Dragon+=['BGS_067','BGS_067e','TB_BaconUps_117','TB_BaconUps_117e']#
	BG_PoolSet_Dragon.append('BGS_067')
	BG_Dragon_Gold['BGS_067']='TB_BaconUps_117' #	
class BGS_067:# <12>[1453]
	""" Drakonid Enforcer
	After a friendly minion loses [Divine Shield], gain_+2/+2. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(Buff(SELF,'BGS_067e'))
	pass
BGS_067e=buff(2,2)
class TB_BaconUps_117:# <12>[1453]
	""" Drakonid Enforcer
	After a friendly minion loses [Divine Shield], gain_+4/+4. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(Buff(SELF,'TB_BaconUps_117e'))
	pass
TB_BaconUps_117e=buff(4,4)




#Twilight Emissary(3)  ### OK ### (3)->(2)
if BG_Twilight_Emissary:
	BG_Minion_Dragon+=['BGS_038','BGS_038e','TB_BaconUps_108','TB_BaconUps_108e']#
	BG_PoolSet_Dragon.append('BGS_038')
	BG_Dragon_Gold['BGS_038']='TB_BaconUps_108' #	
class BGS_038:# <12>[1453]
	""" Twilight Emissary
	[Taunt][Battlecry:] Give a friendly Dragon +2/+2. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DRAGON }
	play = Buff(TARGET, 'BGS_038e')
	pass
BGS_038e=buff(2,2)
class TB_BaconUps_108:# <12>[1453]
	""" Twilight Emissary
	[Taunt][Battlecry:] Give a friendly Dragon +4/+4. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DRAGON } 
	play = Buff(TARGET, 'TB_BaconUps_108e')
	pass
TB_BaconUps_108e=buff(4,4)


if BG24__Amber_Guardian:# (3) new 24.2 ## 
	BG_Minion_Dragon+=['BG24_500','BG24_500e','BG24_500_G','BG24_500_Ge']
	BG_PoolSet_Dragon.append('BG24_500')
	BG_Dragon_Gold['BG24_500']='BG24_500_G'
class BG24_500:# (minion)
	""" Amber Guardian
	[Start of Combat:] Give another friendly Dragon +3/+3 and [Divine Shield]. """
	events = BeginBattle(CONTROLLER).on(Buff(RANDOM(FRIENDLY + MINION + DRAGON - SELF), 'BG24_500e'))
	pass
#BG24_500e=buff(3,3,divine_shield=True)
class BG24_500e:
	tags={
		#GameTag.ATK:3,
		#GameTag.HEALTH:3
		GameTag.ATK:2,#24.2.2
		GameTag.HEALTH:2#24.2.2
		}
	def apply(self, target):
		SetDivineShield(target, True).trigger(self)
class BG24_500_G:# (minion)
	""" Amber Guardian
	[Start of Combat:] Give another friendly Dragon +6/+6 and [Divine Shield]. """
	events = BeginBattle(CONTROLLER).on(Buff(RANDOM(FRIENDLY_MINIONS + DRAGON - SELF), 'BG24_500_Ge'))
	pass
class BG24_500_Ge:
	tags={
		#GameTag.ATK:6,
		#GameTag.HEALTH:6
		GameTag.ATK:4,#24.2.2
		GameTag.HEALTH:4#24.2.2
		}
	def apply(self, target):
		SetDivineShield(target, True).trigger(self)



#Cobalt Scalebane(4)  ### OK ### banned 24.2
if BG_Cobalt_Scalebane:
	BG_Minion_Dragon+=['ICC_029','ICC_029e','TB_BaconUps_120','TB_BaconUps_120e']#
	BG_PoolSet_Dragon.append('ICC_029')
	BG_Dragon_Gold['ICC_029']='TB_BaconUps_120' #	
class ICC_029:
	""" Cobalt Scalebane
	At the end of your turn, give another random friendly minion +3 Attack. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS), 'ICC_029e'))
ICC_029e=buff(3,0)
class TB_BaconUps_120:# <12>[1453]
	""" Cobalt Scalebane
	At the end of your turn, give another random friendly minion +6 Attack. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS), 'TB_BaconUps_120e'))
TB_BaconUps_120e=buff(6,0)



#Prestor's Pyrospawn(4)  ### maybe ###
if BG_Prestor_s_Pyrospawn:
	BG_Minion_Dragon+=['BG21_012','BG21_012_G']#
	BG_PoolSet_Dragon.append('BG21_012')
	BG_Dragon_Gold['BG21_012']='BG21_012_G' #	
class BG21_012:# <12>[1453]
	""" Prestor's Pyrospawn
	Whenever another friendlyDragon attacks, deal 3 damage to its target. """
	events = BG_Attack(FRIENDLY + DRAGON - SELF).on(Hit(BG_Attack.OTHER, 3))
	pass
class BG21_012_G:# <12>[1453]
	""" Prestor's Pyrospawn
	Whenever another friendlyDragon attacks, deal 6 damage to its target. """
	events = BG_Attack(FRIENDLY + DRAGON - SELF).on(Hit(Attack.DEFENDER, 6))
	pass



#Prized Promo-Drake(4)   ### maybe ###
if BG_Prized_Promo_Drake:
	BG_Minion_Dragon+=['BG21_014','BG21_014e','BG21_014_G']#
	BG_PoolSet_Dragon.append('BG21_014')
	BG_Dragon_Gold['BG21_014']='BG21_014_G' #	
class BG21_014_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		if not isinstance(target, list):
			target = [target]
		count=0
		for card in source.controller.field:
			#if card.race==Race.DRAGON:
			if race_identity(card,Race.DRAGON):
				count += amount
		for card in target:
			Buff(card, buff, atk=count, max_health=count).trigger(source)
class BG21_014:# <12>[1453]
	""" Prized Promo-Drake
	[Start of Combat:] Give adjacent minions +1/+1__for each friendly Dragon. """
	events = BeginBattle(CONTROLLER).on(BG21_014_Action(SELF_ADJACENT, 'BG21_014e', 1))
	pass
class BG21_014e:# <12>[1453]
	""" Promoted
	Increased stats from Promo-Drake """
	pass
class BG21_014_G:# <12>[1453]
	""" Prized Promo-Drake
	[Start of Combat:] Giveadjacent minions +2/+2__for each friendly Dragon. """
	events = BeginBattle(CONTROLLER).on(BG21_014_Action(SELF_ADJACENT, 'BG21_014e', 2))
	pass






#Atramedes (4)   23.6 ### OK ### banned 26.2
if BG_Atramedes:
	BG_Minion_Dragon+=['BG23_362','BG23_362_G']#
	BG_PoolSet_Dragon.append('BG23_362')
	BG_Dragon_Gold['BG23_362']='BG23_362_G' #	
class BG23_362:
	"""Atramedes
	Whenever this attacks, deal 3 damage to the __target and its neighbors."""
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, 3))
	pass
class BG23_362_G:
	"""  """
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, 3), HitAdjacentMinions(BG_Attack.OTHER, 3))
	pass



if BG25__Chronormu:# 4/4/4 dragon ## 25.2.2
	BG_Minion_Dragon+=['BG25_104','BG25_104_G','BG25_104e']
	BG_PoolSet_Dragon.append('BG25_104')
	BG_Dragon_Gold['BG25_104']='BG25_104_G' #
class BG25_104_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		if source.controller==source.controller.game.bartender:
			Buff(source, 'BG25_104e', atk=target.atk, max_health=target.max_health).trigger(source)
class BG25_104:# (minion)
	""" Chronormu
	While this is in Bob's Tavern, gain the stats of any minions sold. """
	events = Sell(CONTROLLER).on(BG25_104_Action(Sell.CARD))
	pass
class BG25_104_G_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		if source.controller==source.controller.game.bartender:
			Buff(source, 'BG25_104e', atk=target.atk*2, max_health=target.max_health*2).trigger(source)
class BG25_104_G:# (minion)
	""" Chronormu
	While this is in Bob's Tavern, gain twice the stats of any minions sold. """
	events = Sell(CONTROLLER).on(BG25_104_G_Action(Sell.CARD))
	pass
class BG25_104e:# (enchantment)
	""" Stats from the Past
	Increased stats. """
	#
	pass


if BG25__General_Drakkisath:# 4/2/8 DRAGON ## new 25.2.2
	BG_Minion_Dragon+=['BG25_309','BG25_309e','BG25_309_G','BG25_309_Ge','BG25_309_Gt','BG25_309t']
	BG_PoolSet_Dragon.append('BG25_309')
	BG_Dragon_Gold['BG25_309']='BG25_309_G' 
	BG_Dragon_Gold['BG25_309t']='BG25_309_Gt' 
class BG25_309:# (minion)
	""" General Drakkisath
	<b>Battlecry:</b> Add a 2/1 Smolderwing to your hand that gives another Dragon +5_Attack. """
	play = Give(CONTROLLER, 'BG25_309t')
	pass
class BG25_309t:# (minion)
	""" Smolderwing
	<b>Battlecry:</b> Give a Dragon +5 Attack. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DRAGON }
	play = Buff(TARGET, 'BG25_309e')
	pass
BG25_309e=buff(5,0)
class BG25_309_G:# (minion)
	""" General Drakkisath
	<b>Battlecry:</b> Add two 2/1 Smolderwings to your hand that each give another Dragon +5_Attack. """
	play = Give(CONTROLLER, 'BG25_309t'), Give(CONTROLLER, 'BG25_309t')
	pass
class BG25_309_Gt:# (minion)
	""" Smolderwing
	<b>Battlecry:</b> Give a Dragon +10 Attack. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DRAGON }
	play = Buff(TARGET, 'BG25_309_Ge')
	pass
BG25_309_Ge=buff(10,0)


#Tarecgosa(3)->(4)(25.6) ->(3)(26.2)    ## OK ###
if BG_Tarecgosa:
	BG_Minion_Dragon+=['BG21_015','BG21_015_G']#
	BG_PoolSet_Dragon.append('BG21_015')
	BG_Dragon_Gold['BG21_015']='BG21_015_G' #	
class BG21_015_Action0(TargetedAction):
	TARGET = ActionArg()# self
	def do(self, source, target):
		target.sidequest_list0 = [] 
class BG21_015_Action1(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		#target = target[0]
		if not isinstance(buff, list):
			buff = [buff]
		target.sidequest_list0 += buff
class BG21_015_Action2(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		#target = target[0]
		if target.deepcopy_original!=None:
			for buff in target.sidequest_list0:
				buff.apply(target.deepcopy_original)
class BG21_015_Action3(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		#target = target[0]
		if target.deepcopy_original!=None:
			for buff in target.sidequest_list0:
				buff.apply(target.deepcopy_original)
				buff.apply(target.deepcopy_original)
#旧：これは戦闘時に受ける付与効果を永続的に維持する。
#新：これは自分が戦闘時に付与した効果を永続的に維持する。
class BG21_015:# <12>[1453]
	""" Tarecgosa
	This permanently keeps enchantments from combat. """
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.TECH_LEVEL:3}
	elif Config.BG_VERSION>=2560:
		option_tags={GameTag.TECH_LEVEL:4}
	else:
		option_tags={GameTag.TECH_LEVEL:3}
	events = [
		BeginBattle(CONTROLLER).on(BG21_015_Action0(SELF)),
		Buff(SELF).on(BG21_015_Action1(SELF, Buff.BUFF)),
		EndBattle(CONTROLLER).on(BG21_015_Action2(SELF))
	]
	pass
class BG21_015_G:# <12>[1453]
	""" Tarecgosa
	This permanently doubles and keeps enchantments from combat. """
	if Config.BG_VERSION>=2560:
		option_tags={GameTag.TECH_LEVEL:4}
	else:
		option_tags={GameTag.TECH_LEVEL:3}
	events = [
		BeginBattle(CONTROLLER).on(BG21_015_Action0(SELF)),
		Buff(SELF).on(BG21_015_Action1(SELF, Buff.BUFF)),
		EndBattle(CONTROLLER).on(BG21_015_Action3(SELF))
	]
	pass




## Electric Synthesizer (Dragon) (5)-> (4)
#BG26__Electric_Synthesizer=(Config.BG_VERSION>=2620) #(4)
if BG26__Electric_Synthesizer:# 
	BG_Minion_Dragon+=['BG26_963','BG26_963e']
	BG_Minion_Dragon+=['BG26_963_G','BG26_963_Ge']
	BG_PoolSet_Dragon.append('BG26_963')
	BG_Dragon_Gold['BG26_963']='BG26_963_G'
class BG26_963:# (minion)
	""" Electric Synthesizer
	<b>Battlecry:</b> Give your other Dragons +3 Attack. """
	#(5/3/7)<b>Battlecry:</b> Give your other Dragons +4 Attack. """
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.TECH_LEVEL:5}
	play = Buff(FIRNEDLY_MINIONS + DRAGON - SELF, 'BG26_963e')
	pass
if Config.BG_VERSION>=2620:
	BG26_963e=buff(3,0)
class BG26_963_G:# (minion)
	""" Electric Synthesizer
	<b>Battlecry:</b> Give your other Dragons +6 Attack. """
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.TECH_LEVEL:5}
	play = Buff(FIRNEDLY_MINIONS + DRAGON - SELF, 'BG26_963_Ge')
	pass
if Config.BG_VERSION>=2620:
	BG26_963_Ge=buff(6,0)



## Stormbringer (Dragon) (4)
#BG26__Stormbringer=(Config.BG_VERSION>=2620) #(4)
if BG26__Stormbringer:# 
	BG_Minion_Dragon+=['BG26_966','BG26_966e']
	BG_Minion_Dragon+=['BG26_966_G']
	BG_PoolSet_Dragon.append('BG26_966')
	BG_Dragon_Gold['BG26_966']='BG26_966_G'
class BG26_966_Action(GameAction):# 
	BUFF=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, buff, amount):# 
		if buff.atk>0:
			Buff(source, 'BG26_966e', atk=buff.atk*amount).trigger(source)
		pass# 
class BG26_966:# (minion)
	""" Stormbringer
	After a different friendly Dragon gains Attack, this also gains it. """
	events = Buff(FRIENDLY + DRAGON - SELF).on(BG26_966_Action(Buff.BUFF, 1))
	pass
class BG26_966e:
	""" """
	pass
class BG26_966_G:# (minion)
	""" Stormbringer
	After a different friendly Dragon gains Attack, this also gains it twice. """
	events = Buff(FRIENDLY + DRAGON - SELF).on(BG26_966_Action(Buff.BUFF, 2))
	pass


#### tavern tier 5

#Murozond(5)   ### OK ####
if BG_Murozond:
	BG_Minion_Dragon+=['BGS_043','TB_BaconUps_110']#
	BG_PoolSet_Dragon.append('BGS_043')
	BG_Dragon_Gold['BGS_043']='TB_BaconUps_110' #	
class BGS_043:# <12>[1453]
	""" Murozond
	[Battlecry:] Add a minion from your last opponent's warband to your hand. """
	def play(self):
		controller = self.controller
		gamemaster = controller.game.parent
		last_warband = gamemaster.last_warband(controller)
		if len(last_warband)>0:
			new_card = random.choice(last_warband)
			Give(controller, new_card).trigger(self)
	pass
class TB_BaconUps_110:# <12>[1453]
	""" Murozond
	[Battlecry:] Add a minion from your last opponent's warband to your hand.Make it Golden! """
	def play(self):
		controller = self.controller
		gamemaster = controller.game.parent
		last_warband = gamemaster.last_warband(controller)
		if len(last_warband)>0:
			new_card = random.choice(last_warband)
			gold_id = gamemaster.BG_Gold[new_card]
			Give(controller, gold_id).trigger(self)## I want to check whether no error before excuting
	pass



#Razorgore, the Untamed (5)  ### need check (alternative) ### banned 26.2
if BG_Razorgore_the_Untamed:
	BG_Minion_Dragon+=['BGS_036','BGS_036e','TB_BaconUps_106','TB_BaconUps_106e']#
	BG_PoolSet_Dragon.append('BGS_036')
	BG_Dragon_Gold['BGS_036']='TB_BaconUps_106' #	
class BGS_036_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target.controller
		count = 0
		for card in controller.field:
			if race_identity(card,Race.DRAGON):
				count += amount
		Buff(target, 'BGS_036e', atk=count, max_health=count).trigger(controller)
		pass
class BGS_036:# <12>[1453]
	""" Razorgore, the Untamed
	At the end of your turn, gain +1/+1 for each Dragon you have. """
	events = OWN_TURN_END.on(BGS_036_Action(SELF, 1))
	#events = OWN_TURN_END.on(Buff(SELF, 'BGS_036e') * Count(FRIENDLY_MINIONS + DRAGON))
	pass
BGS_036e=buff(1,1)
class TB_BaconUps_106:# <12>[1453]
	""" Razorgore, the Untamed
	At the end of your turn, gain +2/+2 for each Dragon you have. """
	events = OWN_TURN_END.on(BGS_036_Action(SELF, 2))
	#events = OWN_TURN_END.on(Buff(SELF, 'TB_BaconUps_106e') * Count(FRIENDLY_MINIONS + DRAGON))
	pass
TB_BaconUps_106e=buff(2,2)



if BG25__Cyborg_Drake:# 5/2/8 dragon ## new 25.2.2 banned 26.2
	BG_Minion_Dragon+=['BG25_043','BG25_043e','BG25_043_G','BG25_043_Ge']
class BG25_043:# (minion)
	""" Cyborg Drake
	<b>Divine Shield</b> Your <b>Divine Shield</b> minions have +10 Attack. """
	update=Refresh(FRIENDLY + MINION + DIVINE_SHIELD, buff='BG25_043e')
	pass
BG25_043e=buff(10,0)
class BG25_043_G:# (minion)
	""" Cyborg Drake
	<b>Divine Shield</b> Your <b>Divine Shield</b> minions have +20 Attack. """
	update=Refresh(FRIENDLY + MINION + DIVINE_SHIELD, buff='BG25_043_Ge')
	pass
BG25_043_Ge=buff(20,0)


## Disco Shuffler (Dragon) (5)
#BG26__Disco_Shuffler=(Config.BG_VERSION>=2620)# (5/4/3)
if BG26__Disco_Shuffler:# 
	BG_Minion_Dragon+=['BG26_355','BG26_355t','BG26_355t2']
	BG_Minion_Dragon+=['BG26_355_G','BG26_355_Gt','BG26_355_Gt2']
	BG_PoolSet_Dragon.append('BG26_355')
	BG_Dragon_Gold['BG26_355']='BG26_355_G'
	BG_Dragon_Gold['BG26_355t']='BG26_355_Gt'
	BG_Dragon_Gold['BG26_355t2']='BG26_355_Gt2'
class BG26_355_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_355:# (minion)
	""" Disco Shuffler
	<b>Choose One - </b>Trigger a friendly minion's <b>Battlecry</b>; or <b>Discover</b> a <b>Battlecry</b> minion. """
	choose = ('BG26_355t','BG26_355t2')
	pass
class BG26_355t:
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_BATTLECRY:0}
	play = PlayBattlecry(TARGET)
	pass
class BG26_355t2:
	play = Discover(CONTROLLER, RandomBGMinion(has_battlecry=True))
	pass
class BG26_355_G:# (minion)
	""" Disco Shuffler
	<b>Choose One - </b>Trigger a friendly minion's <b>Battlecry</b> twice; or <b>Discover</b> 2 <b>Battlecry</b> minions. """
	choose = ('BG26_355_Gt','BG26_355_Gt2')
	pass
class BG26_355_Gt:
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_BATTLECRY:0}
	play = PlayBattlecry(TARGET),PlayBattlecry(TARGET)
	pass
class BG26_355_Gt2:
	play = DiscoverTwice(CONTROLLER, RandomBGMinion(has_battlecry=True))
	pass



## Sanctum Rester (Dragon) (5)
#BG26__Sanctum_Rester=(Config.BG_VERSION>=2620)# (5/5/5)
if BG26__Sanctum_Rester:# 
	BG_Minion_Dragon+=['BG26_356','BG26_356e']
	BG_Minion_Dragon+=['BG26_356_G','BG26_356_Ge']
	BG_PoolSet_Dragon.append('BG26_356')
	BG_Dragon_Gold['BG26_356']='BG26_356_G'
class BG26_356_Action(GameAction):# 
	def do(self, source):# 
		pass# 
class BG26_356:# (minion)
	""" Sanctum Rester
	<b>Start of Combat:</b> Give your other Dragons +8 Health. """
	events = BeginBattle(CONTROLLER).on(Buff(FRIENDLY_MINIONS + DRAGON - SELF, 'BG26_356e'))
	pass
BG26_356e=buff(0,8)
class BG26_356_G:# (minion)
	""" Sanctum Rester
	<b>Start of Combat:</b> Give your other Dragons +16 Health. """
	events = BeginBattle(CONTROLLER).on(Buff(FRIENDLY_MINIONS + DRAGON - SELF, 'BG26_356_Ge'))
	pass
BG26_356_Ge=buff(0,8)


##### tavern tier 6

#Kalecgos, Arcane Aspect (6)  ### maybe ###
if BG_Kalecgos_Arcane_Aspect:
	BG_Minion_Dragon+=['BGS_041','BGS_041e','TB_BaconUps_109','TB_BaconUps_109e']#
	BG_PoolSet_Dragon.append('BGS_041')
	BG_Dragon_Gold['BGS_041']='TB_BaconUps_109' #	
class BGS_041:# <12>[1453]
	""" Kalecgos, Arcane Aspect
	After you trigger a Battlecry, give your Dragons +1/+1.""" ## new 26.2
	##	After you play a minion with [Battlecry], give your Dragons +1/+1. ## old
	if Config.BG_VERSION>=2620:
		events = Battlecry(FRIENDLY + BATTLECRY).on(Buff(FRIENDLY_MINIONS + DRAGON, 'BGS_041e'))
	else:
		events = BG_Play(CONTROLLER, FRIENDLY + BATTLECRY).on(Buff(FRIENDLY_MINIONS + DRAGON, 'BGS_041e'))
	pass
BGS_041e=buff(1,1)
class TB_BaconUps_109:# <12>[1453]
	""" Kalecgos, Arcane Aspect
	After you play a minion with [Battlecry], give your Dragons +2/+2. """
	if Config.BG_VERSION>=2620:
		events = Battlecry(FRIENDLY + BATTLECRY).on(Buff(FRIENDLY_MINIONS + DRAGON, 'TB_BaconUps_109e'))
	else:
		events = BG_Play(CONTROLLER, FRIENDLY + BATTLECRY).on(Buff(FRIENDLY_MINIONS + DRAGON, 'TB_BaconUps_109e'))
	pass
TB_BaconUps_109e=buff(2,2)





