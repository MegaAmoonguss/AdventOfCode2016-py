def main():
    with open('Day01_Input.txt') as file:
        directions = file.read().split(', ')
    
    # The direction being faced, 0 = North, 1 = East, 2 = South, 3 = West
    facing = 0
    moves = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    coordinates = [0, 0]
    locations = [[0, 0]]
    repeat_found = False
    for d in directions:
        if d[0] == 'R':
            facing += 1
        else:
            facing -= 1
        facing %= 4
                
        for _ in range(int(d[1:])):
            coordinates = [x + y for x, y in zip(coordinates, moves[facing])]
            
            if coordinates in locations and not repeat_found:
                print('First repeat at', str(coordinates) + ',', int(abs(coordinates[0]) + abs(coordinates[1])), 'blocks away.')
                repeat_found = True
            elif not repeat_found:
                locations.append(list(coordinates))
            
    print('End at', str(coordinates) + ',', int(abs(coordinates[0]) + abs(coordinates[1])), 'blocks away.')

if __name__ =='__main__':
    main()