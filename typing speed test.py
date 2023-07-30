from tkinter import *
import random
from time import time

global stime, etime, fspeed, inwords, errors


root=Tk()
root.title("TYPING SPEED TESTER")   #Title
root.geometry("950x800")

def getvals():
  etime=time()
  print(etime,stime)

  def speed(stime, etime, inprompt):
    time_delay= (etime-stime)/60
    a= len(inprompt)/5
    #calculating speed
    fspeed= a/time_delay
    tspeed=round(fspeed,2)

    labelfortimer=Label(root,text='Your speed (wpm):',font=('arial',20,'italic bold'),fg='red')
    labelfortimer.place(x=300,y=300)
    timercount=Label(root,text=tspeed,font=('arial',20,'italic bold'),fg='blue')
    timercount.place(x=300,y=350)
    return(fspeed)
   
 
  def error(prompt, inprompt):
    errors=0
    words=prompt.split()
    inwords=inprompt.split()
    #calculating errors
    for i in range(min(len(inwords), len(words))):
      try:
        if (words[i]!=inwords[i]):
          errors+=1
      except:
        errors+=1
    labelerror=Label(root,text='Total errors:',font=('arial',20,'italic bold'),fg='red')
    labelerror.place(x=300,y=400)
    errorcount=Label(root,text=errors,font=('arial',20,'italic bold'),fg='blue')
    errorcount.place(x=300,y=450)

    msg1=Label(root,text="The average typing speed for boys is 44 words per minute. \nThis is slightly faster than for girls, who clock in at 37 wpm.",font=('arial',13))
    msg1.place(x=250,y=600)

    msg2=Label(root,text="The average accuracy for a typist is around 92%,meaning they make 8 mistakes for every 100 words typed.\n The desired accuracy for professional typing positions is around 97% or higher.",font=('arial',13))
    msg2.place(x=100,y=650)

    #calculating accuracy
    correct_words=len(inprompt)-errors
    if len(inprompt)!=0:
      acc= (correct_words/len(inprompt))*100
    else:
      acc=0                #to avoid ZeroDivisionError

    labelacc=Label(root,text='Your accuracy:',font=('arial',20,'italic bold'),fg='red')
    labelacc.place(x=300,y=500)
    acount=Label(root,text=round(acc,2),font=('arial',20,'italic bold'),fg='blue')
    acount.place(x=300,y=550)
    percent=Label(root,text="%",font=('arial',20,'italic bold'),fg='blue')
    percent.place(x=385,y=550)


    return errors

  inprompt=uservalue.get()

  #to print output in console
  print("\n############################\n")
  print("Total time elapsed: ", etime-stime)
  print(f"Speed: {round(speed(stime,etime,inprompt),2)} wps (words per second)")
  print(f"Error: {round(error(prompt,inprompt),2)}")
  print("\n############################\n")


name=Label(text="Check your typing speed NOW!", bg="Yellow",font="Arial 30 bold", pady=30, padx=20)
name.grid()

sample_texts=["""Lorem Ipsum is simply dummy text of \nthe printing and typesetting industry.""",
"""Lorem Ipsum has been the industry's standard dummy \ntext ever since the 1500s""",
"""It has survived five centuries and the \nleap into electronic typesetting, remaining unchanged.""",
"""It was popularised in the 1960s with the release of \nLetraset sheets containing Lorem Ipsum passages.""",
  """It is said that a reader will be \ndistracted by the readable content of a page when looking at its layout.""",
"""The point of using Lorem Ipsum is that it has a more-or-less \nnormal distribution of letters.""",
"""Many desktop publishing packages and web page editors now use \nLorem Ipsum as their default model text.""",
"""Various versions have evolved over the years, sometimes by \naccident, sometimes on purpose.""",
"""All the Lorem Ipsum generators on the Internet tend to repeat \npredefined chunks as necessary.""",
"""It uses a dictionary of over 200 Latin words, combined with a \nhandful of model sentence structures."""]

prompt=random.choice(sample_texts)

text=Label(root, text=prompt, font="Arial 18 ", pady=10, padx=10)
text.grid()

htext=Label(root, text="(Type the above text)", font="Times_new_roman 10 ", pady=10, padx=10)
htext.grid()

uservalue=StringVar()
stime=time()

userentry=Entry(root, textvariable=uservalue, width=90, font="Times_new_roman 12 ")
userentry.grid(padx=10,pady=10)

Button(text="Submit", command=getvals).grid(row=8, column=4)

root.mainloop()
