#using sqlalchemy version 0.9.4
#http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html
import os
from databaseCreation import Ability
from databaseCreation import Weakness
from databaseCreation import Flaw
from databaseCreation import Perk
from databaseCreation import AttackFlaw
from databaseCreation import AttackPerk
from databaseCreation import CharacterWeakness
from databaseCreation import CharacterAbility
from databaseCreation import CharacterAttack
from databaseCreation import Character
from databaseCreation import Game
from databaseCreation import GameCharacter
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

class DataAccess():
    database = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'ova.db?check_same_thread=False')
    engine = create_engine(database, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    def __init__(self):
        #Session = sessionmaker(bind=engine)
        #session = Session()
        self.name = 'doStuff'
        #self.addBaseData()

    def getSession(self):
        return self.session
    # Returns a list of objects (can be found in databaseCreation) of the type resquested
    def getAbilities(self):
        return self.session.query(Ability).order_by(Ability.name)
            
    def getWeaknesses(self):
        return self.session.query(Weakness).order_by(Weakness.name)
            
    def getFlaws(self):
        return self.session.query(Flaw).order_by(Flaw.name)
            
    def getPerks(self):
        return self.session.query(Perk).order_by(Perk.name)

    def getCharacters(self, username):
        return self.session.query(Character).filter(Character.user_id==username)

    def getCharacter(self, char_id):
        return self.session.query(Character).filter(Character.id==char_id).first()

    def getCharAbilities(self, char_id):
        return self.session.query(CharacterAbility).filter(CharacterAbility.character_id==char_id)

    def getAbilityDetails(self, ability_id):
        return self.session.query(Ability).filter(Ability.id==ability_id).first()

    def getCharWeaknesses(self, char_id):
        return self.session.query(CharacterWeakness).filter(CharacterWeakness.character_id==char_id)

    def getWeaknessDetails(self, weakness_id):
        return self.session.query(Weakness).filter(Weakness.id==weakness_id).first()

    def getCharAttacks(self, char_id):
        return self.session.query(CharacterAttack).filter(CharacterAttack.character_id==char_id)

    def getAttackFlaws(self, attack_id):
        return self.session.query(AttackFlaw).filter(AttackFlaw.attack_id==attack_id)

    def getFlawDetails(self, flaw_id):
        return self.session.query(Flaw).filter(Flaw.id==flaw_id).first()

    def getAttackPerks(self, attack_id):
        return self.session.query(AttackPerk).filter(AttackPerk.attack_id==attack_id)

    def getPerkDetails(self, perk_id):
        return self.session.query(Perk).filter(Perk.id==perk_id).first()

    def addGame(self, owner_id, name):
        game = Game(owner_id=owner_id, name=name)
        self.session.add(game)
        self.session.commit()
        return game
    
    def getGames(self):
        return self.session.query(Game)

    def getGameOwner(self, game_id):
        return self.session.query(Game).filter(Game.id == game_id).first().owner_id

    def getGameCharacters(self, game_id):
        chars = []
        for gc in self.session.query(GameCharacter).filter(GameCharacter.game_id == game_id):
            char = self.getCharacter(gc.character_id)
            if char != None:
                chars.append(char)
            else:
                print 'character no longer exists' 
        return chars
    
    def searchGameCharacters(self, name, user):
        chars = []
        for char in self.session.query(Character).filter(Character.name == name).filter(Character.user_id == user):
            if char != None:
                chars.append(char)
            else:
                print 'no char' 
        return chars

    def addCharacterToGame(self, game_id, character_id):
        if self.getCharacter(character_id) != None:
            gameChar = self.session.query(GameCharacter).filter(GameCharacter.game_id == game_id).\
                                  filter(GameCharacter.character_id == character_id).first()
            if gameChar == None:
                gameChar = GameCharacter(game_id = game_id, character_id = character_id)

                self.session.add(gameChar)
                self.session.commit()
                print 'added game char'
                return 'Character Added'
            else:
                print 'already in game'
                return 'Character Already in Game'
        else:
            print 'added character does not exist'
            return 'Character Does Not Exist'

    def removeCharacterFromGame(self, game_id, character_id):
        if self.getCharacter(character_id) != None:
            gameChar = self.session.query(GameCharacter).filter(GameCharacter.game_id == game_id).\
                                      filter(GameCharacter.character_id == character_id).first()
            if gameChar != None:
                self.session.delete(gameChar)
                self.session.commit()
                return 'Character Removed'
            else:
                return 'Character Was Not In Game'
        else:
            return 'Character Does Not Exist'
            

    def deleteGame(self, game_id):
        for gameChar in self.session.query(GameCharacter).filter(GameCharacter.game_id == game_id):
            self.session.delete(gameChar)

        game = self.session.query(Game).filter(Game.id == game_id).first()
        if game != None:
            self.session.delete(game)
            
        self.session.commit()

    # Print them to console for testing
    def printAbilities(self):
        print 'Abilities'
        for ab in self.session.query(Ability).order_by(Ability.name):
            print ab.__repr__()
            
    def printWeaknesses(self):
        print 'Weaknesses'
        for wk in self.session.query(Weakness).order_by(Weakness.name):
            print wk.__repr__()
            
    def printFlaws(self):
        print 'Flaws'
        for fl in self.session.query(Flaw).order_by(Flaw.name):
            print fl.__repr__()
            
    def printPerks(self):
        print 'Perks'
        for pk in self.session.query(Perk).order_by(Perk.name):
            print pk.__repr__()

    def printDummyCharacter(self):
        num = self.session.query(Character).filter(Character.user_id=='Sid').count()
        print "number of characters: " + str(num)
        char = self.session.query(Character).filter(Character.user_id=='Sid')[0]
        print char.name
        print char.health
        attacks = self.session.query(CharacterAttack).filter(CharacterAttack.character_id==char.id)
        print attacks[0].name

    def addDummyCharacter(self):
        character = Character(user_id='ova.app.test@gmail.com', name='Codex', combat_notes='', defense='2', health='40', endurance='60', tv='22', background='codex is a member of the knights of good', appearance='red hair', personality='strong willed', other_notes='she is a priestess')
        self.session.add(character)
        self.session.commit()
        attack1 = CharacterAttack(character_id=character.id, name='holy cross', roll='5', dx='6', end='0', note='does aoe damage')
        self.session.add(attack1)
        self.session.commit()
        perk1 = self.session.query(Perk).filter(Perk.name=='Ranged')[0]
        flaw1 = self.session.query(Flaw).filter(Flaw.name=='No Damage')[0]
        af1 = AttackFlaw(flaw_id=flaw1.id, attack_id=attack1.id, multiplier='1', note='')
        self.session.add(af1)
        self.session.commit()
        ap1 = AttackPerk(perk_id=perk1.id, attack_id=attack1.id, multiplier='1', note='')
        self.session.add(ap1)
        self.session.commit()
        ability1 = self.session.query(Ability).filter(Ability.name=='Agile')[0]
        weakness1 = self.session.query(Weakness).filter(Weakness.name=='Ageism')[0]
        ca1 = CharacterAbility(ability_id=ability1.id,
                               character_id=character.id,
                               ability_value='+3',
                               ability_note='')
        self.session.add(ca1)
        self.session.commit()
        cw1 = CharacterWeakness(weakness_id=weakness1.id,
                               character_id=character.id,
                               weakness_value='-3',
                               weakness_note='')
        self.session.add(cw1)
        self.session.commit()

    def addDummy(self):
        test_ability = Ability(name='test', description='this is a test ability')
        test_weakness = Weakness(name='test', description='this is a test weakness')
        test_flaw = Flaw(name='test', description='this is a test flaw', cost=-15, multiples='Y')
        test_perk = Perk(name='test', description='this is a test perk', cost=15, multiples='N')

        self.session.add(test_ability)
        self.session.add(test_weakness)
        self.session.add(test_flaw)
        self.session.add(test_perk)
        self.session.commit()

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
            
        self.session.commit()
        
        
        















