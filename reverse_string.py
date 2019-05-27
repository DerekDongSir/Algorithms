def reverse_string1(chars, m):
    ''' chars refers to the given string while m refers to the number
    of chars needed to be moved from head to back'''
    # 空间复杂度 为 2 * len(chars)
    former_str = chars[:m] # 利用切片得到 前 n 个字符
    back_str = chars[m:] # 得到后面的字符串
    new_str = back_str + former_str # 字符串拼接得到新 字符串
    return new_str

def reverse_string2(chars, m):
    ''' abcdef ----> defabc'''
    ls = list(chars) # python 中字符串不能被改变，故转化为 列表进行操作
    for _ in range(m): # 每次将开头的元素取出并添加到列表的末尾
        ls.append(ls.pop(0))
    return ''.join(ls)

def reverse_string3(chars, m):
    # 通过 3 次 反转交换得到结果
    def reverse(s,front,back): # 将字符串进行反转,此处 s 应为 列表
        # front, back =0, len(s)
        while front < back:
            s[front],s[back] = s[back],s[front]
            front += 1
            back -= 1
    ls = list(chars) # 将 字符串 转为 列表
    reverse(ls,0,m-1) # 将前面的字符串进行反转 abc-->cba
    reverse(ls,m,len(ls)-1) # 将后面的字符串进行反转 def-->fed
    reverse(ls,0,len(ls)-1) # 对整个字符串进行一次反转cbafed-->def
    # 对 同一个列表进行操作 时间复杂度为 n 空间复杂度为 n
    return ''.join(ls)

from sys import argv
script, index = argv
chars = input("请输入字符串：\n")
m = int(input("请输入要反转的字符数量：\n"))
if index == '1':
    print(reverse_string1(chars, m))
elif index == '2':
    print(reverse_string2(chars, m))
elif index == '3':
    print(reverse_string3(chars, m))
else:
    print("Illegal input !")
