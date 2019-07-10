from tkinter import *
from tkinter import font
from tkinter import filedialog
import tkinter as tk
import speech_recognition as sr
import os
root = Tk("text editor")


txt = Text(root,bg="white",font ="bold",fg ="black",spacing2="5")

def save():

    global txt

    t = txt.get("1.0", "end-1c")
    
    savelocation=filedialog.asksaveasfilename()

    file=open(savelocation, "w+")
    
    file.write(t)
    
    file.close()

def run1():
     import os
     print("hello")
     os.system('start "C:\Program Files (x86)\CodeBlocks\MinGW\bin\gcc.exe"')


def speach_to_text():
   r = sr.Recognizer()
   with sr.Microphone() as source:
              try:
                      print("Speak:")
                      audio = r.listen(source,timeout=None)
                      st = r.recognize_google(audio)
                      print("hello"+str)
              except:
                      print("error")
              
              var =st.split()
          #     print(var[0],var[1])
          #     if st in ("yeah"):
          #         st ="a"

                  
              l1=("declare integers","integers","variable decleration")
              if st in ("include studio","include io header"):
                 txt.insert(tk.END,"#include<stdio.h>\n")  
              elif st in ("int main","mamath return","main with written","main with return","mean with written","mean with the return","inter means","intervene"):
                 txt.insert(tk.END,"""int main()
   { \n""")
              elif st in ("main without return","main without written","mean without written","mean without return"):
                  txt.insert(tk.END,"""void main()
   {\n""")
              elif st in ("return","return with zero"):
                  txt.insert(tk.END,"return (0)")
              elif st in l1 :
                  txt.insert(tk.END,"int ")
              elif st in ("declare float","float variabes","float","floats"):
                  txt.insert(tk.END,"float ")
              elif st in ("declare characters","character variabes","characters","character"):
                  txt.insert(tk.END,"char ")
              
              elif st in ("end","semicolon"):
                  txt.insert(tk.END,";\n ")
              elif st in ("add a and b","add two variables","add"):
                  txt.insert(tk.END,"c =a+b;\n")
              elif st in ("close"):
                  txt.insert(tk.END,"}")
              elif st in ("comma","komaa","kumar","karma"):
                   txt.insert(tk.END,",")
              elif var[0] in ("print"):
                   txt.insert(tk.END,"""printf(" %d\n ","""+var[1]+");\n")
              elif st in ("equals"):
                   txt.insert(tk.END,"=")
              elif st in ("multiplication","star"):
                   txt.insert(tk.END,"*")     
              elif st in ("division","mod"):
                   txt.insert(tk.END,"/")
              elif st in ("save","shave"):
                   save()
              elif st in ("run","Run"):
                   run1()
              else:
                   print("not found")
                   #txt.insert(tk.END,st.lower())
    

def run():
     pass
##    import os
##    #t = txt.get("1.0", "end-1c")
##    
##    #savelocation=filedialog.asksaveasfilename()
##
##    #file=open(savelocation, "w+"
##    #file.write(t)
##    import subprocess
##    #subprocess.call(["C://Program Files//notepad++.exe","C://Users//Hari krishnaa//AppData//Local//Programs//Python//Python36-32//txt.py"])
##    os.system('start "C:\TDM-GCC-64\bin\gcc.exe"')
##    #file.close()
 #exec(open("./gcc.exe"))


              
#button=Button(root, text="Save", command=saveas)
helv36 = font.Font(family='Helvetica', size=25, weight='bold')
#button['font'] = helv36

b1=Button(root, text="Speak", command=speach_to_text,bg = "blue",font=helv36)
b2 =Button(root, text="run",command=run)

b1.grid()
b2.grid()
#button.grid()

scrl =tk.Scrollbar(root,command =txt.yview)

scrl.grid(row =0, column =1, sticky='nsew')
txt['yscrollcommand'] = scrl.set(0,0)


txt.grid()
root.mainloop()
