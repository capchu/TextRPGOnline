from dataAccess import DataAccess
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
    DA = DataAccess()
    attacks = []
    a1perks = []
    a1perks.append(ClientPerk('1', DA.getPerkDetails(1).name, '1',''))
    a1perks.append(ClientPerk('16', DA.getPerkDetails(16).name,'1',''))
    a1flaws = []
    a1flaws.append(ClientFlaw('2', DA.getFlawDetails(2).name, '1',''))
    a1flaws.append(ClientFlaw('14', DA.getPerkDetails(14).name, '1',''))
    attacks.append(ClientAttack('Fan of Blades', a1perks, a1flaws, '5', '4',
                            '0', 'throws 6 blades infront of him in a cone'))
    a2perks = []
    a2perks.append(ClientPerk('3', DA.getPerkDetails(3).name, '1',''))
    a2perks.append(ClientPerk('5', DA.getPerkDetails(5).name, '1',''))
    a2flaws = []
    a2flaws.append(ClientFlaw('5', DA.getFlawDetails(5).name, '1',''))
    a2flaws.append(ClientFlaw('8', DA.getFlawDetails(8).name, '1',''))
    attacks.append(ClientAttack('Backstab', a2perks, a2flaws, '7', '2',
                            '15', 'does double damage if unseen by target'))
    abilities = []
    abilities.append(ClientAbility('7', DA.getAbilityDetails(7).name, '+3', ''))
    abilities.append(ClientAbility('13', DA.getAbilityDetails(13).name, '+1', ''))
    abilities.append(ClientAbility('32', DA.getAbilityDetails(32).name, '+5', ''))
    weaknesses = []
    weaknesses.append(ClientWeakness('2', DA.getWeaknessDetails(2).name, '-3',''))
    weaknesses.append(ClientWeakness('14', DA.getWeaknessDetails(14).name,'-1',''))
    weaknesses.append(ClientWeakness('28', DA.getWeaknessDetails(28).name,'-5','(Eye Sight)'))

    Leon = ClientCharacter('Sid', 'Leon2', '', abilities,
                 weaknesses, attacks, '4', '35', '70',
                 '25', 'Born on the Streets', 'Cloaked', 'Sullen',
                 '', '', '')

    CDA.addClientCharacter(Leon)

def printClientCharacter(char):
    print str(char.id) + ":" + char.name
    print " abilities:"
    for ab in char.abilities:
        print " " + ab.toString()
    print " weaknesses:"
    for wk in char.weaknesses:
        print " " + wk.toString()
    print " attacks:"
    for atk in char.attacks:
        print " " + atk.name
        pkfl = ''
        for pk in atk.perks:
            pkfl += " " + pk.toString()
        for fl in atk.flaws:
            pkfl += " " + fl.toString()
        print "  " + pkfl
        print "  " + atk.note
        print "  roll:" + atk.roll
        print "  dx:" + atk.dx
        print "  cost:" + atk.end
    print " def:" + char.defense
    print " hp:" + char.health
    print " end:" + char.endurance
    print " tv:" + char.tv
    




DA = DataAccess()
#DA.addBaseData()

#DA.addDummyCharacter()
#DA.printDummyCharacter()

    

#DA.printAbilities()
#DA.printWeaknesses()
#DA.printFlaws()
#DA.printPerks()
#addDummyClientCharacter()


for char in DA.getCharacters('Sid'):
    cchar = CDA.getClientCharacter(char.id)
    printClientCharacter(cchar)






    
