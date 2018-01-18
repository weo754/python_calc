from tkinter import *

def onClick(key, display):
    if key != "=":
        display.insert(END, key)
        
    else:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(END, result)

root = Tk()
root.title("계산기")

btn_list = [['7', '8' , '9', '+'],
            ['4', '5' , '6', '-'],
            ['1', '2' , '3', '*'],
            ['C', '0' , '=', '/']]
row, column = 4, 4

textframe = Frame(root)
textframe.pack(side=TOP, padx=3, pady=3, fill=X)

btnframe = Frame(root)
btnframe.pack(side=BOTTOM, padx=5, pady=5, fill=X)

textbar = Entry(textframe, bd=3)
textbar.pack(fill=X, expand=True)

for r in range(0, row):
    for c in range(0, column):
        def cmd(x = btn_list[r][c]):
            onClick(x, textbar)
        
        btn = Button(btnframe, text=btn_list[r][c], width=6, command=cmd)
        btn.grid(row=r, column=c, padx=2, pady=2)

# 화면의 중앙에 오도록 배치
root.update_idletasks() # 창 정보를 update한다. 창의 size를 구하기 위해 이용.
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

size = tuple(map(int, root.geometry().split("+")[0].split('x')))
x = w/2 - size[0]/2
y = h/2 - size[1]/2

root.geometry("%dx%d+%d+%d" %(size+(x, y)))
root.mainloop()
