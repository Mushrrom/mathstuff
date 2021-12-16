import os
import math
import requests     
import time
import mathfunctions
#v 0.1[test]
#HOW DO YOU MAKE THIS RUN IN THE BACKGROUND AND NOT MAKE THE PROGRAM TAKE A LONG TIME TO START UP
"""i = input('Check for updates (may take a while) (y/n)')
if i == 'y':
    print('Checking for updates (this could take a bit)')
    try: 
        req = requests.get("https://raw.githubusercontent.com/Mushrrom/mathstuff/main/version.txt", timeout=10)
    except requests.exceptions.Timeout as err: 
        print('could not check for updates (could not connect)')
        req = '1\n'

    if not(req == '1\n'):
        print('There is an update available: (version: %s)' %req)"""
#What are you doing here?
#testofmathstuff.py
os.system("title " + "Math stuff By me")
num = 0
i = 1
print('\n')
print("Some math stuff so that I can save time because I'm lazy :) (it's currently a buggy mess)")
print('Code available at https://github.com/Mushrrom/mathstuff')
print('Releases available at https://github.com/Mushrrom/mathstuff/releases (check here to manualy check for updates)')
print('type h for help')
print("\n")

#all the function stnuff so that the actual thing doesnt grt really cluttered up :) 

Pathforthestuff = '%s/mushrrom/mathstuff' % os.environ['appdata']
if not os.path.exists(Pathforthestuff):
    print('If this is your first time using the program type h or help for help\n')
    os.makedirs(Pathforthestuff)
    with open('%s/mushrrom/mathstuff/test.txt' %os.environ['appdata'], 'w') as file: #CHANGE THIS TO MUSHRROM FOLDER
        data = ['1\n', '1\n', 'false\n']
        file.writelines(data)




 
going = True
while going == True:
    commandinput = input(": ") 
    #Calculates factors
    if commandinput.startswith("h") or commandinput.startswith("help"):
        commandinput = commandinput.replace("help", "")
        commandinput = commandinput.replace("h", "")
        print(commandinput)
        helpstuff = commandinput.replace(" ", "")
        mathfunctions.help(helpstuff)
    elif commandinput.startswith("f ") or commandinput.startswith("factor "):
        commandinput = commandinput.replace("f ", "")
        num = int(commandinput.replace("factor ", ""))
        factors = mathfunctions.calcfactors(commandinput)
        print('\n')
        print(factors[0])
        print(factors[1])

    elif commandinput.startswith("lcm"):
        commandinput = commandinput.replace("lcm ", "")
        commandinput = commandinput.replace("lcm ", "")    
        mathfunctions.calclcm(commandinput)
    elif commandinput.startswith("exit"):
        going = False
    elif commandinput.startswith('settings'):
        commandinput = commandinput.replace('settings', '')
        commandinput = commandinput.replace(' ', '')
        mathfunctions.dosettings(commandinput)
    elif commandinput.startswith('surd'):
        commandinput = commandinput.replace('surd', '')
        commandinput = commandinput.replace(' ', '')
        print(mathfunctions.surd(commandinput))
    else:
        print("Unknown command: %s" %commandinput)