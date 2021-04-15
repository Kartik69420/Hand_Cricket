'''Author : Kartik Sharma
Code : Python
Game : Hand cricket (first game)
Date: 07-01-2021'''
#                    **************************
print("")
print("@  @     @      @ @ @@@@@ @ @  @\n@ @     @  @    @  @  @   @ @ @\n@@     @@@@@@   @@    @   @ @@\n@ @   @      @  @ @   @   @ @ @\n@  @ @        @ @  @  @   @ @  @")

def sound():
    from playsound import playsound
    playsound('C:\\Users\\Kartik\\Downloads\\Music\\Ipl.mp3')
sound()

print("Welcome to LOCAL Hand Cricket tournament, hosted by Kartik Sharma")
print("")

print("You are:\nBatting")
print("")
personRun = 1
f = 0
runList = []
while(personRun != f):
 personRun= int(input("Choose your run:\n"))

 if personRun < 7 and personRun > 0 :
    safe = True
 else: 
    safe = False

 import random

 def cricket():
    return random.randint(1 , 6)
        

 f = cricket()
 print("Computer runs " + str(f))

 if safe: 
    if personRun == f:
        print("You are out")
        boundary = False
    else:
        boundary = True
        print("You are safe")


    if boundary:
        if personRun == 4 or personRun == 6:
           print("Boundary")
           sound()
 else:
        print("Invalid run")


 if boundary:
    runList.append(personRun)
   
 else:
    pass
   
 if personRun == f :

    totalRuns = sum(runList)
    print(f'Total runs scored by you are { totalRuns }' )