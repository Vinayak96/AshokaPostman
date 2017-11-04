import csv
import re
from salutation_removal import *
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

def POS_tag(a):
    if a.startswith('N'):
        return 'n'
    elif a.startswith('V'):
        return 'v'
    else:
        return None

xl = pd.ExcelFile('OSL.xlsx')
df1 = xl.parse('Sheet1')
col1 = df1.Subject
col2 = df1.Body
col3 = []
for i in range(len(col1)):
    col3.append(col1[i]+' '+ col2[i])

master_dict = {}
lem = WordNetLemmatizer()
ps = PorterStemmer()
stop = set(stopwords.words('english'))
Ashoka_untouched = ['ds','cs','cts','fc','ct','osl','oaa']
Selected_Attributes = ['course','wifi','reimbursement','login','booking','ds','cancellation','clicker','registration','card','working','id','drop','projector','room','event','meeting']
for i in col3:
    body = get_body(i)
    EB = re.sub('[^A-Za-z]+', ' ', body)
    tokens = word_tokenize(EB)
    for j in tokens:
        if pos_tag([j])[0][1]!= 'NNP':
            j = j.lower()
            pos = POS_tag(pos_tag([j])[0][1])
            if j not in stop and j not in Ashoka_untouched:
                if (pos==None):
                    k = lem.lemmatize(j)
                if pos == 'n':
                     k = lem.lemmatize(j,pos='n')
                if pos == 'v':
                     k = lem.lemmatize(j,pos='v')
                if k not in master_dict.keys():
                    master_dict[k]=0
                else:
                    pass
            if j in Ashoka_untouched:
                if j not in master_dict.keys():
                    master_dict[j]=0
                else:
                    pass
columns = []
for i in master_dict.keys():
    columns.append(i)
rows =[]
m = 0
for i in col3:
    body = get_body(i)
    EB = re.sub('[^A-Za-z]+', ' ', body)
    tokens = word_tokenize(EB)
    for j in tokens:
      if pos_tag([j])[0][1]!='NNP':
        j = j.lower()
        pos = POS_tag(pos_tag([j])[0][1])
        if (pos==None):
            t = lem.lemmatize(j)
        if pos == 'n':
             t = lem.lemmatize(j,pos='n')
        if pos == 'v':
             t = lem.lemmatize(j,pos='v')
        if t in master_dict.keys():
            master_dict[t]+=1
    writer=csv.writer(open('OSLCountVector.csv','a',newline=''))
    if m==0:
        writer.writerow(columns)
        m+=1
    for i in columns:
        if i in master_dict.keys() :
            rows.append(master_dict[i])
    writer.writerow(rows)
    rows = []
    for keys in master_dict.keys():
        master_dict[keys]=0






