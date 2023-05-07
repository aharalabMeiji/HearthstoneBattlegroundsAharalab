class Config:# ()is the default value

	HEARTHSTONE=3
	#3: Hearthstone battleground

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

	#3 battlegrounds options
	BUDDY_SYSTEM = 0### buddy system (- 23.1) -April 2022
	NEW_BUDDY_SYSTEM = 1 ### buddy system 25.6 - 26.0
	DARKMOON_TICKET_FOR_ALL=0 ## darkmoon tickets for all player anytime
	DARKMOON_TICKET_FOR_ALL_BY_HALF=0 ## darkmoon tickets for all player sometimes
	QUEST_REWARD=0 ## quest and reward system（24.2 - 25.2.2)
	QUEST_PRESET=''##  preset a quest at the beginning
	REWARD_PRESET_FIRST=0 ## preset a reward at the beginning (for debugging)
	REWARD_PRESET=''

	######## player1 is a humna or not
	PLAYER1_HUMAN=0 ## battleground with a human player(human play:1 full autoplay:0)
	RANDOM_RACE=1 #random sampling from races（default:1）
	#sampling from ['beast','demon','dragon','elemental','mecha','murloc','naga','pirate','quilboar','undead']
	RACE_CHOICE=['naga','dragon']# valid when RANDOM_RACE=0

	#card preset
	HERO_1='' #The first player ('Human1') are allowed to get a specific hero
	CARD_PRESET1='' #The first player ('Human1') are allowed to have a specific card in his hand.
	CARD_PRESET2='' #The first player ('Human1') are allowed to have a specific card in his hand.
	ALL_PLAYERS_LOGINFO = 1 ## show all logs of playings of all players at Bob's tavern.

