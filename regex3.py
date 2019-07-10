import re
import os
from nltk.tag import StanfordPOSTagger
#st = " "
st = input()
a= re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s",st)
b = []
k = 0
l = 0

jar=r'C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-postagger-2017-06-09\stanford-postagger.jar'
model=r'C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-postagger-2017-06-09\models\english-bidirectional-distsim.tagger'
os.environ['JAVAHOME']=r"C:\Program Files\Java\jdk-9\bin\java.exe"

pos_tagger =StanfordPOSTagger(model,jar,encoding='utf8')

#text = pos_tagger.tag(word_tokenize("I am going to school"))
inc =0
new = []

for i in a:
    #print(i)
    length = 0
    b = []
    b =i.split()
    length = len(b)
    p = []
    p = pos_tagger.tag(b)
    k = 0
    nnp = 0
    prp = 0
    con = 0
    num = 0
    dt = 0
    for j in p: 
        #print(p[k][1])
        if p[k][1] in ("NNP","NN","NNS","NNPS"):
            nnp += 1
        elif p[k][1] in ("PRP","PRP$"):
            prp += 1
        elif p[k][1] == "IN":
             con += 1
        elif p[k][1] == "CD":
            num += 1
        elif p[k][1] == "DT":
            dt += 1
        k += 1
        

    #print("length "+ str(length),"nnp "+ str(nnp),"prp "+str(prp),"con "+ str(con),"cd "+str(num))
    if length >= 4:
        #if dt <= 2:
            if (con >= 1) or (nnp >=4) or (num >=1):
                inc += 1
                new.append(i)
                print(inc,i)
    
inc  = 0
number = 0
#print(new)
for i in new:
       g =i.split()
       ind =0
       j = 0
       inc =0
       c = pos_tagger.tag(g)
       #print(c)
       for k in c:
          if inc == 0:
              
             if c[j][1] in ("NNP","NNPS"):
                 inc += 1
                 g[ind] ="who"
             elif c[j][1] == "DT":
                 g[ind] =""
             elif c[j][1] in ("NN","NNS"):
                 inc += 1
                 g[ind] ="which"
             elif c[j][1] == "CC":
                 inc += 1
                 g[ind] ="why"
             elif c[j][1] == "RB":
                 inc += 1
                 g[ind] =""
             elif c[j][1] == "UH":
                 inc += 1
                 g[ind] =""
             j += 1
             ind += 1
       number += 1
       print(str(number)+" ", end ='')
       for it in g:
           print(it+" ",end = '')
       print("?")     





