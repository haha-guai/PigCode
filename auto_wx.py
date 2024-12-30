from wxauto import WeChat
import time
wx = WeChat()
print('添加监听对象：（输入”##q##“退出添加）')
print("输入备注或对方网名")

listen_list = []
name = ''
person_num = 1

while name != '##q##':
    name = input(f'第{person_num}位监听对象：')
    if name == '##q##':
        break
    listen_list.append(name)
    person_num += 1

for i in listen_list:
    wx.AddListenChat(who=i, savepic=True)


wait = 1
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who  # 获取聊天窗口名（人或群名）
        one_msgs = msgs.get(chat)  # 获取消息内容
        # 回复收到
        for msg in one_msgs:
            msgtype = msg.type  # 获取消息类型
            content = msg.content  # 获取消息内容，字符串类型的消息内容
            print(f'【{who}】：{content}')

            if msgtype == 'friend':
                chat.SendMsg('代码测试中，自动回复[玫瑰][玫瑰][玫瑰]')  # 回复收到
    time.sleep(wait)