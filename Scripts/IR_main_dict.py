import csv
import re
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

xl = pd.ExcelFile('new.xlsx')
df1 = xl.parse('Main')
col1 = df1.Subject
col2 = df1.Body
col3 = df1.Department
'''x2 = pd.ExcelFile('test.xlsx')
df2 = x2.parse('Sheet1')
col4 = df2.Subject'''
master_dict = {}
lem = WordNetLemmatizer()
ps = PorterStemmer()
stop = set(stopwords.words('english'))
Ashoka_untouched = ['ds','cs','cts','fc','ct','osl','oaa']
Selected_Attributes = ['course','wifi','reimbursement','login','booking','ds','cancellation','clicker','registration','card','working','id','drop','projector','room','event','meeting']
for i in col1:
    EB = re.sub('[^A-Za-z0-9]+', ' ', i)
    tokens = word_tokenize(EB.lower())
    for j in tokens:

            if j not in stop and j not in Ashoka_untouched:
                k = lem.lemmatize(j)
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
for i in col1:
    EB = re.sub('[^A-Za-z0-9]+', ' ', i)
    tokens = word_tokenize(EB.lower())
    for j in tokens:
        t = ps.stem(j)
        if t in master_dict.keys():
            master_dict[t]+=1
    writer=csv.writer(open('Subject.csv','a',newline=''))
    if m==0:
        print('hello')
        writer.writerow(columns)
        m+=1
    for i in columns:
        if i in master_dict.keys() :
            rows.append(master_dict[i])
    writer.writerow(rows)
    rows = []
    for keys in master_dict.keys():
        master_dict[keys]=0






