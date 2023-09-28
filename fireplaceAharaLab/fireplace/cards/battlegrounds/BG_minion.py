from pickle import NONE
from ..utils import *
from fireplace.battlegrounds import BG_utils

BG_Tavern_Tipper=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2620) ##(1/2/2) new 23.6 ## banned 26.2
BG_Wrath_Weaver=True #(1/1/3)
BG_Mistake=(Config.BG_VERSION>=2620)### (1/1/3)new 26.2

BG_Acolyte_of_C_Thun=(Config.BG_VERSION<2360)## (2) banned 23.6
BG_Kooky_Chemist=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2420)##(2) new 23.6 banned 24.2
BG_Menagerie_Mug=(Config.BG_VERSION<2360 or Config.BG_VERSION>=2460)##(2/2/2) banned 23.6 ### renew 24.6
BG_Patient_Scout=(Config.BG_VERSION>=2460) ## (2/1/1) ## new 24.6 ### OK ###
BG_PoeticPenPal=(Config.BG_VERSION>=2560 and Config.BG_VERSION<2620) ## (2/2/4) ## new 25.6 ## banned 26.2
BG_Prophet_of_the_Boar=True##(2/2/3)
BG_Selfless_Hero=True##(2/2/1)
BG_Sparring_Partner=(Config.BG_VERSION>=2360)##(2/3/2) new 23.6
BG_Spawn_of_N_Zoth=(Config.BG_VERSION<2460)##(2) ### banned 24.6
BG_Unstable_Ghoul=(Config.BG_VERSION<2360)##(2) banned 23.6
BG_Whelp_Smuggler=False##(2/2/5) banned when? ## renew 25.? #########
BG_Yrel=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2460)##(2) new 23.6 ### banned 24.6

BG_Arm_of_the_Empire=(Config.BG_VERSION<2620)##(3/4/4) banned 26.2
BG_Bird_Buddy=(Config.BG_VERSION<2620)##(3/2/4) banned 26.2
BG_Boulderfist_Ogre=True##(3/6/7)
BG_Budding_Greenthumb=(Config.BG_VERSION<2360 or Config.BG_VERSION>=2520)##(3/1/4) banned 23.6 ## renew 25.2
BG_Faceless_Disciple=(Config.BG_VERSION>=2460) ## (3/6/4) new 24.6 ### OK ###
BG_Houndmaster=(Config.BG_VERSION<2560)##(3/4/3) ### banned 25.6
BG_Khadgar=(Config.BG_VERSION<2520)##(3) ## banned 25.2
BG_Nightmare_Amalgam=(Config.BG_VERSION>=2320 and Config.BG_VERSION<2460)##(3) RENEW  23.2 ## banned 24.6
BG_Shifter_Zerus=((Config.BG_VERSION>=2360 and Config.BG_VERSION<2420))##(3) new 23.6 banned 24.2 ## revive 24.6 as a reward option## 
BG_Soul_Juggler=(Config.BG_VERSION<2620)##(3/3/5) banned 26.2

BG_Ball_of_Minions=(Config.BG_VERSION>=2460 and Config.BG_VERSION<2620) ##(4) new 24.6  banned 26,2### OK ###
BG_Champion_of_Y_Shaarj=(Config.BG_VERSION<2360)##(4)banned 23.6
BG_Defender_of_Argus=(Config.BG_VERSION<2360)##(4)banned 23.6
BG_Fireworks_Fanatic=(Config.BG_VERSION>=2560) ##(4/4/3) new 25.6
BG_Impatient_Doomsayer=(Config.BG_VERSION<2620)##(4/2/6) banned 26.2
BG_Majordomo_Executus=(Config.BG_VERSION<2520)##(4) banned 25.2
BG_Master_of_Realities=(Config.BG_VERSION<2620) ##(5/6/6)->(4/4/4) when? ### banned 26.2
BG_Menagerie_Jug=True##(4/3/3)
BG_Reef_Explorer=(Config.BG_VERSION>=2320 and Config.BG_VERSION<2460)##(4)# NEW 23.2 ### banned 24.6
BG24__Rendle_the_Mistermind=(Config.BG_VERSION>= 2420 and Config.BG_VERSION<2560) ## (4/4/5) new 24.2 banned 25.6
BG25__Sindorei_Straight_Shot=(Config.BG_VERSION>=2522) ## (4/3/4) new 25.2.2
BG_Strongshell_Scavenger=True##(4/2/3)
BG_Treasure_Seeker_Elise=(Config.BG_VERSION>=2420) ##(4/5/5) new 24.2
BG_Tunnel_Blaster=(Config.BG_VERSION>=2360)##(4/3/7) new 23.6
BG_Vigilant_Stoneborn=(Config.BG_VERSION>=2460) ## (4/2/6) new 24.6 ### OK ###
BG_Witchwing_Nestmatron=(Config.BG_VERSION<2420 or (Config.BG_VERSION>=2504 and Config.BG_VERSION<2520)) ##(4) banned 24.2 renew 25.0.4 banned 25.2
BG26__Upbeat_Duo=(Config.BG_VERSION>=2620)### new 26.2


BG_Baron_Rivendare=(Config.BG_VERSION<2520)##(5) ## banned 25.2
BG_Brann_Bronzebeard=True##(5/2/4)
BG_Deadly_Spore=(Config.BG_VERSION<2360)##(5)banned 23.6
BG_Interrogator_Whitemane=(Config.BG_VERSION>=2460 and Config.BG_VERSION<2504) ## (5) new 24.6  ## banned 25.0.4
BG_Kangor_s_Apprentice=True##(5/3/6)
BG_Leeroy_the_Reckless=(Config.BG_VERSION>=2320)##(5/6/2) NEW 23.2
BG_Lightfang_Enforcer=True##(5/2/2)
BG_Mythrax_the_Unraveler=(Config.BG_VERSION<2420 or (Config.BG_VERSION>=2504 and Config.BG_VERSION<2520)) ##(5) banned 24.2  ## revive 25.0.4 banned 25.2
BG_Nomi_Kitchen_Nightmare=True##(5/4/4)
BG25__Titus_Rivendare=(Config.BG_VERSION>=2520)# 5/1/7 neutral ## new 25.2
BG24__Tortollan_Blue_Shell=(Config.BG_VERSION>=2420) ## (5/4/7) new 24.2 ### OK ###
##(6)->(5)  banned 22.3 ## new 26.0 
BG_Friend_of_a_Friend=((Config.BG_VERSION>=2600 and Config.BG_VERSION<2620) or Config.BG_VERSION<2230)  ## banned 2620
BG26__Drakkari_Enchanter =(Config.BG_VERSION>=2620)### (5/1/5) new 26.2


BG_Amalgadon=(Config.BG_VERSION<2230)##(6) banned 22.3
BG_Mantid_Queen=True ## (6/5/5) ## new when?
BG_Nadina_the_Red=True##(6/7/4)
BG_Orgozoa_the_Tender=(Config.BG_VERSION>=2320)###(6/3/7) NEW 23.2
BG_Seafood_Slinger=(Config.BG_VERSION>=2504 and Config.BG_VERSION<2620) ##(6/5/5) banned -> resurrect 25.0.4 ## banned 26.2
BG24__Tea_Master_Theotar=(Config.BG_VERSION>=2420 and Config.BG_VERSION<2620)# (6/6/6) new 24.2 banned 26.2
BG24_The_Walking_Fort=(Config.BG_VERSION>=2460 and Config.BG_VERSION<2522) ##(6) new 24.6 ### banned until 25.2.2 ###
BG_Uther_the_Lightbringer=(Config.BG_VERSION>=2360) ##(6/5/6) new 23.6
BG_Zapp_Slywick=True##(6/7/10)
BG_Archdruid_Hamuul=(Config.BG_VERSION>=2543 and Config.BG_VERSION<2560) ## (6/8/8)
BG_The_Boogie_Monster=(Config.BG_VERSION>=2620) ## (6/3/8) new 26.2



BG_Minion=[]

BG_PoolSet_Minion=[]

BG_Minion_Gold={}

#### TIER 1 ####


### Tavern Tipper ### OK ### 23/9/5
if BG_Tavern_Tipper:####Tavern Tipper (1) ### 23.6 new ## banned 26.2
	BG_Minion += ['BG23_352','BG23_352e','BG23_352_G','BG23_352_Ge',]#	
	BG_PoolSet_Minion.append('BG23_352')
	BG_Minion_Gold['BG23_352']='BG23_352_G'
	## Tavern Tipper (1) >= 23.6 #OK#
	pass
# 	<Entity CardID="BG23_352" ID="92871" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Tavern Tipper</enUS>
# 			<jaJP>チップ欲しガール</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>[x]If you have any unspent
# Gold at the end of
# __your turn, gain +1/+2.</enUS>
# 			<jaJP>[x]自分のターンの終了時
# 未使用の
# ゴールドがある場合
# ____+1/+2を獲得する。_</jaJP>
# 		</Tag>
# 		<Tag enumID="32" name="TRIGGER_VISUAL" type="Int" value="1"/>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="2"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="2"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1453"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="92874"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="1"/>
# 	</Entity>
class BG23_352_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = source.controller
		if controller.mana>0:
			Buff(target, buff).trigger(source)
			pass
class BG23_352:
	"""Tavern Tipper (1) >= 23.6
	If you have any unspent Gold at the end of your turn, gain +1/+2."""
	if Config.BG_VERSION>=2360:
		if Config.LOCALE=='enUS':
			option_cardtext={
				GameTag.CARDNAME:"Tavern Tipper",
				GameTag.CARDTEXT:"If you have any unspent Gold at the end of your turn, gain +1/+2."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={
				GameTag.CARDNAME:"Tavern Tipper",
				GameTag.CARDTEXT:"自分のターンの終了時、未使用のゴールドがある場合+1/+2を獲得する。"}
	events = OWN_TURN_END.on(BG23_352_Action(SELF,'BG23_352e'))
	pass
BG23_352e=buff(1,2)
class BG23_352_G:
	"""
	If you have any unspent Gold at the end of __your turn, gain +2/+4."""
	if Config.BG_VERSION>=2360:
		if Config.LOCALE=='enUS':
			option_cardtext={
				GameTag.CARDNAME:"Tavern Tipper",
				GameTag.CARDTEXT:"If you have any unspent Gold at the end of your turn, gain +2/+4."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={
				GameTag.CARDNAME:"Tavern Tipper",
				GameTag.CARDTEXT:"自分のターンの終了時、未使用のゴールドがある場合+2/+4を獲得する。"}
	events = OWN_TURN_END.on(BG23_352_Action(SELF,'BG23_352_Ge'))
	pass
BG23_352_Ge=buff(2,4)



### Wrath Weaver ### OK ### 23/9/5
if BG_Wrath_Weaver:#Wrath Weaver	1	1	3	-	-
	BG_Minion += ['BGS_004','BGS_004e','TB_BaconUps_079','TB_BaconUps_079e',]
	BG_PoolSet_Minion.append('BGS_004')
	BG_Minion_Gold['BGS_004']='TB_BaconUps_079'
	pass
#Wrath Weaver	1	1	3	 ### maybe ###
# 	<Entity CardID="BGS_004" ID="59670" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Wrath Weaver</enUS>
# 			<jaJP>憤怒の織屋</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>After you play a Demon, deal 1 damage to your hero and gain +2/+1.</enUS>
# 			<jaJP>[x]自分が悪魔を
# 手札から使用した後
# 自分のヒーローに
# 1ダメージを与え
# _+2/+1を獲得する。</jaJP>
# 		</Tag>
# 		<Tag enumID="32" name="TRIGGER_VISUAL" type="Int" value="1"/>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="4"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="1"/>
# 		<Tag enumID="48" name="COST" type="Int" value="1"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1453"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="201" name="FACTION" type="Int" value="3"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="59679"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="1"/>
# 		<Tag enumID="1456" name="IS_BACON_POOL_MINION" type="Int" value="1"/>
# 		<Tag enumID="1593" name="1" type="Int" value="1"/>
# 	</Entity>

class BGS_004:# <12>[1453] おりや
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +2/+1. """
	##After you play a Demon, deal 1 damage to your hero and gain +2/+2. """
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.ATK:1, GameTag.HEALTH:4}
		if Config.LOCALE=='enUS':
			option_cardtext={
				GameTag.CARDNAME:"Wrath Weaver",
				GameTag.CARDTEXT:"After you play a Demon, deal 1 damage to your hero and gain +2/+1."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"自分が悪魔を手札から使用した後、自分のヒーローに1ダメージを与え、+2/+1を獲得する。"}
	else:
		option_tags={GameTag.ATK:1, GameTag.HEALTH:3 }
		if Config.LOCALE=='enUS':
			option_cardtext={
				GameTag.CARDTEXT:"After you play a Demon, deal 1 damage to your hero and gain +2/+2."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"自分が悪魔を手札から使用した後、自分のヒーローに1ダメージを与え、+2/+2を獲得する。"}
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'BGS_004e'))
	pass
if Config.BG_VERSION>=2620:
	BGS_004e=buff(2,1)# <12>[1453]
else:
	BGS_004e=buff(2,2)# <12>[1453]
