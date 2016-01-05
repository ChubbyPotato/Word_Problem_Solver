"""
Name-Suhan Gui
Credit-Stack Overflow, Alexandru Munteanu
"""
import math
import re
####################################################
shhh=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")
problem=shhh.lower()
####################################################
donfail=problem.count('?')
while donfail==0:
    print("You forgot a question mark")
    break
####################################################
folater=problem.count('$')
problem_=''.join( c for c in problem if  c not in '$')
####################################################
deci=re.findall("\d+.\d+", problem_) #find decimals
len_dec=len(deci)
dci=int(len_dec) #i dunno wat dis is for
rangedci=list(range(dci)) #oh
word_=problem_.split()
list0 = [item for item in word_ if item not in deci] #DESTROY THE DECIMALS!
####################################################
problem__=" ".join(list0)
####################################################
sentences = re.split(' *[\.\?!][\'"\)\]]* *', problem__) #split into sentences!
####################################################
um=len(sentences)
num=um-1
sentrange=list(range(0,num))
####################################################
while num > 10:
    print("\nWord problem too long!")
    break
while um==0:
    print("You forgot a period somewhere")
    break
####################################################
additions=['plus','added','adds','add','gains','gained','gain','sum','produces','total','more','total?','and','altogether']
subtractions=['spent','removed','removes','subtracted','minus','subtract','take','takes','subtracts','eats','loses','loose','paid','give','gave','spends']
multiplications=['times','multiplied','multiplies']
divisions=['split','divided','divides','splits']
####################################################
AA2='how much'
Baa='what is the area of the'
bacch='what is the volume of the'
new='how many'
####################################################
circ='circle'
pie='pie'
squ='square'
rekt='rectangle'
tri='triangle'
####################################################
sattup2=False
amount=False
awea=False
awea2=False
####################################################
regg='regular'
####################################################
bade='base'
spher='sphere'
radii='radius'
spheer='ball'
cuba='cube'
idunno='box'
egypt='triangular pyramid'
trueegypt='rectangular pyramid'
longbox='rectangular prism'
side='side'
####################################################
monet='dollar'
####################################################
jhfdh=problem.split()
intbut=[x for x in jhfdh if x.isdigit()]
jeru=len(intbut)
jujer=list(range(jeru))
####################################################
if num >0 and num <=10:
    print("\nOk. Lets split your problem into statements:")
    for x in sentrange:
        wordd=sentences[x].split()
        inte_=[x for x in wordd if x.isdigit()]
####################################################
        num_of_ints=len(inte_)
        rangeinte=list(range(0,num_of_ints))
        intess=int(num_of_ints)
        if num_of_ints>0:
            for x in rangeinte:
                list2 = [item for item in wordd if item not in inte_] #DESTROY THE INTEGERS!
        else:
            list2=wordd
####################################################
        problem___=" ".join(list2)#ESTA UN PROBLEMA?
        if intess<1 or dci < 1:
            if donfail>=1:
                if AA2 in problem:
                    questionhi=True
                    sattup2=True
                elif Baa in problem___:
                    questionhi=True
                    awea2=True
                elif bacch in problem___:
                    questionhi=True
                    awea=True
                elif new in problem___:
                    questionhi=True
                    amount=True
                else:
                    questionhi=False
            else:
                questionhi=False
        else:
            questionhi=False #NAH
####################################################
        if questionhi==True:
            print("\n-Sentence {0} is asking...".format(x+1))
            if sattup2 == True or amount == True:
                if folater>0:
                    hai='dollars'
                else:
                    if jeru>0:
                        in1= intbut[0]
                        me= problem.split()
                        thing= me.index(in1)
                        je=thing+1
                        hai=me[je]
                    elif len_dec>0:
                        de1= deci[0]
                        me1= problem.split()
                        thing1= me1.index(de1)
                        je1=thing1+1
                        hai= me1[je1]
                    else:
                        print("No numbers")
                        break
####################################################
            if sattup2:
                print("\nhow much the {0} costs.".format(hai))
            elif awea2:
                if circ in problem___:
                    hai='circle'
                elif pie in problem___:
                    hai='circle'
                    print(True)
                elif rekt in problem___:
                    hai='rectangle'
                elif tri in problem___:
                    hai='triangle'
                elif squ in problem___:
                    hai='square'
                elif tri in problem___:
                    hai='triangle'
                print("\nfor the area of a {0}.".format(hai))
            elif awea:
                print("\nfor the volume of a {0}.".format(hai))
            elif amount:
                print("\nfor the number of {0}.".format(hai))

        else:
            print("\n-Sentence {0} is saying...".format(x+1))
#################################################### 
            sattup2i=False
            amounti=False
            aweai=False
            awea2i=False
####################################################
            if AA2 in problem:
                sattup2i=True
            elif Baa in problem:
                awea2i=True
            elif bacch in problem:
                aweai=True
            elif new in problem:
                amounti=True
####################################################
            if amounti or sattup2i:
                if intess>0:
                    int1= inte_[0]
                    meh= problem.split()
                    thingy= meh.index(int1)
                    jeh=thingy+1
                    waer=meh[jeh]
                    print("\nthat there are {0} {1}".format(int1,waer))
                elif len_dec>0:
                    dec1= deci[0]
                    meh1= problem.split()
                    thingy1= meh1.index(dec1)
                    jeh1=thingy1+1
                    waer1= meh1[jeh1]
                    print("\nthat there are {0} {1}".format(dec1,waer1))
                else:
                    print("No numbers")
