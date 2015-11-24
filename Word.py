"""
Name-Suhan Gui
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes. This was $14 less than twice what she spent for a blouse. How much was the blouse?
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

problem__=" ".join(list1)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split the sentences!

um=len(sentences)
num=um-1
sentrange=list(range(0,num))

while num > 10:
    print("\nWord problem too long!")
    break

while um==0:
    print("You forgot a period somewhere pal")
    break

additions=['plus','added','adds','add','gains','gained','gain','sum','more']
additions_=['plus']
additions__=['+']

twice=['twice']
twice_=['2 times']
twice__=['2x']

sq_root=['root']
sq_root_=['^(-2)']

subtractions=['spent','removed','remove','removes','takes','gone','less']
subtractions_=['minus']
subtractions__=['-']

multiplications=['times','multiplied','multiply']
multiplications_=['times']
multiplications__=['x']

divisions=['split','splitted','divide']
divisions_=['divided by']
divisions__=['/']

print("\nOk. Lets split your problem into statements:")

for x in sentrange:
    wordd=sentences[x].split()
    senteeee=sentences[x]
    inte=[int(s) for s in problem_.split() if s.isdigit()]
    inte_=str(inte)
    num_of_ints=len(inte_) #for storage
    list2 = [item for item in wordd if item not in inte_] #DESTROY THE INTEGERS!
    if num_of_ints==0:
        list3 = [item for item in wordd if item not in inte_]
        list4 = [item for item in wordd if item not in inte_]
        list5 = [item for item in wordd if item not in inte_]
        list6 = [item for item in wordd if item not in inte_]
        list7 = [item for item in wordd if item not in inte_]
        list8 = [item for item in wordd if item not in inte_]
        list9 = [item for item in wordd if item not in inte_]
        list10 = [item for item in wordd if item not in inte_]
        list11 = [item for item in wordd if item not in inte_]
    elif num_of_ints>0:
