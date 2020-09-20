import json
import urllib3
from bs4 import BeautifulSoup

def get_naver_dict_definition(word):
    STEM = 'http://ac.dict.naver.com/enkodict/ac?st=11001&r_lt=11001&q='
    http = urllib3.PoolManager()
    r = http.request('GET', STEM +word)
    soup = BeautifulSoup(r.data, 'lxml')
    try:
        text = json.loads(soup.text)['items'][0][0]
        translation = text[1][0]
        if word == text[0][0]:
            return translation
        return None
    except:
        return None
