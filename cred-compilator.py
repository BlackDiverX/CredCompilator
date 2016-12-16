#!/usr/bin/python
# cred-compilator.py
# Version: 1.0
# License: Apache License Version 2.0
# Author: Georgii Starostin
# E-mail# blackdiverx@gmail.com
# Site: http://BlackDiver.net

import sys
if len (sys.argv) != 6:
	print ("Утилита для создания всех комбинация слов из двух словарей.")
	print ("Синтаксис:")
	print ("python cred-compilator.py <InFile1> <InFile2> <break> <format> <OutFile>")
	print ("<InFile1> - входной файл 1;")
	print ("<InFile2> - входной файл 2;")
	print ("<break> - разделитель между словами. Чтобы создать список без разделителя, нужно вместо разделителя поставить '';")
	print ("<format> - формат вывода[unix|win|mac]. Устаналивает формат перевода строки;")
	print ("<OutFile> - файл результатов.")
	print ("")
	print ("Пример:")
	print ("python cred-compilator.py Name.txt Family.txt . unix Result.txt")
	print ("Результат:")
	print ("Список вида: имя.фамилия")
	exit()

def formattype(x):
	return{
		"unix":"\n",
		"win":"\r\n",
		"mac":"\r"
		}.get(x)

with open(sys.argv[1] , "r",encoding='utf-8', errors='ignore') as ins:
    Farray = []
    for line in ins:
        Farray.append((line))

with open(sys.argv[2] , "r",encoding='utf-8', errors='ignore') as ins:
    Narray = []
    for line in ins:
        Narray.append(line)



f = open(sys.argv[5],'w')
i = 0
while i<len(Farray):
	n = 0
	while n<len(Narray):
		f.write((Farray[i]).rstrip('\r').rstrip('\n')+sys.argv[3]+ Narray[n].rstrip('\r').rstrip('\n')+formattype(sys.argv[4]))
		n=n+1
	i=i+1
f.close()
