# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

problem.replace(".", "&")

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)

num=len(sentences)
el_range=range(0,num)

while num > 9:
    print("\nWord problem too long!")
    break

if num==1:
    words1=sentences[0].split()
elif num==2:
    words1=sentences[0].split()
    words2=sentences[1].split()
elif num==2:
    words1=sentences[0].split()
    words2=sentences[1].split()
    print(words2)
    words3=sentences[2].split()
elif num==2:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
elif num==2:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
    words5=sentences[4].split()
elif num==2:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
    words5=sentences[4].split()
    words6=sentences[5].split()
elif num==2:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
    words5=sentences[4].split()
    words6=sentences[5].split()
    words7=sentences[6].split()
else:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
    words5=sentences[4].split()
    words6=sentences[5].split()
    words7=sentences[6].split()
    words8=sentences[7].split()

problem.replace("&", ".")
