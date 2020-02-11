#coding:utf8

print("Hello World")
##fichier  créé 
filecreated=open ('h.txt',mode='a')
filenewline=filecreated.write ("Bonjour les gars")
filecreated.close ()
## texte ajouté
fileopen=open ('h.txt',mode='r')
filereadlines=fileopen.readlines()
subs='cookie'
###

re=[i for i in filereadlines if subs in i ]
if (re==[]):
    print ("Aucun résultat trouvé")
else :
    print ("résultat trouvé ::> ",re)
fileopen.close()
