import stemming
a="Hari created a new module for nlp"
b = a.split()
j = 0
for i in b:
    if i in ("VBD","VBN"):
       b[j] = stemming.past_ex(a)
    j += 1
print("Did ", end='')
for i in b:
    print(i+" ", end = '')
print("?")

