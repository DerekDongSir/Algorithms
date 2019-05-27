#在一个字符串中找到第一个只出现一次的字符。如输入abaccdeff，则输出b。
def first_count_one(string):
    '''Given one string, return the first character which
    only appears one time '''
    for char in string:
        '''pythonic solution'''
        if string.count(char) == 1: # return the first char that occurs once
            return char
    else:
        return False


def first_count_one_2(string):
    if not string:
        return False
    count_record = [0 for _ in range(26)] # 记录用列表记录字符出现的次数
    for char in string:
        count_record[ord(char)-ord('a')] += 1
    for i in range(len(count_record)):
        if count_record[i] == 1: #
            return chr(i + ord('a'))
    else:
        return False

from sys import argv
script, string = argv
print(first_count_one_2(string))
