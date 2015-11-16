"""
Name-Suhan
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes.  This was $14 less than twice what she spent for a blouse.  How much was the blouse?
"""
import math
import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

words_of_problem=problem.split()  #exterminate the decimals!
deci=re.findall("\d+.\d+", problem)
len_dec=len(deci)
len_tru=len_dec-1
dec_range=range(0,len_dec)
dec=deci[1:-1]
bush=abs(dec)
print(bush)
while deci > 0:
    jeff=problem.remove(de)
    print(jeff)

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