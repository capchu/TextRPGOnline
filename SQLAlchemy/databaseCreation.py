#using sqlalchemy version 0.9.4
#http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html
import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import aliased
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

database = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'ova.db')
engine = create_engine(database, echo=False)
Base = declarative_base()

class Ability(Base):
    __tablename__ = 'abilities'
    id = Column(Integer, Sequence('ability_id_seq'), primary_key=True)
    name = Column(String(50))
    description = Column(String(2048))

    def __repr__(self):
        return "<Ability(id='%s', name='%s', description='%s')>" % (
                                self.id, self.name, self.description)

class Weakness(Base):
    __tablename__ = 'weaknesses'
    id = Column(Integer, Sequence('weakness_id_seq'), primary_key=True)
    name = Column(String(50))
    description = Column(String(2048))

    def __repr__(self):
        return "<Weakness(id='%s', name='%s', description='%s')>" % (
                                self.id, self.name, self.description)

class Flaw(Base):
    __tablename__ = 'flaws'
    id = Column(Integer, Sequence('flaws_id_seq'), primary_key=True)
    name = Column(String(50))
    description = Column(String(2048))
    cost = Column(String(10))
    multiples = Column(String(10))

    def __repr__(self):
        return "<Flaw(id='%s', name='%s', description='%s', cost='%s', multiples='%s')>" % (
                               self.id, self.name, self.description, self.cost, self.multiples)

class Perk(Base):
    __tablename__ = 'perks'
    id = Column(Integer, Sequence('perks_id_seq'), primary_key=True)
    name = Column(String(50))
    description = Column(String(2048))
    cost = Column(String(10))
    multiples = Column(String(10))

    def __repr__(self):
        return "<Perk(id='%s', name='%s', description='%s', cost='%s', multiples='%s')>" % (
                                self.id, self.name, self.description, self.cost, self.multiples)

class AttackFlaw(Base):
    __tablename__ = 'attack_flaws'
    id = Column(Integer, Sequence('attack_flaw_id_seq'), primary_key=True)
    flaw_id = Column(Integer, ForeignKey("flaws.id"), nullable=False)
    attack_id = Column(Integer, ForeignKey("character_attacks.id"), nullable=False)
    multiplier = Column(String(10))
    note = Column(String(2048))
    
    def __repr__(self):
        return "<AttackFlaw(flaw_id='%s', attack_id='%s', multiplier='%s', note='%s')>" % (
                                self.flaw_id, self.attack_id, self.multiplier, self.note)

class AttackPerk(Base):
    __tablename__ = 'attack_perks'
    id = Column(Integer, Sequence('attack_perk_id_seq'), primary_key=True)
    perk_id = Column(Integer, ForeignKey("perks.id"), nullable=False)
    attack_id = Column(Integer, ForeignKey("character_attacks.id"), nullable=False)
    multiplier = Column(String(10))
    note = Column(String(2048))
    
    def __repr__(self):
        return "<AttackPerk(perk_id='%s', attack_id='%s', multiplier='%s', note='%s')>" % (
                                self.perk_id, self.attack_id, self.multiplier, self.note)

class CharacterAttack(Base):
    __tablename__ = 'character_attacks'
    id = Column(Integer, Sequence('attack_id_seq'), primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    name = Column(String(50))
    roll = Column(String(50))
    dx = Column(String(50))
    end = Column(String(50))
    note = Column(String(2048))
    
    def __repr__(self):
        return "<CharacterAttack(id='%s', character_id='%s', name='%s', roll='%s', dx='%s', end='%s', note='%s')>" % (
                                self.id, self.character_id, self.name, self.roll, self.dx, self.end, self.note)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, Sequence('character_id_seq'), primary_key=True)
    user_id = Column(String(50))
    name = Column(String(50))
    combat_notes = Column(String(2048))
    defense = Column(String(50))
    health = Column(String(50))
    endurance = Column(String(50))
    tv = Column(String(50))
    background = Column(String(2048))
    appearance = Column(String(2048))
    personality = Column(String(2048))
    other_notes = Column(String(2048))
    portrait_url = Column(String(150))
    icon_url = Column(String(150))
       
    def __repr__(self):
        return "<CharacterAttack(id='%s', user_id='%s', name='%s', combat_notes='%s', defense='%s', health='%s', endurance='%s', tv='%s', background='%s', appearance='%s', personality='%s', other_notes='%s', portrait_url='%s', icon_url='%s')>" % (
                                self.id, self.user_id, self.name, self.combat_notes, self.defense, self.health, self.endurance, self.tv, self.background, self.appearance, self.personality, self.other_notes, self.portrait_url, self.icon_url)

class CharacterAbility(Base):
    __tablename__ = 'character_ability'
    id = Column(Integer, Sequence('character_ability_id_seq'), primary_key=True)
    ability_id = Column(Integer, ForeignKey("abilities.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    ability_value = Column(String(10))
    ability_note = Column(String(2048))
    
    def __repr__(self):
        return "<CharacterAbility(ability_id='%s', character_id='%s', ability_value='%s', ability_note='%s')>" % (
                                self.ability_id, self.character_id, self.ability_value, self.ability_note)

class CharacterWeakness(Base):
    __tablename__ = 'character_weakness'
    id = Column(Integer, Sequence('character_weakness_id_seq'), primary_key=True)
    weakness_id = Column(Integer, ForeignKey("weaknesses.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    weakness_value = Column(String(10))
    weakness_note = Column(String(2048))
    
    def __repr__(self):
        return "<CharacterAbility(weakness_id='%s', character_id='%s', weakness_value='%s', weakness_note='%s')>" % (
                                self.weakness_id, self.character_id, self.weakness_value, self.weakness_note)

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, Sequence('game_id_seq'), primary_key=True)
    owner_id = Column(String(50))
    name = Column(String(50))
    
    def __repr__(self):
        return "<Game(owner_id='%s', name='%s')>" % (
                                self.owner_id, self.name)

class GameCharacter(Base):
    __tablename__ = 'game_characters'
    id = Column(Integer, Sequence('game_char_id_seq'), primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    
    def __repr__(self):
        return "<GameCharacters(game_id='%s', character_id='%s')>" % (
                                self.game_id, self.character_id)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


    














