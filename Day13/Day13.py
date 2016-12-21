def main():
    favorite = 1358
    dim = 100
    global building
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
            else:
                building[y][x] = '.'
    
    for r in range(len(building)):
        for c in range(len(building[0])):
            if r == 39 and c == 31:
                print('O', end='')
            else:
                print(building[r][c], end='')
        print()

#===============================================================================
# def move_dfs(coordinates, adj, length):
#     if coordinates == [39, 31]:
#         return length
#     
#     adj = [False, False, False, False]
#     if building[coordinates[0]][coordinates[1] - 1] == '.':
#         adj[0] = True
#     if building[coordinates[0]][coordinates[1] + 1] == '.':
#         adj[1] = True
#     if building[coordinates[0] - 1][coordinates[1]] == '.':
#         adj[2] = True
#     if building[coordinates[0] + 1][coordinates[1]] == '.':
#         adj[3] = True
#      
#     if len(path) < 150:
#         if not True in doors:
#             print('FAILURE: ', path)
#         elif occurrences(True, doors) == 1:
#             index = doors.index(True)
#             coordinates = [x + y for x, y in zip(coordinates, moves[index])]
#             path += directions[index]
#             move_dfs(coordinates, path, input, doors)
#         else:
#             for i in reversed(range(len(doors))):
#                 if doors[i] == True:
#                     move_dfs([x + y for x, y in zip(coordinates, moves[i])], path + directions[i], input, doors)
#      
# def occurrences(e, l):
#     count = 0
#     for o in l:
#         if o == e:
#             count += 1
#     return count
#===============================================================================

if __name__ == '__main__':
    main()