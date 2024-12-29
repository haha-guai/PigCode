import requests
import re
import time
import hashlib
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'}

keyword = input('输入搜索的关键词:\n')
start_time = time.time()

url = 'https://complexsearch.kugou.com/v2/search/song'
# 酷狗音乐搜索页网址

if not os.path.exists('music_download/'):
    os.mkdir('music_download/')
# 确保下载目录存在


def get_sign1(data_time):
    s = [
        'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
        'appid=1014',
        'bitrate=0',
        'callback=callback123',
        f'clienttime={data_time}',
        'clientver=1000',
        'dfid=2UHEJn1n8SAc183Vkl1eueOo',
        'filter=10',
        'inputtype=0',
        'iscorrection=1',
        'isfuzzy=0',
        f'keyword={keyword}',
        'mid=a7fac3cb03371483e44099f089baf239',
        'page=1',
        'pagesize=30',
        'platform=WebFilter',
        'privilege_filter=0',
        'srcappid=2919',
        'token=',
        'userid=0',
        'uuid=a7fac3cb03371483e44099f089baf239',
        'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    ]
    #  生成签名的列表
    string = ''.join(s)  # 将列表合并成字符串
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    sign = MD5.hexdigest()  # 将字符串转换成32位哈希值
    return sign


datatime = int(time.time() * 1000)  # 访问时间，精确到毫秒的时间戳
# 只用一个时间戳，防止因两个时间不一致导致的签名错误
signature1 = get_sign1(datatime)  # 获取签名

search_data1 = {
    'callback': 'callback123',
    'srcappid': '2919',
    'clientver': '1000',
    'clienttime': f'{datatime}',
    'mid': 'a7fac3cb03371483e44099f089baf239',
    'uuid': 'a7fac3cb03371483e44099f089baf239',
    'dfid': '2UHEJn1n8SAc183Vkl1eueOo',
    'keyword': f'{keyword}',
    'page': '1',
    'pagesize': '30',
    'bitrate': '0',
    'isfuzzy': '0',
    'inputtype': '0',
    'platform': 'WebFilter',
    'userid': '0',
    'iscorrection': '1',
    'privilege_filter': '0',
    'filter': '10',
    'token': '',
    'appid': '1014',
    'signature': f'{signature1}'
}
# 歌曲信息页网址参数

response = requests.get(url=url, params=search_data1, headers=headers)
data_sum = response.content.decode()
re_rule = '"EMixSongID":"(.*?)"'
id_list = re.findall(re_rule, data_sum)
# 解析网页并获取id

while '' in id_list:  # 去除空id
    id_list.remove('')

id_list = list(set(id_list))  # 去除重复id
print('获得歌曲id：', len(id_list))


def get_sign2(data_time, audio_id):
    s = [
        'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
        'appid=1014',
        f'clienttime={data_time}',
        'clientver=20000',
        'dfid=2UHEJn1n8SAc183Vkl1eueOo',
        f'encode_album_audio_id={audio_id}',
        'mid=a7fac3cb03371483e44099f089baf239',
        'platid=4',
        'srcappid=2919',
        'token=',
        'userid=0',
        'uuid=a7fac3cb03371483e44099f089baf239',
        'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    ]
    string = ''.join(s)
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    sign = MD5.hexdigest()
    return sign


# 获取特定歌曲信息页签名

count = 0  # 共写入文件数
for id in id_list:  # 循环下载id列表中的所有音乐
    datatime = int(time.time() * 1000)
    signature = get_sign2(datatime, id)
    data = {
        'srcappid': '2919',
        'clientver': '20000',
        'clienttime': f'{datatime}',
        'mid': 'a7fac3cb03371483e44099f089baf239',
        'uuid': 'a7fac3cb03371483e44099f089baf239',
        'dfid': '2UHEJn1n8SAc183Vkl1eueOo',
        'appid': '1014',
        'platid': '4',
        'encode_album_audio_id': f'{id}',
        'token': '',
        'userid': '0',
        'signature': f'{signature}',
    }

    music_json_data = str(
        requests.get(url='https://wwwapi.kugou.com/play/songinfo', params=data, headers=headers).json())
    # 获取歌曲信息，并将json格式的信息转为字符串
    music_url = re.findall("'play_url': '(.*?)'", music_json_data)[0]  # 歌曲链接
    music_name = re.findall("'audio_name': '(.*?)'", music_json_data)[0]  # 歌曲名称

    if music_url != '':  # 防止歌曲链接为空
        while '|' in music_name:  # 通过替换，防止歌曲名中存在违规字符
            music_name = music_name.replace('|', '_')
        music_resopnse = requests.get(url=music_url, headers=headers).content  # 获取歌曲文件信息
        with open(f'music_download\\{count}' + music_name + '.mp3', 'wb') as f:  # 将歌曲写入特定文件夹
            f.write(music_resopnse)
        print(str(count) + music_name + '  已完成')
        count += 1  # 下载数
print(f'\n共下载{count}首', '耗时', f'{time.time() - start_time}')
