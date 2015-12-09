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

folater=problem.count('$')
problem_=''.join( c for c in problem if  c not in '$')

deci=re.findall("\d+.\d+", problem_) #find decimals
len_dec=len(deci)
dci=int(len_dec)
word_=problem_.split()
list0 = [item for item in word_ if item not in deci] #DESTROY THE DECIMALS!

problem__=" ".join(list0)

sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split into sentences!

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
additions_='plus'
additions__='+'

subtractions=['spent','removed','removes','subtracted','minus','subtract','take','takes','subtracts','eats','loses','loose','paid']
subtractions_='minus'
subtractions__='-'

multiplications=['times','multiplied','multiplies']
multiplications_='times'
multiplications__='x'

divisions=['split','divided','divides']
divisions_='divided by'
divisions__='/'

possess=['has','of','his','her','their','our','my','your']

equal=['equals']
equal__='='

AA1='when'
AA2='how much'
AA3='what time'
AA4='how long did it take'
AA5='how long was the'
AA6='what is the length of the'
AA7='what is the width of the'
Baa='what is the area of the'
bacch='what is the volume of the'
werd='how wide'
heght='what is the height of the'
tallness='how tall'

circ='circle'
squ='square'
rekt='rectangle'
tri='triangle'

sattup1=False
sattup2=False
sattup3=False
sattup4=False
sattup5=False
heigh=False
heighe=False

bad=False
rond=False
cube=False
rectpyramid=False
tripyramid=False

awea=False
awea2=False
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
teim="o'clock"
tim='am'
ti='pm'
monet='dollar'

if num >0 and num <=10:
    print("\nOk. Lets split your problem into statements:")
    for x in sentrange:
        wordd=sentences[x].split()
        inte_=[x for x in wordd if x.isdigit()]
        num_of_ints=len(inte_)#for storage
        rangeinte=list(range(0,num_of_ints))
        intess=int(num_of_ints)
        if num_of_ints>0:
            for x in rangeinte:
                list2 = [item for item in wordd if item not in inte_] #DESTROY THE INTEGERS!
        else:
            list2=wordd

        problem___=" ".join(list2)#ESTA UN PROBLEMA?
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
                    sattup6=True
                elif AA7 in problem___:
                    questionhi=True
                    awea0=True
                elif Baa in problem___:
                    questionhi=True
                    awea2=True
                elif bacch in problem___:
                    questionhi=True
                    awea=True
                elif werd in problem___:
                    questionhi=True
                    widet=True
                elif heght in problem___:
                    heigh=True
                    questionhi=True
                elif tallness in problem___:
                    heighe=True
                    questionhi=True
                else:
                    questionhi=False
            else:
                questionhi=False
        else:
            questionhi=False #NAH

        if questionhi==True:
            print("\nThis statement is saying...")
            if sattup1:
                print("\nIt is asking when the {0} is.")
            elif sattup2:
                print("\nIt is asking how much the {0} costs.")
            elif sattup3:
                print("\nIt is asking what time it is.")
            elif sattup4:
                print("\nIt is asking how long the {0} was.")
            elif sattup5:
                print("\nIt is asking for the length of the {0} is.")
            elif awea0:
                print("\nIt is asking what the width of the {0} is.")
            elif sattup6:
                print("\nIt is asking what the length of the {0} is.")
            elif widet:
                print("\nIt is asking for the width of the {0}")
            elif awea2:
                print("\nIt is asking what the area of the {0} is.")
            elif awea:
                print("\nIt is asking for the volume of the {0}.")
            elif heigh:
                print("\nIt is asking for the hieght of the {0}")
            elif heighe:
                print("\nIt is asking for the hieght of the {0}")

        else:
            print("\nThis sentence is saying...")
            if sattup1:
                if teim in problem___:
                    
                elif tim in problem___:
                    
                elif ti in problem___:
                    
            elif sattup2:
                if folater > 0:
                    unit='dollar(s)'
                if monet in problem___:
                    unit='dollars(s)'