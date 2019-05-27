''' Given a string, find the longest palindrome in the string'''
def longestPalindrome1(chars):
    if not len(chars): # if the string is empty,then return 0
        return 0
    max_length = 0 # dynamicly store the max length of palindromes
    for middle_point in range(0,len(chars)): # middle_point refer to the middle position of string
        j = 0 # j refer to the distance of moving forward and backward from middle_point
        while middle_point + j < len(chars) and middle_point - j > -1: # the odd case
            if chars[middle_point + j] != chars[middle_point - j]:
                break
            else:
                j += 1
        temp = j << 1 - 1 # the max length of palindrome at present point
        if max_length < temp:
            max_length = temp # update the max length

        j = 0
        while middle_point + j + 1 < len(chars) and middle_point - j > -1: # the even case
            if chars[middle_point + j + 1] != chars[middle_point - j]:
                 break
            else:
                j += 1
        temp = j << 1
        if max_length < temp:
            max_length = temp

    return max_length




from sys import argv
script, index = argv
chars = input("Please the string:\n")
if index == "1":
    print(longestPalindrome1(chars))
else:
    print("Illegal input !")
