#using sqlalchemy version 0.9.4
#http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html
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

engine = create_engine('sqlite:///ova.db', echo=False)
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

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


    














