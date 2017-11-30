from scipy import linalg,dot,array
import csv
import re
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd


def transform(matrix, dimensions=1):
		
                new_matrix=array(matrix,dtype=float)
                rows,cols = new_matrix.shape

                if dimensions <= rows:
                        u,sigma,vt = linalg.svd(new_matrix)
                        for index in range(rows - dimensions, rows):
                             sigma[index] = 0

                        transformed_matrix = dot(dot(u, linalg.diagsvd(sigma, len(new_matrix), len(vt))) ,vt)

                        return transformed_matrix

                else:
                        print("dimension reduction cannot be greater than %s" % rows)

df1 = pd.read_csv('OSLCountVector.csv')

c = df1.columns.values
subject = df1.values


cv = TfidfTransformer()
tfidf = cv.fit_transform(subject)

tfidf1 = tfidf.toarray()
lsi=transform(tfidf1,2)

writer = csv.writer(open('OSL_TFIDF.csv','a',newline=''))
columns = c
writer.writerow(columns)
for i in lsi:
   k = i.tolist()
   writer.writerow(k)


