from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from PyDictionary import PyDictionary
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

dictionary = PyDictionary()
synonyms =[]
'''
print(pos_tag(['functioning'])[0][1])
lem = WordNetLemmatizer()
print(lem.lemmatize('removal', pos='n'))'''
for syn in wordnet.synsets("work"):
    for l in syn.lemmas():
        synonyms.append(l.name())
print(set(synonyms))
print(pos_tag(['Car']))
