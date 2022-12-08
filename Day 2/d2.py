#Getting the data.

with open('./Day 2/d2_input.txt', 'r') as file:

    array = [ x.replace(' ', '') for x in file.read().strip().split("\n")]

#Made every "round" into two letters ('AB'), and put all of them into an array.

#Since checking every letter's score and the outcome of a "round" would be an
#"if-statement-nightmare", I will be using a scoreboard to calculate the total score.

    scoreboard_1 = {
        "AX": 4,
        "AY": 8,
        "AZ": 3,

        "BX": 1,
        "BY": 5,
        "BZ": 9,
        
        "CX": 7,
        "CY": 2,
        "CZ": 6
    }


    def part_1(rounds):
        total = 0
        for round in rounds:

            total += scoreboard_1[round]

        return total
    
#Part two changes how the scoreboard works, so:

    scoreboard_2 = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,

        "BX": 1,
        "BY": 5,
        "BZ": 9,
        
        "CX": 2,
        "CY": 6,
        "CZ": 7
    }

    def part_2(rounds):
        total = 0
        for round in rounds:

            total += scoreboard_2[round]

        return total

    print(part_1(array), part_2(array))

