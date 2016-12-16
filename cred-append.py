#!/usr/bin/python
# cred-append.py
# Version: 1.0
# License: Apache License Version 2.0
# Author: Georgii Starostin
# E-mail# blackdiverx@gmail.com
# Site: http://BlackDiver.net

import sys
if len (sys.argv) != 6:
	print ("Утилита для добавления текста в начало или конец строки.")
	print ("Синтаксис:")
	print ("python cred-append.py <InFile> <append-text> <position> <format> <OutFile>")
	print ("<InFile> - входной файл;")
	print ("<append-text> - текст для добавления в конец строки;")
	print ("<position> - добавление в начало [start] или конец [end] строки;")
	print ("<format> - формат вывода[unix|win|mac]. Устаналивает формат перевода строки;")
	print ("<OutFile> - файл результатов.")
	print ("")
	print ("Пример:")
	print ("python cred-append.py Logins.txt a end unix Result.txt")
	exit();

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

f = open(sys.argv[5],'w')

if sys.argv[3] == 'end':
	i = 0
	while i<len(Farray):
		f.write((Farray[i]).rstrip('\r').rstrip('\n')+sys.argv[2]+formattype(sys.argv[4]))
		i=i+1
if sys.argv[3] == 'start':
	i = 0
	while i<len(Farray):
		f.write(sys.argv[2]+(Farray[i]).rstrip('\r').rstrip('\n')+formattype(sys.argv[4]))
		i=i+1
f.close()