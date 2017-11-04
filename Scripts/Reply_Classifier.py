import pandas
import csv
import re
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from sklearn.naive_bayes import MultinomialNB
from NBClassifier import Dept_Classify

a = Dept_Classify()
csv_file=''
test_file = ''
if a == [1.]:
    csv_file = 'IT_ATTR.csv'
    test_file = 'IT_TEST.csv'
if a == [2.]:
    csv_file = 'OAA_ATTR.csv'
    test_file = 'OAA_TEST.csv'
if a ==[3.]:
    csv_file = 'OSL_ATTR.csv'
    test_file = 'OSL_TEST.csv'


dataframe = pandas.read_csv(csv_file)
colnames=dataframe.columns.values

def POS_tag(a):
    if a.startswith('N'):
        return 'n'
    elif a.startswith('V'):
        return 'v'
    else:
        return None



def Test_Conversion(s,b):
    stop = set(stopwords.words('english'))
    Ashoka_untouched = ['ds','cs','cts','fc','ct','osl','oaa']
    lem = WordNetLemmatizer()
    master_dict = {}
    c = s + ' '+ b
    c = re.sub('[^A-Za-z]+', ' ', c)
    tokens = word_tokenize(c)
    columns = colnames[:-1]
    m =0
    for i in columns:
        if i not in master_dict.keys():
            master_dict[i]= 0

    for j in tokens:

                    pos = POS_tag(pos_tag([j])[0][1])
                    if (pos==None):
                        t = lem.lemmatize(j)
                    if pos == 'n':
                         t = lem.lemmatize(j,pos='n')
                    if pos == 'v':
                         t = lem.lemmatize(j,pos='v')
                    if t in master_dict.keys():
                         master_dict[t]+=1
    writer=csv.writer(open(test_file,'w',newline=''))
    if m==0:
        writer.writerow(columns)
        m+=1
    rows = []
    for i in colnames:
        if i in master_dict.keys() :
            rows.append(master_dict[i])
    writer.writerow(rows)





arr = dataframe.values
subject="Course addition"
body="Hey, Please add me to of history course. Regards Poop."
Test_Conversion(subject,body)
df1 = pandas.read_csv(test_file)
test = df1.values
X = arr[:,0:-1]
Y = arr[:,-1:]
Y = Y.ravel()
clf = MultinomialNB().fit(X,Y)
result = clf.predict(test)
print(result)

