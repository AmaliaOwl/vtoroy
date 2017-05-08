import requests
import json
import re
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import datetime

from collections import Counter

def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)

posts = []
item_count = 200

postVScomment = []
ageVScomment = []
cityVScomment = []

result = vk_api('wall.get', owner_id=-76982440, v='5.63', count=100)
posts += result["response"]["items"]

while len(posts) < item_count:
    result = vk_api('wall.get', owner_id=-76982440, v='5.63', count=100, offset=len(posts))
    posts += result['response']["items"]
print(len(posts))

s = ''
s_2 = ''
for i in range(0, len(posts)):
    s += posts[i]['text'] + '\n'
    postid = posts[i]['id']
    comm = []
    com_number = posts[i]['comments']['count']
    comments = vk_api('wall.getComments', owner_id=-76982440, post_id=postid, v='5.63', count=100)
    comm += comments
    while len(comm) < com_number:
        comments = vk_api('wall.getComments', owner_id=-76982440, post_id=postid, v='5.63', count=100, offset=len(comm))
        comm += comments['response']["items"]
    
    av_comment = 0
    for j in range(0, com_number):
        print(comm[j]['text'])
        s_2 += comm[j]['text'] + '\n'
        av_comment += len(comm[j]['text'])
        #print(comm[j]['date'])
        #print(comm[j]['from_id'])

        #comment_date = datetime.datetime.fromtimestamp(comm[j]['date']).strftime('%Y-%m-%d')
        #print(comment_date)
        #user_info = vk_api('users.get', user_ids=comm[j]['from_id'], fields='bdate', v='5.63')
        #print(user_info)
        #birthday = datetime.datetime.fromtimestamp(user_info['response'][0]['bdate']).strftime('%Y.%m.%d')
        #print(birthday)
        
        user_info = vk_api('users.get', user_ids=comm[j]['from_id'], fields='city', v='5.63')
        if 'city' in user_info['response'][0]:
            cityVScomment += [(len(comm[j]['text']), user_info['response'][0]['city']['title'])]
        
    if com_number != 0 :
        av_comment = av_comment/com_number
    else:
        continue
    postVScomment += [[len(posts[i]['text']), av_comment]]
    
f_out = open('D:\\python\\posts.txt', 'w', encoding='utf-8')
f_out.write(s)
f_out.close()

f_out = open('D:\\python\\comments.txt', 'w', encoding='utf-8')
f_out.write(s_2)
f_out.close()

lengh_dict = Counter([i[0] for i in postVScomment]).most_common()
print(lengh_dict)
final_post_comm = []
for i in range(len(lengh_dict)):
    a = lengh_dict[i][0]
    c = 0
    for j in range(len(postVScomment)):
        if postVScomment[j][0] == a:
            c += postVScomment[j][1]
        else:
            continue
    c = c/lengh_dict[i][1]
    final_post_comm += [(a, c)]
print(final_post_comm)
#final_post_comm = Counter([i[0] for i in final_post_comm]).most_common()

plt.figure(figsize=(200,100))
plt.bar(
    range(len(final_post_comm)), 
    [i[1] for i in final_post_comm]
)
plt.xticks(
    range(len(final_post_comm)), 
    [i[0] for i in final_post_comm], 
    rotation='vertical'
)
plt.title('Соотношение длины поста и длины комментариев')
plt.ylabel('значения Y')
plt.xlabel('значения X')
#plt.show()
plt.savefig('D:\\python\\post_com.png')


    
cities_dict = Counter([i[1] for i in cityVScomment]).most_common()
print(cities_dict)
final_cities_comm = []
for i in range(len(cities_dict)):
    a = cities_dict[i][0]
    c = 0
    for j in range(len(cityVScomment)):
        if cityVScomment[j][1] == a:
            c += cityVScomment[j][0]
        else:
            continue
    c = c/cities_dict[i][1]
    final_cities_comm += [(a, c)]
print(final_cities_comm)

plt.figure(figsize=(200,100))
plt.bar(
    range(len(final_cities_comm)), 
    [i[1] for i in final_cities_comm]
)
plt.xticks(
    range(len(final_cities_comm)), 
    [i[0] for i in final_cities_comm], 
    rotation='vertical'
)
#plt.show()
plt.savefig('D:\\python\\city_com.png')
