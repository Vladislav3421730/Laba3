with open('Lessons.txt','r',encoding='utf-8') as LessonsFile:
    lines = LessonsFile.readlines()
    LessonDict = dict()
    for line in lines:
        InfList = list()
        for el in line.split():
            if any(a.isdigit() for a in el):
                InfList.append(el)
            else:
                LessonName = el
        LessonDict[LessonName] = InfList
print("Информация, которая содержиться в файле")
print(LessonDict)
HoursDict=dict()
for key,value in LessonDict.items():
    HoursList=list()
    for el in value:
        part=el.split('(')
        number=int(part[0])
        HoursList.append(number)
    HoursDict[key]=HoursList
print(HoursDict)
print("Название предмета и учёбные часы")
for key,value in HoursDict.items():
    print(f"{key} - {sum(value)}")

