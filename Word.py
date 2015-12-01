"""
Name-Suhan Gui
Credit-Stack Overflow, Alexandru Munteanu

Jane spent $42 for shoes.  This was $14 less than twice what she spent for a blouse.  How much was the blouse?
"""
import math
import re
#import enchant

problem=input("What is your mathematical word problem? (Spelling, grammar, and punctuation count!!)\n\nYour problem: ")

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
sentrange=list(range(0,num))

while num > 10:
    print("\nWord problem too long!")
    break

while um==0:
    print("You forgot a period somewhere pal")
    break

additions=['plus','added','adds','add','gains','gained','gain','sum','produces']
additions_=['plus']
additions__=['+']

subtractions=['spent','removed','removes','subtracted','minus','subtract','take','takes','subtracts','eats']
subtractions_=['minus']
subtractions__=['-']

multiplications=['times','multiplied','multiplies']
multiplications_=['times']
multiplications__=['x']

divisions=['split','divided','divides']
divisions_=['divided by']
divisions__=['/']

equal=['is equal to']
equal__=['=']

los_questions=['When','when','how much','How much','What time','what time','how long did it take','How long did it take','How long was','how long was']

if num >0 and num <=10:
    print("\nOk. Lets split your problem into statements:")
    for x in sentrange:
        wordd=sentences[x].split()
        #inte=[int(s) for s in wordd.split() if s.isdigit()]
        inte=4
        rangeinte=list(range(inte))
        inte_=str(inte)
        num_of_ints=len(inte_) #for storage
        list2 = [item for item in wordd if item not in inte_] #DESTROY THE INTEGERS!
    
        if num_of_ints==0:
            if len_dec==0:
                if donfail==1:
                    satup=[i for i in list2 if i in los_questions]
                    sattup=len(satup)
                    if sattup>=1:
                        questionhi=True
                    else:
                        questionhi=False
                else:
                    questionhi=False
            else:
                questionhi=False
        else:
            questionhi=False

        if questionhi==True:
            confirmyes=input("Sentence {0} is a question, right? y to confirm. n is reject")
            confirmyes.lower()
            if confirmyes=="y":
                print("This sentence is a question")
                if satup=='when' or satup=="When":
                    print("This question is asking when it is")
                    
                elif satup=="how much" or satup=="How much":
                    print("This is asking how much the  is")
                elif satup=="what time" or satup=="What time":
                    print("This is asking what time it is")
                elif satup=="How long" or satup=="how long":
                    print("This is asking how long the  is")    #REMEMBER TO ENTER THE VARIABLE M8 
                
                else:
                    print("This is not a question mate")
                    questionhi=False
            elif confirmyes=="n":
                questionhi=False

        elif questionhi==False:
            print("")