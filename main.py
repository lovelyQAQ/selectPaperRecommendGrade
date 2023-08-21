# _*_coding : UTF-8 _*_
# 开发团队 : 虚无科技
# 开发人员 : mss
# 开发时间 : 2023/8/18 16:57
# 文件名称 : main.PY
# 开发工具 : PyCharm
import pyperclip
import tkinter as tk
import pyautogui
import time
import numpy as np
from PIL import Image, ImageTk


def loadPaperData():
    # 读取csv数据集
    paper_data = np.genfromtxt('paper.csv', delimiter=',', dtype=str, encoding='utf-8')
    paper_data_index_x = list(paper_data[:, 0])
    paper_data_index_y = list(paper_data[:, 1])
    paper_data_context = list(paper_data)

    data1 = dict(zip(paper_data_index_x, paper_data_context))
    data2 = dict(zip(paper_data_index_y, paper_data_context))
    data1.update(data2)
    return data1


def main():

    # 加载数据
    paper_data = loadPaperData()
    title = ['简称', '全称', '级别', '类型', '出版社']

    def selectPaper():
        context = '未查询到!'
        index = entry.get()

        if index in paper_data:
            context = paper_data[index]

        tree.item('I001', values=(title[0], context[0]))
        tree.item('I002', values=(title[1], context[1]))
        tree.item('I003', values=(title[2], context[2]))
        tree.item('I004', values=(title[3], context[3]))
        tree.item('I005', values=(title[4], context[4]))

    def copy_clipboard():
        # 加载剪贴板并查询
        content = pyperclip.paste()
        entry.delete(0, tk.END)
        entry.insert(0, content)
        context = '未查询到!'
        index = content

        if index in paper_data:
            context = paper_data[index]
        tree.item('I001', values=(title[0], context[0]))
        tree.item('I002', values=(title[1], context[1]))
        tree.item('I003', values=(title[2], context[2]))
        tree.item('I004', values=(title[3], context[3]))
        tree.item('I005', values=(title[4], context[4]))

    # 创建一个窗口，并设置其大小和背景色
    root = tk.Tk()
    root.geometry('850x400')
    root.resizable(width=False, height=False)
    root.iconbitmap('./image/t.ico')
    root.bg = "white"
    root.title('Paper推荐等级查询')
    photo = ImageTk.PhotoImage(Image.open("./image/yl.jpg").resize((216, 384)))

    root.geometry("+374+182")

    s = tk.ttk.Style()
    s.configure('Treeview', rowheight=30)
    # (1)创建 Treeview 控件
    tree = tk.ttk.Treeview(root, height=5, selectmode="none", style='Treeview')
    tree.grid(row=0, rowspan=6, columnspan=3, padx=3)

    # (2)定义列名
    tree["columns"] = ("NAME", "CONTENT")
    # (3)设置列的标题名称
    tree.heading("#0", text="*")
    tree.heading("NAME", text="NAME")
    tree.heading("CONTENT", text="CONTENT")

    # (4)设置列宽度(像素)
    tree.column("#0", width=50, anchor="center")
    tree.column("NAME", width=70, anchor="center")
    tree.column("CONTENT", width=500, anchor="center")
    tree.insert("", tk.END, text='*', values=('简称'))
    tree.insert("", tk.END, text='*', values=('全称'))
    tree.insert("", tk.END, text='*', values=('级别'))
    tree.insert("", tk.END, text='*', values=('类型'))
    tree.insert("", tk.END, text='*', values=('出版社'))

    # 添加输入框
    entry = tk.Entry(root, font=("宋体", 25), fg="red")
    entry.configure(bg="light gray", borderwidth=4, font=("Arial", 16))
    entry.grid(row=0, column=0, padx='4px', pady='5px')

    # 添加点击按钮
    button = tk.Button(root, text="查询", fg="green", command=selectPaper)
    button.configure(bg="white", font=("Arial", 10), width=5, height=1)
    button.grid(row=0, column=1)

    # 添加点击按钮
    button_c = tk.Button(root, text="剪贴板", fg="green", command=copy_clipboard)
    button_c.configure(bg="white", font=("Arial", 10), width=5, height=1)
    button_c.grid(row=0, column=2)
    # # 在窗口中添加一个标签，用于显示文本
    #
    # label = tk.Label(root, text='', font=("黑体", 14), fg="black", wraplength=300)
    # label.grid(row=1, column=0, columnspan=2)

    l1 = tk.Label(root, image=photo)
    l1.grid(row=0, column=4, rowspan=4)

    # 永远置顶
    # root.attributes('-topmost', 1)
    # 进入事件循环，等待用户操作窗口
    root.mainloop()


if __name__ == '__main__':
    main()
