class Config:# ()is the default value

	HEARTHSTONE=3
	#3: Hearthstone battleground

	#LOCALE
	LOCALE='jaJP'#'enUS'

	#LOGINFO
	LOGINFO=0 # as log.info
	LOGINFO_INDENT=0
	def log(function, message):
		if Config.LOGINFO_INDENT>0:
			for repeat in range(Config.LOGINFO_INDENT):
				print("====>", end="")
		print("( %s )"%(function), end="")
		print(" %s"%(message))
	DEEPCOPY_LOGINFO=0
	#debugLog
	GAMELOG=1 # as debugLog option

	#battlegrounds version management
	#BG_VERSION=2660## 2023/06/28 
	#BG_VERSION=2643## 2023/06/16 
	BG_VERSION=2640## 2023/05/31 
	#BG_VERSION=2622## 
	#BG_VERSION=2620## 2023/05/09 # season 4
	#BG_VERSION=2604## 2023/04/28
	#BG_VERSION=2602## 2023/04/15
	#BG_VERSION=2600## 2023/04/04
	#BG_VERSION=2562## 2023/03/24
	#BG_VERSION=2560## 2023/03/15
	#BG_VERSION=2543## 2023/03/03
	#BG_VERSION=2540## 2023/02/14
	#BG_VERSION=2522## 2023/01/27
	#BG_VERSION=2520## 2023/01/18 # season 3
	#BG_VERSION=2504## 2022/12/20
	#BG_VERSION=2503## 2022/12/10
	#BG_VERSION=2500## 2022/11/29
	#BG_VERSION=2462## 2022/11/11
	#BG_VERSION=2460## 2022/11/02



	#3 battlegrounds options
	BUDDY_SYSTEM = 0### buddy system (- 23.1) -April 2022
	if BG_VERSION>=2560 and BG_VERSION<=2604:
		NEW_BUDDY_SYSTEM = 1 ### buddy system 25.6 - 26.0
	else:
		NEW_BUDDY_SYSTEM = 0
	DARKMOON_TICKET_FOR_ALL=0 ## darkmoon tickets for all player anytime
	DARKMOON_TICKET_FOR_ALL_BY_HALF=0 ## darkmoon tickets for all player sometimes
	QUEST_REWARD=0 ## quest and reward system（24.2 - 25.2.2)
	QUEST_PRESET=''##  preset a quest at the beginning
	REWARD_PRESET_FIRST=0 ## preset a reward at the beginning (for debugging)
	REWARD_PRESET=''


	######## player1 is a humna or not
	PLAYER1_HUMAN=1 ## battleground with a human player(human play:1 full autoplay:0)
	RANDOM_RACE=1 #random sampling from races（default:1）
	#sampling from ['beast','demon','dragon','elemental','mecha','murloc','naga','pirate','quilboar','undead']
	RACE_CHOICE=['naga','elemental']# valid when RANDOM_RACE=0

	#card preset
	HERO_1='TB_BaconShop_HERO_15' #The first player ('Human1') are allowed to get a specific hero
	CARD_PRESET1='BG26_537' #The first player ('Human1') are allowed to have a specific card in his hand.
	CARD_PRESET2='' #The first player ('Human1') are allowed to have a specific card in his hand.
	ALL_PLAYERS_LOGINFO = 1 ## show all logs of playings of all players at Bob's tavern.

