# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

numbers=['1','2','3','4','5','6','7','8','9','0']
problem2=problem.split()
problem.replace("{0}.{0}", "&".format(numbers))

print(problem)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)

um=len(sentences)
num=um-1
el_range=range(0,num)

while num > 9:
    print("\nWord problem too long!")
    break

if num==1:
    words1=sentences[0].split()
elif num==2:
    words1=sentences[0].split()
    words2=sentences[1].split()
elif num==3:
    words1=sentences[0].split()
    words2=sentences[1].split()
    print(words2)
    words3=sentences[2].split()
elif num==4:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
elif num==5:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
    words5=sentences[4].split()
elif num==6:
    words1=sentences[0].split()
    words2=sentences[1].split()
    words3=sentences[2].split()
    words4=sentences[3].split()
    words5=sentences[4].split()
    words6=sentences[5].split()
elif num==7:
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