def calculate(string):
    '''Given one string, calculate the occurence time of each char'''
    count_record = {}
    for char in string: # This solution is pretty simple and elegant
        count_record[char] = count_record.get(char,0) + 1
    for k,v in count_record.items():
        print('{}:{}'.format(k,v))

def calculate_two(string):
    '''Use their ASCIInumbers'''
    if not string:
        print('No character exists')
        return
    record = [0 for _ in range(26)]
    for char in string:
        record[ord(char)-ord('a')] += 1
    for index,value in enumerate(record):
        if value:
            print('{}:{}'.format(chr(index+ord('a')),value))



from sys import argv
script, string = argv
calculate_two(string)
