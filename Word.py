"""
Name-Suhan Gui
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes.  This was $14 less than twice what she spent for a blouse.  How much was the blouse?
"""
import math
import re
#import enchant

shhh=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")
problem=shhh.lower()

donfail=problem.count('?')
while donfail==0:
    print("You forgot a question mark")
    break

problem_=''.join( c for c in problem if  c not in '$')

deci=re.findall("\d+.\d+", problem_) #find decimals
len_dec=len(deci)
dci=str(deci)
word_=problem_.split()
list0 = [item for item in word_ if item not in deci] #DESTROY THE DECIMALS!
list1=['1' if x=='a' else x for x in list0]#REPLACE TEH 'A's

problem__=" ".join(list1)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split the sentences!

um=len(sentences)
num=um-1
sentrange=str(list(range(0,num)))
print(sentrange)

while num > 10:
    print("\nWord problem too long!")
    break

while um==0:
    print("You forgot a period somewhere pal")
    break

additions=['plus','added','adds','add','gains','gained','gain','sum','produces']
additions_=['plus']
additions__=['+']

subtractions=['spent','removed','removes','subtracted','minus','subtract','take','takes','subtracts','eats','loses','loose']
subtractions_=['minus']
subtractions__=['-']

multiplications=['times','multiplied','multiplies']
multiplications_=['times']
multiplications__=['x']

divisions=['split','divided','divides']
divisions_=['divided by']
divisions__=['/']

equal=['equals']
equal__=['=']

AA1='when'
AA2='how much'
AA3='time what'
AA4='how long did it take'
AA5='how long was'
"""
if num >0 and num <=10:
    print("\nOk. Lets split your problem into statements:")
    for x in sentrange:
        wordd=sentences[x].split()
        #inte=[int(s) for s in wordd.split() if s.isdigit()]
        inte=0
        rangeinte=list(range(inte))
        inte_=str(inte)
        num_of_ints=len(inte_) #for storage
        list2 = [item for item in wordd if item not in inte_] #DESTROY THE INTEGERS!

        problem___=" ".join(list2)
        if num_of_ints==1:
            if len_dec==0:
                if donfail==1:
                    if AA1 in problem___:
                        questionhi=True
                        sattup1=True
                    elif AA2 in problem___:
                        questionhi=True
                        sattup2=True
                    elif AA3 in problem___:
                        questionhi=True
                        sattup3=True
                    elif AA4 in problem___:
                        questionhi=True
                        sattup4=True
                    elif AA5 in problem___:
                        questionhi=True
                        sattup5=True
                    else:
                        questionhi=False
                        print("ynah")
                else:
                    questionhi=False
                    print("nah")
            else:
                questionhi=False
                print("ay")
        else:
            questionhi=False
            print("HAHA")

        if questionhi==True:
            confirmyes=input("Sentence {0} is a question, right? y to confirm. n to reject")
            BAB=confirmyes.lower()
            if confirmyes=="y":
                else:
                    print("This is not a question mate")
                    questionhi=False
            elif confirmyes=="n":
                questionhi=False

        elif questionhi==False:
            print("jet")
            """