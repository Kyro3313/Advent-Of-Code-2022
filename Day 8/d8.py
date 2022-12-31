with open(f'./Day 8/d8_input.txt', 'r') as file: 

    tree_array = []

    for i, line in enumerate(file.readlines()):
        line = line.strip()
        tree_array.append([])
        for num in line:
            tree_array[i].append(int(num))
    
    visible_count = (( len(tree_array) + len(tree_array[0]) ) * 2 ) - 4
    
    visual_score = []

    for i, row in enumerate(tree_array):
        if i == 0 or i == (len(tree_array) - 1):
            continue
        for j, tree in enumerate(row):
            if j == 0 or j == (len(row) - 1):
                continue
            else:
                adjacent = []
                adjacent.append(tree_array[i][:j][::-1]) #Left #[::-1] for p2.
                adjacent.append(tree_array[i][j+1:]) #Right
                top = []
                bottom = []
                
                for k in range(len(tree_array)):
                    if k == i:
                        continue
                    elif k < i:
                        top.append(tree_array[k][j])
                    elif k > i:
                        bottom.append(tree_array[k][j])

                adjacent.append(top[::-1])
                adjacent.append(bottom)

                for direction in adjacent:
                    visible = []
                    for number in direction:
                        if number < tree:
                            visible.append(number)
                    if len(visible) == len(direction):
                        visible_count += 1
                        print(tree)
                        break

                #Part 2

                tree_score = 1
                for direction in adjacent:
                    for index, number in enumerate(direction):
                        if number >= tree or index == len(direction) - 1:
                            tree_score *= index + 1
                            break
                visual_score.append(tree_score)
                 
    print(visible_count)
    print(max(visual_score))

    