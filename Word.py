import re

problem=input("What is your mathematical word problem? (Spell, grammar, and punctuation count!)\n\n")
while problem=="":
    problem=input("Please enter your mathematical word problem. (Spell, grammar, and punctuation count!)\n\n")
sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem)
fake=len(sentences)
realnum=fake-1
sent_list=list(range(1,realnum))
