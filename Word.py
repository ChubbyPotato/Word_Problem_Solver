# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count! Also, please have the questions at the end of the word problem!)\n\nYour problem: ")

problem.replace(".", "&")   #finding the decimals

quest=(dict(map(lambda letter:(letter,len(problem)-len(problem.replace(letter,''))),problem)))
converted_quest = list(quest.items())

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)

num=len(sentences)
el_range=range(0,num)

if num > 6:
    print("\nWord problem too long!")
    break

for x in el_range:
    words=sentences[x].split()

jeb=len(words)

#d = enchant.Dict("en_US")

problem.replace("&", ".")    #reconverting decimals
