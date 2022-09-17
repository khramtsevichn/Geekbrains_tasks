"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("test_file.txt", "r", encoding='utf-8') as test_file:
    lines = test_file.readlines()
print('Количество строк в файле:', len(lines))
i = 0
str1 = ""
for line in lines:
    i += 1
    words_in_line = len(line.split())
    str1 = f"В строке номер {str(i)} {str(words_in_line)} слов"
    print(str1)
