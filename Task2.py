with open('Cinema.txt', 'r', encoding='utf-8') as CinemaFile:
    AllFilms = CinemaFile.readlines()
    Finaldict = dict()
    for film in AllFilms:
        result = list()
        for Name in film.split():
            if any(el.isdigit() for el in Name):
                break
            result.append(Name)
        result_string = ' '.join(result)
        listInf = list()
        for el in film.split():
            if any(a.isdigit() for a in el):
                listInf.append(el)
        Finaldict[result_string] = listInf

print(Finaldict)

print("Фильмы, где цена меньше 15 рублей")
result = True
for key, value in Finaldict.items():
    if int(value[1]) < 15:
        result = False
        print(f"{key} {value[0]} {value[1]} {value[2]}")
if result:
    print("Таких фильмов нет")