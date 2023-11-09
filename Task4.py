import json
with open('Firms.txt',encoding='utf-8') as FirmsFile:
    Lines=FirmsFile.readlines()
    FinalList=list()
    ProfitDict=dict()
    MinusDict=dict()
    AverageProfitDict=dict()
    for line in Lines:
        el=line.split()
        if int(el[2])-int(el[3])>0:
            ProfitDict[el[0]]=int(el[2])-int(el[3])
        else:
            MinusDict[el[0]] = int(el[2]) - int(el[3])
    AverageProfitDict["AverageProfit"]=sum(ProfitDict.values())/len(ProfitDict)
FinalList.append(ProfitDict)
FinalList.append(MinusDict)
FinalList.append(AverageProfitDict)
print("Конечный лист")
print(FinalList)
with open('Firms.json','w',encoding='utf-8') as JsonFile:
    json.dump(FinalList,JsonFile,indent=3,ensure_ascii=False)