#using sqlalchemy version 0.9.4
#http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html
from databaseCreation import Ability
from databaseCreation import Weakness
from databaseCreation import Flaw
from databaseCreation import Perk
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
Session = sessionmaker(bind=engine)
session = Session()

class DataAccess():
    def __init__(self):
        self.name = 'doStuff'
        #self.addBaseData()

    # Returns a list of objects (can be found in databaseCreation) of the type resquested
    def getAbilities(self):
        return session.query(Ability).order_by(Ability.name)
            
    def getWeaknesses(self):
        return session.query(Weakness).order_by(Weakness.name)
            
    def getFlaws(self):
        return session.query(Flaw).order_by(Flaw.name)
            
    def getPerks(self):
        return session.query(Perk).order_by(Perk.name)

    # Print them to console for testing
    def printAbilities(self):
        for ab in session.query(Ability).order_by(Ability.name):
            print ab.__repr__()
            
    def printWeaknesses(self):
        for wk in session.query(Weakness).order_by(Weakness.name):
            print wk.__repr__()
            
    def printFlaws(self):
        for fl in session.query(Flaw).order_by(Flaw.name):
            print fl.__repr__()
            
    def printPerks(self):
        for pk in session.query(Perk).order_by(Perk.name):
            print pk.__repr__()

    def addDummy(self):
        test_ability = Ability(name='test', description='this is a test ability')
        test_weakness = Weakness(name='test', description='this is a test weakness')
        test_flaw = Flaw(name='test', description='this is a test flaw', cost=-15, multiples='Y')
        test_perk = Perk(name='test', description='this is a test perk', cost=15, multiples='N')

        session.add(test_ability)
        session.add(test_weakness)
        session.add(test_flaw)
        session.add(test_perk)
        session.commit()

    #ONLY RUN THIS ONCE AFTER CREATING A NEW DB (otherwise we will get multiples of every row)
    def addBaseData(self):
        #print 'here'
        connection = engine.connect()
        f = open('sql/OVA_Abilities.sql')
        sqlText = str(f.read())
        #sqlText = 'INSERT INTO abilities (name, description) VALUES ("Agile","You are naturally adept at moving your body skillfully. Your graceful movements can impress others, as well as aid in a variety of derring-do. Add your Agile dice to Attack rolls and while balancing, dancing, performing aerial feats, or taking on other activities that test your coordination and grace. You may also add Agile to Defense rolls when in cluttered or otherwise difficult to navigate terrain.")'
        splitOn = "**"
        for stmnt in sqlText.split(splitOn):
            #print stmnt
            #print '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=appended=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
            connection.execute(stmnt)

        f = open('sql/OVA_Weaknesses.sql')
        sqlText = str(f.read())
        for stmnt in sqlText.split(splitOn):
            connection.execute(stmnt)

        f = open('sql/OVA_Flaws.sql')
        sqlText = str(f.read())
        for stmnt in sqlText.split(splitOn):
            connection.execute(stmnt)

        f = open('sql/OVA_Perks.sql')
        sqlText = str(f.read())
        for stmnt in sqlText.split(splitOn):
            connection.execute(stmnt)
            
        session.commit()
        
        
        















