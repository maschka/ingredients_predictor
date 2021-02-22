import numpy as np
import pandas as pd


from sklearn.feature_extraction.text import CountVectorizer

def my_preprocessor(doc):
	return doc

def my_tokenizer(x):
	return x

def create_vectorization(training_X):
	vectorizer  = CountVectorizer(preprocessor= my_preprocessor, tokenizer = my_tokenizer)
	vectorizer.fit_transform(training_X)
	return vectorizer

from sklearn.preprocessing import OneHotEncoder

 
list1 = [["one"], ["two"], ["three"]]

list2 = [["two"], ["one"], ["two"]]
# v = create_vectorization(list1)
# print (v.get_feature_names())
# print( v.vocabulary_)
# print(v.transform(list2))
enc = OneHotEncoder(sparse = False)
enc.fit(list1)
print(enc.transform(list2))