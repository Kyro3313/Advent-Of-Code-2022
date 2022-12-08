with open('./Day 5/d5_input.txt', 'r') as file: 
    
    line = file.readline()
    columns = len(line) // 4
    containers = []
    for i in range(columns):
        containers.insert(i, [])

    
    file.seek(0)
    for line in file.readlines():
        if line.split(' ')[0] != 'move':
            for i , char in enumerate(line): 
                if char.isalpha():
                    containers[line.index(char, i - 1) // 4].append(char)
        

        else:
            splitted = line.strip().split()
            a = int(splitted[1])
            b = int(splitted[3]) - 1
            c = int(splitted[5]) - 1
            
            #Part 1
            # for i, v in enumerate(containers[b][:a]):
            #     containers[c].append(containers[b][i])


            for i, v in enumerate(containers[b][:a][::-1]):
                containers[c].insert(0, v)
            containers[b] = containers[b][a:]
            
    print(containers)
    for list in containers:
        print(list[0], end='')
        
