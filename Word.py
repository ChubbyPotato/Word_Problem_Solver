# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count! Also, please have the questions at the end of the word problem!)\n\n")
while problem=="":
    problem=input("Please enter your mathematical word problem. (Spelling, grammar, and punctuation count! Also, please have questions at the end of the word problem!)\n\n")

quest=(dict(map(lambda letter:(letter,len(problem)-len(problem.replace(letter,''))),problem)))
converted_quest = list(quest.items())
converted_quest.sort(key=lambda f: (-f[1], f[0]))
for x in converted_quest:
    if x[0]!=0 and x[0]!=(" ") and x[0]!=("'")
        print(x[0]*x[1])

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)
num=len(sentences)
sent_list=list(range(1,num))
for x in sent_list:
    sents=sentences[x-1]
    print(sents)