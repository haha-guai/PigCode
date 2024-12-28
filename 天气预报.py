import requests
import re
from tkinter import *

root = Tk()
root.title("天气查询")
root.geometry("700x400")

label1 = Label(root, text="天气情况获取中\n......\n\n请稍等", font=("宋体", 30))
label1.place(x=0, y=0, width=700, height=400)

src_url = 'https://weather.cma.cn/web/weather/57682.html'

a = requests.get(src_url)
b = a.content.decode()

sr_text = f'数据来源：中国气象局·天气预报\n{src_url}'

time_re = '<div class=\"hd\">\n *(7.*?）)'#天气预报更行时间
c = re.findall(time_re, b)

time_week = '(星期.)\n *<br>(../..)\n.*\n.*\n.*\n.*\n.*\n *(.*)\n.*\n.*\n *(.*)\n.*\n.*\n *(.*)\n.*\n.*\n.*\n.*\n *(.*)\n.*\n.*\n *(.*)'# 星期与日期
d = re.findall(time_week, b)

label1.place_forget()
label_sour = Label(root, text=sr_text, font=('宋体', 20))
label_sour.place(x=0, y=0, width=700, height=100)

for i in range(7):
    if i % 2 == 0:
        color = 'pink'
    else:
        color = 'lightblue'
    label = Label(root,
                  text=f'{d[i][0]}\n{d[i][1]}\n\n{d[i][2]}\n\n{d[i][3]}  {d[i][4]}\n\n{d[i][5]}~{d[i][6]}',
                  font=('宋体', 12), bg=color)


    label.place(x=(100*i), y=100, width=100, height=300)

#星期、日期、天气、风向、风力、最高温、最低温

root.mainloop()