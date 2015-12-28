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
    print("You forgot a period somewhere")
    break

additions=['plus','added','adds','add','gains','gained','gain','sum','produces','total','more','total?']
subtractions=['spent','removed','removes','subtracted','minus','subtract','take','takes','subtracts','eats','loses','loose','paid','give']
multiplications=['times','multiplied','multiplies']
divisions=['split','divided','divides']

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
jujer=list(range(jeru))

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
                for y in jujer:
                    in1= intbut[y]
                    me= problem.split()
                    thing= me.index(in1)
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
                print("\nfor the length of the {0} is".format(hai))
            elif awea0:
                print("\nwhat the width of the {0} is".format(hai))
            elif sattup6:
                print("\nwhat the length of the {0} is".format(hai))
            elif widet:
                print("\nfor the width of the {0}".format(hai))
            elif awea2:
                print("\nwhat the area of the {0} is".format(hai))
            elif awea:
                print("\nfor the volume of the {0}".format(hai))
            elif heigh:
                print("\nfor the hieght of the {0}".format(hai))
            elif heighe:
                print("\nfor the hieght of the {0}".format(hai))
            elif amount:
                print("\nfor the number of {0}".format(hai))

        else:
            print("\n-Sentence {0} is saying...".format(x+1))
                
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
            
            if amounti:
                if intess>0:
                    int1= inte_[x]
                    meh= problem.split()
                    thingy= meh.index(int1)
                    jeh=thingy+1
                    waer=meh[jeh]
                    print("\nthat there are {0} {1}".format(int1,waer))

                elif len_dec>0:
                    dec1= deci[x]
                    meh1= problem.split()
                    thingy1= meh1.index(dec1)
                    jeh1=thingy1+1
                    waer1= meh1[jeh1]
                    print("\nthat there are {0} {1}".format(dec1,waer1))
                        
                else:
                    print("No numbers")

print("\nThe answer:")
list3= problem.split()
if amounti:
    j=[item for item in list3 if item not in additions]
    je=[item for item in list3 if item not in subtractions]
    jef=[item for item in list3 if item not in multiplications]
    jeff=[item for item in list3 if item not in divisions]
    
    addonly=False
    
    if list3 != j:
        if list3==je:
            if list3==jef:
                if list3 ==jeff:
                    addonly=True
                    
    if list3 != je:
        if list3==je:
            if list3==jef:
                if list3 ==jeff:
                    subonly=True
    
    if list3 != jef:
        if list3==j:
            if list3==je:
                if list3 ==jeff:
                    multonly=True
    
    if list3 != jeff:
        if list3==j:
            if list3==je:
                if list3 ==jef:
                    divionly=True
    
    if addonly:
        if jeru>=1:
            do=intbut[0]
            dos=int(do)
            total=dos
        if jeru>=2:
            tre=intbut[1]
            tres=int(tre)
            total+=tres
            to1=True
        if jeru>=3:
            cuatr=intbut[2]
            cuatro=int(cuatr)
            total+=cuatro
        if jeru>=4:
            cinc=intbut[3]
            cinco=int(cinc)
            total+=cinco
        if jeru==5:
            sei=intbut[4]
            seis=int(sei)
            total+=seis
        if jeru>5:
            print("Too many")
        
        if 

    elif subonly:
        for z in rangeinte:
            j=inte_[z]
    elif multonly:
        for z in rangeinte:
            j=inte-[z]
    elif jeff!=list3:
        for z in rangeinte:
            j=inte-[z]
    else:
        print("Too complicated")