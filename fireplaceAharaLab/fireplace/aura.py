from .logging import log
from .managers import CardManager
from .config import Config

class AuraBuff:
	def __init__(self, source, entity):
		self.source = source
		self.entity = entity
		self.tags = CardManager(self)

	def __repr__(self):
		return "<AuraBuff %r -> %r>" % (self.source, self.entity)

	def update_tags(self, tags):
		self.tags.update(tags)
		self.tick = self.source.game.tick

	def remove(self):
		if Config.LOGINFO:
			Config.log("AuraBuff.remove","Destroying %r"% self)
		if self in self.entity.slots:
			self.entity.slots.remove(self)
		if self in self.source.game.active_aura_buffs:
			self.source.game.active_aura_buffs.remove(self)

	def _getattr(self, attr, i):
		value = getattr(self, attr, 0)
		if callable(value):
			return value(self.entity, i)
		return i + value


class Refresh:
	"""
	Refresh a buff or a set of tags on an entity
	"""
	def __init__(self, selector, tags=None, buff=None, priority=50):
		self.selector = selector
		self.tags = tags
		self.buff = buff
		self.priority = priority

	def trigger(self, source):
		entities = self.selector.eval(source.game.entities + source.game.hands, source) # game ? entities + hands?
		for entity in entities:
			if self.buff and hasattr(entity, 'refresh_buff'):
				entity.refresh_buff(source, self.buff)
			else:
				tags = {}
				if self.tags:
					for tag, value in self.tags.items():
						if not isinstance(value, int) and not callable(value):
							value = value.evaluate(source)
						tags[tag] = value
				if hasattr(entity, 'refresh_tags'):
					entity.refresh_tags(source, tags)

	def __repr__(self):
		return "Refresh(%r, %r, %r)" % (self.selector, self.tags or {}, self.buff or "")


class TargetableByAuras:
	def refresh_buff(self, source, id):
		for buff in self.buffs:
			if hasattr(buff, 'source') and source and hasattr(buff.source, 'entity_id') and hasattr(source, 'entity_id'):
				if buff.source.entity_id == source.entity_id and buff.id == id:
					buff.tick = source.game.tick
					break
		else:
			if Config.LOGINFO:
				Config.log("TargetableByAuras.refresh_buff","Aura from %r buffs %r with %r"%( source, self, id))
			buff = source.buff(self, id)
			buff.tick = source.game.tick
			source.game.active_aura_buffs.append(buff)

	def refresh_tags(self, source, tags):
		for slot in self.slots:
			if slot.source is source:
				slot.update_tags(tags)
				break
		else:
			buff = AuraBuff(source, self)
			if Config.LOGINFO:
				Config.log("TargetableByAuras.refresh_tags","Creating %r"% buff)
			buff.update_tags(tags)
			self.slots.append(buff)
			source.game.active_aura_buffs.append(buff)