""" Wrath Woven, Increased stats. """
class TB_BaconUps_079:# <12>[1453]
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +4/+4. """
	if Config.BG_VERSION>=2620:
		option_tags={GameTag.ATK:2, GameTag.HEALTH:8}
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"After you play a Demon, deal 1 damage to your hero and gain +4/+2."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"自分が悪魔を手札から使用した後、自分のヒーローに1ダメージを与え、+4/+2を獲得する。"}
	else:
		option_tags={GameTag.ATK:2, GameTag.HEALTH:6}
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"After you play a Demon, deal 1 damage to your hero and gain +4/+4."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"自分が悪魔を手札から使用した後、自分のヒーローに1ダメージを与え、+4/+4を獲得する。"}
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'TB_BaconUps_079e'))
	pass
if Config.BG_VERSION>=2620:
	TB_BaconUps_079e=buff(4,2)# <12>[1453]
else:
	TB_BaconUps_079e=buff(4,4)# <12>[1453]
""" Wrath Woven,	Increased stats. """


### Mistake (1)
#BG_Mistake=(Config.BG_VERSION>=2620)### new 26.2
if BG_Mistake:
	BG_Minion += ['BG_NX2_050', 'BG_NX2_050_G']
	BG_PoolSet_Minion.append('BG_NX2_050')
	BG_Minion_Gold['BG_NX2_050']='BG_NX2_050_G'
# 	<Entity CardID="BG_NX2_050" ID="102255" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Mistake</enUS>
# 			<jaJP>失敗作</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>&lt;i&gt;This has all minion types&lt;/i&gt;.</enUS>
# 			<jaJP>[x]&lt;i&gt;これは全ての
# ミニオンの種族を持つ。&lt;/i&gt;</jaJP>
# 		</Tag>
# 		<Tag enumID="342" name="ARTISTNAME" type="String">Matt Dixon</Tag>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="3"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="1"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1776"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="200" name="CARDRACE" type="Int" value="26"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="203" name="RARITY" type="Int" value="4"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="102256"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="1"/>
# 		<Tag enumID="1456" name="IS_BACON_POOL_MINION" type="Int" value="1"/>
# 	</Entity>

class BG_NX2_050: ##
	""" Mistake
	<i>This has all minion types</i>. """ 
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"This has all minion types"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"<i>これは全てのミニオンの種族を持つ。</i>"}
	#
	pass
class BG_NX2_050_G: ##
	""" Mistake
	<i>This has all minion types</i>. """ 
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"This has all minion types"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"<i>これは全てのミニオンの種族を持つ。</i>"}
	#
	pass


########### TIER 2 #################################


##BG_Acolyte_of_C_Thun=(Config.BG_VERSION<2360)## (2) banned 23.6
if BG_Acolyte_of_C_Thun:#Acolyte of C'Thun	2	2	3
	BG_Minion += ['BGS_106','TB_BaconUps_255',]#	1
	BG_PoolSet_Minion.append('BGS_106')
	BG_Minion_Gold['BGS_106']='TB_BaconUps_255'
	pass
# 	<Entity CardID="BGS_106" ID="63614" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Acolyte of C'Thun</enUS>
# 			<jaJP>クトゥーンの侍祭</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>&lt;b&gt;Taunt&lt;/b&gt;
# &lt;b&gt;Reborn&lt;/b&gt;</enUS>
# 			<jaJP>&lt;b&gt;挑発&lt;/b&gt;、&lt;b&gt;蘇り&lt;/b&gt;</jaJP>
# 		</Tag>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="3"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="2"/>
# 		<Tag enumID="48" name="COST" type="Int" value="1"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1453"/>
# 		<Tag enumID="190" name="TAUNT" type="Int" value="1"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="1085" name="REBORN" type="Int" value="1"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="65658"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="2"/>
# 	</Entity>

class BGS_106:# <12>[1453] クトゥーンのじさい
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Taunt][Reborn]"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[挑発]、[蘇り]"}
	pass
class TB_BaconUps_255:# <12>[1453]
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Taunt][Reborn]"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[挑発]、[蘇り]"}
	pass



### OK ### 23/9/5 ###
#BG_Kooky_Chemist=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2420)##(2) new 23.6 banned 24.2
if BG_Kooky_Chemist:## Kooky Chemist (2) ### OK ### ## 23.6 new banned 24.2
	BG_Minion += ['BG_CFM_063','BG_CFM_063e','BG_CFM_063_G',]#	
	BG_PoolSet_Minion.append('BG_CFM_063')
	BG_Minion_Gold['BG_CFM_063']='BG_CFM_063_G'
	pass
# 	<Entity CardID="BG_CFM_063" ID="92883" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Kooky Chemist</enUS>
# 			<jaJP>妙ちくりんな薬剤師</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>&lt;b&gt;Battlecry:&lt;/b&gt; Swap the Attack and Health of a minion.</enUS>
# 			<jaJP>[x]&lt;b&gt;雄叫び:&lt;/b&gt;
# ミニオン1体の
# 攻撃力と体力を
# 入れ替える。</jaJP>
# 		</Tag>
# 		<Tag enumID="342" name="ARTISTNAME" type="String">Dave Allsop</Tag>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="4"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="4"/>
# 		<Tag enumID="48" name="COST" type="Int" value="4"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="25"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="203" name="RARITY" type="Int" value="1"/>
# 		<Tag enumID="218" name="BATTLECRY" type="Int" value="1"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="92885"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="2"/>
# 		<Tag enumID="2347" name="1" type="Int" value="1"/>
# 		<Tag enumID="2534" name="1" type="Int" value="1"/>
# 	</Entity>
class BG_CFM_063_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		amount=target.atk-target.max_health
		Buff(target, "BG_CFM_063e", max_health=amount, atk=-amount).trigger(source)
class BG_CFM_063:
	""" Kooky Chemist (2) 
	Battlecry: Swap the Attack and Health of a minion."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0,
				 PlayReq.REQ_FRIENDLY_TARGET: 0,
				 PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Battlecry: Swap the Attack and Health of a minion."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]ミニオン1体の攻撃力と体力を入れ替える。"}
	play = BG_CFM_063_Action(TARGET, "BG_CFM_063e")
	pass
class BG_CFM_063e:
	pass
class BG_CFM_063_G:
	"""
	[Battlecry:] Swap the Attack and Health of a minion."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0,
				 PlayReq.REQ_FRIENDLY_TARGET: 0,
				 PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Battlecry: Swap the Attack and Health of a minion."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]ミニオン1体の攻撃力と体力を入れ替える。"}
	play = BG_CFM_063_Action(TARGET, "BG_CFM_063e")
	pass


### need check ### 23/9/5 ###
#BG_Menagerie_Mug=(Config.BG_VERSION<2360 or Config.BG_VERSION>=2460)##(2/2/2) banned 23.6 ### renew 24.6
if BG_Menagerie_Mug:#Menagerie Mug	2	2	2 ### 
	BG_Minion += ['BGS_082','BGS_082e','TB_BaconUps_144','TB_BaconUps_144e',]#	1
	BG_PoolSet_Minion.append('BGS_082')
	BG_Minion_Gold['BGS_082']='TB_BaconUps_144'
	pass
# 	<Entity CardID="BGS_082" ID="63435" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Menagerie Mug</enUS>
# 			<jaJP>ミナジェリのマグ</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>[x]&lt;b&gt;Battlecry:&lt;/b&gt; Give 3 random# friendly minions of different# minion types +1/+1.</enUS>
# 			<jaJP>[x]&lt;b&gt;雄叫び:&lt;/b&gt;# 異なる種族のランダムな# 味方のミニオン3体に# +1/+1を付与する。</jaJP>
# 		</Tag>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="2"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="2"/>
# 		<Tag enumID="48" name="COST" type="Int" value="3"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1453"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="218" name="BATTLECRY" type="Int" value="1"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="63489"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="2"/>
# 		<Tag enumID="1456" name="IS_BACON_POOL_MINION" type="Int" value="1"/>
# 	</Entity>
class BGS_082_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target
		field = controller.field
		sample=[]
		cds=[]
		for rc in source.controller.game.parent.BG_races:
			cards=[cd for cd in field if BG_utils.isRacesCards(cd, rc)==True]
			if len(cards)>0:
				cds.append(cards)
		if len(cds)>3:
			cds=random.sample(cds, 3)
		for cards in cds:
			rcds=[cd for cd in cards if not cd in sample]
			if len(rcds)>0:
				sample.append(random.choice(rcds))
		for c in sample:
			Buff(c,buff).trigger(source)
class BGS_082:# <12>[1453]
	""" Menagerie Mug マナジェリ
	[Battlecry:] Give 3 random friendly minions of different minion types +1/+1. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give 3 random friendly minions of different minion types +1/+1."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]異なる種族のランダムな味方のミニオン3体に+1/+1を付与する。"}
	play = BGS_082_Action(CONTROLLER,'BGS_082e')
	pass
BGS_082e=buff(1,1)# <12>[1453]
""" Sip of Tea, +1/+1. """
class TB_BaconUps_144:# <12>[1453]
	""" Menagerie Mug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +2/+2. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give 3 random friendly minions of different minion types +2/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]異なる種族のランダムな味方のミニオン3体に+2/+2を付与する。"}
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_144e')
	pass
TB_BaconUps_144e=buff(2,2)# <12>[1453]
""" Sip of Tea, +2/+2. """


##need check ### 23/9/5
#BG_Patient_Scout=(Config.BG_VERSION>=2460) ## (2/1/1) ## new 24.6 ### OK ###
#Patient Scout(BG24_715) ## new 24.6 ### OK ###
if BG_Patient_Scout:#Patient Scout	2	1	1	
	BG_Minion += ['BG24_715','BG24_715_G',]#	
	BG_PoolSet_Minion.append('BG24_715')
	BG_Minion_Gold['BG24_715']='BG24_715_G'
	pass
# 	<Entity CardID="BG24_715" ID="97604" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Patient Scout</enUS>
# 			<jaJP>辛抱強い斥候</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>[x]When you sell this,
# &lt;b&gt;Discover&lt;/b&gt; a Tier @ minion.
# &lt;i&gt;(Upgrades each turn!)&lt;/i&gt;</enUS>
# 			<jaJP>[x]これを売る時
# グレード@ミニオン1体を
# &lt;b&gt;発見&lt;/b&gt;する。&lt;i&gt;（毎ターン
# アップグレード！）&lt;/i&gt;</jaJP>
# 		</Tag>
# 		<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
# 		<Tag enumID="32" name="TRIGGER_VISUAL" type="Int" value="1"/>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="1"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="1"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1453"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="1342" name="USE_DISCOVER_VISUALS" type="Int" value="1"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="97605"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="2"/>
# 		<ReferencedTag enumID="415" name="DISCOVER" type="Int" value="1"/>
# 	</Entity>
class BG24_715_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
class BG24_715_Action(GameAction):
	def do(self, source):
		BG24_715_Choice(source.controller, RandomBGAdmissible(tech_level=source.script_data_num_1)*3).trigger(source)
		pass
class BG24_715_Action2(GameAction):
	def do(self, source):
		source.script_data_num_1=min(source.script_data_num_1+1, 6)
		pass
class BG24_715:##
	""" Patient Scout
	When you sell this, [Discover] a Tier @ minion. <i>(Upgrades each turn!)</i>"""
	# @ = self.script_data_num_1
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"When you sell this, [Discover] a Tier @ minion. (Upgrades each turn!)"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"これを売る時グレード@ミニオン1体を[発見]する。<i>（毎ターンアップグレード！）</i>"}
	events = [
		Sell(CONTROLLER, SELF).on(BG24_715_Action()),
		BeginBar(CONTROLLER).on(BG24_715_Action2())
	]
	pass
class BG24_715_G_Choice(Choice):
	def choose(self, card):
		if self.source.sidequest_counter_1==0:
			self.next_choice=self
			self.source.sidequest_counter_1=1
		else:
			self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
class BG24_715_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source):
		BG24_715_G_Choice(source.controller, RandomBGAdmissible(tech_level=source.script_data_num_1)*3).trigger(source)
		pass
class BG24_715_G:
	""" Patient Scout
	When you sell this, [Discover] two Tier @ minions. <i>(Upgrades each turn!)</i>"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"When you sell this, [Discover] two Tier @ minions. (Upgrades each turn!)"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"これを売る時グレード@ミニオン2体を[発見]する。<i>（毎ターンアップグレード！）</i>"}
	events = [
		Sell(CONTROLLER, SELF).on(BG24_715_G_Action()),
		BeginTurn(CONTROLLER).on(BG24_715_Action2())
	]
	pass


#BG_PoeticPenPal=(Config.BG_VERSION>=2560 and Config.BG_VERSION<2620) ## (2/2/4) ## new 25.6 ## banned 26.2
## Poetic Pen Pal 
if BG_PoeticPenPal:## Poetic Pen Pal (BG25_105)(2/2/4) new 25.6
	BG_Minion += ['BG25_105','BG25_105_G',]#	1
	BG_PoolSet_Minion.append('BG25_105')
	BG_Minion_Gold['BG25_105']='BG25_105_G'
	pass
# 	<Entity CardID="BG25_105" ID="101433" version="2">
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Poetic Pen Pal</enUS>
# 			<jaJP>詩的なペンフレンド</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>&lt;b&gt;Battlecry:&lt;/b&gt; Reduce the Cost of your next Buddy by (2).</enUS>
# 			<jaJP>[x]&lt;b&gt;雄叫び:&lt;/b&gt;
# 自分の次の
# バディのコストを
# （2）減らす。</jaJP>
# 		</Tag>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="4"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="2"/>
# 		<Tag enumID="48" name="COST" type="Int" value="2"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1453"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="218" name="BATTLECRY" type="Int" value="1"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="101434"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="2"/>
# 	</Entity>
class BG25_105:##############################
	""" Poetic Pen Pal (2/2/4)
	[Battlecry:] Reduce the Cost of your next Buddy by (2)."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Reduce the Cost of your next Buddy by (2)."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]自分の次のバディのコストを（2）減らす。"}	
	pass
class BG25_105_G:#############################
	""" Poetic Pen Pal (2/4/8)
	[Battlecry:] Reduce the Cost of your next Buddy by (4)."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Reduce the Cost of your next Buddy by (4)."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]自分の次のバディのコストを（4）減らす。"}	
	pass


### 23/9/7 ###
#BG_Prophet_of_the_Boar=True##(2/2/3)
#Prophet of the Boar	2	3	3	-		 ### OK ###
if BG_Prophet_of_the_Boar:#(BG20_203)Prophet of the Boar	2	3	3
	BG_Minion += ['BG20_203','BG20_203_G',]#	1
	BG_PoolSet_Minion.append('BG20_203')
	BG_Minion_Gold['BG20_203']='BG20_203_G'
	pass
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Prophet of the Boar</enUS>
# 			<jaJP>巨猪の預言者</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>&lt;b&gt;Taunt&lt;/b&gt;
# After you play a Quilboar, get a &lt;b&gt;Blood Gem&lt;/b&gt;.</enUS>
# 			<jaJP>[x]&lt;b&gt;挑発&lt;/b&gt;
# キルボアを手札から
# 使用した後、&lt;b&gt;血の宝石&lt;/b&gt;
# 1個を得る。</jaJP>
# 		</Tag>
# 		<Tag enumID="32" name="TRIGGER_VISUAL" type="Int" value="1"/>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="3"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="2"/>
# 		<Tag enumID="48" name="COST" type="Int" value="3"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="1453"/>
# 		<Tag enumID="190" name="TAUNT" type="Int" value="1"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="12"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="70155"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="2"/>
# 		<Tag enumID="1845" name="1" type="Int" value="1"/>
# 		<ReferencedTag enumID="1966" name="BLOOD_GEM" type="Int" value="1"/>
# 	</Entity>
class BG20_203_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		if controller.once_per_turn==0:
			for repeat in range(amount):
				Give(controller, 'BG20_GEM').trigger(source)
			controller.once_per_turn=1
class BG20_203:# <12>[1453]
	""" Prophet of the Boar # renew 24.6
	[Taunt] After you play a Quilboar, get a [Blood Gem]. """ #>=2460
	##[Once per Turn:] After you play a Quilboar, gain a [Blood Gem]. """ # <2460
	if Config.BG_VERSION>=2460:
		option_tags={GameTag.TAUNT:1 }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Taunt] After you play a Quilboar, get a [Blood Gem]."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"[挑発]キルボアを手札から使用した後、[血の宝石]1個を得る。"}
		events = BG_Play(CONTROLLER, MINION + QUILBOAR).after(Give(CONTROLLER, 'BG20_GEM'))
	else:
		option_tags={GameTag.TAUNT:0 }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Once per Turn:] After you play a Quilboar, gain a [Blood Gem].."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"1ターン1回：キルボアを手札から使用した後、血の宝石1個を獲得する。"}
		events = BG_Play(CONTROLLER, MINION + QUILBOAR).after(BG20_203_Action(CONTROLLER, 1))	
	pass
class BG20_203_G:# <12>[1453]
	""" Prophet of the Boar # renew 24.6
	[Taunt] After you play a Quilboar, get 2 [Blood Gems]."""
	#[Once per Turn:] After you play a Quilboar, gain 2 [Blood Gems]. """
	if Config.BG_VERSION>=2460:
		option_tags={GameTag.TAUNT:1 }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Taunt] After you play a Quilboar, get 2 [Blood Gem]."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"[挑発]キルボアを手札から使用した後、[血の宝石]2個を得る。"}
		events = BG_Play(CONTROLLER, MINION + QUILBOAR).after(Give(CONTROLLER, 'BG20_GEM'),Give(CONTROLLER, 'BG20_GEM'))
	else:
		option_tags={GameTag.TAUNT:0 }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Once per Turn:] After you play a Quilboar, gain 2 [Blood Gem].."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"1ターン1回：キルボアを手札から使用した後、血の宝石2個を獲得する。"}
		events = BG_Play(CONTROLLER, MINION + QUILBOAR).after(BG20_203_Action(CONTROLLER, 2))
	pass


