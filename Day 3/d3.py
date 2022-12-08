from string import ascii_lowercase, ascii_uppercase


with open('./Day 3/d3_input.txt', 'r') as file:

    letter_value = ascii_lowercase + ascii_uppercase
    
    lines = file.read().split('\n')


    def part_1(array):

        total = 0

        for line in array:
            
            l = len(line)
            str1 = line[(l//2):]
            str2 = line[:(l//2)]
            found = ""

            for char in str1:
                if char in str2 and not (char in found):
                    found += char
                    total += letter_value.index(char) + 1

        return total

    print(part_1(lines))


    ##Part 2

    triple_lines = []

    for index, line in enumerate(lines):
        
        if ((index + 1) % 3 == 0): 
            triple_lines.append([lines[index-2], lines[index-1], lines[index]])

    def part_2(array):

        total = 0
        
        for group in array:
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    total += letter_value.index(char) + 1
                    break                   

        return total 
        


    print(part_2(triple_lines))
        

        
