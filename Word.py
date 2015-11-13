# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

problem.replace(".", "&")   #finding the decimals

quest=(dict(map(lambda letter:(letter,len(problem)-len(problem.replace(letter,''))),problem)))
converted_quest = list(quest.items())

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)

num=len(sentences)
el_range=range(0,num)

while num > 9:
    print("\nWord problem too long!")
    break

words1=sentences[0].split()
words2=sentences[1].split()
if num>2:
    words3=sentences[2].split()
    if num==3:
elif num>3:
    words4=sentences[3].split()
    if num==4:
elif num>4:
    words5=sentences[4].split()
    if num==5:
elif num>5:
    words6=sentences[5].split()
elif num>6:
    words7=sentences[6].split()
    if num==7:
        break
elif num==8:
    words8=sentences[7].split()
    break

print(words8)

#d = enchant.Dict("en_US")
#if d=False:
#   
problem.replace("&", ".")    #reconverting decimals
