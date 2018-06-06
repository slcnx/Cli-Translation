#!/usr/bin/python3
# encoding:utf-8
import requests
import json
import sys
import argparse
from googletrans import Translator


translator = Translator(service_urls=[
      'translate.google.cn',
    ])
# 扇贝单词 只能翻译一个单词
shanbei = 'https://www.shanbay.com/api/v1/bdc/search/?version=2&word='



def shanbei_trans(word):
    '''
    只能翻译单个单词
    '''
    try:
        response = requests.get(shanbei + word).text
        response = json.loads(response)
        if response and response['msg'] == 'SUCCESS':
            print('\033[1;31;40m')
            print(word)
            print('\033[0m')
            print('CN:%s' % response['data']['definitions']['cn'][0]['defn'])
            print('EN:%s' % response['data']['definitions']['en'][0]['defn'])
            return True
        else:
            return False
    except Exception:
        return False

def google_trans(word,dest="zh-CN"):
    print(translator.translate(word,dest=dest).text)
        
def detect_lang(word):
    lang_info = translator.detect(word)
    return lang_info.lang if lang_info.confidence > 0.9 else None
        
def args_parser():
    parser = argparse.ArgumentParser(description='Translate Some Shit')

    parser.add_argument('-v', dest='verbose', action='store_true', 
                        help='trans chinese to english')
    parser.add_argument('-s', dest='shanbei', action='store_true',
                            help='use Shanbei to translate single word')
    parser.add_argument('-d', dest='dest', action='store',
                        help='specify destination language,zh-CN default')
    parser.add_argument(dest='source', metavar='source', nargs='*',
                         help='source word to translate')
    args = parser.parse_args()
    return args
    
    
if __name__ == '__main__':
    args = args_parser()
    source = ' '.join(args.source)
    language = detect_lang(source)
    if language == None:
        print("No legal language detected")
        sys.exit()

    if args.shanbei == True :
        shanbei_trans(args.source[0])

    if args.dest != None:
        google_trans(source, dest=args.dest[0])
    elif args.verbose == True or language == "zh-CN":
        google_trans(source,dest='en')
    else:
        google_trans(source)

