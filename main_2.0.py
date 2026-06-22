from tkinter import *
from random import choice
w=0
l=0
def reset_game():
       global w,l
       w=0
       l=0   
       lable4['text']=f'SCORE : {w} - {l}' 
       lable3['text']=f''
       lable2['fg']='#fff95b'
       lable2['text']= "LET'S START"       
def game(choicee):
      computer= choice([1, 0, -1])
      code={"snake":1,"gun":0,"water":-1}
      comselect={1:"snake",0:"gun",-1:"water"}
      you=code[choicee]
      if   you==computer:
            x='draw'
            lable2['fg']='#f9bc2c'
            lable2['text']= x
      elif((you==1 and computer==0) or (you==0 and computer==-1) or (you==-1 and computer==1)):
            x="you lose"
            lable2['fg']='red'
            lable2['text']= x
            global l
            l+=1
      elif((you==1 and computer==-1) or (you==0 and computer==1) or (you==-1 and computer==0)):
              x='you win'
              lable2['fg']='#2feaa8'
              lable2['text']= x
              global w
              w+=1
      lable3['text']=f' (Computer){comselect[computer]} Vs {choicee}'
      lable4['text']=f'SCORE : {w} - {l}'
            
    


win=Tk()
win.title('Snake_water_gun')

lable=Label(win,text='Snake-water-gun'
            ,font=("impact",40,'underline')
            ,fg='#fff95b',
            bg="#0F1D48")
lable.pack()
win.config(bg='#0F1D48')
win.geometry('600x600')
lable2=Label(win,text="LET'S START"
            ,font=('Comic Sans MS',20,'italic')
            ,fg='#fff95b',
            bg="#0F1D48")
icon=PhotoImage(file='logo.png.png')
win.iconphoto(True,icon)
lable2.pack(pady=40)

sbutton=Button(win,text='Snake',font=("Courier New",15,'bold'),bg='#fffbaf'
               ,activebackground='#fffbaf',
               fg='#145277',command=lambda:game('snake'))
sbutton.place(x=160,y=300)
wbutton=Button(win,text='water',font=("Courier New",15,'bold'),bg='#fffbaf'
               ,activebackground='#fffbaf',
               fg='#145277', command=lambda: game('water'))
wbutton.place(x=260,y=300)
gbutton=Button(win,text='gun',font=("Courier New",15,'bold'),bg='#fffbaf'
               ,activebackground='#fffbaf',
               fg='#145277',command=lambda: game('gun'))
gbutton.place(x=360,y=300)
lable3=Label(win,text=''
                     ,bg='#0F1D48',fg='#eed991'
                     ,font=('Comic Sans MS',20,'italic'))
lable3.pack(pady=50)
lable4=Label(win,text=f'SCORE : {w} - {l}'
                     ,bg='#0F1D48',fg='#eed991'
                     ,font=('Comic Sans MS',20,'bold'))
lable4.place(x=150,y=390)
reset=Button(win,text='RESET',font=("Calibri",15,'bold'),bg='#f9e7bb',command=reset_game) 
reset.place(x=200,y=450)


win.mainloop()