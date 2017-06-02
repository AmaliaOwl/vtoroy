import pymorphy2
import re
import random

from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

ANIM_NOUN_list = ()
INAN_NOUN_list = ()
TRAN_VERB_list = ()
INTR_VERB_list = ()
ADJF_list = ()
ADJS_list = ()
COMP_list = ()
INFN_list = ()
PRTF_list = ()
PRTS_list = ()
GRND_list = ()
NUMR_list = ()
ADVB_list = ()
NPRO_list = ()
PRED_list = ()
PREP_list = ()
COMJ_list = ()
PRCL_list = ()
INTJ_list = ()

def reading(address):
    f = open(address, 'r', encoding = 'utf-8')
    txt = f.read()  
    f.close()
    new_text = txt.split(' ')
    t = 0
    while t < 100:
        for word in new_text:
            analisys = morph.parse(word)
            first = analisys[0]
            grammar = first.tag
            POS = first.tag.POS
            if POS == 'NOUN':
                if first.tag.animacy == 'anim':
                    ANIM_NOUN_list += first.normal_form
                    print(first.normal_form)
                elif first.tag.animacy == 'inan':
                    INAN_NOUN_list += first.normal_form
                    print(first.normal_form)
                else:
                    continue
            elif POS == 'VERB':
                if first.tag.transitivity == 'tran':
                    TRAN_VERB_list += first.normal_form
                elif first.tag.transitivity == 'intr':
                    INTR_NOUN_list += first.normal_form   
            elif POS == 'ADJF':
                ADJF_list += first.normal_form
            elif POS == 'ADJS':
                ADJS_list += first.normal_form
            elif POS == 'COMP':
                COMP_list += first.normal_form
            elif POS == 'INFN':
                INFN_list += first.normal_form
            elif POS == 'PRTF':
                PRTF_list += first.normal_form
            elif POS == 'PRTS':
                PRTS_list += first.normal_form
            elif POS == 'GRND':
                GRND_list += first.normal_form
            elif POS == 'NUMR':
                NUMR_list += first.normal_form
            elif POS == 'ADVB':
                ADVB_list += first.normal_form
            elif POS == 'NPRO':
                NPRO_list += first.normal_form
            elif POS == 'PRED':
                PRED_list += first.normal_form
            elif POS == 'COMJ':
                COMJ_list += first.normal_form
            elif POS == 'PRCL':
                PRCL_list += first.normal_form
            elif POS == 'INTJ':
                INTJ_list += first.normal_form
            else:
                continue
            t += 1
    return ANIM_NOUN_list, INAN_NOUN_list, TRAN_VERB_list, INTR_VERB_list, ADJF_list, ADJS_list, COMP_list, INFN_list, PRTF_list, PRTS_list, GRND_list, NUMR_list,
ADVB_list, NPRO_list, PRED_list, PREP_list, COMJ_list, PRCL_list, INTJ_list

def anagram_making(text):
    string = ''
    new_text = text.split(' ')
    for word in new_text:
        analisys = morph.parse(word)
        first = analisys[0]
        grammar = first.tag
        POS = first.tag.POS
        if POS == 'NOUN':
            if first.tag.animacy == 'anim':
                c = random.randint(0, len(ANIM_NOUN_list))
                word_0 = morph.parse(ANIM_NOUN_list[c])[0]
                word_1 = word_0.inflect(grammar)
                string += word_1 + ' '
            elif first.tag.animacy == 'inan':
                c = random.randint(0, len(INAN_NOUN_list))
                word_0 = morph.parse(INAN_NOUN_list[c])[0]
                word_1 = word_0.inflect(grammar)
                string += word_1 + ' '
            else:
                continue
        elif POS == 'VERB':
            if first.tag.transitivity == 'tran':
                c = random.randint(0, len(TRAN_VERB_list))
                word_0 = morph.parse(TRAN_VERB_list[c])[0]
                word_1 = word_0.inflect(grammar)
                string += word_1 + ' '
            elif first.tag.transitivity == 'intr':
                c = random.randint(0, len(INTR_VERB_list))
                word_0 = morph.parse(INTR_VERB_list[c])[0]
                word_1 = word_0.inflect(grammar)
                string += word_1 + ' '
        elif POS == 'ADJF':
            c = random.randint(0, len(ADJF_list))
            word_0 = morph.parse(ADJF_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'ADJS':
            c = random.randint(0, len(ADJS_list))
            word_0 = morph.parse(ADJS_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'COMP':
            c = random.randint(0, len(COMP_list))
            word_0 = morph.parse(COMP_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'INFN':
            c = random.randint(0, len(INFN_list))
            word_0 = morph.parse(INFN_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'PRTF':
            c = random.randint(0, len(PRTF_list))
            word_0 = morph.parse(PRTF_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'PRTS':
            c = random.randint(0, len(PRTS_list))
            word_0 = morph.parse(PRTS_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'GRND':
            c = random.randint(0, len(GRND_list))
            word_0 = morph.parse(GRND_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'NUMR':
            c = random.randint(0, len(NUMR_list))
            word_0 = morph.parse(NUMR_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'ADVB':
            c = random.randint(0, len(ADVB_list))
            word_0 = morph.parse(ADVB_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'NPRO':
            c = random.randint(0, len(NPRO_list))
            word_0 = morph.parse(NPRO_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'PRED':
            c = random.randint(0, len(PRED_list))
            word_0 = morph.parse(PRED_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'COMJ':
            c = random.randint(0, len(COMJ_list))
            word_0 = morph.parse(COMJ_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'PRCL':
            c = random.randint(0, len(PRCL_list))
            word_0 = morph.parse(PRCL_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        elif POS == 'INTJ':
            c = random.randint(0, len(INTJ_list))
            word_0 = morph.parse(INTJ_list[c])[0]
            word_1 = word_0.inflect(grammar)
            string += word_1 + ' '
        else:
            string += word + ' '              
    print(string)


def send_anagram(message):
    ana = anagram_making(message.text)
    bot.send_message(message.chat.id, anagram)


txt = reading('D:\\python\\Telegram Bot 2\\1grams-3.txt')
processing =anagram_making(input('Введите текст'))
