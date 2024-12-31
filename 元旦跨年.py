from wxauto import WeChat
import time

wx = WeChat()
friend_dict = {}
friend_list = []
friend_infos = wx.GetAllFriends()

for friend in friend_infos:
    try:
        if '跨年' in friend['tags']:
            friend_list.append(friend['nickname'])
    except:
        pass

time_str = '2025-01-01 00:00:00'
time_format = '%Y-%m-%d %H:%M:%S'
time_struct = time.strptime(time_str, time_format)
timestamp = time.mktime(time_struct)
while timestamp > time.time():
    time.sleep(3)

for friend in friend_list:
    wx.SendMsg('元旦快乐', friend)