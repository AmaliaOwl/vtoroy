#!/usr/bin/python
# -*- coding: utf-8
import re
import os
from pymystem3 import Mystem
mystem = Mystem()
import json
import sqlite3

def func(address):
    f = open(address, 'r', encoding = 'utf-8')
    txt = f.read()
    f.close()           
    return txt

txt = func('D:\\python\\text000.txt')

annotation = mystem.analyze(txt)
annotation_json = json.dumps(annotation, ensure_ascii=False, indent=4) 

f_out = open('D:\\python\\mystem_results.txt', 'w', encoding='utf-8')
f_out.write(annotation_json)
f_out.close()
print('DONE')

txt = func('D:\\python\\mystem_results.txt')

txt = re.sub('"text": "\n"', ' ', txt)
txt = re.sub('n', '', txt)
txt = re.sub('\r', ' ', txt)
txt = re.sub('\n', ' ', txt)
txt = re.sub('\t', ' ', txt)
txt = re.sub('[{}\[\]]', '', txt)
txt = re.sub(' +', ' ', txt)
txt = re.sub(r'"text": "\"', '', txt)
txt = re.sub(r'"text": "\\"', '', txt)

if txt.startswith(' "aalysis"'):
    raw_text = re.findall('"lex".+?"text": ".+?".+?"text": ".+?"', txt)

else:
    raw_text = re.findall('"text".+?"lex": ".+?".+?"text": ".+?"', txt)
    
vocab = {}
flag = 0

f = open('D:\\python\\script.txt', 'a', encoding = 'utf-8')
creation1 = "CREATE TABLE Lemmas\n(\nLemmaID int,\nWordForm varchar(255),\nLemma varchar(255)\n);\n"
creation2 = "CREATE TABLE text_an\n(\nwordID int,\nWordForm varchar(255),\nleft_p varchar(255),\nright_p varchar(255),\nNumber int,\nLink int\n);\n"

f.write(creation1)
f.write(creation2)

left_p = ' '
for i in raw_text:
    if txt.startswith(' "aalysis"'):
        regex1 = re.search('"lex": "(.+?)".+?"text": "(.+?)".+?"text": "(.+?)"',i)
        word_form = regex1.group(2)
        lemma = regex1.group(1)
    else:
        regex1 = re.search('"text": "(.+?)".+?"lex": "(.+?)".+?"text": "(.+?)"',i) 
        word_form = regex1.group(1)
        lemma = regex1.group(2)

    if lemma not in vocab:
        definition = word_form
        vocab[lemma] = definition
    else:
        continue

flag2 = 0

vocab2 = {}
for lemma in vocab:
    string1 = "INSERT INTO Lemmas" + "\n"+ "VALUES ("
    flag2 += 1
    fl2 = str(flag2)
    word = vocab.get(lemma)
    lemma = lemma.lower()
    word = word.lower()
    string1 += "'" + fl2 + "'" + ', '  + "'" + word + "'" + ', ' + "'" + lemma + "'" + ");\n"
    f.write(string1)
    if word not in vocab2:
        definition = fl2
        vocab2[word] = definition
    else:
        continue
print(vocab2)

for i in raw_text:
    if txt.startswith(' "aalysis"'):
        regex1 = re.search('"lex": "(.+?)".+?"text": "(.+?)".+?"text": "(.+?)"',i)
        word_form = regex1.group(2)
        lemma = regex1.group(1)
        right_p = regex1.group(3)
        string2 = "INSERT INTO text_an" + "\n"+ "VALUES ("
        flag += 1
        fl = str(flag)
        wf_temp = word_form.lower()
        if wf_temp in vocab2:
            link = vocab2.get(wf_temp)
        else:
            continue
        string2 += "'"+fl+"'"+', '+"'"+word_form+"'"+', '+"'"+left_p+"'"+', '+"'"+right_p+"'"+', '+"'"+fl+"'"+', '+ "'"+link+"'"+ ");\n"
        f.write(string2)
        left_p = right_p

    else:
        regex1 = re.search('"text": "(.+?)".+?"lex": "(.+?)".+?"text": "(.+?)"',i) 
        word_form = regex1.group(1)
        lemma = regex1.group(2)
        right_p = regex1.group(3)
        string2 = "INSERT INTO text_an" + "\n"+ "VALUES ("
        flag += 1
        fl = str(flag)
        wf_temp = word_form.lower()
        if wf_temp in vocab2:
            link = vocab2.get(wf_temp)
        else:
            continue
        string2 += "'"+fl+"'"+', '+"'"+word_form+"'"+', '+"'"+left_p+"'"+', '+"'"+right_p+"'"+', '+"'"+fl+"'"+', '+ "'"+link+"'"+ ");\n"
        f.write(string2)
        left_p = right_p
    
f.close()   

