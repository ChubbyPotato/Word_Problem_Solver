"""
Name-Suhan Gui
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes.  This was $14 less than twice what she spent for a blouse. How much was the blouse?
"""
import math
import re

shhh=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")
problem=shhh.lower()

donfail=problem.count('?')
while donfail==0:
    print("You forgot a question mark")
    break

problem_=''.join( c for c in problem if  c not in '$')

deci=re.findall("\d+.\d+", problem_) #find decimals
len_dec=len(deci)
dci=int(len_dec)
word_=problem_.split()
list0 = [item for item in word_ if item not in deci] #DESTROY THE DECIMALS!

problem__=" ".join(list0)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split the sentences!

um=len(sentences)
num=um-1
sentrange=list(range(0,num))

while num > 10:
    print("\nWord problem too long!")
    break

while um==0:
    print("You forgot a period somewhere pal")
    break

additions=['plus','added','adds','add','gains','gained','gain','sum','produces','total','more']
additions_=['plus']
additions__=['+']

subtractions=['spent','removed','removes','subtracted','minus','subtract','take','takes','subtracts','eats','loses','loose','paid']
subtractions_=['minus']
subtractions__=['-']

multiplications=['times','multiplied','multiplies']
multiplications_=['times']
multiplications__=['x']

divisions=['split','divided','divides']
divisions_=['divided by']
divisions__=['/']

possess=['has','of','his','her','their','our','my','your']

equal=['equals']
equal__=['=']

AA1='when'
AA2='how much'
AA3='what time is'
AA4='how long did it take'
AA5='how long was'
AA6='what is the length of'
AA7='what is the width of'
Baa='what is the area of the'
bacch='what is the volume of the'

circ='circle'
squ='square'
rekt='rectangle'
tri='triangle'

sattup1=False
sattup2=False
sattup3=False
sattup4=False
sattup5=False

bad=False
rond=False
cube=False
rectpyramid=False
tripyramid=False

awea=False
awea1=False
awea0=False

regg='regular'

bade='base'
spher='sphere'
radii='radius'
spheer='ball'
cuba='cube'
idunno='box'
egypt='triangular pyramid'
trueegypt='rectangular pyramid'
longbox='rectangular prism'

if num >0 and num <=10:
    print("\nOk. Lets split your problem into statements:")
    for x in sentrange:
        wordd=sentences[x].split()
        inte_=[x for x in wordd if x.isdigit()]
        num_of_ints=len(inte_)#for storage
        rangeinte=list(range(0,num_of_ints))
        intess=int(num_of_ints)
        for x in rangeinte:
            inte=inte_[x]
        list2 = [item for item in wordd if item not in inte] #DESTROY THE INTEGERS!

        problem___=" ".join(list2)#ESTA UN PROBLEMA?
        print(problem___)
        if intess<1 or dci < 1:
            if donfail>=1:
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
                elif AA6 in problem___:
                    questionhi=True
                    
                elif AA7 in problem___:
                    questionhi=True
                    if
                elif Baa in problem___:
                    questionhi=True
                    if
                elif Bacch in problem___:
                    questionhi=True
                    awea=True
                else:
                    questionhi=False
            else:
                questionhi=False
        else:
            questionhi=False #NAH

        if questionhi==True:
            if sattup1 == True:
                print("It is asking when the {0} is.")
            elif sattup2 == True:
                print("It is asking how much the {0} costs.")
            elif sattup3 == True:
                print("It is asking what time it is.")
            elif sattup4 == True:
                print("It is asking how long the {0} was.")
            elif sattup5 == True:
                print("It is asking for the length of the.")
            elif awea0==True:
                print("It is asking what the length of the {0} is.")
            elif awea1=True:
                print("It is asking what the width of the {0} is.")
            elif awea=True:
                print("It is asking for the volume of the {0}.")

        elif questionhi==False:
            print("\nThis is a statement saying...")