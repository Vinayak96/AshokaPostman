import csv
import re
from salutation_removal import *
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

df1 = pd.read_csv('subjectBody.csv')

c = df1.columns.values
subject = df1.values


cv = TfidfTransformer()
tfidf = cv.fit_transform(subject)

tfidf1 = tfidf.toarray()
writer = csv.writer(open('tfidf.csv','a',newline=''))
columns = c
writer.writerow(columns)
for i in tfidf1:
   k = i.tolist()
   writer.writerow(k)



