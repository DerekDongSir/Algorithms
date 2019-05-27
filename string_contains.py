from sys import argv
script, index = argv
str_big = input('Please enter the longer string-->')
str_small = input("Please enter the shorter string-->")
def str_contains_solution1(str_big, str_small):
    ''' The fuction tests whether chars in str_small are all
    in str_big. If the result is yes, return True,otherwise return False  '''
    res = True
    for i in str_small:
        if i not in str_big:
            res = False
            break
    return res
def str_contains_solution2(str_big, str_small):
    ''' convert the string into set and then use < to tell
    whether the small one is a subset of the big one'''
    return True if set(str_small) < set(str_big) else False

def str_contains_solution3(str_big, str_small):
    ''' ord(char)----the ASCII number
        chr(ASCII number)----char '''
    map_big = 0
    for i in str_big:
        map_big |= (1  <<  (ord(i) - ord('a')))
    for j in str_small:
        if not map_big  & (1 << (ord(j) - ord('a'))):
            return False
    else:
        return True

def str_contains_solution4(str_big, str_small):
    '''Given that all the inputs are from the charset"a-z",
    then we can build a relationship between chars and numbers
    composed of 26 prime numbers '''
    def is_prime(num):
        for i in range(int(pow(num,0.5)),1,-1):
            if not num % i:
                return False
        else:
            return True
    def create_prime_numbers(): # 利用 yield 关键字 取 质数
        n = 1
        while True:
            n += 1
            if is_prime(n):
                yield n
    f = create_prime_numbers() # 注意 和 next 连用
    num_list = [next(f) for i in range(26)] # 得到从 2 开始的 26 个质数
    num_big = 1 # 储存长字符串字符对应的质数的乘积值
    for i in str_big:
        map = num_list[ord(i) - ord('a')]
        if num_big % map:
            num_big *= map
    for j in str_small:
        map = num_list[ord(j) - ord('a')]
        if num_big % map:
            return False
    else:
        return True



if index == '1':
    print(str_contains_solution1(str_big, str_small))
elif index == '2':
    print(str_contains_solution2(str_big, str_small))
elif index == '3':
    print(str_contains_solution3(str_big, str_small))
elif index == '4':
    print(str_contains_solution4(str_big, str_small))
else:
    print("Illegal input ! ! !")
