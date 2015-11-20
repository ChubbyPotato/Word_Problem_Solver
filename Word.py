"""
Name-Suhan
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes.  This was $12 less than twice what she spent for a blouse.  How much was the blouse?
"""
import math
import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

while problem=="":
    print("You forgot to put in the problem")
    break

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

inte=[int(s) for s in problem__.split() if s.isdigit()] #Locate integers
inte_=str(inte)
list1 = [item for item in list0 if item not in inte_] #DESTROY THE INTEGERS!

problem__=" ".join(list1)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split the sentences!

um=len(sentences)
num=um-1

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
    words3=sentences[0].split()
if num>=4:
    words4=sentences[1].split()
if num>=5:
    words5=sentences[0].split()
if num>=6:
    words6=sentences[1].split()
if num>=7:
    words7=sentences[0].split()
if num>=8:
    words8=sentences[1].split()
if num>=9:
    words9=sentences[0].split()
if num==10:
    words10=sentences[1].split()
    
"""
#Finale!
print("Ok. Lets split your problem into statements

if num_>=1:
    print("For the first sentece
if num_>=2:
    
if num_>=3:
    
if num_>=4:
    
if num_>=5:
    
if num_>=6:
    
if num_>=7:
    
if num_>=8:
    
if num>=9:
    
if num==10:
    
"""