from dataAccess import DataAccess

DA = DataAccess()
#DA.addBaseData()
#DA.printAbilities()
#DA.printWeaknesses()
#DA.printFlaws()
#DA.printPerks()


for ab in DA.getAbilities():
    print str(ab.id) + ":" + ab.name

for wk in DA.getWeaknesses():
    print str(wk.id) + ":" + wk.name

for pk in DA.getPerks():
    print str(pk.id) + ":" + pk.name

for fl in DA.getFlaws():
    print str(fl.id) + ":" + fl.name
