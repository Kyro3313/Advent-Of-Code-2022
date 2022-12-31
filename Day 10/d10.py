with open('./Day 10/d10_input.txt', 'r') as file: 
    lines = file.read().strip().split('\n')

    x = 1
    cycle = 1
    strength = []

    for line in lines:

        command = line.split(' ')[0]

        if command == 'noop':
            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                strength.append(cycle * x)

        elif command == 'addx':
            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                strength.append(cycle * x)

            number = line.split(' ')[1]
            x += int(number)

            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                strength.append(cycle * x)
        
        


    print(sum(strength))
        
    ##Part 2

    def add_pixel():
        global x, pixel_num, drawing

        if pixel_num in range(x - 1, x + 2):
            drawing += '#'
            pixel_num += 1
        
        else:
            drawing += '.'
            pixel_num += 1

        if pixel_num in [40, 80, 120, 160, 200, 240]:
            pixel_num = 0
            drawing += '\n'
        

    x = 1
    cycle = 1
    pixel_num = 0
    drawing = ''

    for line in lines:

        command = line.split(' ')[0]

        if command == 'noop':

            add_pixel()
            cycle += 1

        elif command == 'addx':

            add_pixel()
            cycle += 1

            add_pixel()
            cycle += 1
            number = line.split(' ')[1]
            x += int(number)

            

    print(drawing)

   