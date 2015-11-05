import re

problem=input("What is your mathematical word problem?\n\n")
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', problem)
print(sentences)