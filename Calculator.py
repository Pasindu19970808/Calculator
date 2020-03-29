import tkinter

root = tkinter.Tk()
root.title('Calculator')

e = tkinter.Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4,padx = 10,pady = 10)

global numlist
global operationlist

numlist = [None,None]
operationlist = []

def button_add():
    current = float(e.get())
    operationlist.append('+')
    if (numlist[0] is None) and (numlist[1] is None):
        numlist[0] = current
        e.delete(0,'end')
    elif (numlist[0] is not None) and (numlist[1] is None):
        numlist[1] = current
        e.delete(0,'end')
    
def button_minus():
    current = float(e.get())
    operationlist.append('-')
    if (numlist[0] is None) and (numlist[1] is None):
        numlist[0] = current
        e.delete(0,'end')
    elif (numlist[0] is not None) and (numlist[1] is None):
        numlist[1] = current
        e.delete(0,'end')   
        
def button_multiply():
    current = float(e.get())
    operationlist.append('*')
    if (numlist[0] is None) and (numlist[1] is None):
        numlist[0] = current
        e.delete(0,'end')
    elif (numlist[0] is not None) and (numlist[1] is None):
        numlist[1] = current
        e.delete(0,'end')

def button_divide():
    current = float(e.get())
    operationlist.append('/')
    if (numlist[0] is None) and (numlist[1] is None):
        numlist[0] = current
        e.delete(0,'end')
    elif (numlist[0] is not None) and (numlist[1] is None):
        numlist[1] = current
        e.delete(0,'end')
    
    
def button_equal():
    second = float(e.get())
    numlist[1] = second
    if operationlist[-1] == '+':
        numlist[0] = float(numlist[1]) + float(numlist[0])
        numlist[1] = None
    elif operationlist[-1] == '-':
        numlist[0] = float(numlist[0]) - float(numlist[1])
        numlist[1] = None
    elif operationlist[-1] == '*':
        numlist[0] = float(numlist[1]) * float(numlist[0])
        numlist[1] = None
    elif operationlist[-1] == '/':
        numlist[0] = float(numlist[0]) / float(numlist[1])
        numlist[1] = None
    e.delete(0,'end')
    e.insert('end',str(numlist[0]))
 
def clear():
    numlist[0] = None
    numlist[1] = None
    operationlist[:] = []
    e.delete(0,'end')
   

def one():
    e.insert('end',1)
def two():
    e.insert('end',2)
def three():
    e.insert('end',3)
def four():
    e.insert('end',4)
def five():
    e.insert('end',5)
def six():
    e.insert('end',6)
def seven():
    e.insert('end',7)
def eight():
    e.insert('end',8)
def nine():
    e.insert('end',9)
def zero():
    e.insert('end',0)

    
#in tkinter you dont specify  a function using paranthesis. However to enable that we use lambda   
#operator buttons
button1 = tkinter.Button(root, text = "+",padx = 19, pady = 25, command = lambda: button_add())
button2 = tkinter.Button(root, text = "-",padx = 20, pady = 25, command = lambda: button_minus())
button3 = tkinter.Button(root, text = "*",padx = 20, pady = 25, command = lambda: button_multiply())
button4 = tkinter.Button(root, text = "/",padx = 20, pady = 25, command = lambda: button_divide())
button15 = tkinter.Button(root, text = "Clear",padx = 10 , pady = 25, command = clear)
button16 = tkinter.Button(root, text = "=",padx = 19,pady = 25, command = lambda: button_equal())
#number buttons
button5 = tkinter.Button(root, text = "1",padx = 20, pady = 25,command = one)
button6 = tkinter.Button(root, text = "2",padx = 20, pady = 25,command = two)
button7 = tkinter.Button(root, text = "3",padx = 20, pady = 25,command = three)
button8 = tkinter.Button(root, text = "4",padx = 20, pady = 25,command = four)
button9 = tkinter.Button(root, text = "5",padx = 20, pady = 25,command = five)
button10 = tkinter.Button(root, text = "6",padx = 20, pady = 25,command = six)
button11 = tkinter.Button(root, text = "7",padx = 20, pady = 25,command = seven)
button12 = tkinter.Button(root, text = "8",padx = 20, pady = 25,command = eight)
button13 = tkinter.Button(root, text = "9",padx = 20, pady = 25,command = nine)
button14 = tkinter.Button(root, text = "0",padx = 20, pady = 25,command = zero)

button5.grid(row = 3, column = 0)
button6.grid(row = 3, column = 1)
button7.grid(row = 3, column = 2)
button8.grid(row = 2, column = 0)
button9.grid(row = 2, column = 1)
button10.grid(row = 2, column = 2)
button11.grid(row = 1, column = 0)
button12.grid(row = 1, column = 1)
button13.grid(row = 1, column = 2)
button14.grid(row = 4, column = 1)
button15.grid(row = 5, column = 1)
button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 2)
button3.grid(row = 1, column = 3)
button4.grid(row = 2, column = 3)
button16.grid(row = 3,column = 3)





root.mainloop()


    
    
    