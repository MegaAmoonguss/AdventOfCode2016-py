def main():
    with open("Day03_Input.txt") as file:
        contents = file.readlines()
        
    sides = []
    for line in contents:
        sides.append([int(n.strip()) for n in line.split("  ") if not n.strip() == ''])
        
    count = 0
    for triangle in sides:
        triangle = sorted(triangle)
        if triangle[0] + triangle[1] > triangle[2]:
            count += 1
    
    print(count)
    
if __name__ == '__main__':
    main()