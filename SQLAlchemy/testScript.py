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

def addDummyClientCharacter2():
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

    Leon = ClientCharacter('ova.app.test@gmail.com', 'Leon', '', abilities,
                 weaknesses, attacks, '4', '35', '70',
                 '25', 'Born on the Streets', 'Cloaked', 'Sullen',
                 '', '', '')

    CDA.addClientCharacter(Leon)

def addDummyClientCharacter3():
    DA = DataAccess()
    attacks = []
    a1perks = []
    a1perks.append(ClientPerk('15', DA.getPerkDetails(15).name, '1',''))
    a1perks.append(ClientPerk('10', DA.getPerkDetails(10).name,'1',''))
    a1flaws = []
    a1flaws.append(ClientFlaw('12', DA.getFlawDetails(12).name, '1',''))
    a1flaws.append(ClientFlaw('11', DA.getPerkDetails(11).name, '1',''))
    attacks.append(ClientAttack('Bomba', a1perks, a1flaws, '7', '7',
                            '15', 'Oh Yeah'))
    a2perks = []
    a2perks.append(ClientPerk('6', DA.getPerkDetails(6).name, '1',''))
    a2perks.append(ClientPerk('1', DA.getPerkDetails(1).name, '1',''))
    a2flaws = []
    a2flaws.append(ClientFlaw('1', DA.getFlawDetails(1).name, '1',''))
    a2flaws.append(ClientFlaw('4', DA.getFlawDetails(4).name, '1',''))
    attacks.append(ClientAttack('StarScream', a2perks, a2flaws, '7', '2',
                            '15', 'does double damage if unseen by target'))
    abilities = []
    abilities.append(ClientAbility('17', DA.getAbilityDetails(17).name, '+3', ''))
    abilities.append(ClientAbility('1', DA.getAbilityDetails(1).name, '+1', ''))
    abilities.append(ClientAbility('30', DA.getAbilityDetails(30).name, '+5', ''))
    weaknesses = []
    weaknesses.append(ClientWeakness('21', DA.getWeaknessDetails(21).name, '-3',''))
    weaknesses.append(ClientWeakness('24', DA.getWeaknessDetails(24).name,'-1',''))
    weaknesses.append(ClientWeakness('20', DA.getWeaknessDetails(20).name,'-5','(Eye Sight)'))

    Leon = ClientCharacter('ova.app.test@gmail.com', 'Amy', '', abilities,
                 weaknesses, attacks, '5', '40', '50',
                 '22', 'Born on in the USA', 'Dress', 'Exited',
                 '', '', '')

    CDA.addClientCharacter(Leon)

def addDummyClientCharacter4():
    DA = DataAccess()
    attacks = []
    a1perks = []
    a1perks.append(ClientPerk('11', DA.getPerkDetails(11).name, '1',''))
    a1perks.append(ClientPerk('10', DA.getPerkDetails(10).name,'1',''))
    a1flaws = []
    a1flaws.append(ClientFlaw('5', DA.getFlawDetails(5).name, '1',''))
    a1flaws.append(ClientFlaw('1', DA.getPerkDetails(1).name, '1',''))
    attacks.append(ClientAttack('Fan of Codex', a1perks, a1flaws, '5', '4',
                            '0', 'Says Hi to Codex'))
    a2perks = []
    a2perks.append(ClientPerk('1', DA.getPerkDetails(1).name, '1',''))
    a2perks.append(ClientPerk('3', DA.getPerkDetails(3).name, '1',''))
    a2flaws = []
    a2flaws.append(ClientFlaw('15', DA.getFlawDetails(15).name, '1',''))
    a2flaws.append(ClientFlaw('3', DA.getFlawDetails(3).name, '1',''))
    attacks.append(ClientAttack('Backstab', a2perks, a2flaws, '7', '2',
                            '15', 'does double damage if unseen by target'))
    abilities = []
    abilities.append(ClientAbility('17', DA.getAbilityDetails(17).name, '+3', ''))
    abilities.append(ClientAbility('3', DA.getAbilityDetails(3).name, '+1', ''))
    abilities.append(ClientAbility('2', DA.getAbilityDetails(2).name, '+5', ''))
    weaknesses = []
    weaknesses.append(ClientWeakness('21', DA.getWeaknessDetails(21).name, '-3',''))
    weaknesses.append(ClientWeakness('1', DA.getWeaknessDetails(1).name,'-1',''))
    weaknesses.append(ClientWeakness('2', DA.getWeaknessDetails(2).name,'-5','(Eye Sight)'))

    Leon = ClientCharacter('ova.app.test@gmail.com', 'Jacob', '', abilities,
                 weaknesses, attacks, '9', '10', '10',
                 '1', 'Smells Funny', 'Looks Funny', 'Funny',
                 '', '', '')

    CDA.addClientCharacter(Leon)

