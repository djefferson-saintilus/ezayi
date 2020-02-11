#coding:utf8

print("Hello World")
filecreated=open ('h.txt',mode='a')
filenewline=filecreated.write ("Bonjour les gars")
fileopen=open ('h.txt',mode='r')
filereadlines=fileopen.readlines()
if(filereadlines[1].find("cookie")==True):
    print ("Un cookie Est présent")
else :
    print ("Pas de cookie présent")
