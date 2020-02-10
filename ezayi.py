#coding:utf8
#-------
# Kal
#------
#importation locale
#var vibration et message
import os,sys,time,androidhelper
dro=androidhelper.Android()
#import sendmail
#message delivrer a screen
#err=dro.makeToast("SUCCESS")
#
#vibration tel
#vri=dro.vibrate(duration='100')
#
#captiver picture
#cap=dro.cameraCapturePicture('/sdcard/spy.jpg')

###code main ####
#
def calcul():
    files=0
    if(files == 0):
        try:
            with open("ip.txt",mode='a') as f :
                print ("file created sucess")
        except:
            print("")
        print("")
        inc=files + 1
        if(inc==1):
            #insertion de data in files
            os.system("ifconfig > ip.txt")
            try:
                with open('ip.txt',mode='r') as f:
                    print(f.read())
            except:
                
        else:
            print("file not created")
calcul()
