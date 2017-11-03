from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from PyDictionary import PyDictionary
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

dictionary = PyDictionary()
'''synonyms =[]
for syn in wordnet.synsets("removal"):
    for l in syn.lemmas():
        synonyms.append(l.name())
print(pos_tag(['functioning'])[0][1])
lem = WordNetLemmatizer()
print(lem.lemmatize('removal', pos='n'))'''
print(dictionary.synonym("work"))

print(pos_tag(['Car']))