### 23/9/7 ###xxx
#BG_Selfless_Hero=True##(2/2/1)
#Selfless Hero	2	2	1	-	### OK ###
if BG_Selfless_Hero:#Selfless Hero	2	2	1
	BG_Minion += ['BG_OG_221','TB_BaconUps_014',]#	
	BG_PoolSet_Minion.append('BG_OG_221')
	BG_Minion_Gold['BG_OG_221']='TB_BaconUps_014'
	pass
# 		<Tag enumID="185" name="CARDNAME" type="LocString">
# 			<enUS>Selfless Hero</enUS>
# 			<jaJP>献身の英雄</jaJP>
# 		</Tag>
# 		<Tag enumID="184" name="CARDTEXT" type="LocString">
# 			<enUS>&lt;b&gt;Deathrattle:&lt;/b&gt; Give a random friendly minion &lt;b&gt;Divine Shield&lt;/b&gt;.</enUS>
# 			<jaJP>[x]&lt;b&gt;断末魔:&lt;/b&gt;
# ランダムな味方の
# ミニオン1体に
# _____&lt;b&gt;聖なる盾&lt;/b&gt;を付与する。</jaJP>
# 		</Tag>
# 		<Tag enumID="342" name="ARTISTNAME" type="String">Rafael Zanchetin</Tag>
# 		<Tag enumID="45" name="HEALTH" type="Int" value="1"/>
# 		<Tag enumID="47" name="ATK" type="Int" value="2"/>
# 		<Tag enumID="48" name="COST" type="Int" value="1"/>
# 		<Tag enumID="183" name="CARD_SET" type="Int" value="21"/>
# 		<Tag enumID="199" name="CLASS" type="Int" value="5"/>
# 		<Tag enumID="202" name="CARDTYPE" type="Int" value="4"/>
# 		<Tag enumID="203" name="RARITY" type="Int" value="3"/>
# 		<Tag enumID="217" name="DEATHRATTLE" type="Int" value="1"/>
# 		<Tag enumID="1429" name="BACON_TRIPLE_UPGRADE_MINION_ID" type="Int" value="58143"/>
# 		<Tag enumID="1440" name="TECH_LEVEL" type="Int" value="2"/>
# 		<Tag enumID="1456" name="IS_BACON_POOL_MINION" type="Int" value="1"/>
# 		<ReferencedTag enumID="194" name="DIVINE_SHIELD" type="Int" value="1"/>
class BG_OG_221_Action(TargetedAction):
	TARGET = ActionArg()# controller
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller=target
		cards = [card for card in controller.field if card.divine_shield==False]
		if len(cards)>amount:
			cards=random.sample(cards, amount)
		for card in cards:
			card.divine_shield=True
class BG_OG_221:
	"""Selfless Hero:  けんしん
	[Deathrattle:] Give a random friendly minion [Divine Shield]."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Give a random friendly minion [Divine Shield]."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[断末魔:]ランダムな味方のミニオン1体に[聖なる盾]を付与する。"}	
	deathrattle = BG_OG_221_Action(CONTROLLER, 1)
class TB_BaconUps_014:# <5>[1453]
	""" Selfless Hero
	[Deathrattle:] Give 2_random friendly minions [Divine Shield]. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Give 2 random friendly minion [Divine Shield]."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[断末魔:]ランダムな味方のミニオン2体に[聖なる盾]を付与する。"}	
	deathrattle = BG_OG_221_Action(CONTROLLER, 2)
	pass


### 23/9/7 ###
#BG_Sparring_Partner=(Config.BG_VERSION>=2360)##(2/3/2) new 23.6
if BG_Sparring_Partner:#### Sparring Partner (2/3/2) ### OK ####
	BG_Minion += ['BG_AT_069','BG_AT_069_G',]#	
	BG_PoolSet_Minion.append('BG_AT_069')
	BG_Minion_Gold['BG_AT_069']='BG_AT_069_G'
	## Sparring Partner (2) >= 23.6
	pass
class BG_AT_069:
	"""Sparring Partner (2/3/2) >= 23.6
	Taunt Battlecry: Give a minion Taunt."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Taunt Battlecry: Give a minion Taunt."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[挑発]、[雄叫び:]ミニオン1体に[挑発]を付与する。"}		
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Taunt(TARGET)
class BG_AT_069_G:
	"""
	[Taunt] [Battlecry:] Give a minion [Taunt]."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Taunt] [Battlecry:] Give a minion [Taunt]."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[挑発]、[雄叫び:]ミニオン1体に[挑発]を付与する。"}		
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Taunt(TARGET)


### 23/9/24 #### 
#BG_Spawn_of_N_Zoth=(Config.BG_VERSION<2460)##(2) ### banned 24.6
if BG_Spawn_of_N_Zoth:#Spawn of N'Zoth	2	2	2	- ### OK ### banned 24.6
	BG_Minion += ['BG_OG_256','OG_256e','TB_BaconUps_025','TB_BaconUps_025e',]#	
	BG_PoolSet_Minion.append('BG_OG_256')
	BG_Minion_Gold['BG_OG_256']='TB_BaconUps_025'
	pass
class BG_OG_256:# んぞす
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +1/+1. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Give your minions +1/+1."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[断末魔:]味方のミニオン全てに+1/+1を付与する。"}
	deathrattle = Buff(FRIENDLY_MINIONS, 'OG_256e')#
	pass
OG_256e=buff(1,1)
class TB_BaconUps_025:# <12>[1453]
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +2/+2. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Give your minions +2/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[断末魔:]味方のミニオン全てに+2/+2を付与する。"}
	deathrattle = Buff(FRIENDLY_MINIONS, 'TB_BaconUps_025e')#
	pass
TB_BaconUps_025e = buff(2,2)


### 23/9/24 ###
#BG_Unstable_Ghoul=(Config.BG_VERSION<2360)##(2) banned 23.6
if BG_Unstable_Ghoul:#Unstable Ghoul	2	1	3	-### OK ### ##banned 23.6
	BG_Minion += ['FP1_024','TB_BaconUps_118',]#	
	BG_PoolSet_Minion.append('FP1_024')
	BG_Minion_Gold['FP1_024']='TB_BaconUps_118'
	pass
class FP1_024:# <12>[1453] ぐうる
	""" Unstable Ghoul
	[Taunt]. [Deathrattle:] Deal 1 damage to all minions. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Taunt]. [Deathrattle:] Deal 1 damage to all minions."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[挑発]、[断末魔:]全てのミニオンに1ダメージを与える。"}		
	deathrattle = Hit(ALL_MINIONS, 1),Deaths()
	pass
class TB_BaconUps_118:# <12>[1453]
	""" Unstable Ghoul
	[Taunt][Deathrattle:] Deal 1 damage to all minions twice. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Taunt]. [Deathrattle:] Deal 1 damage to all minions twice."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[挑発]、[断末魔:]全てのミニオンに1ダメージを与える。これを2回行う。"}		
	deathrattle = Hit(ALL_MINIONS, 1), Deaths(), Hit(ALL_MINIONS, 1), Deaths()
	pass


### 23/9/24 ###
#BG_Whelp_Smuggler=False##(2/2/5) banned when? ## renew 25.? #########
if BG_Whelp_Smuggler:#Whelp Smuggler	2	2	5	- ### OK ###
	BG_Minion += ['BG21_013','BG21_013e','BG21_013_G',]#	
	BG_PoolSet_Minion.append('BG21_013')
	BG_Minion_Gold['BG21_013']='BG21_013_G'
	pass
class BG21_013_Action(TargetedAction):## 密輸人
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		if buff.atk>0:
			Buff(target, 'BG21_013e', max_health=amount).trigger(source)
			pass
class BG21_013:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +1_Health. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After a friendly Dragon gains Attack, give it +1_Health."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方のドラゴンが攻撃力を獲得した後それに体力+1を付与する。"}	
	events = Buff(FRIENDLY + DRAGON).on(BG21_013_Action(Buff.TARGET, Buff.BUFF, 1))
	pass
class BG21_013e:
	pass
class BG21_013_G:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +2_Health. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After a friendly Dragon gains Attack, give it +2_Health."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方のドラゴンが攻撃力を獲得した後それに体力+2を付与する。"}
	events = Buff(FRIENDLY + DRAGON).on(BG21_013_Action(Buff.TARGET, Buff.BUFF, 2))
	pass




### 23/9/24 ###
#BG_Yrel=(Config.BG_VERSION>=2360 and Config.BG_VERSION<2460)##(2) new 23.6 ### banned 24.6
if BG_Yrel:## Yrel (2) ### need check ### banned 24.6
	BG_Minion += ['BG23_350','BG23_350e','BG23_350_G','BG23_350_Ge',]#	
	BG_PoolSet_Minion.append('BG23_350')
	BG_Minion_Gold['BG23_350']='BG23_350_G'
	##  Yrel (2) >=23.6
	pass
class BG23_350_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		## in BG battle
		controller = target
		races = []
		for card in controller.field:
			if hasattr(card, 'race') and card.race != Race.INVALID and not card.race in races:
				races.append(card.race)
		if len(races)>0:
			for race in races:
				targets=[]
				if race != Race.ALL:
					for card in controller.field:
						if hasattr(card, 'race') and card.race == race:
							targets.append(card)
					if len(targets)>0:
						Buff(random.choice(targets),buff).trigger(source)
				else:
					for card in controller.field:
						if hasattr(card, 'race') and card.race == race:
							Buff(card,buff).trigger(source)
class BG23_350:
	"""Yrel (2) >=23.6
	After this attacks, give a friendly minion of each minion type +1/+2."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After this attacks, give a friendly minion of each minion type +1/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"これが攻撃した後味方のミニオンの各種族1体ずつにそれぞれ+1/+2を付与する。"}
	events = BG_Attack(SELF).on(BG23_350_Action(CONTROLLER, 'BG23_350e'))
BG23_350e=buff(1,2)
class BG23_350_G:
	"""Yrel (2) >=23.6
	After this attacks, give a friendly minion of each minion type +2/+4."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After this attacks, give a friendly minion of each minion type +2/+4."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"これが攻撃した後味方のミニオンの各種族1体ずつにそれぞれ+2/+4を付与する。"}
	events = BG_Attack(SELF).on(BG23_350_Action(CONTROLLER, 'BG23_350_Ge'))
BG23_350_Ge=buff(2,4)


##################### TIER 3 ###################################


### 23/9/25 ###
if BG_Arm_of_the_Empire:#Arm of the Empire	3	4	4	-		 ### maybe ###
	BG_Minion += ['BGS_110','BGS_110e','TB_BaconUps_302','TB_BaconUps_302e',]#	
	BG_PoolSet_Minion.append('BGS_110')
	BG_Minion_Gold['BGS_110']='TB_BaconUps_302'
	pass
class BGS_110:# <12>[1453] 帝国の腕
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +2 Attack permanently. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Whenever a friendly [Taunt]minion is attacked,give it +2 Attack permanently."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方の&lt;b&gt;挑発&lt;/b&gt;ミニオンが攻撃される度それに攻撃力+2を永続的に付与する。"}
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(BG_Attack.OTHER,'BGS_110e'))
	pass
BGS_110e=buff(2,0)# <12>[1453]
""" Armed!, +2 Attack """
class TB_BaconUps_302:# <12>[1453]
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +4 Attack permanently. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Whenever a friendly [Taunt]minion is attacked,give it +4 Attackpermanently."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方の&lt;b&gt;挑発&lt;/b&gt;ミニオンが攻撃される度それに攻撃力+4を永続的に付与する。"}
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(BG_Attack.OTHER,'TB_BaconUps_302e'))
	pass
TB_BaconUps_302e=buff(4,0)# <12>[1453]
""" Double Armed!, +4 Attack """


### 23/9/25 ###
if BG_Bird_Buddy:#Bird Buddy	3	2	4	-		 ### maybe ### banned 26.2
	BG_Minion += ['BG21_002','BG21_002e','BG21_002_G','BG21_002_Ge',]#	
	BG_PoolSet_Minion.append('BG21_002')
	BG_Minion_Gold['BG21_002']='BG21_002_G'
	pass
class BG21_002:# <12>[1453]  愛鳥家
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +1/+1. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (1):] Give your Beasts +1/+1."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[仇討 (1):] 味方の獣すべてに+1/+1を付与する。"}
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 1, [Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002e')]))
	pass
BG21_002e=buff(1,1)
""" Well Fed, +1/+1. """
class BG21_002_G:# <12>[1453]
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +2/+2. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (1):] Give your Beasts +2/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[仇討 (1):] 味方の獣すべてに+2/+2を付与する。"}
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 1, [Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002_Ge')]))
	pass
BG21_002_Ge=buff(2,2)# <12>[1453]
""" Well Fed,  +2/+2. """


### 23/9/26  ###
if BG_Boulderfist_Ogre:## Boulderfist Ogre(3/6/7) ### new 25.6
	BG_Minion += ['BG_CS2_200','BG_CS2_200_G',]#	
	BG_PoolSet_Minion.append('BG_CS2_200')
	BG_Minion_Gold['BG_CS2_200']='BG_CS2_200_G'
class BG_CS2_200:
	""" Boulderfist Ogre
	"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:""}#vannila
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:""}#vannila
	pass
class BG_CS2_200_G:
	""" Boulderfist Ogre
	<i>Six Attack and seven Health are [already] perfect stats for the Tavern Tier!</i>"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:""}#vannila
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:""}#vannila
	pass


### 23/9/26 ###
#Budding Greenthumb	3	1	4	-
if BG_Budding_Greenthumb:### maybe ### ##banned 23.6
	BG_Minion += ['BG21_030','BG21_030e','BG21_030_G','BG21_030_Ge',]#	
	BG_PoolSet_Minion.append('BG21_030')
	BG_Minion_Gold['BG21_030']='BG21_030_G'
	pass
class BG21_030:# <12>[1453]  栽培家
	""" Budding Greenthumb
	[Avenge (3):] Give adjacent minions +2/+1 permanently. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (3):] Give adjacent minions +2/+1 permanently."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;仇討（3）:&lt;/b&gt;隣接するミニオンに+2/+1を永続的に付与する。"}
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(SELF_ADJACENT, 'BG21_030e')]))
	pass
BG21_030e=buff(2,1)
class BG21_030_G:# <12>[1453]
	""" Budding Greenthumb
	[Avenge (3):] Giveadjacent minions+4/+2 permanently. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (3):] Give adjacent minions +4/+2 permanently."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;仇討（3）:&lt;/b&gt;隣接するミニオンに+4/+2を永続的に付与する。"}
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(SELF_ADJACENT, 'BG21_030_Ge')]))
	pass
BG21_030_Ge=buff(4,2)


### 23/9/26 ###
#Faceless Disciple(3) (6/4) (BG24_719) ### OK ###
if BG_Faceless_Disciple:#Faceless Disciple(3) 
	BG_Minion += ['BG24_719','BG24_719_G',]#	
	BG_PoolSet_Minion.append('BG24_719')
	BG_Minion_Gold['BG24_719']='BG24_719_G'
