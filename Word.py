# Name-Suhan
# Credit-Stack Overflow, Alexandru Munteanu

import re

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count! Also, please have the questions at the end of the word problem!)\n\n")
while problem=="":
    problem=input("Please enter your mathematical word problem. (Spelling, grammar, and punctuation count! Also, please have questions at the end of the word problem!)\n\n")

a="a"
a=1

quest=(dict(map(lambda letter:(letter,len(problem)-len(problem.replace(letter,''))),problem)))
converted_quest = list(quest.items())
if "?" in converted_quest:
    print("jeff")

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)

num=len(sentences)
sent_list=list(range(1,num))
for x in sent_list:
    sents=sentences[x-1]