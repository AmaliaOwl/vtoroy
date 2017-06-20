import telebot  
#import conf
import flask
import sys 
import gensim, logging
import os
from pymorphy2 import MorphAnalyzer 
morph = MorphAnalyzer()

TOKEN = os.environ['290920017:AAFM85lep-lTAYFJdZmqu3Yh1Xzz5eiwtRg']

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) 
m = 'D:\\python\\Telegram_Bot_3\\ruscorpora_1_300_10.bin.gz' 
if m.endswith('.vec.gz'): 
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False) 
elif m.endswith('.bin.gz'): 
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True) 
else: 
    model = gensim.models.KeyedVectors.load(m) 

model.init_sims(replace=True) 

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(TOKEN, threaded=False)  # бесплатный аккаунт pythonanywhere запрещает работу с несколькими тредами

bot.remove_webhook()
bot.set_webhook(url='https://<flask_app for heroku>.herokuapp.com/bot')
#WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Здравствуйте! Это бот, который находит лишнее по смыслу слово."\
                         "Введите не менее четырех слов через пробел.")

@bot.message_handler(func=lambda m: True)  # этот обработчик реагирует на любое сообщение
def send_len(message):
        text = message.text
        clearText = re.sub("[.,\-\s]", " ", text)
        text_list = clearText.split() 
        if len(text_list) < 4:
            bot.send_message(message.chat.id, 'Вы ввели слишком мало слов!')
        else:
            new_words = ''
            flag = 0
            for i in text_list: 
                ana = morph.parse(i)
                for j in range (0,len(ana)):
                    word = ana[j].word
                    lemma = ana[j].normal_form
                    if word == lemma and ana[j].tag.POS != None:
                        new_words += word + '_' + ana[j].tag.POS + ' '
                        flag += 1
                        break
                    elif ana[j].tag.POS == None:
                        break
                    else:
                        continue
                if flag >= 3:
                        answer1 = model.doesnt_match(new_words.split())
                        answer2 = re.sub("_(.+)", "", answer1)
                        bot.send_message(message.chat.id, answer2)
                else:
                        bot.send_message(message.chat.id, 'Вы ввели какую-то ерунду вместо слов!')  
                
	

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'


@app.route('/bot', methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
