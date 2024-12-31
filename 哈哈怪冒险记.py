from tkinter import *


def first_play():
    try:
        with open('game_data.txt', 'r', encoding='utf-8') as f:
            game_data = f.read()
        return 0
    except FileNotFoundError:
        return 1

class Settings():
    def __init__(self, game):
        game.root.geometry('1000x600')
        game.root.title('哈哈怪历险记')

class Game():
    def __init__(self):
        self.root = Tk()
        self.menu = MyMenu(self)
        self.settings = Settings(self)

    def basic_place(self):
        pass
    def create_player(self):
        if first_play():
            frame = Frame(self.root, bg='gainsboro')
            frame.place(x=500, y=0, width=600, height=400, anchor='n')

            label1 = Label(frame, text='创建角色', font=("宋体", 20), fg='green')
            label1.place(x=0, y=0, width=350, height=40, anchor='nw')

            l_name = Label(frame, text="昵称", font=("宋体", 15))
            l_name.place(x=350, y=0, width=50, height=40, anchor='nw')

            e_name = Entry(frame, font=("宋体", 15))
            e_name.insert(0, "    输入你的昵称")
            e_name.place(x=400, y=0, width=200, height=40, anchor='nw')

            p_label1 = Label(frame, text=f"请选择\n你的角色", font=("宋体", 30))
            p_label2 = Label(frame, text='-未选择-',fg='red', font=("宋体", 20))

            p_label1.place(x=400, y=40, width=200, height=150, anchor='nw')
            p_label2.place(x=400, y=190, width=200, height=40, anchor='nw')

            image1 = PhotoImage(file='static\\image\\忧郁哥.png')
            image2 = PhotoImage(file='static\\image\\绿毛龟.png')
            image3 = PhotoImage(file='static\\image\\鼠儿哥.png')
            image4 = PhotoImage(file='static\\image\\阳光男孩.png')
            i_player1 = Button(frame, image=image1, command=lambda: p_label2.config(text='忧郁哥'))
            i_player1.image = image1
            i_player2 = Button(frame, image=image2, command=lambda: p_label2.config(text='绿毛龟'))
            i_player2.image = image2
            i_player3 = Button(frame, image=image3, command=lambda: p_label2.config(text='鼠儿哥'))
            i_player3.image = image3
            i_player4 = Button(frame, image=image4, command=lambda: p_label2.config(text='阳光男孩'))
            i_player4.image = image4
            ip_list = [i_player1, i_player2, i_player3, i_player4]

            n_player1 = Label(frame, text='忧郁哥', font=("宋体", 15))
            n_player2 = Label(frame, text='绿毛龟', font=("宋体", 15))
            n_player3 = Label(frame, text='鼠儿哥', font=("宋体", 15))
            n_player4 = Label(frame, text='阳光男孩', font=("宋体", 15))
            np_list = [n_player1, n_player2, n_player3, n_player4]

            for i in range(4):
                ip_list[i].place(x=(i * 100), y=40, width=100, height=150, anchor='nw')
                np_list[i].place(x=(i * 100), y=190, width=100, height=40, anchor='nw')

            config_button = Button(frame, text="确认", command=lambda: frame.place_forget())
            config_button.place(x=600, y=400, width=40, height=40, anchor='se')

            return e_name.get()
        else:
            self.basic_place()

    def run(self):
        welcome_play(self)

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

def welcome_play(game):
    def enter_game():
        label2.pack_forget()
        game.create_player()
    label1 = Label(game.root, text='欢迎来到\n哈哈怪历险记', font=('宋体', 50))
    label1.pack()
    game.root.after(0, lambda:label1.pack_forget())   #代改

    label2 = Label(game.root, text='\n\n正在进入游戏\n请耐心等待\n……', font=('宋体', 30))
    label2.pack()
    game.root.after(0, enter_game)   #代改

    #game.root.after(5000, lambda: label2.config(text="\n\n权限不足\n请先V五块给李猪儿"))

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