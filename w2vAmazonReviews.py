#Basic Importing

import sqlite3
import pandas as pd
import numpy as np
import nltk
import string
import re
from nltk.corpus import stopwords
nltk.download("stopwords")
import gensim
from tqdm import tqdm

#We define a function to return -ve for 2 or less stars and +ve for 4 or more stars
def partition(x):
    if x<3:
        return 0
    return 1

#We don't take the scores == 3 because we can't classify them as positive or negative
con = sqlite3.connect('Amazon_reviews.sqlite')
data = pd.read_sql_query(""" SELECT * FROM Reviews WHERE Score != 3 LIMIT 1000""", con)

#Basic filter
actual_score=data["Score"]
positiveNegative=actual_score.map(partition)
data["Score"]=positiveNegative
data=data.drop(["HelpfulnessNumerator","HelpfulnessDenominator","ProfileName","Summary"],axis=1)

#data preprocessing

stop = set(stopwords.words('english')) 
sno = nltk.stem.SnowballStemmer('english') 

def cleanhtml(sentence): 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    return cleantext
def cleanpunc(sentence): 
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    return  cleaned

textArray=np.array(data["Text"])
cleanedTextArray=[]
for sent in textArray:
    sent=cleanhtml(sent);
    sent=cleanpunc(sent);
    sentArray=sent.split()
    cleanedSent=[]
    for word in sentArray:
        word=word.lower();
        if(word not in stop):
            word=sno.stem(word)
            cleanedSent.append(word);
    cleanedTextArray.append(cleanedSent)

data["Text"]=cleanedTextArray

#conversion to vector

list_of_sent=data["Text"]
w2v_model=gensim.models.Word2Vec(list_of_sent,min_count=5,size=50, workers=4)
w2v_words=list(w2v_model.wv.vocab)

listof_sent_vec=[]
for sent in tqdm(list_of_sent): 
    sent_vec = np.zeros(50) 
    cnt_words =0; 
    for word in sent: 
        if word in w2v_words:
            vec = w2v_model.wv[word]
            sent_vec += vec
            cnt_words += 1
    if cnt_words != 0:
        sent_vec /= cnt_words
    listof_sent_vec.append(sent_vec)
print(len(listof_sent_vec))
print(len(listof_sent_vec[0]))

#conversion to features

list_col=tuple(range(50))
vectorized_data=pd.DataFrame(data=listof_sent_vec, columns=list_col)
vectorized_data["Score"]=data["Score"]
vectorized_data["Time"]=data["Time"]
print(vectorized_data)

vectorized_data.to_csv("Amazon_reviews_vectorized.csv")
