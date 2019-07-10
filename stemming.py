import re

def gerund(string):
     a = []
     str = string
     tmp = re.findall(r'[a-z]*ing\s',str)
     print(tmp)
     for word in tmp:
         j = 0
         for letter in word:
           try:
             if word[j] == word[j+1]:
                 a.append(re.findall(r'[a-z].*',word[0:(j+1)]))
             j += 1
           except:
             j =0

     return a         

def present_ex(string):
     a = []
     str = string
     tmp = re.findall(r'[a-z]*ing',str)
     for word in tmp:
         j =0
         inc = 0
         for letter in word:
             try:
                 if word[j] in ("a","e","i","o","u"):
                     inc += 1
                     if ((inc == 2) and (word[j+1] in ("n","N"))):
                         a.append(re.findall(r'[a-z].*',word[0:j]))
                 j += 1
             except:
                j = 0
     return a


def past_ex(i):
     str = i
     tmp = re.findall(r'[a-z]*ed',str)
     for word in tmp:
         j =0
         inc = 0
         for letter in word:
             try:
                 if word[j] == "e" and word[j+1] == "d":
                      return word[0:j]
                 j += 1
             except:
                j = 0

##def present(string):
##     str= string
##     tmp =re.findall(''
     


                     
