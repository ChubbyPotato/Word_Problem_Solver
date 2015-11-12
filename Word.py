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
words3=sentences[2].split()
words4=sentences[3].split()
words5=sentences[4].split()
words6=sentences[5].split()
words7=sentences[6].split()
words8=sentences[7].split()



#d = enchant.Dict("en_US")
#if d=False:
#   
problem.replace("&", ".")    #reconverting decimals
