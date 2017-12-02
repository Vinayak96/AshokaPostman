import sys
import requests
from bs4 import BeautifulSoup


def get_google_spelling(phrase):
    page = get_page(phrase)

    spell_tag = get_spell_tag(page)
    
    if spell_tag is None or spell_tag.text == "":
        return phrase
    else:
        return spell_tag.text


def get_spell_tag(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    spell_tag=soup.find_all('a',{'class' : 'spell'})
    if(len(spell_tag)==0):
       spell_tag=soup.find_all('span',{'class' : 'spell'})[0].a
    else:
       spell_tag=spell_tag[0]
    return spell_tag

def get_page(search):
    
    headers = {
        "User-Agent" :
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0",
    }
    url = "http://www.google.com/search?q="+search
    page = requests.get(url, headers=headers)
    return page

