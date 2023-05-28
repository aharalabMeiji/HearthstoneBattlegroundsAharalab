#!/usr/bin/env python
import sys
from hearthstone.enums import *
from utils import *
from fireplace import cards
#from fireplace.debug_utilities import printClasses, printClasses_BG24, parse, parseDeck, printPool
from fireplace.config import Config

sys.path.append("..")




####################################################################

### HEARTHSTONE=3

def battleground_main():
	from fireplace.battlegrounds.BG_utils import  BG_main
	for repeat in range(50):
		BG=BG_main()
		BG.BG_main()
	pass


def printClasses_BG26():
	from hearthstone import cardxml
	mySet="BG26_"# "BG24", "BG24_Reward",BG24_Quest
	raceName="Undead"
	race=Race.UNDEAD
	filename=mySet.lower()+"_minion_"+raceName.lower()

	f = open("%s.py"%filename, 'w')
	f.write('from ..utils import *\n')
	f.write('\n')
	f.write ("%s=[]\n\n"%(mySet))
	db, xml = cardxml.load(locale='enUS')
	f.write('\n'%())
	keyID='XXX_000'
	for _id in db.keys():
		_card = db[_id]
		if getattr(_card,'race')==race and mySet in _card.id and _card.id[5] in ['0','1','2','3','4','5','6','7','8','9']: 
			if not keyID in _card.id:
				f.write("## %s (%s) (%s)\n"%(_card.name, raceName, _card.tags[GameTag.TECH_LEVEL]))
				f.write("%s_%s=(Config.BG_VERSION>=2620)\n"%(mySet,_card.name.replace(' ','_').replace('-','_').replace("'",'').replace(':','').replace('!','').replace('=','')))
				f.write('if %s_%s:# \n'%(mySet,_card.name.replace(' ','_').replace('-','_').replace("'",'').replace(':','').replace('!','').replace('=','')))
				f.write("\tBG_Minion_%s+=['%s']\n"%(raceName, _card.id))
				f.write("\tBG_PoolSet_%s.append('%s')\n"%(raceName, _card.id))
				f.write("\tBG_%s_Gold['%s']=''\n"%(raceName, _card.id))
				keyID=_card.id		
				f.write('class %s_Action(GameAction):# \n'%(_card.id))
				f.write('\tdef do(self, source):# \n'%())
				f.write('\t\tpass# \n'%())
			else:
				f.write("\tBG_Minion_%s+=['%s']\n"%(raceName, _card.id))

			f.write('class %s:# '%(_card.id))
			if _card.type==4:
				f.write("(minion)")
			if _card.type==5:
				f.write("(spell)")
			if _card.type==6:
				f.write("(enchantment)")
			if _card.race==15:
				f.write("(demon)")
			if _card.race==14:
				f.write("(murloc)")
			f.write("\n")
			f.write('\t""" %s\n'%(_card.name))
			f.write('\t%s """\n'%(_card.description.replace('\n',' ').replace('[x]','').replace('[','[').replace(']',']')))
			f.write('\t#\n'%())
			f.write('\tpass\n'%())
			f.write('\n'%())
		pass
	f.close()
	pass


if __name__ == "__main__":
	battleground_main()
