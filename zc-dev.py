#!/usr/bin/python
#-*-coding:utf-8-*-

import os

print """

\t+------------------------------------+
\t|                                    |
\t|            ZC-Dev v1.0             |
\t|                                    |
\t|     http://facebook.com/ZHLinux    |
\t|                                    |
\t+------------------------------------+
"""

print """

    1) Create C source file    5) Permissions
    2) Edit C source file      6) Move bin folder
    3) Compile C Source file   7) Excute Program
    4) Rename your program     8) Clean and close


"""
sel=raw_input(" ZC-Dev > ")

if sel=="ls":
	print "\n"
	os.system("ls -l")
        sel=raw_input("\n ZC-Dev > ")
if sel=="1":
	open("main.c","w")
	print("\n Main file created !\n")
	sel=raw_input(" ZC-Dev > ")

if sel=="2":
	os.system("nano main.c")
	sel=raw_input(" ZC-Dev > ")
if sel=="3":
	os.system("gcc -Wall -c main.c")
	os.system("gcc -Wall -o main main.o")
	sel=raw_input(" ZC-Dev > ")
if sel=="4":
	name=raw_input("\n New name : ")
	os.system("mv main "+name)
	sel=raw_input("\n ZC-Dev > ")
if sel=="5":
	name1=raw_input("\n Enter your program name : ")
	os.system("sudo chmod +x "+name1)
	sel=raw_input("\n ZC-Dev > ")
if sel=="6":
	name2=raw_input("\n Enter your program name : ")
	os.system("sudo mv "+name2+" /usr/bin/")
	sel=raw_input("\n ZC-Dev > ")
if sel=="7":
	name3=raw_input("\n Enter your program name : ")
	print("\n")
	os.system("\t"+name3)
	print "\n"
	sel=raw_input("\n ZC-Dev > ")

if sel=="8":
	os.system("sudo rm -r main.c main.o")
	exit()
