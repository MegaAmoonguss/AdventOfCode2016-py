from hashlib import md5
from itertools import compress

def main():
    # input = 'awrkjxxr'
    input = 'ihgpwlah'
    
    global moves
    global directions
    moves = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}
    directions = ['U', 'D', 'L', 'R']
     
    move((0, 0), input)
    
def move(coordinates, input):
    path = ''
    queue = ['']
    
    while queue:
        # parent = coordinates
        path = path[len(path) - 1] + queue[0]
        queue.pop(0)
        
        doors = [False, False, False, False]
        hash = md5((input + path).encode('utf-8')).hexdigest()[:4]
        
        for i in range(len(hash)):
            if 98 <= ord(hash[i]) <= 102:
                doors[i] = True
        
        for d in compress(directions, doors):
            queue.append(d)
    
#===============================================================================
# def move_dfs(coordinates, path, input):
#     if coordinates == [3, 3]:
#         solutions.append(path)
#     
#     doors = [False, False, False, False]
#     
#     hash = md5((input + path).encode('utf-8')).hexdigest()[:4]
#     
#     for i in range(len(hash)):
#         if ord(hash[i]) >= 98 and ord(hash[i]) <= 102:
#             doors[i] = True
#     
#     if coordinates[0] + 1 == 4:
#         doors[3] = False
#     if coordinates[0] - 1 == -1:
#         doors[2] = False
#     if coordinates[1] + 1 == 4:
#         doors[1] = False
#     if coordinates[1] - 1 == -1:
#         doors[0] = False
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