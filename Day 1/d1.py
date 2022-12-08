import os

os.chdir('../Advent-Of-Code-2022/Day 1')

file = open("./d1_input.txt", "r")

def get_most_calories():
    arr = []
    calories = 0
    for line in file.readlines():
        if line != "\n":
            calories += int(line)
        else:
            arr.append(calories)
            calories = 0
    
    arr.sort(reverse=True)
    
    ## For Part One of the puzzle, only "return arr[0]" was necessary,
    ## for Part Two, however, we need to find the three highest numbers and sum them.

    sum = arr[0] + arr[1] + arr[2]

    return sum

print(get_most_calories())

