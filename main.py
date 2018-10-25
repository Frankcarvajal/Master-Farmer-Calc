#Master farmer pickpocket calc
##Choose the amount of thieving xp
gain_xp = 250000
##################################
xp = 43
pps = gain_xp/xp
print("number of pickpockets",pps)
pps = 2*pps #rouge outfit
seeds = dict()

seeds["limp"] = pps/86.3
seeds["harralander"] = pps/206
seeds["ranarr"] = pps/302
seeds["toadflax"] = pps/443
seeds["irit"] = pps/651
seeds["avantoe"] = pps/947
seeds["kwuarm"] = pps/1389
seeds["snapdragon"] = pps/2083
seeds["cadantine"] = pps/2976
seeds["lantadyme"] = pps/4167

tot=0
for key, value in seeds.items():
    if key != "limp":
        tot += value
    print(f'{key} seeds: {value}')
#XP Gains and number of herbs
print("Total number of seeds", tot, "and farm runs",tot/4)
print(f"Minimum of {80/60*tot/4} hours of waiting, thats {80/60*tot/4/24} days")
n = 7
seeds["limp"] *=3
seeds["harralander"] *= n*(67.5+6.25)
seeds["ranarr"] *= n*(87.5+7.5)
seeds["toadflax"] *= n*(80+8)
seeds["irit"] *= n*(100+8.75)
seeds["avantoe"] *= n*(112.5+10)
seeds["kwuarm"] *= n*(125+11.25)
seeds["snapdragon"] *= n*(142.5+11.75)
seeds["cadantine"] *= n*(150+12.5)
seeds["lantadyme"] *= n*(157.5+13.125)

tot = 0
print("total limps:",seeds["limp"])
for key, value in seeds.items():
    if key != "limp":
        tot += value
        print(f"Herb xp from {key}: {value}")
print("Total herb xp:",tot, "of", 992895-750988)
print("minimum of", pps/2*1.2/3600, "hours")