class BG24_719_Target(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		tier=min(target.tech_level+1,6)
		newcard=RandomBGAdmissible(tech_level=tier).evaluate(controller)
		Morph(target, newcard[0]).trigger(source)
		pass
class BG24_719:
	""" Faceless Disciple
	#[Battlecry:] Transform a minion into one from a Tavern Tier higher."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Transform a minion into one from a Tavern Tier higher."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;ミニオン1体をグレードが1高いミニオンに変身させる。"}
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0  }
	play = BG24_719_Target(TARGET)
class BG24_719_G_Target(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		tier=min(target.tech_level+2,6)
		newcard=RandomBGAdmissible(tech_level=tier).evaluate(controller)
		Morph(target, newcard[0]).trigger(source)
		pass
class BG24_719_G:
	""" Faceless Disciple
	#[Battlecry:] Transform a minion into one from 2 Tavern Tiers higher."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Transform a minion into one from 2 Tavern Tiers higher."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;ミニオン1体をグレードが2高いミニオンに変身させる。"}
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0  }
	play = BG24_719_G_Target(TARGET)


### 23/9/26 ###
#Houndmaster	3	4	3	-		 
if BG_Houndmaster:#Houndmaster	3	4	3	-		 ### maybe ###
	BG_Minion += ['BG_DS1_070','DS1_070o','TB_BaconUps_068','TB_BaconUps_068e',]#	
	BG_PoolSet_Minion.append('BG_DS1_070')
	BG_Minion_Gold['BG_DS1_070']='TB_BaconUps_068'
	pass
class BG_DS1_070:# <3>[1453] 猟犬使い
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +2/+2 and [Taunt]."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give a friendly Beast +2/+2 and [Taunt]."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;味方の獣1体に[b]+2/+2と&lt;b&gt;挑発&lt;/&gt;を付与する。"}
	requirements = {
		PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0,PlayReq.REQ_MINION_TARGET:0, 
		PlayReq.REQ_TARGET_WITH_RACE:Race.BEAST }
	play = Buff(TARGET, 'DS1_070o')
	pass
DS1_070o=buff(2,2,taunt=True)
class TB_BaconUps_068:# <3>[1453]
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +4/+4 and [Taunt]. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give a friendly Beast +4/+4 and [Taunt]."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;味方の獣1体に[b]+4/+4と&lt;b&gt;挑発&lt;/&gt;を付与する。"}
	requirements = {
		PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0,PlayReq.REQ_MINION_TARGET:0, 
		PlayReq.REQ_TARGET_WITH_RACE:Race.BEAST }
	play = Buff(TARGET, 'TB_BaconUps_068e')
	pass
TB_BaconUps_068e=buff(4,4,taunt=True)# <3>[1453]
""" Master's Presence, +4/+4 and [Taunt]. """


### 23/9/26 ###
#Khadgar	3	2	2	-	  	 
if BG_Khadgar:#Khadgar	3	2	2	-	  	 ### maybe ### banned 25.2
	BG_Minion += ['BG_DAL_575','TB_BaconUps_034',]#	
	BG_PoolSet_Minion.append('BG_DAL_575')
	BG_Minion_Gold['BG_DAL_575']='TB_BaconUps_034'
	pass
class BG_DAL_575_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = source.controller
		index=0
		if target in controller.field:
			index=controller.field.index(target)
			pass
		target=get00(target)
		for repeat in range(amount):
			Summon(controller, target.id).trigger(source)
			pass
class BG_DAL_575:#カドガー
	""" Khadgar
	Your cards that summon minions summon twice_as_many. """
	##############  infinite loop?
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your cards that summon minions summon twice_as_many."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"ミニオンを召喚する自分のカードは通常の2倍召喚する。"}
	events = DeathrattleSummon(CONTROLLER, FRIENDLY + MINION).after(BG_DAL_575_Action(DeathrattleSummon.CARD, 1))
	#events = Summon(CONTROLLER, FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD)))
	pass
class TB_BaconUps_034:# <4>[1453]
	""" Khadgar
	Your cards that summon minions summon three times as many. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your cards that summon minions summon three times as many."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"ミニオンを召喚する自分のカードは通常の3倍召喚する。"}
	events = Summon(CONTROLLER, FRIENDLY_MINIONS).after(BG_DAL_575_Action(DeathrattleSummon.CARD,2))
	#events = Summon(CONTROLLER, FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD))*2)
	pass



##Nightmare Amalgam (3) 
if BG_Nightmare_Amalgam:##Nightmare Amalgam (3) RENEW  23.2 ## banned 24.6
	BG_Minion += ['BG_GIL_681','BG_GIL_681_G', ]#	
	BG_PoolSet_Minion.append('BG_GIL_681')
	BG_Minion_Gold['BG_GIL_681']='BG_GIL_681_G'
	# Nightmare Amalgam 3 RENEW  23.2
	pass
class BG_GIL_681:
	""" Nightmare Amalgam (3)
	<i>This has all minion types.</i>"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"<i>This has all minion types.</i>"}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;i&gt;これは全てのミニオンの種族を持つ。&lt;/i&gt;"}
	pass
class BG_GIL_681_G:
	""" Nightmare Amalgam (3)
	<i>This has all minion types.</i>"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"<i>This has all minion types.</i>"}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;i&gt;これは全てのミニオンの種族を持つ。&lt;/i&gt;"}
	pass


### 23/9/26 ###
## Shifter Zerus (3)
##BG_Shifter_Zerus=((Config.BG_VERSION>=2360 and Config.BG_VERSION<2420))
##(3) new 23.6 banned 24.2 ## revive 24.6 as a reward option## 
if BG_Shifter_Zerus:## Shifter Zerus (3) ### hard ### banned 24.2 ## come back 24.6
	BG_Minion += ['BGS_029','BGS_029e','TB_BaconUps_095', 'TB_BaconUps_095e']#	
	BG_PoolSet_Minion.append('BGS_029')
	BG_Minion_Gold['BGS_029']='TB_BaconUps_095'
	## Shifter Zerus (3) >=23.6
	pass
class BGS_029_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = source.controller
		card = RandomBGAdmissible(tech_level_less=controller.tavern_tier).evaluate(controller)
		card=get00(card)
		if card!=None:
			Buff(card, 'BGS_029e').trigger(source)
			card.zone=Zone.HAND
			source.discard()
		pass
class BGS_029:## OK
	"""Shifter Zerus (3) >=23.6
	Each turn this is in your hand, transform it into a random minion."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Each turn this is in your hand, transform it into a random minion."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"このカードが自分の手札にある場合毎ターンこれはランダムなミニオンに変身する。"}
	class Hand:
		events = WhenDrawn(CONTROLLER, SELF).after(BGS_029_Action(SELF))
class BGS_029e:
	class Hand:
		events = BeginBar(CONTROLLER,0).on(BGS_029_Action(OWNER))
	pass
class BGS_029_G_Action(TargetedAction):
	TARGET=ActionArg()## target = owner
	def do(self, source, target):
		controller = source.controller
		card = RandomBGAdmissible(tech_level_less=controller.tavern_tier).evaluate(controller)
		card=get00(card)
		gold_id = controller.game.parent.BG_Gold.get(card.id, 0)
		if gold_id==0:
			return
		card = controller.card(gold_id)
		card = get00(card)
		Buff(card, 'BGS_029e').trigger(source)
		card.zone=Zone.HAND
		target.discard()
		pass
class TB_BaconUps_095:
	"""
	Each turn this is in your hand, transform it into a random Golden minion."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Each turn this  is in your hand, transform it into a random Golden minion."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"このカードが自分の手札にある場合、毎ターンこれはランダムなゴールデンミニオンに変身する。"}
	class Hand:
		events = WhenDrawn(CONTROLLER, SELF).after(BGS_029_G_Action(SELF))
class TB_BaconUps_095e:
	class Hand:
		events = BeginBar(CONTROLLER,0).on(BGS_029_G_Action(OWNER))
	pass
	

### 23/9/26 ###
#Soul Juggler	3	3	5	-
if BG_Soul_Juggler:#Soul Juggler	3	3	5	-	 	 ### maybe ### banned 26.2
	BG_Minion += ['BGS_002','TB_BaconUps_075',]#	
	BG_PoolSet_Minion.append('BGS_002')
	BG_Minion_Gold['BGS_002']='TB_BaconUps_075'
	pass
class BGS_002:# <9>[1453] ソールジャグラー
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After a friendly Demon dies, deal 3 damage to a random enemy minion."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方の悪魔が死んだ後ランダムな敵のミニオン1体に3ダメージを与える。"}
	events = Death(FRIENDLY + DEMON).after(Hit(RANDOM(ENEMY_MINIONS), 3))
	pass
class TB_BaconUps_075:# <9>[1453]
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion twice. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After a friendly Demon dies, deal 3 damage to a random enemy minion twice."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方の悪魔が死んだ後に2回、ランダムな敵のミニオン1体に3ダメージを与える。"}
	events = Death(FRIENDLY + DEMON).after(Hit(RANDOM(ENEMY_MINIONS), 3), Hit(RANDOM(ENEMY_MINIONS), 3))
	pass



#################### TIER 4 ###################################



### 23/9/27 ###
### Ball of Minions(BG24_017) ### OK ### banned 26.2
if BG_Ball_of_Minions:#Ball of Minions	4	5	5		
	BG_Minion += ['BG24_017','BG24_017e','BG24_017_G',]#	
	BG_PoolSet_Minion.append('BG24_017')
	BG_Minion_Gold['BG24_017']='BG24_017_G'
	pass
class BG24_017_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=CardArg()
	AMOUNT=IntArg()
	def do(self, source, target, card, amount):
		controller=source.controller
		card=get00(card)
		if card==None:
			return
		cards = [cd for cd in controller.field]
		if len(cards)>amount:
			cards = random.sample(controller.field, amount)
		for minion in cards:
			Buff(minion, 'BG24_017e', atk=card.atk, max_health=card.max_health).trigger(source)
		pass
class BG24_017:
	""" Ball of Minions (4  5  5)
	When you sell this, give its stats to a random friendly minion."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"When you sell this, give its stats to a random friendly minion."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"これを売った時その攻撃力・体力をランダムな味方のミニオン1体に付与する。"}
	events = Sell(CONTROLLER, SELF).after(BG24_017_Action(CONTROLLER, Sell.CARD, 1))
class BG24_017e:
	pass
class BG24_017_G:
	""" Ball of Minions
	When you sell this, give its stats to two random friendly minions.""" 
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"When you sell this, give its stats to two random friendly minions."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"これを売った時その攻撃力・体力をランダムな味方のミニオン2体に付与する。"}
	events = Sell(CONTROLLER, SELF).after(BG24_017_Action(CONTROLLER, Sell.CARD, 2))
	pass



### 23/9/27 ###
#Champion of Y'Shaarj	4	4	4		 
if BG_Champion_of_Y_Shaarj:#Champion of Y'Shaarj	4	4	4		 ### maybe #####banned 23.6
	BG_Minion += ['BGS_111','BGS_111e','TB_BaconUps_301','TB_BaconUps_301e',]#	
	BG_PoolSet_Minion.append('BGS_111')
	BG_Minion_Gold['BGS_111']='TB_BaconUps_301'
	pass
class BGS_111:# <12>[1453]  ヤシャラージュ
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +1/+1 permanently. """
	### revised ???? 1/1 -> 1/2 once upon a time
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Whenever a friendly [Taunt] minion is attacked, gain +1/+2 permanently."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方の&lt;b&gt;挑発&lt;/b&gt;ミニオンが攻撃される度+1/+2を永続的に獲得する。"}
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'BGS_111e'))
	pass
BGS_111e=buff(1,2)# <12>[1453]
""" Y'Shaarj!!!,  +1/+2. """
class TB_BaconUps_301:# <12>[1453]
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +2/+2 permanently. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Whenever a friendly [Taunt] minion is attacked, gain +2/+4 permanently."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"味方の&lt;b&gt;挑発&lt;/b&gt;ミニオンが攻撃される度+2/+4を永続的に獲得する。"}
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'TB_BaconUps_301e'))
	pass
TB_BaconUps_301e=buff(2,4)# <12>[1453]
""" Y'Shaarj!!!!!!,  +2/+4. """



### 23/9/27 ###
#Defender of Argus	4	3	3	 	 
if BG_Defender_of_Argus:#Defender of Argus	4	3	3	 	 ### OK ###
	BG_Minion += ['EX1_093','EX1_093e','TB_BaconUps_009','TB_BaconUps_009e',]#	
	BG_PoolSet_Minion.append('EX1_093')
	BG_Minion_Gold['EX1_093']='TB_BaconUps_009'
	pass
class EX1_093:# <12>[1453]   アルガス
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give adjacent minions +1/+1 and [Taunt]."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt; 隣接するミニオンに+1/+1と&lt;b&gt;挑発&lt;/b&gt;を付与する。"}
	play = Buff(SELF_ADJACENT, 'EX1_093e')
	pass
EX1_093e=buff(1,1,taunt=True)
""" Hand of Argus, +2/+2 and [Taunt]. """
class TB_BaconUps_009:# <12>[1453]
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +2/+2 and [Taunt]. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give adjacent minions +2/+2 and [Taunt]."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;隣接するミニオンに+2/+2と&lt;b&gt;挑発&lt;/b&gt;を付与する。"}
	play = Buff(SELF_ADJACENT, 'TB_BaconUps_009e')
	pass
TB_BaconUps_009e=buff(2,2,taunt=True)# <12>[1453]
""" Hand of Argus,  +2/+2 and [Taunt]. """



### 23/9/27 ###
## Fireworks Fanatic 4  4  3
if BG_Fireworks_Fanatic: ##(4/4/3) new 25.6
	BG_Minion += ['BG25_922','BG25_922e','BG25_922_G','BG25_922_Ge',]#	
	BG_PoolSet_Minion.append('BG25_922')
	BG_Minion_Gold['BG25_922']='BG25_922_G'
	pass
class BG25_922_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if target.id in [minion.id for minion in source.controller.hand + source.controller.field]:
			for minion in source.controller.field:
				Buff(minion, 'BG25_922e').trigger(source)
			pass
class BG25_922: ##
	""" Fireworks Fanatic
	Whenever you get a minion you already have, give your minions +1/+1."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Whenever you get a minion you already have, give your minions +1/+1."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分が既に持っているミニオンを得る度味方のミニオン全てに+1/+1を付与する。"}
	events = [
		Give(CONTROLLER, MINION).on(BG25_922_Action(Give.CARD)),
		Buy(CONTROLLER, MINION).on(BG25_922_Action(Buy.CARD))
		]
BG25_922e=buff(1,1)
class BG25_922_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if target.id in [minion.id for minion in source.controller.hand + source.controller.field]:
			for minion in source.controller.field:
				Buff(minion, 'BG25_922_Ge').trigger(source)
			pass
class BG25_922_G:
	""" Fireworks Fanatic
	Whenever you get a minion you already have, give your minions +2/+2."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Whenever you get a minion you already have, give your minions +2/+2."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分が既に持っているミニオンを得る度味方のミニオン全てに+2/+2を付与する。"}
	events = [
		Give(CONTROLLER, MINION).on(BG25_922_G_Action(Give.CARD)),
		Buy(CONTROLLER, MINION).on(BG25_922_G_Action(Buy.CARD))
		]
BG25_922_Ge=buff(2,2)


