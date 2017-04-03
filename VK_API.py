import urllib.request  # импортируем модуль 
req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=5774269&post_id=1417&count=20') 
response = urllib.request.urlopen(req) # да, так тоже можно, не обязательно делать это с with, как в примере выше
result = response.read().decode('utf-8')

print(result)

import json
data = json.loads(result) 
print(type(data))

#f = open('D:\\python\\script.txt', 'a', encoding = 'utf-8')
#creation1 = "CREATE TABLE Lemmas\n(\nid записи int,\nid коммента int,\nтекст коммента varchar(255),\nid автора int\n);\n"
#f.write(creation1)


print(data["response"][1]["text"])



