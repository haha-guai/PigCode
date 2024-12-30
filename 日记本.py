from tkinter import*
import time
from random import choice
import os
from tkinter import messagebox

word = ''# 将文本内容暂存在该变量中
security_code = "天不生我李猪儿,剑道万古如长夜    飞天皮儿哥"
#写入时显示的密码文本来源

def no_input(event):
    return 'break'
# 限制密码文本框手动输入功能

def dir_make():
    time_sum = time.localtime()
    if not os.path.exists('日记Data/'):
        os.mkdir('日记Data/')
    if not os.path.exists(f'日记Data/{time_sum.tm_year}/'):
        os.mkdir(f'日记Data/{time_sum.tm_year}/')
    if not os.path.exists(f'日记Data/{time_sum.tm_year}/{time_sum.tm_mon}/'):
        os.mkdir(f'日记Data/{time_sum.tm_year}/{time_sum.tm_mon}/')
    # 总目录/年份/月份
#创建目录

def quit_ask():
    quit_choice = messagebox.askyesno(title='猪儿哥的温馨提示', message='是否退出\n请确保已保存文件')
    if quit_choice:
        root.destroy()
    else:
        pass
# 退出前询问

root = Tk()
root.geometry('600x700')
root.title('日记本')
root.protocol("WM_DELETE_WINDOW", quit_ask)# 退出前询问
# GUI基础设置

frame_write = Frame(root)
frame_write.place(x=0, y=0, width=600, height=700)
# 写入时显示页面

frame_read = Frame(root)
# 阅读时显示页面

read_text = Text(frame_read, font=('宋体', 15), bg='lightgreen')
# 阅读时显示的文本框

write_entry = Entry(frame_write, show=choice(security_code), font=('宋体', 15), bg='lightblue')
write_entry.place(x=0, y=500, width=600, height=50)
# 写入文本的输入密码框

write_text = Text(frame_write, font=('宋体', 15), bg='lightgreen')
write_text.bind('<Button-1>', no_input)# 绑定函数，使文本内容无法在写入界面被更改
write_text.place(width=600, height=450)
#写入时显示的密码文本框

def submit_button_use():
    global word
    entry_word = write_entry.get()# 输入框文本内容
    write_entry.delete(0, END)
    word += entry_word# 向文本实际内容添加输入框内容
    view_word = ''
    for i in range(0, len(word)):#  重置写入页显示内容
        char = choice(security_code)
        view_word += char
    write_text.delete(1.0, END)
    write_text.insert(1.0, view_word)
#提交输入框内的文本
    
submit_button = Button(frame_write, text="上传", font=('宋体', 15), command=submit_button_use)
submit_button.place(x=550, y=450, width=50, height=50)
#提交按钮

def save_button_use():
    save_time = time.localtime()
    str_time1 = f'{save_time.tm_year}/{save_time.tm_mon}/'
    str_time2 = f'{save_time.tm_mday}日{save_time.tm_hour}时{save_time.tm_min}分'
    #获取时间并定义格式化字符串
    dir_make()# 创建目录
    with open('日记Data/' + f'{str_time1}' + f"{str_time2}.txt", 'w', encoding='utf-8') as f:#将内容写入文件并添加时间
        f.write(word + f'\n{str_time1}')
    messagebox.showinfo(title='猪儿哥的温馨提示', message='保存成功\n@~@')
    #保存成功弹窗
# 保存文件

save_button1 = Button(frame_write, text="保存", font=('宋体', 15), command=save_button_use)
save_button1.place(x=450, y=450, width=50, height=50)
# 写入页保存按钮
save_button2 = Button(frame_read, text="保存", font=('宋体', 15), command=save_button_use)
# 阅读页保存按钮

def come_back():
    global word
    frame_read.place_forget()
    word = read_text.get(1.0, END).rstrip()# 更新word内容，保存阅读页的修改,清除尾部自带换行符
    frame_write.place(x=0, y=0, width=600, height=700)
    submit_button.place(x=550, y=450, width=50, height=50)
    write_text.place(width=600, height=450)
    write_entry.place(x=0, y=500, width=600, height=50)
    look_button.place(x=500, y=450, width=50, height=50)
    save_button1.place(x=450, y=450, width=50, height=50)
# 从阅读页返回

back_button = Button(frame_read, text="返回", font=('宋体', 15), command=come_back)
# 阅读页返回按钮

def look_button_use():
    frame_write.place_forget()
    read_text.delete(1.0, END)
    read_text.insert(1.0, word)# 将word中的内容显示到阅读页
    frame_read.place(x=0, y=0, width=600, height=700)
    read_text.place(width=600, height=650)
    back_button.place(x=550, y=650, width=50, height=50)
    save_button2.place(x=500, y=650, width=50, height=50)
    root.after(5000, come_back)# 5s自动返回
#切换到阅读界面

look_button = Button(frame_write, text="显示", font=('宋体', 15), command=look_button_use)
look_button.place(x=500, y=450, width=50, height=50)
# 显示按钮

root.mainloop()
'''
缺陷：
    换段落
    显示时间
    输入框显示修正
    UI美化
'''