import os
import time
clear = lambda: os.system('cls')



f = "0"
a = 0



while a < 10:
    clear()
    print("╭╮╭╮╭╮╱╱╱╱╱╱╭━━━┳━━━┳━━━╮")
    print("┃┃┃┃┃┃╱╱╱╱╱╱╰╮╭╮┃╭━╮┃╭━╮┃")
    print("┃┃┃┃┃┣━━┳╮╱╭╮┃┃┃┃┃╱┃┃╰━━╮")
    print("┃╰╯╰╯┃╭╮┃┃╱┃┃┃┃┃┃┃╱┃┣━━╮┃")
    print("╰╮╭╮╭┫╭╮┃╰━╯┣╯╰╯┃╰━╯┃╰━╯┃")
    print("╱╰╯╰╯╰╯╰┻━╮╭┻━━━┻━━━┻━━━╯")
    print("╱╱╱╱╱╱╱╱╭━╯┃             ")
    print("╱╱╱╱╱╱╱╱╰━━╯             ")
    print("WayDOS")
    time.sleep(0.5)
    clear()
    print("╭╮╭╮╭╮╱╱╱╱╱╱╭━━━┳━━━┳━━━╮")
    print("┃┃┃┃┃┃╱╱╱╱╱╱╰╮╭╮┃╭━╮┃╭━╮┃")
    print("┃┃┃┃┃┣━━┳╮╱╭╮┃┃┃┃┃╱┃┃╰━━╮")
    print("┃╰╯╰╯┃╭╮┃┃╱┃┃┃┃┃┃┃╱┃┣━━╮┃")
    print("╰╮╭╮╭┫╭╮┃╰━╯┣╯╰╯┃╰━╯┃╰━╯┃")
    print("╱╰╯╰╯╰╯╰┻━╮╭┻━━━┻━━━┻━━━╯")
    print("╱╱╱╱╱╱╱╱╭━╯┃             ")
    print("╱╱╱╱╱╱╱╱╰━━╯             ")
    print("WayDOS.")
    time.sleep(0.5)
    clear()
    print("╭╮╭╮╭╮╱╱╱╱╱╱╭━━━┳━━━┳━━━╮")
    print("┃┃┃┃┃┃╱╱╱╱╱╱╰╮╭╮┃╭━╮┃╭━╮┃")
    print("┃┃┃┃┃┣━━┳╮╱╭╮┃┃┃┃┃╱┃┃╰━━╮")
    print("┃╰╯╰╯┃╭╮┃┃╱┃┃┃┃┃┃┃╱┃┣━━╮┃")
    print("╰╮╭╮╭┫╭╮┃╰━╯┣╯╰╯┃╰━╯┃╰━╯┃")
    print("╱╰╯╰╯╰╯╰┻━╮╭┻━━━┻━━━┻━━━╯")
    print("╱╱╱╱╱╱╱╱╭━╯┃             ")
    print("╱╱╱╱╱╱╱╱╰━━╯             ")
    print("WayDOS..")
    time.sleep(0.5)
    clear()
    print("╭╮╭╮╭╮╱╱╱╱╱╱╭━━━┳━━━┳━━━╮")
    print("┃┃┃┃┃┃╱╱╱╱╱╱╰╮╭╮┃╭━╮┃╭━╮┃")
    print("┃┃┃┃┃┣━━┳╮╱╭╮┃┃┃┃┃╱┃┃╰━━╮")
    print("┃╰╯╰╯┃╭╮┃┃╱┃┃┃┃┃┃┃╱┃┣━━╮┃")
    print("╰╮╭╮╭┫╭╮┃╰━╯┣╯╰╯┃╰━╯┃╰━╯┃")
    print("╱╰╯╰╯╰╯╰┻━╮╭┻━━━┻━━━┻━━━╯")
    print("╱╱╱╱╱╱╱╱╭━╯┃             ")
    print("╱╱╱╱╱╱╱╱╰━━╯             ")
    print("WayDOS...")
    time.sleep(0.5)
    

    a = a+1
a = 0
time.sleep(3.5)

if os.path.isdir("bin"):
    while True:
        d = input(os.getcwd())

        if d == ".cls":
            clear()
        
        if d == ".printtext":
            txt = input("Enter text: ")
            print(txt)
        
        if d == ".dir":
            print(os.listdir())

        #if(d == ".cd", f := input()):
            #os.chdir(f)


while a < 10:
    print("Copying files")
    time.sleep(0.5)
    clear()
    print("Copying files.")
    time.sleep(0.5)
    clear()
    print("Copying files..")
    time.sleep(0.5)
    clear()
    print("Copying files...")
    time.sleep(0.5)
    clear()
    a = a+1
a = 0

time.sleep(4)

while a < 100:
    print("/> Creating Folder 'BIN' ")
    time.sleep(0.1)
    print("/> Creating Folder 'ETC' ")
    time.sleep(0.9)
    print("/> Creating Folder 'SBIN' ")
    time.sleep(0.5)
    print("/> Creating Folder 'USR' ")
    time.sleep(0.1)
    print("/> Creating Folder 'VAR' ")
    time.sleep(0.08)
    print("/bin/> Creating File 'CAT' ")
    time.sleep(0.008)
    print("/bin/> Creating File 'CHGRP' ")
    time.sleep(0.008)
    print("/bin/> Creating File 'CHMOD' ")
    time.sleep(0.008)
    print("/bin/> Creating File 'CHOWN' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'CP' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'DATA' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'DD' ")
    time.sleep(0.9)
    print("/bin/> Creating File 'DF' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'DMESG' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'ECHO' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'FALSE' ")
    time.sleep(0.9)
    print("/bin/> Creating File 'HOSTNAME' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'KILL' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'LN' ")
    time.sleep(0.5)
    print("/bin/> Creating File 'LOGIN' ")
    time.sleep(0.1)
    print("/bin/> Creating File 'LS' ")

    if not os.path.isdir("bin"):
        os.mkdir("bin")

    if not os.path.isdir("root"):
        os.mkdir("root")
    print("根据古老的传统，在Taxila的亚历山大大帝的印度战役期间，马其顿人会见了印度先贤-体操运动员。 亚历山大派他的宫廷哲学家Onesicritus去了解他们生活和教义的特殊性。 在斯特拉博的叙述中，卡兰向亚历山大的大使指出了西方人的奢侈和饱足感，之后他建议脱衣服并开始哲学辩论。 亚历山大希望其中一位印度先贤加入他的随从。 该地区的统治者Taxil承认马其顿人的宗主权，说服卡兰加入亚历山大的军队。几年后，当卡兰病倒时，他决定自杀并自焚。 根据古代历史学家的说法，他决定去世，以免因体弱和疾病而等待死亡。 宏伟的自焚仪式引起了人们的注意，并被马其顿人记住，这反映在许多古代资料中。")

    if not os.path.isdir("etc"):
        os.mkdir("etc")
    
    time.sleep(0.1)
    a = a+1
a = 0

clear()

time.sleep(4)



