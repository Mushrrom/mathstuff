import os
import math
#What are you doing here?
#testofmathstuff.py
os.system("title " + "Math stuff By me")
num = 0
#Allnums = "the factors of " + str(num) + " are: "
#squarenums = "The square factors of " + str(num) + " are: "
i = 1
print("Some math stuff so that I can save time because I'm lazy :)")
print('available at https://github.com/Mushrrom/mathstuff')
print('type h for help')
print("\n")

#all the function stuff so that the actual thing doesnt grt really cluttered up :) 

#regular functions-------------
def calcfactors(calcnum):

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
    print("\n")
    print(Allnums)
    print(squarenums)

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
    print("The lowest common multiple of %i and %i is %i (%s)" %(num1, num2, num1current, calculation ))

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




#debug functions----------------

def calcfactors_debug(calcnum):

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
    print("\n")
    print(Allnums)
    print(squarenums)

Pathforthestuff = '%s/mushrrom/mathstuff' % os.environ['appdata']
if not os.path.exists(Pathforthestuff):
    print('If this is your first time using the program type h or help for help')
    os.makedirs(Pathforthestuff)


 
going = True
while going == True:
    #num = int(input("Enter Number: "))
    commandinput = input(": ") 
    #Calculates factors
    if commandinput.startswith("h") or commandinput.startswith("help"):
        commandinput = commandinput.replace("help", "")
        commandinput = commandinput.replace("h", "")
        print(commandinput)
        helpstuff = commandinput.replace(" ", "")
        help(helpstuff)
    elif commandinput.startswith("f ") or commandinput.startswith("factor "):
        commandinput = commandinput.replace("f ", "")
        num = int(commandinput.replace("factor ", ""))
        calcfactors(num) 
    elif commandinput.startswith("lcm"):
        commandinput = commandinput.replace("lcm ", "")
        commandinput = commandinput.replace("lcm ", "")    
        calclcm(commandinput)
    elif commandinput.startswith("exit"):
        going = False
    elif commandinput.startswith('settings'):
        commandinput = commandinput.replace('settings', '')
        commandinput = commandinput.replace(' ', '')
        dosettings(commandinput)

    else:
        print("Unknown command: %s" %commandinput)