####################################################
print("\nThe answer:")
####################################################
elsent1=sentences[1]
if num>=3:
    elsent2=sentences[2]
if num>=4:
    elsent3=sentences[3]
if num>=5:
    elsent4=sentences[4]
if num>=6:
    elsent5=sentences[5]
if num>=7:
    elsent6=sentences[6]
if num>=8:
    elsent7=sentences[7]
if num>=9:
    elsent8=sentences[8]
if num>=10:
    elsent9=sentences[9]
####################################################
list3= problem.split()
####################################################
if amount==True or sattup2==True:
    j=[item for item in list3 if item not in additions]
    je=[item for item in list3 if item not in subtractions]
    jef=[item for item in list3 if item not in multiplications]
    jeff=[item for item in list3 if item not in divisions]
####################################################

    j1=[item for item in elsent1 if item not in additions]
    je1=[item for item in elsent1 if item not in subtractions]
    jef1=[item for item in elsent1 if item not in multiplications]
    jeff1=[item for item in elsent1 if item not in divisions]
    if num>=3:
        j2=[item for item in elsent2 if item not in additions]
        je2=[item for item in elsent2 if item not in subtractions]
        jef2=[item for item in elsent2 if item not in multiplications]
        jeff2=[item for item in elsent2 if item not in divisions]
    if num>=4:
        j3=[item for item in elsent3 if item not in additions]
        je3=[item for item in elsent3 if item not in subtractions]
        jef3=[item for item in elsent3 if item not in multiplications]
        jeff3=[item for item in elsent3 if item not in divisions]
    if num>=5:
        j4=[item for item in elsent4 if item not in additions]
        je4=[item for item in elsent4 if item not in subtractions]
        jef4=[item for item in elsent4 if item not in multiplications]
        jeff4=[item for item in elsent4 if item not in divisions]
    if num>=6:
        j5=[item for item in elsent5 if item not in additions]
        je5=[item for item in elsent5 if item not in subtractions]
        jef5=[item for item in elsent5 if item not in multiplications]
        jeff5=[item for item in elsent5 if item not in divisions]
####################################################
    addonly=False
    subonly=False
    multonly=False
    divionly=False

    addsub=False
    addmult=False
    adddivi=False

    subadd=False
    submult=False
    subdivi=False
    
    multadd=False
    multsub=False
    multdivi=False
    
    diviadd=False
    divisub=False
    divimult=False
####################################################
    allist=intbut+deci
    check=len(allist)
####################################################
    if list3 != j:
        if list3==je:
            if list3==jef:
                if list3 ==jeff:
                    addonly=True
    if list3 != je:
        if list3==j:
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

####################################################
    if addonly:
        if check>4:
            print("Too many numbers!")
        else:
            if check>=1:
                un=allist[0]
                uno=float(un)
                total=uno
            if check>=2:
                do=allist[1]
                dos=float(do)
                total+=dos
            if check>=3:
                tre=allist[2]
                tres=float(tre)
                total+=tres
            if check==4:
                cuatr=allist[3]
                cuatro=float(cuatr)
                total+=cuatro
        print("There are: {0} {1}".format(total,hai))
    elif subonly:
        if check>4:
            print("Too many numbers!")
        else:
            if check>=1:
                un=allist[0]
                uno=float(un)
                total1=uno
            if check>=2:
                do=allist[1]
                dos=float(do)
                total1-=dos
            if check>=3:
                tre=allist[2]
                tres=float(tre)
                total1-=tres
            if check==4:
                cuatr=allist[3]
                cuatro=float(cuatr)
                total1-=cuatro
        print("There are: {0} {1}".format(total1,hai))
    elif multonly:
        if check>4:
            print("Too many numbers!")
        else:
            if check>=1:
                un=allist[0]
                uno=float(un)
                total=uno
            if check>=2:
                do=allist[1]
                dos=float(do)
                total=dos*total
            if check>=3:
                tre=allist[2]
                tres=float(tre)
                total=tres*total
            if check==4:
                cuatr=allist[3]
                cuatro=float(cuatr)
                total=cuatro*total
        print("There are: {0} {1}".format(total,hai))
    elif divionly:
        if check>4:
            print("Too many numbers!")
        else:
            if check>=1:
                un=allist[0]
                uno=float(un)
                total=uno
            if check>=2:
                do=allist[1]
                dos=float(do)
                total=total/dos
            if check>=3:
                tre=allist[2]
                tres=float(tre)
                total=total/tres
            if check==4:
                cuatr=allist[3]
                cuatro=float(cuatr)
                total=total/cuatro
    else:
        print("Too complicated")
####################################################
elif awea: #IST TEH VOLUME
    print(hai)
    if spheriical:
        are=4/3*3.14*radiu*radiu*radiu
    elif cubee:
        are=side*side*side
    elif cylinde:
        are=radiu*radiu*3.14*heightt
    elif prism:
        if basee:
            base=base
        else:
            if nsquare== True or nrekt==True:
                base=l*w
            elif ntri:
                base=0.5*base*heightt

    print("The volume of the {0} is {1} units cubed".format(hai,are))
####################################################
elif awea2: #ESTA TEH TRU AWEA
    print("The area of the {0} is {1} units squared")
####################################################
#FIN