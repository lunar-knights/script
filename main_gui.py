from tkinter import *
import src.add_food as add_food
import src.add_times as add_times


def af():
    text.delete(0.0, END)
    try:
        text.insert(INSERT, add_food.add_food())
    except Exception:
        text.insert(INSERT, "连接或者参数异常!")


def at():
    text.delete(0.0, END)
    try:
        text.insert(INSERT, add_times.add_times())
    except Exception:
        text.insert(INSERT, "连接或者参数异常!")


root = Tk()

root.title("这UI简直就是在搞笑 v2.3.3.3")

theLabel = Label(root, text="就是来搞笑的！")
theLabel.grid(row=0, column=1)

Button(root, text="填写饭票", width=10, command=af).grid(
    row=1, column=0, padx=10, pady=5)
Button(root, text="填写工时", width=10, command=at).grid(
    row=1, column=1, padx=10, pady=5)
Button(root, text="撤！", width=10, command=root.quit).grid(
    row=1, column=2, padx=10, pady=5)

text = Text(root, width=60, height=3)
text.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
