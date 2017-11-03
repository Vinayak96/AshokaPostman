# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfTransformer
# load data
transformer = TfidfTransformer(smooth_idf=False)
dataframe = pandas.read_csv('tfidf.csv')
f = list(dataframe.columns.values)
array = dataframe.values
X = array[:,0:-1]
Y = array[:,-1:]
test = SelectKBest(score_func=chi2, k=50)
fit = test.fit(X, Y)
numpy.set_printoptions(precision=3)
features = fit.transform(X)
a = test.get_support(True)
atr = a.tolist()
for i in atr:
    print(f[i])
