
##from nltk.tag import StanfordNERTagger
##from nltk.tokenize import word_tokenize
##
##jar=r'C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-postagger-2017-06-09\stanford-postagger.jar'
##model=r'C:\Users\Hari krishnaa\AppData\Local\Programs\Python\Python36-32\stanford-postagger-2017-06-09\models\english-bidirectional-distsim.tagger'
##os.environ['JAVAHOME']=r"C:\Program Files\Java\jdk-9\bin\java.exe"
##
##st = StanfordNERTagger(model,jar,encoding='utf-8')
##
##text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
##
##tokenized_text = word_tokenize(text)
##classified_text = st.tag(tokenized_text)
##
##print(classified_text)


import ner
tagger = ner.HttpNER(host='localhost', port=8080)
st = tagger.get_entities("University of California is located in California, United States")
print(st)
                        