def updateDummyClientCharacter4(char_id):
    DA = DataAccess()
    attacks = []
    a1perks = []
    a1perks.append(ClientPerk('1', DA.getPerkDetails(11).name, '1',''))
    a1perks.append(ClientPerk('2', DA.getPerkDetails(10).name,'1',''))
    a1flaws = []
    a1flaws.append(ClientFlaw('1', DA.getFlawDetails(5).name, '1',''))
    a1flaws.append(ClientFlaw('2', DA.getPerkDetails(1).name, '1',''))
    attacks.append(ClientAttack('Sleep', a1perks, a1flaws, '5', '4',
                            '0', 'Take A Nap'))
    a2perks = []
    a2perks.append(ClientPerk('4', DA.getPerkDetails(1).name, '1',''))
    a2perks.append(ClientPerk('3', DA.getPerkDetails(3).name, '1',''))
    a2flaws = []
    a2flaws.append(ClientFlaw('4', DA.getFlawDetails(15).name, '1',''))
    a2flaws.append(ClientFlaw('3', DA.getFlawDetails(3).name, '1',''))
    attacks.append(ClientAttack('Backstab', a2perks, a2flaws, '7', '2',
                            '15', 'does double damage if unseen by target'))
    abilities = []
    abilities.append(ClientAbility('1', DA.getAbilityDetails(17).name, '+1', ''))
    abilities.append(ClientAbility('2', DA.getAbilityDetails(3).name, '+1', ''))
    abilities.append(ClientAbility('3', DA.getAbilityDetails(2).name, '+1', ''))
    weaknesses = []
    weaknesses.append(ClientWeakness('1', DA.getWeaknessDetails(21).name, '-5',''))
    weaknesses.append(ClientWeakness('2', DA.getWeaknessDetails(1).name,'-5',''))
    weaknesses.append(ClientWeakness('3', DA.getWeaknessDetails(2).name,'-5',''))

    Leon = ClientCharacter('ova.app.test@gmail.com', 'Jacobugath', '', abilities,
                 weaknesses, attacks, '1', '10', '10',
                 '1', 'Mighty Warrior', 'Looks Like Godzilla', 'Sleepy',
                 '', '', '')

    CDA.updateClientCharacter(Leon, char_id)

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
#addDummyClientCharacter2()
#addDummyClientCharacter3()
#addDummyClientCharacter4()

for char in DA.getCharacters('ova.app.test@gmail.com'):
    cchar = CDA.getClientCharacter(char.id)
    printClientCharacter(cchar)

print 'Game Stuff'
#DA.addGame('ova.app.test@gmail.com', 'workingGame')
DA.addCharacterToGame(6, 3)
DA.addCharacterToGame(6, 2)
DA.addCharacterToGame(6, 1)

DA.deleteGame(1)

for game in DA.getGames():
    print str(game.id) + ":" + game.name + " " + game.owner_id
    for char in DA.getGameCharacters(game.id):
        print char.name
 
#updateDummyClientCharacter4(4)
#CDA.deleteClientCharacter(1)



    
