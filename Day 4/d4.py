
with open('./Day 4/d4_input.txt', 'r') as file:

    
    overlapping = 0
    partially_overlapping = 0


    for line in file.readlines():

        interval_1, interval_2 = line.strip().split(',')
        a, b = [int(x) for x in interval_1.split('-')]
        c, d = [int(x) for x in interval_2.split('-')]

        if ( a <= c and b >= d ) or ( c <= a and d >= b ):
            overlapping += 1
        
        
        if ( a <= c and b >= c ) or ( c <= a and d >= a ):
            partially_overlapping += 1
           

    print(overlapping, partially_overlapping)

