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
from dataAccess import DataAccess

class ClientCharacter():
    def __init__(self, user_id, name, combat_notes, ability_list, weakness_list, attack_list,
                 defense, health, endurance, tv, background, appearance, personality,
                 other_notes, portrait_url, icon_url):
        self.id = ''
        self.user_id = user_id
        self.name = name
        self.combat_notes = combat_notes
        self.ability_list = ability_list
        self.weakness_list = weakness_list
        self.attack_list = attack_list
        self.defense = defense
        self.health = health
        self.endurance = endurance
        self.tv = tv
        self.background = background
        self.appearance = appearance
        self.personality = personality
        self.other_notes = other_notes
        self.portrait_url = portrait_url
        self.icon_url = icon_url

class ClientAbility():
    def __init__(self, ability_id, ability_value, ability_note):
        self.ability_id = ability_id
        self.ability_value = ability_value
        self.ability_note = ability_note

    def toString(self):
        DA = DataAccess()
        return self.ability_value + " " + DA.getAbilityDetails(self.ability_id).name + " " + self.ability_note

class ClientWeakness():
    def __init__(self, weakness_id, weakness_value, weakness_note):
        self.weakness_id = weakness_id
        self.weakness_value = weakness_value
        self.weakness_note = weakness_note

    def toString(self):
        DA = DataAccess()
        return self.weakness_value + " " + DA.getWeaknessDetails(self.weakness_id).name + " " + self.weakness_note
       

class ClientAttack():
    def __init__(self, name, perks, flaws, roll, dx, end, note):
        self.name = name
        self.perks = perks
        self.flaws = flaws
        self.roll = roll
        self.dx = dx
        self.end = end
        self.note = note

class ClientFlaw():
    def __init__(self, flaw_id, multiplier, note):
        self.flaw_id = flaw_id
        self.multiplier = multiplier
        self.note = note

    def toString(self):
        DA = DataAccess()
        return DA.getFlawDetails(self.flaw_id).name + " " + self.multiplier + " " + self.note
      

class ClientPerk():
    def __init__(self, perk_id, multiplier, note):
        self.perk_id = perk_id
        self.multiplier = multiplier
        self.note = note

    def toString(self):
        DA = DataAccess()
        return DA.getPerkDetails(self.perk_id).name + " " + self.multiplier + " " + self.note

class ClientDataAccess():

    def addClientCharacter(self, cchar):
        DA = DataAccess()
        session = DA.getSession()
        character = Character(user_id=cchar.user_id, name=cchar.name,
                        combat_notes=cchar.combat_notes, defense=cchar.defense,
                        health=cchar.health, endurance=cchar.endurance,
                        tv=cchar.tv, background=cchar.background,
                        appearance=cchar.appearance, personality=cchar.personality,
                        other_notes=cchar.other_notes)
        session.add(character)
        session.commit()
        cchar.id = character.id
        for at in cchar.attack_list:
            attack = CharacterAttack(character_id=character.id, name=at.name,
                                roll=at.roll, dx=at.dx, end=at.end, note=at.note)
            session.add(attack)
            session.commit()
            for pk in at.perks:
                aperk = AttackPerk(perk_id=pk.perk_id, attack_id=attack.id,
                                   multiplier=pk.multiplier, note=pk.note)
                session.add(aperk)
                session.commit()
            for fl in at.flaws:
                aflaw = AttackFlaw(flaw_id=fl.flaw_id, attack_id=attack.id,
                                   multiplier=fl.multiplier, note=fl.note)
                session.add(aflaw)
                session.commit()

        for ab in cchar.ability_list:
            cability = CharacterAbility(ability_id=ab.ability_id,
                               character_id=character.id,
                               ability_value=ab.ability_value,
                               ability_note=ab.ability_note)
            session.add(cability)
            session.commit()

        for wk in cchar.weakness_list:
            cweakness = CharacterWeakness(weakness_id=wk.weakness_id,
                               character_id=character.id,
                               weakness_value=wk.weakness_value,
                               weakness_note=wk.weakness_note)
            session.add(cweakness)
            session.commit()
        session.commit()

        print cchar.id
        
    def getClientCharacter(self, char_id):
        DA = DataAccess()
        char = DA.getCharacter(char_id)
        ability_list = []
        for ab in DA.getCharAbilities(char.id):
            ability_list.append(ClientAbility(ab.ability_id, ab.ability_value, ab.ability_note))

        weakness_list = []
        for wk in DA.getCharWeaknesses(char.id):
            weakness_list.append(ClientWeakness(wk.weakness_id, wk.weakness_value, wk.weakness_note))

        attack_list = []
        for at in DA.getCharAttacks(char.id):
            perks = []
            for pk in DA.getAttackPerks(at.id):
                perks.append(ClientPerk(pk.perk_id, pk.multiplier, pk.note))
            flaws = []
            for fl in DA.getAttackFlaws(at.id):
                flaws.append(ClientFlaw(fl.flaw_id, fl.multiplier, fl.note))
            attack_list.append(ClientAttack(at.name, perks, flaws, at.roll,
                                            at.dx, at.end, at.note))

        cchar = ClientCharacter(char.user_id, char.name, char.combat_notes,
                            ability_list, weakness_list, attack_list,
                            char.defense, char.health, char.endurance, char.tv,
                            char.background, char.appearance, char.personality,
                            char.other_notes, char.portrait_url, char.icon_url)
        cchar.id = char_id
        return cchar        













        
    
    
        
        
