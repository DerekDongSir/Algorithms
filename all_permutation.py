from sys import argv
def all_permutation(ls,locate):
    '''given a string ,output all the permutation answers'''
    if locate == len(ls)-1: # 不需要进行交换，返回
        return
    else:
        for i in range(locate+1,len(ls)): # 当前位置和之后位置的每一个进行一次交换
            l = ls.copy() # 对当前列表进行拷贝，后续操作是对新列表的操作
            l[locate],l[i] = l[i],l[locate]
            print(''.join(l)) # 列表改变之后得到一个结果，进行一次输出打印，
            all_permutation(l,locate+1)
        all_permutation(ls,locate+1)
script,string = argv
all_permutation(list(string),0)
