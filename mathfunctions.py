import os
import math

def calclcm(nums):
    #print(nums)
    nums = nums.split()
    #print(nums)

    num1 = int(nums[0])
    num2 = int(nums[1])
    num1current = num1
    num2current = num2
    num1multipliedby = 1
    num2multipliedby = 1
    while num1current != num2current:
        if num1current < num2current:
            num1multipliedby += 1
            num1current = num1 * num1multipliedby
        elif num2current < num1current:
            num2multipliedby += 1
            num2current = num2 * num2multipliedby
    calculation = "%i x %i, %i x %i" %(num1, num1multipliedby, num2, num2multipliedby)
    print("The lowest common multiple of %i and %i is %i (%s)" %(num1, num2, num1current, calculation ))\

def calcfactors(calcnum):
    calcnum = int(calcnum)
    i = 1
    Allnums = "the factors of " + str(calcnum) + " are: "
    squarenums = "The square factors of " + str(calcnum) + " are: "
    percent = -1
    while i < calcnum:
        if float(calcnum/i).is_integer():
            Allnums += str(i) + ", "
            squareroot = math.sqrt(i)
            if float(squareroot).is_integer():
                squarenums += str(i) + ", "
        i+=1

        if not int((i / calcnum)*100) == percent:
            percent = int((i / calcnum)*100)
            print("\r Progress: " + str(percent) + "% completed     ", end="")
            
    return(Allnums,squarenums)

def calcfactors(calcnum):
    calcnum = int(calcnum)
    i = 1
    Allnums = "the factors of " + str(calcnum) + " are: "
    squarenums = "The square factors of " + str(calcnum) + " are: "
    squarefactorslist = []
    percent = -1
    while i < calcnum:
        if float(calcnum/i).is_integer():
            Allnums += str(i) + ", "
            squareroot = math.sqrt(i)
            if float(squareroot).is_integer():
                squarenums += str(i) + ", "
                squarefactorslist.append(int(i))
        i+=1

        if not int((i / calcnum)*100) == percent:
            percent = int((i / calcnum)*100)
            print("\r Progress: " + str(percent) + "% completed     ", end="")
    if len(squarefactorslist) == 0:
        highestsquarefactor = 0
    else:
        a = len(squarefactorslist) - 1
        highestsquarefactor = squarefactorslist[a]
    return(Allnums,squarenums, highestsquarefactor)

def help(helpstuff):
    if len(helpstuff) == 0:
        print("Command info. Type 'help command' for more info")
        print("factor: Shows factors and square factors of a number. (f, factor)")
        print("lcm: finds the lowest common multiple of numbers (lcm)")
        print("help: shows info on commands. (help, h)")
        print("exit: exits program")
        print("")
    elif helpstuff == "factor" or helpstuff == "f": #Is there a better way to do this?
        print("finds factors and square factors of a number")
        print("Usage: 'f 123' or 'factor 123' (finds factors of 123)")
    elif helpstuff == "lcm":
        print("Finds the lowest common multiple of two numbers")
        print("Usage: 'lcm 12 13' (finds the lowest common multiple of 12 and 13)")
    elif helpstuff == "h" or helpstuff == "help":
        print("why do you need help on the help command")
        print("help: shows info on a command")
        print("Usage: 'h', 'help', 'help command', 'h command'") 
    else:
        print("help: unkonwn command %s" %helpstuff)

def dosettings(setting):
    if setting == '':
        print('usage: settings [setting] true')
        print('debug: shows some stuff, useful for debugging the program, will slow stuff down a lot (true/false)') #unused at the moment lmao
    elif setting.startswith('debug'):
        setting = setting.replace('debug', '')
        if setting == '':
            with open('%s/mushrrom/mathstuff/test.txt' %os.environ['appdata']) as file: #CHANGE THIS TO MUSHRROM FOLDER
                data = file.readlines()
                print(data)
            ison = data[2]
            print("debug is currently set to: %s" %ison)

        elif setting == 'true' or setting == 'True':
            with open('%s/mushrrom/mathstuff/test.txt' %os.environ['appdata']) as file: #CHANGE THIS TO MUSHRROM FOLDER
                data = file.readlines()
            data[2] = "true\n"
            with open('%s/mushrrom/mathstuff/test.txt' %os.environ['appdata'], 'w') as file:
                file.writelines(data)

        elif setting == 'false' or setting == 'False':
            with open('%s/mushrrom/mathstuff/test.txt' %os.environ['appdata'], ) as file: #CHANGE THIS TO MUSHRROM FOLDER
                data = file.readlines()
            data[2] = "false\n"
            with open('%s/mushrrom/mathstuff/test.txt' %os.environ['appdata'], 'w') as file:
                file.writelines(data)
        else:
            print("Debug can only be set to true or false")

def surd(num):
    stuff = calcfactors(num)
    highfactor = stuff[2]
    print('\n')
    if highfactor == 0 or highfactor == 1:
        output = "The surd of %s cannot be simplified" %num
    else:
        morestuff = (int(num)/int(highfactor))
        
        output = 'this can be simplified to %s √%s' %(int(math.sqrt(highfactor)), int(morestuff))
    return(output)
