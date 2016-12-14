def main():
    favorite = 1358
    dim = 45
    building = [[' ' for _ in range(dim)] for _ in range(dim)]
    
    for y in range(dim):
        for x in range(dim):
            num = bin((x*x + 3*x + 2*x*y + y + y*y) + favorite)
            ones = 0
            for c in num:
                if c == '1':
                    ones += 1
            if ones % 2 == 1:
                if x == 31 and y == 39:
                    building[y][x] = 'X'
                else:
                    building[y][x] = '#'
    
    for r in range(len(building)):
        for c in range(len(building[0])):
            if r == 39 and c == 31:
                print('O', end='')
            else:
                print(building[r][c], end='')
        print()

if __name__ == '__main__':
    main()