### 23/9/27 ###
#Impatient Doomsayer	4	2	6	
if BG_Impatient_Doomsayer:#Impatient Doomsayer	4	2	6	### maybe ### banned 26.2
	BG_Minion += ['BG21_007','BG21_007_G',]#	
	BG_PoolSet_Minion.append('BG21_007')
	BG_Minion_Gold['BG21_007']='BG21_007_G'
	pass
	#Impatient Doomsayer	4
class BG21_007:# <12>[1453]  終魔通予言者
	""" Impatient Doomsayer
	[Avenge (4):] Add a random Demon to your hand. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (4):] Add a random Demon to your hand."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;仇討（4）:&lt;/b&gt;ランダムな悪魔1体を_自分の手札に追加する。"}
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [GiveInBattle(CONTROLLER, RandomBGDemon())]))
	pass
class BG21_007_G:# <12>[1453]
	""" Impatient Doomsayer
	[Avenge (4):] Add 2 random Demons to your hand. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (4):] Add 2 random Demons to your hand."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"]&lt;b&gt;仇討（4）:&lt;/b&gt;ランダムな悪魔2体を_自分の手札に追加する。"}
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [GiveInBattle(CONTROLLER, RandomBGDemon()), GiveInBattle(CONTROLLER, RandomBGDemon())]))
	pass



### 23/9/27 ###
#Majordomo Executus	4	6	3		 
if BG_Majordomo_Executus:#Majordomo Executus	4	6	3		 ### OK ###
	BG_Minion += ['BGS_105','BGS_105e','TB_BaconUps_207',]#	
	BG_PoolSet_Minion.append('BGS_105')
	BG_Minion_Gold['BGS_105']='TB_BaconUps_207'
	pass
	#Majordomo Executus	4
class BGS_105_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.field)>0:
			left_card = controller.field[0]
			count=1
			for card in controller.play_this_turn:
				#if card.type==CardType.MINION and card.race==Race.ELEMENTAL:
				if race_identity(card, Race.ELEMENTAL):
					count += 1
			Buff(left_card, 'BGS_105e', atk=count, max_health=count).trigger(source)
		pass
	pass
class BGS_105:# <12>[1453]
	""" Majordomo Executus エグゼクタス
	At the end of your turn, give your left-most minion +1/+1. Repeat for each Elementalyou played this turn. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn, give your left-most minion +1/+1. Repeat for each Elementalyou played this turn."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分のターンの終了時味方の一番左のミニオンに+1/+1を付与する。このターンに手札から使用したエレメンタルの数だけ繰り返す。"}
	events = OWN_TURN_END.on(BGS_105_Action(CONTROLLER))
	pass
class BGS_105e:# <12>[1453]
	""" Aegis of the Firelord
	Increased stats. """
	pass
class TB_BaconUps_207_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.field)>0:
			left_card = controller.field[0]
			count=1
			for card in controller.play_this_turn:
				#if card.type==CardType.MINION and card.race==Race.ELEMENTAL:
				if race_identity(card, Race.ELEMENTAL):
					count += 1
			Buff(left_card, 'BGS_105e', atk=count*2, max_health=count*2).trigger(source)
		pass
	pass
class TB_BaconUps_207:# <12>[1453]
	""" Majordomo Executus
	At the end of your turn, giveyour left-most minion +2/+2.Repeat for each Elementalyou played this turn. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn, giveyour left-most minion +2/+2.Repeat for each Elementalyou played this turn."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分のターンの終了時味方の一番左のミニオンに+2/+2を付与する。このターンに手札から使用したエレメンタルの数だけ繰り返す。"}
	events = OWN_TURN_END.on(TB_BaconUps_207_Action(CONTROLLER))



### 23/9/27 ###
#Master of Realities(4)	 ### maybe ### banned 26.2
if BG_Master_of_Realities:
	BG_Minion += ['BG21_036','BG21_036e','BG21_036_G','BG21_036_Ge',]#	
	BG_PoolSet_Minion.append('BG21_036')
	BG_Minion_Gold['BG21_036']='BG21_036_G'
	pass
# (5/6/6) -> (4/4/4)  2522
class BG21_036_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if buff.id!='BG21_036e' and buff.id!='BG21_036_Ge':
			if buff.atk>0 or buff.max_health>0:
				Buff(source, 'BG21_036e').trigger(source)
class BG21_036:# <12>[1453] 多重現実の支配者
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +1/+1. """
	if Config.BG_VERSION>= 2522:
		option_tags={GameTag.TECH_LEVEL:4, GameTag.ATK:4, GameTag.HEALTH:4}
	else:
		option_tags={GameTag.TECH_LEVEL:5, GameTag.ATK:6, GameTag.HEALTH:6}
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[[Taunt].] After a friendly Elemental gains stats, gain +1/+1."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;挑発&lt;/b&gt;味方のエレメンタルが攻撃力か体力を獲得した後+1/+1を獲得する。"}
	events = Buff(FRIENDLY + ELEMENTAL).on(BG21_036_Action(SELF, Buff.BUFF))
	pass
BG21_036e=buff(1,1)
class BG21_036_G_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if buff.id!='BG21_036e' and buff.id!='BG21_036_Ge':
			if buff.atk>0 or buff.max_health>0:
				Buff(source, 'BG21_036_Ge').trigger(source)
class BG21_036_G:# <12>[1453]
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +2/+2. """
	if Config.BG_VERSION>= 2522:
		option_tags={GameTag.TECH_LEVEL:4, GameTag.ATK:8, GameTag.HEALTH:8}
	else:
		option_tags={GameTag.TECH_LEVEL:5, GameTag.ATK:12, GameTag.HEALTH:12}
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[[Taunt].] After a friendly Elemental gains stats, gain +2/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[x]&lt;b&gt;挑発&lt;/b&gt;味方のエレメンタルが攻撃力か体力を獲得した後+2/+2を獲得する。"}
	events = Buff(FRIENDLY + ELEMENTAL).on(BG21_036_G_Action(SELF, Buff.BUFF))
	pass
BG21_036_Ge=buff(2,2)# <12>[1453]
""" The Elemental Plane, +2/+2. """



### 23/9/28 ###
#Menagerie Jug	4	3	3	-		 
if BG_Menagerie_Jug:#Menagerie Jug	4	3	3	-		 ### maybe ###
	BG_Minion += ['BGS_083','BGS_083e','TB_BaconUps_145','TB_BaconUps_145e',]#	
	BG_PoolSet_Minion.append('BGS_083')
	BG_Minion_Gold['BGS_083']='TB_BaconUps_145'
	pass
class BGS_083:# <12>[1453] ミナジェリ
	""" Menagerie Jug
	[Battlecry:] Give 3 random friendly minions of different minion types +2/+2. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give 3 random friendly minions of different minion types +2/+2."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;異なる種族のランダムな味方のミニオン3体に+2/+2を付与する。"}
	play = BGS_082_Action(CONTROLLER,'BGS_083e')## Method of 'Menagerie_Mug'
	pass
BGS_083e=buff(2,2)# <12>[1453]
""" Gulp of Tea,  +2/+2. """
class TB_BaconUps_145:# <12>[1453]
	""" Menagerie Jug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +4/+4. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give 3 randomfriendly minions of differentminion types +4/+4."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;異なる種族のランダムな味方のミニオン3体に+4/+4を付与する。"}
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_145e')
	pass
TB_BaconUps_145e=buff(4,4)# <12>[1453]
""" Gulp of Tea,  +4/+4. """



### 23/9/28 ###
## Reef Explorer(4/3/3) ### OK,  ### NEW 23.2 ### banned 24.6
if BG_Reef_Explorer:#
	BG_Minion += ['BG23_016','BG23_016_G', ]#	
	BG_PoolSet_Minion.append('BG23_016')
	BG_Minion_Gold['BG23_016']='BG23_016_G'
	# Reef Explorer 4 	
	pass
class BG23_016_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		if Config.LOGINFO:
			print("(BG23_016_Choice.choose)%s chooses %r"%(card.controller.name, card))
		card.zone=Zone.HAND
		self.player.choice=None
class BG23_016_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		races = copy(random_picker.BG_races)
		tier=controller.tavern_tier
		for card in controller.field:
			if card.race in races:
				races.remove(card.race)
		BG23_016_Choice(controller, RandomBGMinion(race=races, tech_level_less=tier)*3).trigger(source)
		pass
class BG23_016:# <12>[1453]
	""" Reef Explorer(4)
	[Battlecry: Discover] a minion from a minion type you don't control."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry: Discover] a minion from a minion type you don't control."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;自陣にいない種族のミニオンを1体&lt;b&gt;発見&lt;/b&gt;する。"}
	play = BG23_016_Action(CONTROLLER)
	pass
class BG23_016_G_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			print("(BG23_016_Choice.choose)%s chooses %r"%(card.controller.name, card))
		card.zone=Zone.HAND
		if self.source.sidequest_counter>=1:
			self.next_choice=None
			self.player.choice=None
		else:
			self.player.choice=self.next_choice=self
			self.source.sidequest_counter=1
class BG23_016_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		races = copy(random_picker.BG_races)
		tier=controller.tavern_tier
		for card in controller.field:
			if card.race in races:
				races.remove(card.race)
		BG23_016_G_Choice(controller, RandomBGMinion(race=races, tech_level_less=tier)*3).trigger(source)
		pass
class BG23_016_G:# <12>[1453]
	"""
	[Battlecry: Discover] 2 minions from minion types you don't control."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry: Discover] 2 minions from minion types you don't control."}	
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;自陣にいない種族のミニオンを2体&lt;b&gt;発見&lt;/b&gt;する。"}
	play = BG23_016_G_Action(CONTROLLER)
	pass


### 23/9/28 ###
## Rendle the Mistermind  4/4/5 
if BG24__Rendle_the_Mistermind:# # (4) new 24.2 banned 25.6
	BG_Minion+=['BG24_022','BG24_022_G']
	BG_PoolSet_Minion.append('BG24_022')
	BG_Minion_Gold['BG24_022']='BG24_022_G'
class BG24_022_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.opponent.field)>0:
			high=[]
			for card in controller.opponent.field:
				if high==[] or high[0].tech_level<card.tech_level:
					high=[card]
				elif high[0].tech_level==card.tech_level:
					high.append(card)
			card = random.choice(high)
			card.zone=Zone.SETASIDE
			card.controller=controller
			card.zone=Zone.HAND
		pass
class BG24_022:# (minion)
	""" Rendle the Mistermind
	At the end of your turn, steal the highest Tier minion from Bob's_Tavern. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn, steal the highest Tier minion from Bob's_Tavern. "}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分のターンの終了時ボブの酒場の最もグレードが高いミニオン1体を盗む。"}
	events = OWN_TURN_END.on(BG24_022_Action(CONTROLLER))
	pass
class BG24_022_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		for repeat in range(2):
			if len(controller.opponent.field)>0:
				high=[]
				for card in controller.opponent.field:
					if high==[] or high[0].tech_level<card.tech_level:
						high=[card]
					elif high[0].tech_level==card.tech_level:
						high.append(card)
				if len(high)>2:
					high=random.sample(high, 2)
				for card in high:
					card.zone=Zone.SETASIDE
					card.controller=controller
					card.zone=Zone.HAND
		pass
class BG24_022_G:# (minion)
	""" Rendle the Mistermind
	At the end of your turn, steal the 2 highest Tier minions from Bob's_Tavern. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn, steal the 2 highest Tier minions from Bob's_Tavern."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分のターンの終了時ボブの酒場の最もグレードが高いミニオン2体を盗む。"}
	events = OWN_TURN_END.on(BG24_022_G_Action(CONTROLLER))
	#
	pass


### 23/9/28 ###
# Sindorei Straight Shot 4/3/4
if BG25__Sindorei_Straight_Shot:# ## (4) new 25.2.2
	BG_Minion+=['BG25_016','BG25_016_G','BG25_016e','BG25_016e2']
	BG_PoolSet_Minion.append('BG25_016')
	BG_Minion_Gold['BG25_016']='BG25_016_G'
class BG25_016:# (minion)
	""" Sin'dorei Straight Shot
	[Windfury]. [Divine Shield]. Whenever this attacks, remove [Reborn] and [Taunt] from the target. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Windfury]. [Divine Shield]. Whenever this attacks, remove [Reborn] and [Taunt] from the target."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;疾風&lt;/b&gt;、&lt;b&gt;聖なる盾&lt;/b&gt;これが攻撃する度標的から&lt;b&gt;蘇り&lt;/b&gt;と&lt;b&gt;挑発&lt;/b&gt;を除去する。"}
	events = BG_Attack(SELF, ENEMY+MINION).on(Buff(BG_Attack.OTHER, 'BG25_016e'))
	pass
class BG25_016_G:# (minion)
	""" Sin'dorei Straight Shot
	[Mega-Windfury]. [Divine Shield]. Whenever this attacks, remove [Reborn] and [Taunt] from the target. """ ## old description until when? 
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Windfury]. [Divine Shield]. Whenever this attacks, remove [Reborn] and [Taunt] from the target. "}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;疾風&lt;/b&gt;、&lt;b&gt;聖なる盾&lt;/b&gt;これが攻撃する度標的から&lt;b&gt;蘇り&lt;/b&gt;と&lt;b&gt;挑発&lt;/b&gt;を除去する。"}
	events = BG_Attack(SELF, ENEMY+MINION).on(Buff(BG_Attack.OTHER, 'BG25_016e'))
	pass
BG25_016e=buff(reborn=False,taunt=False)
BG25_016e2=buff(taunt=False)


### 23/9/28 ###
#Strongshell Scavenger	4/2/3 
if BG_Strongshell_Scavenger:#Strongshell Scavenger	4	2	3		 ### OK ###
	BG_Minion += ['BG_ICC_807','ICC_807e','TB_BaconUps_072','TB_BaconUps_072e',]#	
	BG_PoolSet_Minion.append('BG_ICC_807')
	BG_Minion_Gold['BG_ICC_807']='TB_BaconUps_072'
	pass
class BG_ICC_807:# <2>[1453]  クズ拾い
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +2/+2. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give your [Taunt] minions +2/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;&lt;b&gt;挑発&lt;/b&gt;を持つ味方のミニオン全てに+2/+2を付与する。"}
	play = Buff(FRIENDLY + MINION + TAUNT, 'ICC_807e')
	pass
ICC_807e=buff(2,2)# <12>[1453]
""" Strongshell,  +2/+2. """
class TB_BaconUps_072:# <2>[1453]
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +4/+4. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give your [Taunt] minions +4/+4."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;&lt;b&gt;挑発&lt;/b&gt;を持つ味方のミニオン全てに+4/+4を付与する。"}
	play = Buff(FRIENDLY + MINION + TAUNT, 'TB_BaconUps_072e')
	pass
TB_BaconUps_072e=buff(4,4)# <12>[1453]
""" Strongshell,  +4/+4. """



### 23/9/28 ###
# Treasure Seeker Elise 4/5/5
if BG_Treasure_Seeker_Elise: ##(4) new 24.2
	BG_Minion += ['BG23_353','BG23_353_G', 'BG23_353_Gt']#	
	BG_PoolSet_Minion.append('BG23_353')
	BG_Minion_Gold['BG23_353']='BG23_353_G'
class BG23_353:
	""" Treasure-Seeker Elise
	After you [Refresh] 5 times, find the [Golden] Monkey(BG23_353_Gt)! [(@ left!)]"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you [Refresh] 5 times, find the [Golden] Monkey(BG23_353_Gt)! [(@ left!)]"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"5回&lt;b&gt;入替&lt;/b&gt;した後&lt;b&gt;黄金のサル&lt;/b&gt;を見つける！&lt;i&gt;（あと@回！）&lt;/i&gt;"}
	events = Rerole(CONTROLLER).on(SidequestCounter(SELF, 5, [Give(CONTROLLER, 'BG23_353_Gt')]))
	pass
