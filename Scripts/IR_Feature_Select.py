# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfTransformer
import csv
# load data
transformer = TfidfTransformer(smooth_idf=False)
dataframe = pandas.read_csv('OSL_TFIDF.csv')
f = list(dataframe.columns.values)
array = dataframe.values
X = array[:,0:-1]
Y = array[:,-1:]
test = SelectKBest(score_func=chi2, k=50)
fit = test.fit(X, Y)
numpy.set_printoptions(precision=3)
features = fit.transform(X)
a = test.get_support(True)
a = a.tolist()
atr = []
for i in a:
    atr.append(f[i])
writer = csv.writer(open('OSL_ATTR.csv','a',newline=''))
writer.writerow(atr)
for i in features:
   k = i.tolist()
   writer.writerow(k)

