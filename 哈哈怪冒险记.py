from tkinter import *

class Settings():
    def __init__(self, game):
        game.root.geometry('1000x600')
        game.root.title('哈哈怪历险记')

class Game():
    def __init__(self):
        self.root = Tk()
        self.menu = MyMenu(self)
        self.settings = Settings(self)

    def run(self):
        welcome_play(self.root)
        self.root.mainloop()

class MyFrame(Frame):
    def __init__(self, root):
        super().__init__()
        self.config(background='gainsboro')
        exit_button = Button(self, text='-', command=self.forget_self)
        exit_button.place(x=600, y=0, width=20, height=20, anchor="ne")

    def forget_self(self):
        self.place_forget()
    def place_self(self):
        self.place(x=500, y=0, width=600, height=400, anchor="n")

def welcome_play(root):
    label1 = Label(root, text='欢迎来到\n哈哈怪历险记', font=('宋体', 50))
    label1.pack()
    root.after(3000, lambda:label1.pack_forget())

    label2 = Label(root, text='\n\n正在进入游戏\n请耐心等待\n……', font=('宋体', 30))
    label2.pack()
    root.after(5000, lambda: label2.config(text="\n\n权限不足\n请先V五块给李猪儿"))

class MyMenu():
    def __init__(self, game):
        self.menubar = Menu(game.root)
        self.first_menu = Menu(self.menubar)
        self.menubar.add_cascade(label="菜单", menu=self.first_menu)
        self.first_menu.add_command(label="保存", command=None)
        self.first_menu.add_command(label="退出", command=game.root.quit)
        self.first_menu.add_command(label="帮助", command=None)
        self.first_menu.add_command(label="开挂", command=None)
        self.first_menu.add_command(label="捐赠", command=self.donate)
        game.root.config(menu=self.menubar)
    def donate(self):
        image = PhotoImage(file="static\\image\\付款码.png")
        label_image = Label(game.root, image=image)
        label_image.image = image
        label_image.pack()
        label_text = Label(game.root, text="双击收起", font=('宋体', 20))
        label_text.pack()
        def label_forget(event):
            label_image.pack_forget()
            label_text.pack_forget()
        game.root.bind("<Double-Button-1>", label_forget)
class Player():
    pass
class Item():
    pass
class Figure():
    pass
class Map():
    pass

if __name__ == '__main__':
    game = Game()
    game.run()