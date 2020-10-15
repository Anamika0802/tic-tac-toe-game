from tkinter import *
import tkinter.messagebox
root = Tk()
root.iconbitmap('tic-tac-toe.ico')
root.title('tic tak toe')
root.resizable(False,False)
click = True
count =0
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()
xphoto = PhotoImage(file = 'x.png')
ophoto = PhotoImage(file = 'o.png')
def play():
    button1 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ffe6f0',textvariable = btn1,command =lambda:press(1,0,0))
    button1.grid(row =0,column =0)
    button2 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ffe6f0',textvariable = btn2,command =lambda:press(2,0,1))
    button2.grid(row =0,column =1)
    button3 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ffe6f0',textvariable = btn3,command =lambda:press(3,0,2))
    button3.grid(row =0,column =2)
    button4 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ffb3d1',textvariable = btn4,command =lambda:press(4,1,0))
    button4.grid(row =1,column =0)
    button5 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ffb3d1',textvariable = btn5,command =lambda:press(5,1,1))
    button5.grid(row =1,column =1)
    button6 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ffb3d1',textvariable = btn6,command =lambda:press(6,1,2))
    button6.grid(row =1,column =2)
    button7 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ff80b3',textvariable = btn7,command =lambda:press(7,2,0))
    button7.grid(row =2,column =0)
    button8 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ff80b3',textvariable = btn8,command =lambda:press(8,2,1))
    button8.grid(row =2,column =1)
    button9 = Button(root,height = 9,width =19, bd= .5,relief = 'ridge',bg ='#ff80b3',textvariable = btn9,command =lambda:press(9,2,2))
    button9.grid(row =2,column =2)
def press(num,r,c):
    global click,count
    if click == True:
        lablePhoto = Label(root,image =xphoto)
        lablePhoto.grid(row=r,column = c)
        if num == 1:
            btn1.set('x')
        elif num == 2:
            btn2.set('x')
        elif num == 3:
            btn3.set('x')
        elif num == 4:
            btn4.set('x')
        elif num == 5:
            btn5.set('x')
        elif num == 6:
            btn6.set('x')
        elif num == 7:
            btn7.set('x')
        elif num == 8:
            btn8.set('x')
        else:
            btn9.set('x')
        count+=1
        click = False
        checkWin()
    else:
        lablePhoto = Label(root,image =ophoto)
        lablePhoto.grid(row=r,column = c)
        if num == 1:
            btn1.set('o')
        elif num == 2:
            btn2.set('o')
        elif num == 3:
            btn3.set('o')
        elif num == 4:
            btn4.set('o')
        elif num == 5:
            btn5.set('o')
        elif num == 6:
            btn6.set('o')
        elif num == 7:
            btn7.set('o')
        elif num == 8:
            btn8.set('o')
        else:
            btn9.set('o')
        count+=1
        click = True
        checkWin()
def checkWin():
    global count,click
    if(btn1.get()=='x' and btn2.get()=='x' and btn3.get()=='x'or
       btn4.get()=='x' and btn5.get()=='x' and btn6.get()=='x'or
       btn7.get()=='x' and btn8.get()=='x' and btn9.get()=='x'or
       btn1.get()=='x' and btn4.get()=='x' and btn7.get()=='x'or
       btn2.get()=='x' and btn5.get()=='x' and btn8.get()=='x'or
       btn3.get()=='x' and btn6.get()=='x' and btn9.get()=='x'or
       btn1.get()=='x' and btn5.get()=='x' and btn9.get()=='x'or
       btn3.get()=='x' and btn5.get()=='x' and btn7.get()=='x'):
        tkinter.messagebox.showinfo("TIC TAC TOE",p1.get()+" Wins")
        click = True
        count =0
        clear()
        play()
    elif(btn1.get()=='o' and btn2.get()=='o' and btn3.get()=='o'or
       btn4.get()=='o' and btn5.get()=='o' and btn6.get()=='o'or
       btn7.get()=='o' and btn8.get()=='o' and btn9.get()=='o'or
       btn1.get()=='o' and btn4.get()=='o' and btn7.get()=='o'or
       btn2.get()=='o' and btn5.get()=='o' and btn8.get()=='o'or
       btn3.get()=='o' and btn6.get()=='o' and btn9.get()=='o'or
       btn1.get()=='o' and btn5.get()=='o' and btn9.get()=='o'or
       btn3.get()=='o' and btn5.get()=='o' and btn7.get()=='o'):
        tkinter.messagebox.showinfo("TIC TAC TOE",p2.get()+" Wins")
        count =0
        clear()
        play()
    elif(count==9):
        tkinter.messagebox.showinfo("TIC TAC TOE",'Tie Game')
        click = True
        count =0
        clear()
        play()
def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
def welcome():
    mast = Tk()
    mast.iconbitmap('tic-tac-toe.ico')
    mast.title('tic tak toe')
    global p1,p2
    def show_entry_fields():
        print("Player 1 name: %s\nPlayer 2 name: %s"%(p1.get(),p2.get()))
    Label(mast,text = "Player 1 name").grid(row =0)
    Label(mast,text = "Player 2 name").grid(row= 1)
    p1= Entry(mast)
    p2= Entry(mast)
    p1.grid(row=0,column = 1)
    p2.grid(row=1,column = 1)
    Button(mast, text = 'QUIT',command = root.quit).grid(row=3,column = 0,sticky = W, pady = 4)
    Button(mast, text = 'SHOW',command = show_entry_fields).grid(row=3,column = 1,sticky = W, pady = 4)
    mast.mainloop()
    play()
    root.mainloop()

welcome()
