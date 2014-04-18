from dataAccess import DataAccess
from databaseCreation import Character
from clientCharacter import ClientCharacter
from clientCharacter import ClientAttack
from clientCharacter import ClientWeakness
from clientCharacter import ClientAbility
from clientCharacter import ClientPerk
from clientCharacter import ClientFlaw
from clientCharacter import ClientDataAccess

CDA = ClientDataAccess()

def printAbilityNames():
    print 'Abilities'
    for ab in DA.getAbilities():
        print str(ab.id) + ":" + ab.name

def printWeaknessNames():
    print 'Weaknesses'
    for wk in DA.getWeaknesses():
        print str(wk.id) + ":" + wk.name

def printPerkNames():
    print 'Perks'
    for pk in DA.getPerks():
        print str(pk.id) + ":" + pk.name

def printFlawNames():
    print 'Flaws'
    for fl in DA.getFlaws():
        print str(fl.id) + ":" + fl.name

def addDummyClientCharacter():
    attacks = []
    a1perks = []
    a1perks.append(ClientPerk('1','1',''))
    a1perks.append(ClientPerk('16','1',''))
    a1flaws = []
    a1flaws.append(ClientFlaw('2','1',''))
    a1flaws.append(ClientFlaw('14','1',''))
    attacks.append(ClientAttack('Fan of Blades', a1perks, a1flaws, '5', '4',
                            '0', 'throws 6 blades infront of him in a cone'))
    a2perks = []
    a2perks.append(ClientPerk('3','1',''))
    a2perks.append(ClientPerk('5','1',''))
    a2flaws = []
    a2flaws.append(ClientFlaw('5','1',''))
    a2flaws.append(ClientFlaw('8','1',''))
    attacks.append(ClientAttack('Backstab', a2perks, a2flaws, '7', '2',
                            '15', 'does double damage if unseen by target'))
    abilities = []
    abilities.append(ClientAbility('3', '+3', ''))
    abilities.append(ClientAbility('13', '+1', ''))
    abilities.append(ClientAbility('32', '+5', ''))
    weaknesses = []
    weaknesses.append(ClientWeakness('2','-3',''))
    weaknesses.append(ClientWeakness('14','-1',''))
    weaknesses.append(ClientWeakness('28','-5','(Eye Sight)'))

    Leon = ClientCharacter('Sid', 'Leon', '', abilities,
                 weaknesses, attacks, '4', '35', '70',
                 '25', 'Born on the Streets', 'Cloaked', 'Sullen',
                 '', '', '')

    CDA.addClientCharacter(Leon)




DA = DataAccess()
#DA.addBaseData()

#DA.addDummyCharacter()
#DA.printDummyCharacter()

    

#DA.printAbilities()
#DA.printWeaknesses()
#DA.printFlaws()
#DA.printPerks()
addDummyClientCharacter()


for char in DA.getCharacters('Sid'):
    print char.name
    

