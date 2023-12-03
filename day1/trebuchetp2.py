'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line
'''
# between 53315 and 53355 53356 -> 53345?
import re
from math import inf
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

f = open('input1.txt', 'r')
inputs = f.readlines()
#print(inputs)

updatedvalues = []
spelledoutdigits = {'one':'1' , 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'
                    ,'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
for line in inputs:
    line = line.strip('\n')
    print(line)
    min = 100000000000000000000
    minstr = ''
    for digit in spelledoutdigits.keys():
        loc = line.find(digit)
        #print(loc)
        if -1 < loc < min:
            min = loc
            minstr = digit
            #print(minstr)
    if min < 100000000000000000000:
        line = line.replace(minstr, spelledoutdigits[minstr], 1)
        #print(line)
    max = -1
    maxstr = ''
    for digit in spelledoutdigits.keys():
        loc = line.find(digit) 
        if loc > max:
            max = loc
            maxstr = digit
    if max > -1:
        line = spelledoutdigits[maxstr].join(line.rsplit(maxstr, 1))
        line = rreplace(line, maxstr, spelledoutdigits[maxstr], 1)   
    print(line)
    nums = [s for s in line if s.isdigit()]
    startval = nums[0]
    endval=nums[-1]
    newline = int(startval+endval)
    print(newline)
    updatedvalues.append(newline)

    #print(updatedvalues)

print(sum(updatedvalues))
