"""
Name-Suhan
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $4.2 for shoes.  This was $1.2 less than twice what she spent for a blouse.  How much was the blouse?
"""
import math
import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

while problem=="":
    print("You forgot to type your problem")
    break

problem_=''.join( c for c in problem if  c not in '$')

deci=re.findall("\d+.\d+", problem_)
len_dec=len(deci)
dec_range=list(range(0,len_dec))
dci=str(deci)

word_=problem_.split()
list1 = [item for item in word_ if item not in deci]
print(list1)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem_) #split the sentences!

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