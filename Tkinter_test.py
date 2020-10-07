from tkinter import *


price = {'shrimp': 5000, 'chickin': 4500,
         'Bulgogi': 5500, 'cider': 1500,
         'coke': 1500, 'juice': 1500}
root = Tk()
root.title("노데리아 주문표")
root.geometry("220x220")
lab = Label(root, text='노데리아 주문표')
lab.grid(row=0, column=0, columnspan=2)
btn1 = Button(root, text="shrimp", command=lambda: add('shrimp'))
btn1.grid(row=1, column=0)
btn2 = Button(root, text="chicken", command=lambda: add('치킨'))
btn2.grid(row=2, column=0)
btn3 = Button(root, text="Bulgogi", command=lambda: add('불고기'))
btn3.grid(row=3, column=0)
btn4 = Button(root, text="cider", command=lambda: add('사이다'))
btn4.grid(row=1, column=1)
btn5 = Button(root, text="coke", command=lambda: add('콜라'))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="juice", command=lambda: add('주스'))
btn6.grid(row=3, column=1)
btn7 = Button(root, text="Clear", command='')
btn7.grid(row=4, column=0)
btn8 = Button(root, text="exit", command='')
btn8.grid(row=4, column=1)
txt = Text(root, width=30, height=5)
txt.grid(row=5, column=0, columnspan=2)
label = Label(root, text='합계 : ')
label.grid(row=6, column=0, columnspan=2)
root.mainloop()




root.mainloop()