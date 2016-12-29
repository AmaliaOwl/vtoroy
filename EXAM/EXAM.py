import urllib.request
import re
import os

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        print('Error at', pageUrl)
        return 'Error'

text = download_page('http://web-corpora.net/Test2_2016/short_story.html')

txt0 = re.findall('<meta content="(.+?)"', text)

f = open('D:\\python\\letterS.txt', 'a', encoding = 'utf-8')

print('СЛОВА НА "С":\n')
for line in txt0:
    line2 = re.sub('&nbsp;', ' ', line)
    line2 = re.sub('[\.,:;\?!—«»\)\(]', ' ', line2)
    line2 = re.sub('\n', ' ', line2)
    line2 = re.sub(' +', ' ', line2)
    line2 = line2.split(' ')
    for word in line2:
        word2 = word.lower()
        if word2.startswith('с'):
            print(word)
            f.write(word + '\n')
        else:
            continue

txt = re.sub('<.+?>', ' ', text)
txt = re.sub('&nbsp;', ' ', txt)
txt = re.sub('[\.,:;\?!—«»\)\(]', ' ', txt)
txt = re.sub('\n', ' ', txt)
txt = re.sub(' +', ' ', txt)
txt = txt.split(' ')

for word in txt:
    word2 = word.lower()
    if word2.startswith('с'):
        print(word)
        f.write(word + '\n')
    else:
        continue
f.close()

os.system(r"C:\Users\Samsung\.local\bin\mystem.exe -e UTF-8 -dicg " + 'D:\\python\\letterS.txt' +" "+ 'D:\\python\\letterS_mystem.txt')

def func2(address):
    f = open(address, 'r', encoding = 'utf-8')
    txt = f.readlines()
    f.close()
    return txt

an_text = func2('D:\\python\\letterS_mystem.txt')

f = open('D:\\python\\script_LETTERS.txt', 'a', encoding = 'utf-8')
creation2 = "CREATE TABLE text_an\n(\nwordID int,\nLemma varchar(255),\nWordForm varchar(255),\nPOS varchar(255)\n);\n"

f.write(creation2)

flag = 0
print('\nГЛАГОЛЫ НА "С":\n')
for line in an_text:
    regex = re.search('(.+?){', line)
    word_form = regex.group(1)
    string1 = "INSERT INTO text_an" + "\n"+ "VALUES ("
    regex2 = re.search('{(.+?)[\?=]', line)
    lemma = regex2.group(1)
    regex3 = re.search('=(.+?)[=,]', line)
    POS = regex3.group(1)
    flag += 1
    fl = str(flag)
    string1 += "'"+fl+"'"+', '+"'"+lemma+"'"+', '+"'"+word_form+"'"+', '+"'"+POS+"'"+ ");\n"
    f.write(string1)
    if '=V' in line:
        print(word_form)
    else:
        continue   

f.close()
