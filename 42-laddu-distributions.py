laddus=5
friends=["Shankar","Ellamma","Thimmappa","Harika", "Charitha", "Deepak"]

for laddus_distribute in friends:
    if laddus>0:
        print(f"{laddus_distribute} gets a laddu")
        laddus-=1
    else:
        print(f"{laddus_distribute}!. No laddus left. Collect the laddus in next time visit")