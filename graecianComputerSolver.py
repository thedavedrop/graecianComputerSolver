# define baseline, "position0" lists
LstLevel1radius1position0 = [11, 11, 14, 11, 14, 11, 14, 14, 11, 14, 11, 14]
LstLevel1radius2position0 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LstLevel1radius3position0 = [4, 4, 6, 6, 3, 3, 14, 14, 21, 21, 9, 9]
LstLevel1radius4position0 = [8, 3, 4, 12, 2, 5, 10, 7, 16, 8, 7, 8]
LstLevel2radius1position0 = [2, 7, -999, 9, -999, 7, 14, 11, -999, 8, -999, 16]
LstLevel2radius2position0 = [-999, 9, 20, 12, 3, 6, -999, 14, 12, 3, 8, 9]
LstLevel2radius3position0 = [12, 3, 26, 6, -999, 2, 13, 9, -999, 17, 19, 3]
LstLevel2radius4position0 = [-999, 1, -999, 9, -999, 12, -999, 6, -999, 10, -999, 10]
LstLevel3radius1position0 = [7, 13, 21, 17, 4, 5, -999, 7, 8, 9, 13, 9]
LstLevel3radius2position0 = [4, 9, 18, 11, 26, 14, 1, 12, -999, 21, 6, 15]
LstLevel3radius3position0 = [-999, 8, -999, 22, -999, 16, -999, 9, -999, 5, -999, 10]
LstLevel4radius1position0 = [11, -999, 6, 17, 7, 3, -999, 6, -999, 11, 11, 6]
LstLevel4radius2position0 = [9, -999, 12, -999, 4, -999, 7, 15, -999, -999, 14, -999]
LstLevel5radius1position0 = [3, -999, 6, -999, 10, -999, 7, -999, 15, -999, 8, -999]

# create a place to store solution(s)
LstSolutionPositions = []

""" just make sure nothing is nuts...
print(f"before doing anything, LstSolutionPositions = {LstSolutionPositions}")
print(f"before doing anything, LstLevel1radius4position0 = {LstLevel1radius4position0}")
"""

""" confirmed; NO solutions if alter LstLevel1radius4position0...
# make sure NO solutions if alter LstLevel1radius4position0
print(f"original LstLevel1radius4position0 = {LstLevel1radius4position0}")
# this gives position = VALUE of each list element, which is NOT what i want...
# for position in LstLevel1radius4position0:
#     print(f"position = {position}")
#     LstLevel1radius4position0[position] = LstLevel1radius4position0[position] + 1

# print(len(LstLevel1radius4position0)) # gives 12
for index in range(0,len(LstLevel1radius4position0)):
    LstLevel1radius4position0[index] = LstLevel1radius4position0[index] + 1
print(f"altered LstLevel1radius4position0 = {LstLevel1radius4position0}")
"""

