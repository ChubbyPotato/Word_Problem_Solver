"""
Name-Suhan
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes.  This was $12 less than twice what she spent for a blouse.  How much was the blouse?
"""
import math
import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

problem_=''.join( c for c in problem if  c not in '$')

deci=re.findall("\d+.\d+", problem_)
len_dec=len(deci)
dec_range=list(range(0,len_dec))
dci=str(deci)
word_=problem_.split()
list0 = [item for item in word_ if item not in deci]

problem__=" ".join(list0)

inte=[int(s) for s in problem__.split() if s.isdigit()]
print(inte)
list1 = [item for item in list0 if item not in inte]
print(list1)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split the sentences!

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