class BG23_353_G:
	""" Treasure-Seeker Elise
	After you [Refresh] 5 times, find two [Golden] Monkeys!(BG23_353_Gt) [(@ left!)]"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you [Refresh] 5 times, find two [Golden] Monkeys!(BG23_353_Gt) [(@ left!)]"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"5回&lt;b&gt;入替&lt;/b&gt;した後&lt;b&gt;黄金のサル&lt;/b&gt;を2体見つける！&lt;i&gt;（あと@回！）&lt;/i&gt;"}
	events = Rerole(CONTROLLER).on(SidequestCounter(SELF, 5, [Give(CONTROLLER, 'BG23_353_Gt'), Give(CONTROLLER, 'BG23_353_Gt')]))
	pass
class BG23_353_Gt:
	""" Golden Monkey
	&lt;b&gt;挑発&lt;/b&gt;&lt;i&gt;（見つけました！）&lt;/i&gt;""" 
	pass



### 23/9/28 ###
# Tunnel Blaster (4/3/7) 
if BG_Tunnel_Blaster:## Tunnel Blaster (4) ### OK ###
	BG_Minion += ['BG_DAL_775','BG_DAL_775_G', ]#	
	BG_PoolSet_Minion.append('BG_DAL_775')
	BG_Minion_Gold['BG_DAL_775']='BG_DAL_775_G'
	## Tunnel Blaster (4) >= 23.6
	pass
class BG_DAL_775: 
	"""Tunnel Blaster (4) >= 23.6
	Taunt Deathrattle: Deal 3 damage to all minions."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Taunt Deathrattle: Deal 3 damage to all minions."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;挑発&lt;/b&gt;、&lt;b&gt;断末魔:&lt;/b&gt;全てのミニオンに3ダメージを与える。"}
	deathrattle = Hit(ALL_MINIONS, 3)
class BG_DAL_775_G:
	"""
	[Taunt] [Deathrattle:] Deal 3 damage to all minions twice."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Taunt] [Deathrattle:] Deal 3 damage to all minions twice."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;挑発&lt;/b&gt;、&lt;b&gt;断末魔:&lt;/b&gt;全てのミニオンに2回3ダメージを与える。"}
	deathrattle = Hit(ALL_MINIONS, 3) * 2



### 23/9/28 ###
#Vigilant Stoneborn (4/2/6)(BG24_023) ### OK ###
if BG_Vigilant_Stoneborn:#Vigilant Stoneborn	4	2	6		
	BG_Minion += ['BG24_023','BG24_023_G','BG24_023_Ge','BG24_023e']#	
	BG_PoolSet_Minion.append('BG24_023')
	BG_Minion_Gold['BG24_023']='BG24_023_G'
class BG24_023:
	""" Vigilant Stoneborn
	#[Battlecry:] Give a minion +6 Health and [Taunt]."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give a minion +6 Health and [Taunt]."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;ミニオン1体に体力+6と&lt;b&gt;挑発&lt;/b&gt;を付与する。"}
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Buff(TARGET, 'BG24_023e')
BG24_023e=buff(0,6, taunt=True)
class BG24_023_G:
	""" Vigilant Stoneborn
	#[Battlecry:] Give a minion +12 Health and [Taunt]."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Give a minion +12 Health and [Taunt]."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;雄叫び:&lt;/b&gt;ミニオン1体に体力+12と&lt;b&gt;挑発&lt;/b&gt;を付与する。"}
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	# 
	play = Buff(TARGET, 'BG24_023_Ge')
BG24_023_Ge=buff(0,12, taunt=True)



### 23/9/28 ###
#Witchwing Nestmatron	4/3/5  
if BG_Witchwing_Nestmatron:### maybe # ### banned 24.2 ## renew 25.0.4
	BG_Minion += ['BG21_038','BG21_038_G',]#	
	BG_PoolSet_Minion.append('BG21_038')
	BG_Minion_Gold['BG21_038']='BG21_038_G'
	pass
class BG21_038:# <12>[1453] 巣母
	""" Witchwing Nestmatron
	[Avenge (3):] Add a random [Battlecry] minion to your_hand. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (3):] Add a random [Battlecry] minion to your_hand."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;仇討（3）:&lt;/b&gt;ランダムな&lt;b&gt;雄叫び&lt;/b&gt;ミニオン1体を自分の手札に追加する。"}
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [GiveInBattle(CONTROLLER, RandomBGAdmissible(has_battlecry=True))]))
	pass
class BG21_038_G:# <12>[1453]
	""" Witchwing Nestmatron
	[Avenge (3):] Add 2 random [Battlecry] minions to your_hand. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Avenge (3):] Add 2 random [Battlecry] minions to your_hand."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"&lt;b&gt;仇討（3）:&lt;/b&gt;ランダムな&lt;b&gt;雄叫び&lt;/b&gt;ミニオン2体を自分の手札に追加する。"}
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [GiveInBattle(CONTROLLER, RandomBGAdmissible(has_battlecry=True)), GiveInBattle(CONTROLLER, RandomMinion(has_battlecry=True))]))
	pass




### 23/9/28 ###
## Upbeat Duo (4/4/2)-> (4/4/4)
#BG26__Upbeat_Duo=(Config.BG_VERSION>=2620)### new 26.2, renew 26.2.2
if BG26__Upbeat_Duo:
	BG_Minion += ['BG26_199', 'BG_NX2_050_G']
	BG_PoolSet_Minion.append('BG26_199')
	BG_Minion_Gold['BG26_199']='BG_NX2_050_G'
#New: 4 Attack, 4 Health. At the end of every 2 turns, get a plain copy of the minion to the left of this.
#Old: 4 Attack, 2 Health. Battlecry: Choose a minion. At the end of every 2 turns, this gives you a plain copy.
class BG26_199_Action(TargetedAction): ##
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		target = source.target
		if target!=None and getattr(target, 'this_is_minion'):
			if target in source.controller.field:
				Give(source.controller, target.id).trigger(source)
				if amount==2:
					Give(source.controller, target.id).trigger(source)
		pass
class BG26_199_Action2622(GameAction):
	def do(self, source):
		if source in source.controller.field:
			index=source.controller.field.index(source)
			if index>0:
				card=source.controller.field[index-1]
				Give(source.controller, card.id).trigger(source)
		pass
class BG26_199: ##
	""" Upbeat Duo
	At the end of every 2 turns, get a plain copy of the minion to the left of this.""" ## new 2622
	#4 Attack, 2 Health. Battlecry: Choose a minion. At the end of every 2 turns, this gives you a plain copy."""  
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:4, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"At the end of every 2 turns, get a plain copy of the minion to the left of this."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"2ターンごとの終了時左隣のミニオンの未強化コピーを1体得る。&lt;i&gt;（あと{0}ターン！）&lt;/i&gt;"}
		events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_199_Action2622()]))
		pass
	else:
		option_tags={GameTag.ATK:4, GameTag.HEALTH:2, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"Battlecry: Choose a minion. At the end of every 2 turns, this gives you a plain copy."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"雄叫び：ミニオンを1体選択。2ターンごとの終了時、これはその未強化コピー1体を手札に追加する。"}
		requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
		events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_199_Action(TARGET, 1)]))
	pass
class BG26_199_G_Action2622(GameAction):
	def do(self, source):
		if source in source.controller.field:
			index=source.controller.field.index(source)
			if index>0:
				card=source.controller.field[index-1]
				Give(source.controller, card.id).trigger(source)
			if index<len(source.controller.field)-1:
				card=source.controller.field[index+1]
				Give(source.controller, card.id).trigger(source)
		pass
class BG26_199_G: ##
	""" Upbeat Duo
	At the end of every 2 turns, get a plain copy of adjacent minions. <i>({0} |4(turn, turns) left!)</i> """
	#4 Attack, 2 Health. Battlecry: Choose a minion. At the end of every 2 turns, this gives you 2 plain copy.""" 
	if Config.BG_VERSION>=2622:	
		option_tags={GameTag.ATK:8, GameTag.HEALTH:8, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"At the end of every 2 turns, get a plain copy of adjacent minions. <i>({0} |4(turn, turns) left!)"}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"2ターンごとの終了時隣接するミニオンの未強化コピーを1体得る。&lt;i&gt;（あと{0}ターン！）&lt;/i&gt;"}
		events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_199_G_Action2622()]))
		pass
	else:
		option_tags={GameTag.ATK:8, GameTag.HEALTH:4, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"Battlecry: Choose a minion. At the end of every 2 turns, this gives you 2 plain copy."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"雄叫び：ミニオンを1体選択。2ターンごとの終了時、これはその未強化コピー2体を手札に追加する。"}
		requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
		events = OWN_TURN_END.on(SidequestCounter(SELF, 2, [BG26_199_Action(TARGET, 2)]))
	#
	pass


######## TIER 5 ################


if BG_Baron_Rivendare:#Baron Rivendare	5	1	7		 ### maybe ###
	BG_Minion += ['BG_FP1_031','TB_BaconUps_055',]#	
	BG_PoolSet_Minion.append('BG_FP1_031')
	BG_Minion_Gold['BG_FP1_031']='TB_BaconUps_055'
	pass
class BG_FP1_031:# ばろん
	"""Baron Rivendare
	Your minions trigger their [Deathrattles] twice."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your minions trigger their [Deathrattles] twice."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass
class TB_BaconUps_055:# <12>[1453]
	""" Baron Rivendare
	Your minions trigger their [Deathrattles] three times. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your minions trigger their [Deathrattles] three times."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES_ADDITIONAL: True})
	pass


if BG_Brann_Bronzebeard:#Brann Bronzebeard	5	2	4		 ### maybe ###
	BG_Minion += ['BG_LOE_077','LOE_077e','TB_BaconUps_045','TB_BaconUps_045e',]#	
	BG_PoolSet_Minion.append('BG_LOE_077')
	BG_Minion_Gold['BG_LOE_077']='TB_BaconUps_045'
	pass
class BG_LOE_077:#    ぶらん
	""" Brann Bronzebeard
	Your [Battlecries] trigger twice. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your [Battlecries] trigger twice."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_BASE: True})
	pass
class LOE_077e:# 
	""" Bronzebeard Battlecry
	Your [Battlecries] trigger twice. """
	pass
class TB_BaconUps_045:# <12>[1453]
	""" Brann Bronzebeard
	Your [Battlecries] trigger three times. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your [Battlecries] trigger three times."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_ADDITIONAL: True})
	pass
class TB_BaconUps_045e:# <12>[1453]
	""" Bronzebeard Battlecry
	Your [Battlecries] trigger three times. """
	pass




if BG_Deadly_Spore:##Deadly Spore	5	1	1	### OK #####banned 23.6
	BG_Minion += ['BGS_131','TB_BaconUps_251',]#	
	BG_PoolSet_Minion.append('BGS_131')
	BG_Minion_Gold['BGS_131']='TB_BaconUps_251'
	pass
class BGS_131:# <12>[1453]  横死の胞子
	""" Deadly Spore
	[Poisonous] """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Poisonous]"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	pass
class TB_BaconUps_251:# <12>[1453]
	""" Deadly Spore
	[Poisonous] """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Poisonous]"}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	pass


#Interrogator Whitemane 5  5  8 (BG24_704) ## new 24.6 ### OK ### banned 25.0.4
if BG_Interrogator_Whitemane:#Interrogator Whitemane 5  5  8 (BG24_704) 
	BG_Minion += ['BG24_704','BG24_704_e','BG24_704_e_G','BG24_704_G']#	
	BG_PoolSet_Minion.append('BG24_704')
	BG_Minion_Gold['BG24_704']='BG24_704_G'
	pass
class BG24_704_Action1(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller=source.controller
		opponent=controller.opponent
		size1=len(controller.field)
		size2=len(opponent.field)
		index1 = controller.field.index(source)
		index2=int(-index1*1.0+(size1-1)*0.5+(size2-1)*0.5)
		if 0<=index2 and index2<size2:
			card=opponent.field[index2]
			Buff(card, buff).trigger(source)
		pass
class BG24_704:
	""" Interrogator Whitemane -> banned 25.0.4
	#[x][Start of Combat:] Give the enemies opposite this [Taunt]. They take double damage."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Start of Combat:] Give the enemies opposite this [Taunt]. They take double damage."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = BeginBattle(CONTROLLER).on(BG24_704_Action1(SELF, 'BG24_704_e'))
class BG24_704_e:
	def apply(self, target):
		if target==None:
			return
		if hasattr(target, 'double_damage'):
			target.double_damage=1
		target.taunt=True
	pass

class BG24_704_G:
	""" Interrogator Whitemane
	#[Start of Combat:] Give the enemies opposite this [Taunt]. They take triple damage."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Start of Combat:] Give the enemies opposite this [Taunt]. They take triple damage."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = BeginBattle(CONTROLLER).on(BG24_704_Action1(SELF, 'BG24_704_e_G'))
class BG24_704_e_G:
	def apply(self, target):
		if target==None:
			return
		if hasattr(target, 'double_damage'):
			target.double_damage=2
		target.taunt=True
	pass



if BG_Kangor_s_Apprentice:#Kangor's Apprentice	5	3	6		 ### maybe ###
	BG_Minion += ['BGS_012','TB_BaconUps_087',]#	
	BG_PoolSet_Minion.append('BGS_012')
	BG_Minion_Gold['BGS_012']='TB_BaconUps_087'
	pass
class BGS_012_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		cards = []
		for card in controller.death_log:
			if race_identity(card,Race.MECHANICAL):
				cards.append(card)
		for repeat in range(amount):
			if repeat<len(cards):
				Summon(controller, cards[repeat].id).trigger(source)
class BGS_012:# <12>[1453]   ケンゴー
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 2 friendly Mechs that died this combat. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle]: Summon the first 2 friendly Mechs that died this combat."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	deathrattle = BGS_012_Action(CONTROLLER, 2)
	pass
class TB_BaconUps_087:# <12>[1453]
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 4 friendly Mechs that died this combat. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle]: Summon the first 4 friendly Mechs that died this combat. "}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	deathrattle = BGS_012_Action(CONTROLLER, 4)
	#
	pass



if BG_Leeroy_the_Reckless:## Leeroy the Reckless (5)  ### maybe ###
	BG_Minion += ['BG23_318','BG23_318_G', ]#	
	BG_PoolSet_Minion.append('BG23_318')
	BG_Minion_Gold['BG23_318']='BG23_318_G'
	# Leeroy the Reckless 5 NEW 23.2
	pass
class BG23_318_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		killer = target.attacker
		if hasattr(killer,'charge'):# instead of isinstance(killer, Minion)
			Destroy(killer).trigger(source.controller)
		pass
class BG23_318:# <12>[1453]
	""" Leeroy the Reckless (5)
	[Deathrattle:] Destroy the minion that killed this."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Destroy the minion that killed this."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	deathrattle = BG23_318_Action(SELF)
	pass
class BG23_318_G:# <12>[1453]
	"""
	[Deathrattle:] Destroy the minion that killed this."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Destroy the minion that killed this."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	deathrattle = BG23_318_Action(SELF)
	pass



