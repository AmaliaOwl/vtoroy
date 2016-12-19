import re
import os
import json
import datetime
import unicodedata
import codecs

def func(address):
    f = open(address, 'r', encoding = 'utf-8')
    txt = f.read()
    f.close()           
    return txt

txt = func('D:\\python\\dict.xdxf')

vocab = {}
raw_text = re.findall('<ar><k>.+?</k>\n.+?</ar>',txt)

for i in raw_text:
    regex1 = re.search('<k>(.+?)</k>',i)
    if regex1:
        basq_word = regex1.group(1)
        if basq_word not in vocab:
            regex5 = re.search('</k>\n(.+?)</ar>', i)
            eng_word = regex5.group(1)
            definition = eng_word
            vocab[basq_word] = definition
        else:
            continue

class pObj(object):
    pass
pObj = json.dumps(vocab)
output = open("D:\\python\\open_Python\\json_basq_eng.txt", "w")
json.dump(vocab, output)
output.close()

inv_vocab = {v:k for k, v in vocab.items()}


class pObj(object):
    pass
pObj = json.dumps(inv_vocab)
output = open("D:\\python\\open_Python\\json_eng_basq.txt", "w")
json.dump(inv_vocab, output)
output.close()

from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

#дальше как-то не очень получилось
@app.route('/')
def main():
    if request.args:
        name = request.args['eng_word']
        return render_template('results.html', name = name)
   return render_template('search2.html')

@app.route('/results')
def results(): 
    if request.args:
        result = ''
        if name in inv_vocab:
            result = vocab.get(name)
    return render_template('results2.html', result = result)

         
if __name__ == '__main__':
    app.run(debug = True)
