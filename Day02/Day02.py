def main():
    with open("Day02_Input.txt") as file:
        instructions = [l.rstrip() for l in file.readlines()]
        
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    moves = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}
    coordinates = [1, 1]
    
    code = ""
    for button in instructions:
        for move in button:
            next = [x + y for x, y in zip(coordinates, moves[move])]
            
            if 0 <= next[0] <= 2 and 0 <= next[1] <= 2:
                coordinates = list(next)
        
        code += str(keypad[coordinates[0]][coordinates[1]])
    
    print(code)
    
if __name__ =='__main__':
    main()