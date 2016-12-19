# from itertools import compress

def main():
    input = 3004953
    print(take_across(1, [n for n in range(1, input + 1)]))
    
def take_across(current, elves):
    # presents = [True for _ in range(len(elves))]
    
    while elves:
        if len(elves) == 1:
            return elves[0]
        else:
            print(len(elves))
            del elves[len(elves) // 2]
            # elves = list(compress(elves, presents))
            elves = rotate(elves, 1)
            # presents = presents[:-1]
    
def rotate(l, n):
    return l[n:] + l[:n]
        
if __name__ == '__main__':
    main()