def main():
    with open('Day07_Input.txt') as file:
        contents = [l.rstrip() for l in file.readlines()]
    
    print(contents)
    
def check_line(s):
    for i in range(2, len(s)):
        if s[i] == s[i-2] and s[i] != s[i-1]:
            SSL_out = s[i] + s[i-1] + s[i]
            SSL_in = s[i-1] + s[i] + s[i-1]
            
    works = True
    if not SSL_in in s:
        return False
    else:
        bracket = False
        for i in range(3, len(s)):
            if 
    
if __name__ == '__main__':
    main()