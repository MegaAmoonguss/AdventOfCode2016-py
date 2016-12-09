def main():
    with open('Day09_Input.txt') as file:
        global contents
        contents = file.read()
    
    index = 0
    while index < len(contents):
        if contents[index] == '(' and is_marker(index):
            m = 1
            while contents[index+m] != ')':
                m += 1
            nums = [int(n) for n in contents[index+1:index+m].split('x')]
            sub = contents[index+m+1:index+m+1+nums[0]]
            contents = contents[:index] + (nums[1] * sub) + contents[index+m+1+nums[0]:]
            index += (nums[1] * nums[0])
        else:
            index += 1
    print(len(contents))
    
def is_marker(i):
    n = 1
    while contents[i+n] != ')':
        n += 1
    nums = contents[i+1:i+n].split('x')
    try:
        int(nums[0])
        int(nums[1])
        return True
    except ValueError:
        return False
    return False
    
if __name__ == '__main__':
    main()