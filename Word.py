# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count! Also, please have the questions at the end of the word problem!)\n\n")

if problem=="":
    problem=input("Please enter your mathematical word problem. (Spelling, grammar, and punctuation count! Also, please have questions at the end of the word problem!)\n\n")

problem.replace(".", "&")   #finding the decimals

quest=(dict(map(lambda letter:(letter,len(problem)-len(problem.replace(letter,''))),problem)))
converted_quest = list(quest.items())

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)

num=len(sentences)
real_num=num-1
el_range=range(0,real_num)
        
if real_num > 6:
    new_problem=("Word problem too long!")

for x in el_range:
    words=sentences[x].split()

jeb=len(words)
    print(words)

for x in jeb:
    ind_words=words[x]
    print(and_words)
    
problem.replace("&", ".")    #reconverting decimals

#Spell checker
 #enchant.Dict("en_US")