# begin "the algorithm"
for Level2position in range(0,12):
    # make Level2current lists

    # initialize *current lists
    LstLevel2radius1current = LstLevel2radius1position0
    LstLevel2radius2current = LstLevel2radius2position0
    LstLevel2radius3current = LstLevel2radius3position0
    LstLevel2radius4current = LstLevel2radius4position0
    
    # construct *current lists
    for position in range(0,Level2position):
        LastElement = LstLevel2radius1current.pop()
        LstLevel2radius1current.insert(0, LastElement)

        LastElement = LstLevel2radius2current.pop()
        LstLevel2radius2current.insert(0, LastElement)

        LastElement = LstLevel2radius3current.pop()
        LstLevel2radius3current.insert(0, LastElement)

        LastElement = LstLevel2radius4current.pop()
        LstLevel2radius4current.insert(0, LastElement)

    for Level3position in range(0,12):
        # make Level3current lists

        # initialize *current lists
        LstLevel3radius1current = LstLevel3radius1position0
        LstLevel3radius2current = LstLevel3radius2position0
        LstLevel3radius3current = LstLevel3radius3position0
        
        # construct *current lists
        for position in range(0,Level3position):
            LastElement = LstLevel3radius1current.pop()
            LstLevel3radius1current.insert(0, LastElement)

            LastElement = LstLevel3radius2current.pop()
            LstLevel3radius2current.insert(0, LastElement)

            LastElement = LstLevel3radius3current.pop()
            LstLevel3radius3current.insert(0, LastElement)

        for Level4position in range(0,12):
            # make Level4current lists

            # initialize *current lists
            LstLevel4radius1current = LstLevel4radius1position0
            LstLevel4radius2current = LstLevel4radius2position0
            
            # construct *current lists
            for position in range(0,Level4position):
                LastElement = LstLevel4radius1current.pop()
                LstLevel4radius1current.insert(0, LastElement)

                LastElement = LstLevel4radius2current.pop()
                LstLevel4radius2current.insert(0, LastElement)

            for Level5position in range(0,12):
                # make Level5current lists

                # initialize *current lists
                LstLevel5radius1current = LstLevel5radius1position0
                
                # construct *current lists
                for position in range(0,Level5position):
                    LastElement = LstLevel5radius1current.pop()
                    LstLevel5radius1current.insert(0, LastElement)

                # initialize stillCouldBeSolution for "position loop"
                stillCouldBeSolution = 1
                
                # sum numbers at each of 12 positions
                for position in range(0,12):
                    # get "displayed value" for each radius
                    
                    # radius1
                    if LstLevel5radius1current[position] != -999:
                        radius1value = LstLevel5radius1current[position]
                    elif LstLevel4radius1current[position] != -999:
                        radius1value = LstLevel4radius1current[position]
                    elif LstLevel3radius1current[position] != -999:
                        radius1value = LstLevel3radius1current[position]
                    elif LstLevel2radius1current[position] != -999:
                        radius1value = LstLevel2radius1current[position]
                    else:
                        radius1value = LstLevel1radius1position0[position]

                    # radius2
                    if LstLevel4radius2current[position] != -999:
                        radius2value = LstLevel4radius2current[position]
                    elif LstLevel3radius2current[position] != -999:
                        radius2value = LstLevel3radius2current[position]
                    elif LstLevel2radius2current[position] != -999:
                        radius2value = LstLevel2radius2current[position]
                    else:
                        radius2value = LstLevel1radius2position0[position]

                    # radius3
                    if LstLevel3radius3current[position] != -999:
                        radius3value = LstLevel3radius3current[position]
                    elif LstLevel2radius3current[position] != -999:
                        radius3value = LstLevel2radius3current[position]
                    else:
                        radius3value = LstLevel1radius3position0[position]

                    # radius4
                    if LstLevel2radius4current[position] != -999:
                        radius4value = LstLevel2radius4current[position]
                    else:
                        radius4value = LstLevel1radius4position0[position]

                    # calc sum for current position
                    positionSum = radius1value + radius2value + radius3value + radius4value

                    # if can no longer be a solution, update stillCouldBeSolution
                    if positionSum != 42:
                        stillCouldBeSolution = 0
                    
                    # if all 12 sums add to 42, record LevelPositions, because that is a solution
                    if position == 11 and stillCouldBeSolution == 1:
                        LstSolutionPositions.append(f"{Level2position}, {Level3position}, {Level4position}, {Level5position}")
                        # also display all lists in solution
                        print(f"LstLevel5radius1current = {LstLevel5radius1current}")
                        print(f"LstLevel4radius1current = {LstLevel4radius1current}")
                        print(f"LstLevel3radius1current = {LstLevel3radius1current}")
                        print(f"LstLevel2radius1current = {LstLevel2radius1current}")
                        print(f"LstLevel1radius1position0 = {LstLevel1radius1position0}\n")

                        print(f"LstLevel4radius2current = {LstLevel4radius2current}")
                        print(f"LstLevel3radius2current = {LstLevel3radius2current}")
                        print(f"LstLevel2radius2current = {LstLevel2radius2current}")
                        print(f"LstLevel1radius2position0 = {LstLevel1radius2position0}\n")

                        print(f"LstLevel3radius3current = {LstLevel3radius3current}")
                        print(f"LstLevel2radius3current = {LstLevel2radius3current}")
                        print(f"LstLevel1radius3position0 = {LstLevel1radius3position0}\n")

                        print(f"LstLevel2radius4current = {LstLevel2radius4current}")
                        print(f"LstLevel1radius4position0 = {LstLevel1radius4position0}\n")

# display solution(s)
print(f"solution positions (Level2, Level3, Level4, Level5) = {LstSolutionPositions}")
