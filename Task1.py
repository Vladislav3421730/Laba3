with open('File1.txt','w') as file1:
    print("Введите данные для F1 файла. Введите пустую строку для завершения :")
    while True:
        NewStr = input()
        if not NewStr:
            break
        file1.write(NewStr+'\n')
with open('File1.txt', 'r') as file1, open('File2.txt', 'w') as file2:
    for line in file1:
        if line and line[0].isdigit():
            file2.write(line+'\n')
with open('File2.txt', 'r') as file2:
    first_line = file2.readline()
    Words = first_line.split()
    Amount = len(Words)
print(f"Количесвто в первой строке в файле File2.txt : {Amount}")