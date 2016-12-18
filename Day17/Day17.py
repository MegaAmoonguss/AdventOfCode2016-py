from hashlib import md5

def main():
    # input = 'awrkjxxr'
    input = 'ihgpwlah'
    
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    directions = ['U', 'D', 'L', 'R']
    position = [0, 0]
    end = ''
    
    count = 0
    while position != [3, 3]:
        count += 1
        doors = [False, False, False, False]
        
        hash = md5((input + end).encode('utf-8')).hexdigest()[:4]
        
        for i in range(len(hash)):
            if ord(hash[i]) >= 98 and ord(hash[i]) <= 102:
                doors[i] = True
        
        if position[0] + 1 == 4:
            doors[3] = False
        if position[0] - 1 == -1:
            doors[2] = False
        if position[1] + 1 == 4:
            doors[1] = False
        if position[1] - 1 == -1:
            doors[0] = False
        
        if occurrences(True, doors) == 1:
            index = doors.index(True)
            
        # Make this check both all possble paths when 2+ are available
        else:
            if doors[1] == True:
                index = 1
            elif doors[3] == True:
                index = 3
            elif doors[0] == True:
                index = 0
            else:
                index = 2
        position = [x + y for x, y in zip(position, moves[index])]
        end += directions[index]
        
        print(position)
        print(end)
        
    print(count)
    
def occurrences(e, l):
    count = 0
    for o in l:
        if o == e:
            count += 1
    return count
    
if __name__ == '__main__':
    main()