if BG_Lightfang_Enforcer:#Lightfang Enforcer	5	2	2		 ### need check ###
	BG_Minion += ['BGS_009','BGS_009e','TB_BaconUps_082','TB_BaconUps_082e',]#	
	BG_PoolSet_Minion.append('BGS_009')
	BG_Minion_Gold['BGS_012']='TB_BaconUps_082'
	pass
class BGS_009_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		races=[]
		cards=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
				cards.append(card)
			elif not card.race in races:
				races.append(card.race)
				cards.append(card)
		for card in cards:
			Buff(source, 'BGS_009e').trigger(source)
class BGS_009:# <12>[1453]  光牙
	""" Lightfang Enforcer
	At the end of your turn, give a friendly minion of each minion type +2/+2. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn, give a friendly minion of each minion type +2/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER))
	pass
BGS_009e=buff(2,2)# <7>[1453]
""" Blessed,	Increased stats. """
class TB_BaconUps_082:# <12>[1453]
	""" Lightfang Enforcer
	At the end of your turn,give a friendly minionof each minion type+4/+4. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn,give a friendly minionof each minion type+4/+4."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER, 4))
	pass
class TB_BaconUps_082e:# <7>[1453]
	""" Blessed
	Increased stats. """





if BG_Mythrax_the_Unraveler:#Mythrax the Unraveler	5	4	4		 ### maybe ### banned 24.2 ## revive 25.0.4
	BG_Minion += ['BGS_202','BGS_202e','TB_BaconUps_258','TB_BaconUps_258e',]#	
	BG_PoolSet_Minion.append('BGS_202')
	BG_Minion_Gold['BG21_036']='TB_BaconUps_258'
	pass
class BGS_202_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		controller = target
		races=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
			elif not card.race in races:
				races.append(card.race)
		buffsize = len(races)
		for repeat in range(buffsize):
			Buff(source, buff).trigger(source)
class BGS_202:# <12>[1453] ミスラクス
	""" Mythrax the Unraveler
	At the end of your turn,gain +2/+2 for each__minion type you control. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn,gain +2/+2 for each__minion type you control."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'BGS_202e'))
	pass
BGS_202e=buff(2,2)# <12>[1453]
""" Void Echoes, +2/+2. """
class TB_BaconUps_258:# <12>[1453]
	""" Mythrax the Unraveler
	At the end of your turn,gain +4/+4 for each__minion type you control. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn,gain +4/+4 for each__minion type you control."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'TB_BaconUps_258e'))
	pass
TB_BaconUps_258e=buff(4,4)# <12>[1453]
""" Void Echoes, +4/+4. """




if BG_Nomi_Kitchen_Nightmare:#Nomi, Kitchen Nightmare	5	4	4	### OK ###
	BG_Minion += ['BGS_104','BGS_104e1','BGS_104pe','TB_BaconUps_201',]#	
	BG_PoolSet_Minion.append('BGS_104')
	BG_Minion_Gold['BGS_104']='TB_BaconUps_201'
	pass
class BGS_104_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		controller.nomi_powered_up += amount
class BGS_104:# <12>[1453]  ノミ（🐼）
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavern have +1/+1 for the restof the game. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you play an Elemental,Elementals in Bob's Tavern have +1/+1 for the restof the game."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 1))
	pass
class BGS_104e1:# <12>[1453]
	""" Tavern Feast
	Increased stats. """
BGS_104pe=buff(1,1)# <12>[1453]
""" Nomi Player Enchant
Increased stats. """
class TB_BaconUps_201:# <12>[1453]
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavernhave +2/+2 for the restof the game. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you play an Elemental,Elementals in Bob's Tavernhave +2/+2 for the restof the game."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 2))
	pass



if BG25__Titus_Rivendare:# 5/1/7 neutral ## new 25.2
	BG_Minion+=['BG25_354','BG25_354_G']
	BG_PoolSet_Minion.append('BG25_354')
	BG_Minion_Gold['BG25_354']='BG25_354_G'
class BG25_354:# (minion)
	""" Titus Rivendare
	Your [Deathrattles] trigger an extra time. """
	option_tags={GameTag.ATK:1, GameTag.HEALTH:7, }
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your [Deathrattles] trigger an extra time. "}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass

class BG25_354_G:# (minion)
	""" Titus Rivendare
	Your [Deathrattles] trigger 2 extra times. """
	option_tags={GameTag.ATK:2, GameTag.HEALTH:14, }
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your [Deathrattles] trigger 2 extra times. "}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES_ADDITIONAL: True})
	pass



if BG24__Tortollan_Blue_Shell:# new 24.2 (5) ### OK ###
	BG_Minion+=['BG24_018','BG24_018_G']
	BG_PoolSet_Minion.append('BG24_018')
	BG_Minion_Gold['BG24_018']='BG24_018_G'
class BG24_018_Action(TargetedAction):
	TARGET=ActionArg()#controller
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		controller=source.controller
		## tag 1587 gambler_sell_price
		SetAttr(source, 'gambler_sell_price', amount).trigger(source)
class BG24_018:# (minion, 5)
	""" Tortollan Blue Shell
	If you lost your last combat, this minion sells for 5 Gold. """
	tags={1587:1}
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"If you lost your last combat, this minion sells for 5 Gold."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = [
		LoseGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,5)),
		TieGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1)),
		WinGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1))
	]
	pass
class BG24_018_G:# (minion)
	""" Tortollan Blue Shell
	If you lost your last combat, this minion sells for 10 Gold. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"If you lost your last combat, this minion sells for 10 Gold."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = [
		LoseGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,10)),
		TieGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1)),
		WinGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1))
	]
	pass



if BG_Friend_of_a_Friend:#Friend of a Friend	(BANNED 22.3)	5	5	6	-	revive 26.0 -> (5)
	BG_Minion += ['BG22_404','BG22_404_G',]#	
	BG_PoolSet_Minion.append('BG22_404')
	BG_Minion_Gold['BG22_404']='BG22_404_G'
	pass
class BG22_404_Action(GameAction):
	def do(self, source):
		cards = source.controller.game.parent.BG_Hero_Buddy
		Discover(source.controler, RandomID(*cards)).trigger(source)
		pass
class BG22_404:# <12>[1453]  ##########################
	""" Friend of a Friend
	When you sell this [Discover] a Buddy """
	## 2230- [Battlecry: Discover] a Buddy. """
	if Config.BG_VERSION>=2600:
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"When you sell this [Discover] a Buddy"}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"xxx"}
		events = Sell(CONTROLLER, SELF).on(BG22_404_Action())
	elif Config.BG_VERSION<2230:
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Battlecry: Discover] a Buddy."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"xxx"}
		play = BG22_404_Action()
	pass
class BG22_404_G_Choice(Choice):
	def choose(self, card):
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone=Zone.SETASIDE
		card.controller=self.player
		card.zone=Zone.HAND
class BG22_404_G_Action(GameAction):
	def do(self, source):
		cards = source.controller.game.parent.BG_Hero_Buddy
		BG22_404_G_Choice(source.controler, RandomID(*cards)*3).trigger(source)
		pass
class BG22_404_G:# <12>[1453] #############################
	""" Friend of a Friend
	[Battlecry: Discover]two Buddies. """
	if Config.BG_VERSION>=2600:
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"When you sell this [Discover] two Buddies"}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"xxx"}
		events = Sell(CONTROLLER, SELF).on(BG22_404_G_Action())
	else:
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Battlecry: Discover]two Buddies."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"xxx"}
		play = BG22_404_G_Action()
	pass



### Drakkari Enchanter (5)
#BG26__Drakkari_Enchanter =(Config.BG_VERSION>=2620)### new 26.2
if BG26__Drakkari_Enchanter:
	BG_Minion += ['BG_NX2_050', 'BG_NX2_050_G']
	BG_PoolSet_Minion.append('BG_NX2_050')
	BG_Minion_Gold['BG_NX2_050']='BG_NX2_050_G'
