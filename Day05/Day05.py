import hashlib

def main():
    door_id = 'uqwqemis' 
    
    print('Password:', part2(door_id))
    
def part1(door_id):
    password = ''
    n = 0
    while len(password) < 8:
        input = door_id + str(n)
        hash = hashlib.md5(input.encode('utf-8')).hexdigest()
        if hash[:5] == '00000':
            password += hash[5]
        n += 1
    return password

def part2(door_id):
    password = '69_1____'
    n = 13540620
    count = 3
    while count < 8:
        n += 1
        print(str(n) + ', ' + password)
        input = door_id + str(n)
        hash = hashlib.md5(input.encode('utf-8')).hexdigest()
        if hash[:5] == '00000':
            try:
                pass_list = list(password)
                if pass_list[int(hash[5])] == '_':
                    pass_list[int(hash[5])] = hash[6]
                    password = ''.join(pass_list)
                    count += 1
            except ValueError:
                continue
            except IndexError:
                continue
    return password
    
if __name__ == '__main__':
    main()