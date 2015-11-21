"""
Name-Suhan Gui
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes.  This was $14 less than twice what she spent for a blouse.  How much was the blouse?
"""
import math
import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

donfail=problem.count('?')
while donfail==0:
    print("You forgot a question mark")
    break

problem_=''.join( c for c in problem if  c not in '$')

deci=re.findall("\d+.\d+", problem_) #find decimals
len_dec=len(deci)
dec_range=list(range(0,len_dec))
dci=str(deci)
word_=problem_.split()
list0 = [item for item in word_ if item not in deci] #DESTROY THE DECIMALS!
list1=['1' if x=='a' else x for x in list0]#REPLACE TEH 'A's

inte=[int(s) for s in problem_.split() if s.isdigit()]
inte_=str(inte)
list2 = [item for item in list1 if item not in inte_] #DESTROY THE INTEGERS!

problem__=" ".join(list2)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split the sentences!

um=len(sentences)
num=um-1

while num > 10:
    print("\nWord problem too long!")
    break

while um==0:
    print("You forgot a period somewhere pal")
    break

print("\nOk. Lets split your problem into statements:")
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
    words10=sentences[9].split()