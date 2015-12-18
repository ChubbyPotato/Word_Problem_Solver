"""
Name-Suhan Gui
Credit-Stack Overflow, Alexandru Munteanu

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
rangedci=list(range(dci))
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
subtractions=['spent','removed','removes','subtracted','minus','subtract','take','takes','subtracts','eats','loses','loose','paid','give']
multiplications=['times','multiplied','multiplies']
divisions=['split','divided','divides']

possess=['has','of','his','her','their','our','my','your']

equal=['equals']

AA2='how much'
AA5='how long was the'
Baa='what is the area of the'
bacch='what is the volume of the'
heght='what is the height of'
mil='what is the length of'
tallness='how tall'
new='how many'
werd='what is the width of'

circ='circle'
squ='square'
rekt='rectangle'
tri='triangle'

sattup2=False
sattup5=False
heigh=False
heighe=False
amount=False

merican=False
individual=True
metric=False

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
monet='dollar'

jer='inch'
jerr='feet'
jerrr='meter'

jhfdh=problem.split()
intbut=[x for x in jhfdh if x.isdigit()]
jeru=len(intbut)

if num >0 and num <=10:
    print("\nOk. Lets split your problem into statements:")
    for x in sentrange:
        wordd=sentences[x].split()
        inte_=[x for x in wordd if x.isdigit()]

        num_of_ints=len(inte_)
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
                if AA2 in problem:
                    questionhi=True
                    sattup2=True
                elif AA5 in problem___:
                    questionhi=True
                    sattup5=True
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
                elif new in problem___:
                    questionhi=True
                    amount=True
                elif mil in problem___:
                    questionhi=True
                    sattup6=True
                else:
                    questionhi=False
            else:
                questionhi=False
        else:
            questionhi=False #NAH

        if questionhi==True:
            print("\n-Sentence {0} is asking...".format(x+1))
            if jeru>0:
                for y in rangeinte:
                    in1= inte_[y]
                    me= problem.split()
                    print(me)
                    thing= me.index(in1)
                    print(thing)
                    je=thingy+1
                    hai=meh[je]

            elif len_dec>0:
                for y in rangedci:
                    de1= deci[y]
                    me1= problem.split()
                    thing1= me1.index(de1)
                    je1=thingy1+1
                    hai= meh1[je1]
            else:
                print("No numbers")
                break
                        
            if sattup2:
                print("\nhow much the {0} costs.".format(hai))
            elif sattup5:
                print("\nfor the length of the {0} is.".format(hai))
            elif awea0:
                print("\nwhat the width of the {0} is.".format(hai))
            elif sattup6:
                print("\nwhat the length of the {0} is.".format(hai))
            elif widet:
                print("\nfor the width of the {0}.".format(hai))
            elif awea2:
                print("\nwhat the area of the {0} is.".format(hai))
            elif awea:
                print("\nfor the volume of the {0}.".format(hai))
            elif heigh:
                print("\nfor the hieght of the {0}.".format(hai))
            elif heighe:
                print("\nfor the hieght of the {0}.".format(hai))
            elif amount:
                print("\nfor the number of {0}.".format(hai))

        else:
            print("\n-Sentence {0} is saying...".format(x+1))
            if sattup2:
                if folater > 0:
                    unit='dollar(s)'
                if monet in problem___:
                    unit='dollars(s)'
            elif awea:
                volumeunit=True
                if jer in problem___:
                    merican=True
                elif jerr in problem___:
                    merican=True
                elif jerrr in problem___:
                    metric=True
            elif awea2:
                areaunit=True
                if jer in problem___:
                    merican=True
                elif jerr in problem___:
                    merican=True
                elif jerrr in problem___:
                    metric=True
                elif:
                    unit='square units'
            elif heght:
                lengthunit=True
                if jer in problem___:
                    merican=True
                elif jerr in problem___:
                    merican=True
                elif jerrr in problem___:
                    metric=True
            elif tallness:
                lengthunit=True
                if jer in problem___:
                    merican=True
                elif jerr in problem___:
                    merican=True
                elif jerrr in problem___:
                    metric=True
            elif tallness:
                lengthunit=True
                if jer in problem___:
                    merican=True
                elif jerr in problem___:
                    merican=True
                elif jerrr in problem___:
                    metric=True
            elif amount:
                individual=True
                
            sattup2i=False
            sattup5i=False
            heighi=False
            heighei=False
            amounti=False
            aweai=False
            awea2i=False
                
            if AA2 in problem:
                sattup2i=True
            elif AA5 in problem:
                sattup5i=True
            elif Baa in problem:
                awea2i=True
            elif bacch in problem:
                aweai=True
            elif werd in problem:
                wideti=True
            elif heght in problem:
                heighi=True
            elif tallness in problem:
                heighei=True
            elif new in problem:
                amounti=True
            elif mil in problem:
                sattup6i=True
                
            list3= problem___.split()
            
            if amounti:
                j=[item for item in list3 if item not in additions]
                je=[item for item in list3 if item not in subtractions]
                jef=[item for item in list3 if item not in multiplications]
                jeff=[item for item in list3 if item not in divisions]
                if intess>0:
                    for y in rangeinte:
                        int1= inte_[y]
                        meh= problem.split()
                        thingy= meh.index(int1)
                        jeh=thingy+1
                        waer=meh[jeh]
                        print("\nthat there are {0} {1}".format(int1,waer))

                elif len_dec>0:
                    for y in rangedci:
                        dec1= deci[y]
                        meh1= problem.split()
                        thingy1= meh1.index(dec1)
                        jeh1=thingy1+1
                        waer1= meh1[jeh1]
                        print("\nthat there are {0} {1}.".format(dec1,waer1))
                        
                else:
                    print("No numbers")

                if j!=list3:
                    for z in rangeinte:
                        j=inte_[z]
                elif je!=list3:
                    for z in rangeinte:
                        j=inte_[z]
                elif jef!=list3:
                    for z in rangeinte:
                        j=inte-[z]
                elif jeff!=list3:
                    for z in rangeinte:
                        j=inte-[z]
                else:
                    print("Too complicated")