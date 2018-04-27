import tkinter

base = tkinter.Tk()

#标题
base.wm_title("标签测试")

lb1 = tkinter.Label(base, text = "Python")
#给相应组件指定布局
lb1.pack()

lb2 = tkinter.Label(base, text = "绿色背景", background = "green")
lb2.pack()

lb3 = tkinter.Label(base, text = "蓝色背景", background = "blue")
lb3.pack()

base.mainloop()