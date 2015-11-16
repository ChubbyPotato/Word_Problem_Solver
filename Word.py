# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re
from decimals import Decimals
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

deci=re.findall("\d+.\d+", problem)
float((deci))

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)

um=len(sentences)
num=um-1
el_range=range(0,num)

while num > 11:
    print("\nWord problem too long!")
    break

if num=<1:
    words1=sentences[0].split()
if num=<2:
    words2=sentences[1].split()
if num=<3:
    print(words2)
    words3=sentences[2].split()
if num=<4:
    words4=sentences[3].split()
if num=<5:
    words5=sentences[4].split()
if num=<6:
    words6=sentences[5].split()
if num=<7:
    words7=sentences[6].split()
if num=<8:
    words8=sentences[7].split()
if num=<9:
    words9=sentences[8].split()
if num==10:
    words10=sentences[10].split()