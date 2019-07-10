import re
import os
import stemming
from nltk.tag import StanfordPOSTagger
from nltk.tag import StanfordNERTagger

st = input()
a= re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s",st)
b = []
k = 0
l = 0

jar=r'C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-postagger-2017-06-09\stanford-postagger.jar'
model=r'C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-postagger-2017-06-09\models\english-bidirectional-distsim.tagger'
os.environ['JAVAHOME']=r"C:\Program Files\Java\jdk-9\bin\java.exe"

classifier =r"C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-ner-2018-02-27\classifiers\english.all.3class.distsim.crf.ser.gz"
jar  = r"C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-ner-2018-02-27\stanford-ner.jar"


pos_tagger =StanfordPOSTagger(model,jar,encoding='utf8')
st = StanfordNERTagger(classifier,jar)

inc =0
new = []

## SELECTING IMPORTANT SENTENCE FORM THE PARAGRAPH

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
    if length  >= 4:
        if dt <= 2:
            if (con >= 1) or (nnp >=4) or (num >=1):
                inc += 1
                new.append(i)
                print(inc,i)


##FRAMING QUESTION FROM THE SUBJECT OF THE SENTENCE ----> type- I

                
inc  = 0
number = 0
#print(new)
for i in new:
       g =i.split()
       ind =0
       j = 0
       inc =0
       c = pos_tagger.tag(g)
       d = st.tag(g)
       #print(c)
       for k in c:
          if inc == 0:
             
             if c[j][1] == "DT":
                 g[ind] =""
                 
             if c[j][1] == "JJ":
                 inc += 1
                 #print(g[ind])
                 g.remove(g[ind])
                 #print(g[ind])
                 g.remove(g[ind])
                 g =["who"] + g
             elif c[j][1] == "NNS":
                 inc += 1
                 g.remove(g[ind])
                 g =["where"] + g
                 
             elif d[j][1] == "PERSON":
                 inc += 1
                 g.remove(g[ind])
                 g =["Who"] + g
             elif d[j][1] == "LOCATION":
                 inc += 1
                 g[ind] ="which"
             elif d[j][1] == "ORGANIZATION":
                 inc += 1
                 g.remove(g[ind])
                 g =["Which"] + g
             elif c[j][1] == "CC":
                 inc += 1
                 g.remove(g[ind])
                 g =["Why"] + g
             elif c[j][1] == "RB":
                 inc += 1
                 g.remove(g[ind])
             elif c[j][1] == "UH":
                 inc += 1
                 g.remove(g[ind])
             j += 1
             ind += 1
       number += 1
       print(str(number)+" ", end ='')
       for it in g:
           print(it+" ",end = '')
       print("?")


##TYPE TWO YES OR NO  -----> type -II
       check = 0
       chec  = 0
       b= i.split()
       j = 0
       for l in c:
             if check == 0:       
                if l[1] =="DT":
                    b[j] =""
                    check += 1
             if chec == 0 :
                if l[1] == "JJ":
                    b[j]=""
                    chec += 1
             if l[1] == "VBD":
                b[j] = stemming.past_ex(i)
                if b[j] is None:
                  b[j]=""
                print("Did ", end='')
                break
             elif l[1] in ("MD","VBZ"):
               tp   = b[j]
               b[j] = b[j-1]
               b[j-1] = tp  
             j += 1
       for l in b:
          print(l," ", end = '')
       print("?")


##TTPE THREE SPLITTING @ CONJUCTION ----> type - III
       
       b = i.split()
       j =0
       for l in c:
           if l[1] == "IN":
               #print(b[0:j])
               break
           j += 1
       print("Why ", end='')
       for l in b[0:j]:
           print(l+" ",end= '')
       print("?")
                

       


