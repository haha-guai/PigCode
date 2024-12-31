from wxauto import WeChat
import time

wx = WeChat()
friend_list = []
friend_infos = wx.GetAllFriends()

for friend in friend_infos:
    try:
        if '跨年' in friend['tags']:
            friend_list.append(friend['nickname'])
    except:
        pass
print("列表获取成功")

time_str = '2025-01-01 00:00:00'
time_format = '%Y-%m-%d %H:%M:%S'
time_struct = time.strptime(time_str, time_format)
timestamp = time.mktime(time_struct)
while (timestamp - time.time()) > 0:
    if (timestamp - time.time()) >= 3600:
        print(f"剩余：{round(timestamp - time.time()) / 60}min")
        time.sleep(600)
        
    elif (timestamp - time.time()) >= 700:
        print(f"剩余：{round(timestamp - time.time())}s")
        time.sleep(60)
    elif (timestamp - time.time()) >= 60:
        printf(f"剩余：{round(timestamp - time.time())}s")
        time.sleep(3)
    else:
        print(f"剩余：\033[31m{round(timestamp - time.time())}s")
        time.sleep(1)
for friend in friend_list:
    wx.SendMsg('元旦快乐', friend)
    wx.SendMsg('44x.cn/106\n代码自己写的，网页链接偷的,对你的祝福是真的[跳跳]', friend)
    wx.SendMsg('[庆祝]', friend)
