
with open('./Day 9/d9_input.txt', 'r') as file: 
    
    lines = file.read().strip().split('\n')

    tx, ty = 0, 0
    hx, hy = 0, 0

    directions = {
        'R' : [1, 0],
        'U' : [0, 1],
        'L' : [-1,0],
        'D' : [0,-1]
    }

    tail_visited = set()

    def touching(x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    
    for line in lines:
        direction, times = line.split(' ')
        for _ in range(int(times)):
            nx, ny = directions[direction]
            hx += nx
            hy += ny
            if not touching(hx, hy, tx, ty):
                tx2 = 0 if hx == tx else (hx - tx) // abs(hx - tx)
                ty2 = 0 if hy == ty else (hy - ty) // abs(hy - ty) 

                tx += tx2
                ty += ty2
            
            tail_visited.add((tx, ty))
    
    print(tail_visited, len(tail_visited))

    ##Part 2


    knots = [[0,0] for _ in range(10)]

    tail_visited = set()

    for line in lines:
        direction, times = line.split(' ')
        for _ in range(int(times)):
            nx, ny = directions[direction]
            knots[0][0] += nx
            knots[0][1] += ny

            for i in range(1, 10):
                tx, ty = knots[i]
                hx, hy = knots[i - 1]

                if not touching(hx, hy, tx, ty):
                    tx2 = 0 if hx == tx else (hx - tx) // abs(hx - tx)
                    ty2 = 0 if hy == ty else (hy - ty) // abs(hy - ty) 

                    tx += tx2
                    ty += ty2
                
                knots[i] = [tx, ty]
            
            tail_visited.add(tuple(knots[-1]))
    
    print(tail_visited, len(tail_visited))
        
            
