INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Activation", 
"Your Ability requires time to activate before each use. This could be due to cocking, reloading, aiming, recharging, or one of many other reasons. You must spend an entire round to activate your Ability, but you may still make Defense rolls to any incoming attacks. On your next turn (or any turn thereafter), you may use your Ability as normal. Once the Ability is used, time must be spent to activate it again.",
"(-10)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Ammunition", 
"Your Ability may only be activated a certain number of times before it becomes useless. This could represent bullets in a gun, charges in an electric baton, or a limited grant of power from a divine entity. This Flaw may be taken multiple times; if taken once, the Ability can be used around ten times. If taken twice, around five times. If taken three times, this Ability may only be used once. While the exact method of recharging this Ability is up to you, it is generally appropriate that it takes a full day, or at least extensive offtime. If the character can simply reload the Ability with little effort, consider another Flaw, like Activation, instead.",
"(-5)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Assisted", 
"This Ability requires an ally’s help to function. They might launch you in the air for a devestating dive-attack, or you might pool your energies together to power the Ability. In any case, those assisting you with this Ability lose their next action, but they may spend up to half of the Endurance cost of this Ability for you if they choose. This Perk may be taken multiple times; for each time it is taken, you need an additional helping hand. [Familiarity and capability are assumed here. Random strangers cannot assist you, nor could your little sibling launch you into the air. Use common sense in any situation.]",
"(-15)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Backlash", 
"Your Attack comes at the cost of your own well-being, and you may be injured through its use. This Flaw may be taken multiple times; for each time, you receive a quarter of the Damage you inflict with the Attack, rounded up.",
"(-5)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Break", 
"This Ability may only be used once you have exhausted either all of your Health or all of your Endurance. Perhaps you need to build up rage to unleash a fierce attack, or maybe you only feel empowered when the tide of battle has turned against you.",
"(-10)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Buildup", 
"You may not use your Ability right away but must wait for its power to build up. It may be an energy weapon that requires charging, a martial arts move you have to “limber up” for, or just a need to have dramatic timing. This Perk may be taken multiple times; for each time Buildup is taken, you must wait a complete turn before using the Ability. No action is necessary (or lost) to build up. Once the Ability has been used, the waiting period begins again.",
"(-5)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Cancel", 
"Your Ability does not work on a certain class of targets. If this is fairly rare, such as combatants made entirely of metal, you receive -5 to the Endurance cost. If it’s incredibly common, like humans, you can get up to -20. If the Cancel is something that is ridiculously uncommon, like hippopotamuses, you get no subtraction to Endurance.",
"(-0 to -20)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Concentration", 
"This Ability requires a round of your undivided attention to use. You must give up your action and all Defense rolls until your next turn. If injured or severely distracted, the Ability does not work and Endurance is expended anyway. Otherwise, on your next turn you may perform your Ability as normal. This Perk may be taken multiple times; each increasing the turns required to prepare.",
"(-20)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Delayed", 
"Regardless of your initiative, this Ability takes place last in the combat round. If the character using this Ability receives a complication or is otherwise compromised before the end of the turn, the Ability does not work, and Endurance is lost. Making Defense rolls, or even being hit, will not affect this Ability.",
"(-5)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Elaborate Gestures", 
"In order to use this Ability, your entire body must be free to perform some incantation, dance, or ritual. You cannot be holding items, pulling things, navigating terrain, or otherwise occupying any part of your body with another task.",
"(-5)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Feather Blow", 
"Your Attack is of such a nature that it cannot be used to inflict complications. There is no additional effect if the target loses half his or her total Health.",
"(-5)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Ineffective", 
"This Ability is not as effective as others of the same Level. This Flaw may be taken multiple times; for each time you take Ineffective, reduce your Damage Multiplier by 1 when using this Ability. If your Damage Multiplier would be reduced to zero, reduce it to 1/2 instead.",
"(-5)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Inaccurate", 
"Your Attack is particularly inaccurate. Maybe you have little control of it, or the Attack is simply imprecise by nature. Regardless of the cause, you receive a -1 Penalty to your Attack roll. This Flaw may be taken multiple times, increasing the Penalty by one each time it is applied.",
"(-5)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Low Penetration", 
"Your Attack is unusually susceptible to armor. For each time you take Low Penetration, treat your opponent’s Armored Ability as if it were two Levels higher, to a maximum of +5. If the opponent does not have the Armored Ability, there is no additional effect.",
"(-5)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("No Damage", 
"Your Attack is not much of an attack at all. Regardless of how good of a result you receive on your Attack roll, you can never inflict any Damage. However, any other Perks and Complications work as normal. You may not combine this with the Ineffective Flaw.",
"(-20)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Open to Attack", 
"After completing your Ability, you may not make any Defense rolls until your next turn. You may be exhaustively spent, have temporarily exposed a critical weak point, or otherwise thrown caution, and a proper defense, to the wind.",
"(-20)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Recoil", 
"This Ability packs enough of a punch to knock you off your feet. When used, you immediately receive the Stunned complication.",
"(-10)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Requirement", 
"Your Ability may only be used if a certain condition is met. If the requirement is easily accessible (Must be Outside), it is worth -5 Endurance, while an extremely rare and specific requirement (Must be the 12th day of the 4th month of the ancient Galbelzan calendar and a full blue moon) can be worth up to -20. Well, okay, perhaps not that precise, but you get the idea.",
"(-5 to -20)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Self-Only", 
"This Ability may only be used on yourself. It cannot be shared with others or otherwise targeted at other persons or objects. If an Ability is already only usable in this way, then this Flaw should not be taken.",
"(-5)", 
"N"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Unique Flaw", 
"If you do not see a Flaw here that reflects the one you want for your Ability, get together with your Game Master. Together, you can create a new Flaw with the appropriate Endurance cost.",
"(-?)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Unwieldy", 
"Your Ability is of a nature that makes you unsteady after its use. It may be an immense weapon, or perhaps you just become tipsy from exhaustion. This Flaw may be taken multiple times; for each time it is taken, you receive a -1 Penalty to all Defense rolls until your next turn.",
"(-5)", 
"Y"
);

INSERT INTO flaws (name, description, cost, multiples) 
VALUES ("Weapon", 
"This attack is actually a weapon, be it a blade, a gun, or something in between. Should you lose it, have it taken from you, or find yourself disarmed during a battle, you may no longer use this Attack. [With any Flaw, “doubling up” with a character’s Weaknesses is prohibited. If your Attack is already affected by the Limited Uses Weakness, you cannot also apply the Ammunition Flaw. This goes for Focus/Requirement, Gear/Weapon, and so on.]",
"(-5)", 
"N"
);



































