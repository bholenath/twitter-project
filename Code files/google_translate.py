# encoding: utf-8

#from __future__ import unicode_literals
from xgoogle.translate import Translator,TranslationError,DetectionError,LanguageDetector 
from pprint import pprint
import json
import codecs


def g_trans(lang, data):

    try:
        translate = Translator().translate
        #str = "mi nombre es gonsalves anthony"
        #decoded_string = str.encode('utf8', 'ignore').strip().replace("\'", r"\'")
        trans = translate(data, str(lang), 'en')
        #file = open('translated_text.txt', 'a')
        #pretty = pprint.pprint(trans)
        #file.write(pretty)
        pprint(trans.decode('string_escape').decode('utf8'))
        #file.close()

    except TranslationError, e:
        pprint(e) 
        
def g_detect():

    try:
        detect = LanguageDetector().detect
        str1 = 'RT @yoshi_e: 東京ディズニーシーと皆既月食の景色をブログにアップしました！｜Total Lunar Eclipse at Tokyo DisneySea｜東京ディズニーシーの美しい景色と共に皆既月食… http://t.co/5dwSVaM2x1 http://t.…'
        #decode = unicode(str1.strip(), 'utf-8')
        det = detect(str1)
        #pprint(det)
        g_trans(det, str1)
    
    except DetectionError, e:
        pprint(e)        
        
g_detect()       
     