"""
Name-Suhan
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $4.2 for shoes.  This was $1.4 less than twice what she spent for a blouse.  How much was the blouse?
"""
from math import sin, cos, radians
import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

words_of_problem=problem.split()  #exterminate the decimals!
deci=re.findall("\d+.\d+", problem)
print(deci)
len_dec=len(deci)
print(len_dec)
dec_range=range(0,len_dec-1)
dci=str(deci)
dec=dci[1:-1]
print(dec)
d=dec[0]

while len_dec > 0:
    for x in dec_range:
        jeb=str(dec)
        problem.remove(jeb[x])


sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem) #split the sentences!

um=len(sentences)
num=um-1
el_range=range(0,num)

while num > 10:
    print("\nWord problem too long!")
    break

while um==0:
    print("You forgot a period somewhere pal")
    break

if num>=1:
    words1=sentences[0].split()
if num>=2:
    words2=sentences[1].split()
if num>=3:
    words3=sentences[2].split()
if num>=4:
    words4=sentences[3].split()
if num>=5:
    words5=sentences[4].split()
if num>=6:
    words6=sentences[5].split()
if num>=7:
    words7=sentences[6].split()
if num>=8:
    words8=sentences[7].split()
if num>=9:
    words9=sentences[8].split()
if num==10:
    words10=sentences[10].split()