class BG_NX2_050: ##
	""" Drakkari Enchanter
	1 Attack, 5 Health. Your end of turn effects trigger twice.""" 
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Your end of turn effects trigger twice."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = [
		BG_Play(SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',1)),
		Summon(CONTROLLER, SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',1)),
		Destroy(SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',0)),
		Sell(CONTROLLER, SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',0)),
	]
	pass
class BG_NX2_050_G: ##
	""" Drakkari Enchanter
	2 Attack, 10 Health. Your end of turn effects trigger three times.""" 
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:" Your end of turn effects trigger three times."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = [
		BG_Play(SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',2)),
		Summon(CONTROLLER, SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',2)),
		Destroy(SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',0)),
		Sell(CONTROLLER, SELF).on(SetAttr(CONTROLLER, 'turn_end_effects_twice',0)),
	]
	pass




#### TIER 6 ####


if BG_Amalgadon:#Amalgadon	6	6	6	*	 	 ### need check ###  banned 22.3
	BG_Minion += ['BGS_069','TB_BaconUps_121',]#	
	BG_PoolSet_Minion.append('BGS_069')
	BG_Minion_Gold['BGS_069']='TB_BaconUps_121'
	pass
class BGS_069_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		races=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
			elif not card.race in races:
				races.append(card.race)
		buffsize = len(races)*amount
		for repeat in range(buffsize):
			# adapting something
			buff = random.choice(['UNG_999t2e','UNG_999t3e','UNG_999t4e','UNG_999t6e','UNG_999t7e','UNG_999t8e','UNG_999t13e','UNG_999t14e'])
			Buff(source, buff).trigger(source)
		pass
class BGS_069:##  アマルガドン (アルマゲドンではない）
	""" Amalgadon
	[Battlecry:] For each different minion type you have among other minions, [Adapt] randomly."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] For each different minion type you have among other minions, [Adapt] randomly."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	play = BGS_069_Action(CONTROLLER, 1)	
	pass
class TB_BaconUps_121:
	""" Amalgadon
	[Battlecry:] For each different minion type you have among other minions, [Adapt] randomly twice."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] For each different minion type you have among other minions, [Adapt] randomly twice."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	play = BGS_069_Action(CONTROLLER, 2)
	pass

UNG_999t14e=buff(1,1)## 火山の力 ## +1/+1
UNG_999t13e=buff(poisonous=True)## 猛毒の唾 ## 猛毒
#class UNG_999t10e:## 霧隠れ ## 次の自分のターンまで隠れ身状態。
class UNG_999t8e:## 電気の盾 # 聖なる盾
	def apply(self,target):
		target.divine_shield=True
		pass
UNG_999t7e=buff(windfury=True)## 電光石火 # 疾風
UNG_999t6e=buff(taunt=True)## 巨体 # 挑発
#class UNG_999t5e:## 液状膜 ## 呪文とヒーローパワーの標的にならない。
UNG_999t4e=buff(0,3)## 岩状の甲殻 ## 体力+3
UNG_999t3e=buff(3,0)## 炎熱の爪 ##攻撃力+3
class UNG_999t2e:## 動き回る胞子 ##;断末魔:]1/1の植物を2体召喚する。
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = DeathrattleSummon(CONTROLLER, 'UNG_999t2t1')*2
class UNG_999t2t1:## 植物
	""" """




if BG_Mantid_Queen:##########
	BG_Minion += ['BG22_402', 'BG22_402_G', 'BG22_402e', 'BG22_402e2', 'BG22_402e3', 'BG22_402e4' ]#	
	BG_PoolSet_Minion.append('BG22_402')
	BG_Minion_Gold['BG22_402']='BG22_402_G'
class BG22_402_Action(GameAction):
	def do(self, source):
		types=[]
		for card in source.controller.field:
			if types==[]:
				if card.type!=CardType.INVALID:
					types.append(card.type)
			else:
				if card.type!=CardType.INVALID and not card.type in types:
					types.append(card.type)
		amount=len(types)
		if amount>0:
			if amount>4:
				amount=4
			buffs=['55','windfury', 'reborn', 'taunt']
			if amount<4:
				buffs=random.sample(buffs, amount)
			for buff in buffs:
				if buff=='55':
					Buff(source, 'BG22_402e').trigger(source)
				elif buff=='windfury':
					Buff(source, 'BG22_402e2').trigger(source)
				elif buff=='reborn':
					Buff(source, 'BG22_402e3').trigger(source)
				elif buff=='taunt':
					Buff(source, 'BG22_402e4').trigger(source)
class BG22_402: ###########################################
	""" Mantid Queen
	Venomous. Start of Combat: For each of your minion types gain +5/+5, Windfury, Reborn, or Taunt."""
	##Start of Combat: For each of your minion types gain +5/+5, Windfury, Divine Shield, or Taunt. ## old <2620
	### <2620
	###[Poisonous]. [Start of Combat:] For each of your minion types gain +5/+5, [Windfury], ___[Divine Shield], or [Taunt]."""
	if Config.BG_VERSION>=2620:
		##<Tag enumID="2853" name="VENOMOUS" type="Int" value="1"/>
		option_tags={GameTag.VENOMOUS:1,GameTag.POISONOUS:0,}
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"Venomous. Start of Combat: For each of your minion types gain +5/+5, Windfury, Reborn, or Taunt."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"[毒袋]、[戦闘開始時:]自陣のミニオンの種族1種につき、+5/+5、[疾風]、[蘇り]、[挑発]のどれか1つを獲得する。"}
		pass
	else:
		##<Tag enumID="363" name="POISONOUS" type="Int" value="1"/>
		option_tags={GameTag.POISONOUS:1,GameTag.VENOMOUS:0, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"Start of Combat: For each of your minion types gain +5/+5, Windfury, Divine Shield, or Taunt."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"xxx"}
		pass
	events = BeginBattle(CONTROLLER).on(BG22_402_Action())
	pass
class BG22_402_G_Action(GameAction):
	def do(self, source):
		types=[]
		for card in source.controller.field:
			if types==[]:
				if card.type!=CardType.INVALID:
					types.append(card.type)
			else:
				if card.type!=CardType.INVALID and not card.type in types:
					types.append(card.type)
		amount=len(types)*2
		if amount>0:
			if amount>5:
				amount=5
			buffs=['55','55','windfury', 'reborn', 'taunt']
			if amount<5:
				buffs=random.sample(buffs, amount)
			for buff in buffs:
				if buff=='55':
					Buff(source, 'BG22_402e').trigger(source)
				elif buff=='windfury':
					Buff(source, 'BG22_402e2').trigger(source)
				elif buff=='reborn':
					Buff(source, 'BG22_402e3').trigger(source)
				elif buff=='taunt':
					Buff(source, 'BG22_402e4').trigger(source)
class BG22_402_G: ##########if Config.BG_VERSION>=2620###################
	""" Mantid Queen
	[Poisonous]. [Start of Combat:] For each of your minion types gain [Windfury], [Divine Shield], _[Taunt], or +5/+5, twice."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Poisonous]. [Start of Combat:] For each of your minion types gain [Windfury], [Divine Shield], _[Taunt], or +5/+5, twice."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[毒袋]、[戦闘開始時:]自陣のミニオンの種族1種につき2回、+5/+5、[疾風]、[蘇り]、[挑発]のどれか1つを獲得する。"}
	events = BeginBattle(CONTROLLER).on(BG22_402_G_Action())	
	pass
BG22_402e=buff(5,5)
BG22_402e2=buff(windfury=True)
if Config.BG_VERSION>=2620:
	BG22_402e3=buff(reborn=True)
else:
	BG22_402e3=buff(divine_shield=True)
BG22_402e4=buff(taunt=True)


### 23/9/7 ###
if BG_Nadina_the_Red:#Nadina the Red	6	7	4		 ### maybe OK ###
	BG_Minion += ['BGS_040','TB_BaconUps_154',]#	
	BG_PoolSet_Minion.append('BGS_040')
	BG_Minion_Gold['BGS_040']='TB_BaconUps_154'
	pass
class BGS_040_Action2622(GameAction):
	def do(self, source):
		cards = [card for card in source.controller.field if isRaceCard(card, Race.DRAGON)==True]
		if len(cards)>3:
			cards=random.sample(cards, 3)
		for card in cards:
			#GiveDivineShield(card).trigger(source)
			card.divine_shield=True
	pass
class BGS_040_Action(GameAction):
	def do(self, source):
		cards = [card for card in source.controller.field if isRaceCard(card, Race.DRAGON)==True]
		for card in cards:
			card.divine_shield=True
	pass
class BGS_040:# <12>[1453]  ナディナ
	""" Nadina the Red
	Deathrattle: Give 3 friendly Dragons Divine Shield.""" ## new 2622
	##	[Deathrattle:] Give your Dragons [Divine Shield]. 
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:8, GameTag.HEALTH:4, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"Deathrattle: Give 3 friendly Dragons Divine Shield."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"[断末魔:]味方のドラゴン3体に[聖なる盾]を付与する。"}
		deathrattle = BGS_040_Action2622()
	else:
		option_tags={GameTag.ATK:7, GameTag.HEALTH:4, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Give your Dragons [Divine Shield]"}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"断末魔：味方のドラゴン全てに聖なる盾を付与する。"}
		deathrattle = BGS_040_Action()
	pass
class TB_BaconUps_154_Action2622(GameAction):
	def do(self, source):
		cards = [card for card in source.controller.field if isRaceCard(card, Race.DRAGON)==True]
		if len(cards)>6:
			cards=random.sample(cards, 6)
		for card in cards:
			card.divine_shield=True
	pass
class TB_BaconUps_154:# <12>[1453]
	""" Nadina the Red
	[Deathrattle:] Give 6 friendly Dragons [Divine Shield]."""
	## [Deathrattle:] Give your Dragons [Divine Shield]. """
	## lol in any case, at most 6 dragons.
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:16, GameTag.HEALTH:8, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Give 6 friendly Dragons [Divine Shield]."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"[断末魔:]味方のドラゴン6体に[聖なる盾]を付与する。"}
		deathrattle=TB_BaconUps_154_Action2622()
	else:
		option_tags={GameTag.ATK:14, GameTag.HEALTH:8, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Deathrattle:] Give your Dragons [Divine Shield]"}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"断末魔：味方のドラゴン全てに聖なる盾を付与する。"}
		deathrattle = BGS_040_Action()
	pass



if BG_Orgozoa_the_Tender:### Orgozoa, the Tender(6) ### OK ### NEW 23.2
	BG_Minion += ['BG23_015','BG23_015t','BG23_015_G','BG23_015_Gt',]#	
	BG_PoolSet_Minion.append('BG23_015')
	BG_Minion_Gold['BG23_015']='BG23_015_G'
	pass
class BG23_015:# <12>[1453]
	""" Orgozoa, the Tender(6)
	[Spellcraft: Discover] a Naga."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Spellcraft: Discover] a Naga."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[呪文錬成:]ナーガを1体[発見]する。"}
	play = Spellcraft(CONTROLLER,'BG23_015t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_015t'))
	tags={2359:'BG23_015t'}
class BG23_015t:
	play = Discover(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER)))
	tags = {GameTag.TECH_LEVEL:5}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
pass
class BG23_015_G:# <12>[1453]
	"""
	[Spellcraft: Discover] 2 Naga.</enUS>"""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Spellcraft: Discover] 2 Naga."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[呪文錬成:]ナーガを2体[発見]する。"}
	play = Spellcraft(CONTROLLER,'BG23_015_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_015_Gt'))
	tags={2359:'BG23_015_Gt'}
	pass
class BG23_015_Gt:
	play = DiscoverTwice(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER))*3)
	tags = {GameTag.TECH_LEVEL:5}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass




if BG_Seafood_Slinger:#Seafood Slinger	6	5	5		 ### maybe ### ##banned -> resurrect 25.0.4 -> banned 26.2
	BG_Minion += ['BG21_011','BG21_011e','BG21_011e2','BG21_011_G','BG21_011_Ge',]#	
	BG_PoolSet_Minion.append('BG21_011')
	BG_Minion_Gold['BG21_011']='BG21_011_G'
	pass
class BG21_011:# <12>[1453] 板前
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Make a Murloc Golden."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]マーロック1体をゴールデンにする。"}
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = MorphGold(TARGET)
	pass
BG21_011e=buff(3,3)# <12>[1453] ??????????????
class BG21_011e2:# <12>[1453]  ??????????????
	""" Battlecry Self-Trigger [DNT] """
class BG21_011_G:# <12>[1453]
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Make a Murloc Golden."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]マーロック1体をゴールデンにする。"}
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = MorphGold(TARGET)
	pass
BG21_011_Ge=buff(6,6)# <12>[1453]  ????????????


if BG24__Tea_Master_Theotar: # (6) new 24.2
	BG_Minion += ['BG24_020','BG24_020e','BG24_020_G','BG24_020_Ge', ]#	
	BG_PoolSet_Minion.append('BG24_020')
	BG_Minion_Gold['BG24_020']='BG24_020_G'
class BG24_020_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		if target.type==CardType.MINION and target.race==Race.INVALID:
			races=[]
			controller = source.controller
			for card in controller.field:
				if races==[] or not card.race in races:
					races.append(card.race)
			if len(races)>3:
				races = random.sample(races, 3)
			for race in races:
				cards = [card for card in controller.field if card.race==race]
				card = random.choice(cards)
				Buff(card, buff).trigger(source)
		pass
class BG24_020:	
	""" Tea Master Theotar
	After you play a minion with no_minion_type, give 3_friendly minions of different types +2/+2. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you play a minion with no_minion_type, give 3_friendly minions of different types +2/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分が種族なしのミニオンを手札から使用した後、異なる種族の味方のミニオン3体に+2/+2を付与する。"}
	events = Play(CONTROLLER, MINION).on(BG24_020_Action(Play.CARD,'BG24_020e'))
	pass
BG24_020e=buff(2,2)
class BG24_020_G:# (minion)
	""" Tea Master Theotar
	After you play a minion with no_minion_type, give 3_friendly minions of different types +4/+4. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you play a minion with no_minion_type, give 3_friendly minions of different types +4/+4."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分が種族なしのミニオンを手札から使用した後、異なる種族の味方のミニオン3体に+4/+4を付与する。"}
	events = Play(CONTROLLER, MINION).on(BG24_020_Action(Play.CARD,'BG24_020_Ge'))
	#
	pass
BG24_020_Ge=buff(4,4)


if BG24_The_Walking_Fort: # (6) new 24.2 ### OK ###
	BG_Minion += ['BG24_712','BG24_712e','BG24_712_G','BG24_712e_G', ]#	
	BG_PoolSet_Minion.append('BG24_712')
	BG_Minion_Gold['BG24_712']='BG24_712_G'
class BG24_712_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller=target
		cards = [card for card in controller.field if card.type==CardType.MINION and card.taunt==True]
		if len(cards)>4:
			cards=random.sample(cards, 4)
		for card in cards:
			Buff(card, buff).trigger(source)
		pass
class BG24_712:
	""" The Walking Fort(BG24_712) 4/6
	At the end of your turn, give 4 friendly [Taunt] minions +4/+4. """
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn, give 4 friendly [Taunt] minions +4/+4."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分のターンの終了時味方の[挑発]ミニオン4体に+4/+4を付与する。"}
	events = OWN_TURN_END.on(BG24_712_Action(CONTROLLER, 'BG24_712e'))
	pass
BG24_712e=buff(4,4)
class BG24_712_G:
	"""
	At the end of your turn, give 4 friendly [Taunt] minions +8/+8."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"At the end of your turn, give 4 friendly [Taunt] minions +8/+8."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"自分のターンの終了時味方の[挑発]ミニオン4体に+8/+8を付与する。"}
	events = OWN_TURN_END.on(BG24_712_Action(CONTROLLER, 'BG24_712e_G'))
	pass
BG24_712e_G=buff(8,8)


## Uther the Lightbringer (6) ### OK ###
if BG_Uther_the_Lightbringer: ##(6)
	BG_Minion += ['BG23_190','BG23_190e','BG23_190_G','BG23_190_Ge', ]#	
	BG_PoolSet_Minion.append('BG23_190')
	BG_Minion_Gold['BG23_190']='BG23_190_G'
	## Uther the Lightbringer (6) >= 23.6
	pass
class BG23_190_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		if target:
			atk_buff = amount - target.atk
			hlt_buff = amount - target.health
			Buff(target, buff, atk=atk_buff, max_health=hlt_buff).trigger(source)
			pass
class BG23_190:
	"""Uther the Lightbringer (6) >= 23.6
	Battlecry: Set a minion's Attack and Health to 15."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"Battlecry: Set a minion's Attack and Health to 15."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]ミニオン1体の攻撃力と体力を15にする。"}
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}	
	play = BG23_190_Action(TARGET, 'BG23_190e', 15)
class BG23_190e:
	pass
class BG23_190_G:
	"""
	[Battlecry:] Set a minion's Attack and Health to 30."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] Set a minion's Attack and Health to 30."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[雄叫び:]ミニオン1体の攻撃力と体力を30にする。"}
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}	
	play = BG23_190_Action(TARGET, 'BG23_190_Ge', 30)
class BG23_190_Ge:
	pass




if BG_Zapp_Slywick:#Zapp Slywick	6	7	10	 	 ### maybe ###
	BG_Minion += ['BGS_022','TB_BaconUps_091',]#	
	BG_PoolSet_Minion.append('BGS_022')
	BG_Minion_Gold['BGS_022']='TB_BaconUps_091'
	pass
class BGS_022:# <12>[1453] ざっぷ
	""" Zapp Slywick
	[Windfury]This minion always attacks the enemy minion with the lowest Attack. """
	#<ReferencedTag enumID="189" name="WINDFURY" type="Int" value="1"/> ### REF-TAGだ！
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:8, GameTag.HEALTH:16, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Windfury]This minion always attacks the enemy minion with the lowest Attack."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"[疾風]このミニオンは常に最も攻撃力が低い敵のミニオンを攻撃する。_"}
	else:
		option_tags={GameTag.ATK:7, GameTag.HEALTH:10, }
		if Config.LOCALE=='enUS':
			option_cardtext={GameTag.CARDTEXT:"[Windfury]This minion always attacks the enemy minion with the lowest Attack."}
		elif Config.LOCALE=='jaJP':
			option_cardtext={GameTag.CARDTEXT:"xxx"}
	tags = {GameTag.WINDFURY:1}
	#本体実装はBG_Battle.pyの80行あたり
	pass
class TB_BaconUps_091:# <12>[1453]
	""" Zapp Slywick
	[Mega-Windfury]This minion always attacksthe enemy minion withthe lowest Attack. """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/> ###これはオケ
	if Config.BG_VERSION>=2622:
		option_tags={GameTag.ATK:16, GameTag.HEALTH:32, }
	else:
		option_tags={GameTag.ATK:14, GameTag.HEALTH:20, }
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Mega-Windfury]This minion always attacksthe enemy minion withthe lowest Attack."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"[疾風]このミニオンは常に最も攻撃力が低い敵のミニオンを攻撃する。"}
	pass



## Archdruid Hamuul (6/8/8)
if BG_Archdruid_Hamuul:
	BG_Minion += ['BG20_304','BG20_304_G',]#	
	BG_PoolSet_Minion.append('BG20_304')
	BG_Minion_Gold['BG20_304']='BG20_304_G'
class BG20_304_Action(GameAction):
	def do(self, source):
		maxcount=0
		maxrace=None
		for race in [Race.BEAST, Race.DEMON, Race.DRAGON, Race,ELEMENTAL, Race.MECHANICAL, Race.MURLOC, Race.NAGA, Race.PIRATE, Race.UNDEAD]:
			count=0
			for card in source.controller.field:
				if isRaceCard(card, race)==True:
					count+=1
			if count>maxcount:
				maxcount=count
				maxrace=race
		if maxrace!=None:
			source.controller.archidruid_hamuul_rerole_race=maxrace
class BG20_304:#(6/8/8) # 大ドルイド・ハムウル
	""" Archdruid Hamuul
	[Battlecry:] [Refresh] Bob's Tavern with minions of your most common type."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] [Refresh] Bob's Tavern with minions of your most common type."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	play = BG20_304_Action()
	pass
class BG20_304_G:#(6/16/16)
	""" Archdruid Hamuul
	[Battlecry:] [Refresh] Bob's Tavern with minions of your most common type."""
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"[Battlecry:] [Refresh] Bob's Tavern with minions of your most common type."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	pass


### The Boogie Monster ## new 26.2
##BG_The_Boogie_Monster=(Config.BG_VERSION>=2620)
if BG_The_Boogie_Monster: ###
	BG_Minion += ['BG26_176','BG20_304_G','BG26_176_Ge']#	
	BG_PoolSet_Minion.append('BG26_176')
	BG_Minion_Gold['BG26_176']='BG20_304_G'
class BG26_176_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		tech_level = getattr(target, 'tech_level')
		if source.script_data_num_1==tech_level:
			for card in source.controller.field:
				Buff(card, buff).trigger(source)
		pass
class BG26_176:
	""" The Boogie Monster
	3 Attack, 8 Health. After you play a Tier 1 minion, progress to the next Tier and give your minions +1/+2."""
	### <Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you play a Tier 1 minion, progress to the next Tier and give your minions +1/+2."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}
	events = BG_Play(CONTROLLER).after(BG26_176_Action(BG_Play.CARD, 'BG26_176e'))
	pass
BG26_176e=buff(1,2)
class BG26_176_G:
	""" The Boogie Monster
	3 Attack, 8 Health. After you play a Tier 1 minion, progress to the next Tier and give your minions +2/+4."""
	events = BG_Play(CONTROLLER).after(BG26_176_Action(BG_Play.CARD, 'BG26_176_Ge'))
	if Config.LOCALE=='enUS':
		option_cardtext={GameTag.CARDTEXT:"After you play a Tier 1 minion, progress to the next Tier and give your minions +2/+4."}
	elif Config.LOCALE=='jaJP':
		option_cardtext={GameTag.CARDTEXT:"xxx"}

	pass
BG26_176_Ge=buff(2,4)
#######################



#if BG25__Cyborg_Enhancement:# 
#	BG25_+=['BG25_901e']
#class BG25_901e:# (enchantment)
#	""" Cyborg Enhancement
#	+10 Attack. """
#	#
#	pass
#
#	BG25_+=['BG25_901e2']
#class BG25_901e2:# (enchantment)
#	""" Cyborg Enhancement
#	+20 Attack. """
#	#
#	pass

#if BG25__Yaharr:# 
#	BG25_+=['BG25_910t15e']
#class BG25_910t15e:# (enchantment)
#	""" Yaharr!!
#	+2/+2. """
#	#
#	pass

########################