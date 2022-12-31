with open('./Day 6/d6_input.txt', 'r') as file: 

    
    def part_1(text):
        for i in range(4, len(text)):
            letters = set(text[(i-4):i])
            if(len(letters) == 4):
                print(i)
                return i
    
    def part_2(text):
        for i in range(14, len(text)):
            letters = set(text[(i-14):i])
            if(len(letters) == 14):
                print(i)
                return i
            

    part_1(file.read())
    file.seek(0)
    part_2(file.read())
