import hashlib
import re

def main():
    input = 'ahsbgdzn'
    
    num_keys = 0
    index = -1
    while num_keys < 64:
        index += 1
        h = hash2016(input, index)
        m = re.search(r'(.)\1{2,}', h)
        if m:
            found = m.group(1)
            for i in range(index + 1, index + 1001):
                new_hash = hash2016(input, i)
                if found * 5 in new_hash:
                    num_keys += 1
                    break
        print(str(index) + ', ' + str(num_keys))
    print(index)   
    
def hash(s):
    return hashlib.md5(s.encode('utf_8')).hexdigest()
    
def check_hash1(s, n):
    h = hash(s + str(n))
    m = re.search(r'(.)\1{2,}', h)
    return m

def hash2016(s, n):
    s = hashlib.md5((s + str(n)).encode('utf_8')).hexdigest()
    for _ in range(2016):
        s = hashlib.md5(s.encode('utf_8')).hexdigest()
    return s
    
if __name__ == '__main__':
    main()