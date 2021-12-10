from mathstuff import calclcm


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
    if not(len(squarefactorslist) == 0):
        a = len(squarefactorslist) - 1
        highestsquarefactor = squarefactorslist[a]
    return(Allnums,squarenums, highestsquarefactor)

test1 = calcfactors(29)

print(test1[2])