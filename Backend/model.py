import pandas as pd 
import numpy as np 
import ast

import os

# Get the absolute path of the directory containing model.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dfM = pd.read_csv(os.path.join(BASE_DIR, "asset", "dataset", "tmdb_5000_movies.csv"))
dfC = pd.read_csv(os.path.join(BASE_DIR, "asset", "dataset", "tmdb_5000_credits.csv"))
# print(dfM)
# print(dfC)

movies = dfM.merge(dfC,on= "title")
# print(movies.head())

movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
# print(movies.head())

movies.isnull().sum()

movies.dropna(inplace=True)
# print(movies.isnull().sum())


# print(movies.duplicated().sum())
# print(movies.iloc[0].genres)

import ast
def convert(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l

movies['genres'] = movies['genres'].apply(convert)
# print(movies.head())

movies['keywords'] = movies['keywords'].apply(convert)
# print(movies.head())

def convert2(obj):
    l = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter !=3:
            l.append(i["name"])
            counter+=1
        else:
            break
    return l

movies['cast'] = movies['cast'].apply(convert2)
# print(movies.head())

def fatchDirector(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            l.append(i["name"])
    return l

movies['crew'] = movies['crew'].apply(fatchDirector)
# print(movies.head())

movies['overview'] = movies['overview'].apply(lambda x:x.split())
# print(movies.head())

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movies.head()

movies['tages'] = movies['overview']+movies['keywords']+movies['cast']+movies['crew']
# print(movies.head())

newDf = movies[['title','movie_id','tages']].copy()
# print(newDf.head())

newDf['tages'] = newDf['tages'].apply(lambda x: " ".join(x))
# print(newDf['tages'][0])

newDf['tages'] = newDf['tages'].apply(lambda x:x.lower())
# print(newDf['tages'][0])

import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def stem(obj):
    l = []
    for i in obj.split():
        l.append(ps.stem(i))
    return " ".join(l)

# Steming Testing
# ab =stem('in the 22nd century, a paraplegic marine is dispatched to the moon pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization. cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d samworthington zoesaldana sigourneyweaver jamescameron')
# print(ab)

# print(newDf['tages'].apply(stem))


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
vectors = cv.fit_transform(newDf['tages']).toarray()
# print(vectors)

# cv.get_stop_words()

from sklearn.metrics.pairwise import cosine_similarity

simmilarity = cosine_similarity(vectors)
sorted(list(enumerate(simmilarity[0])),reverse=True,key= lambda x:x[1])[1:6]

def recommend(movie):
    movieIndex = newDf[newDf['title']==movie].index[0]
    distance = simmilarity[movieIndex]
    moviesList = sorted(list(enumerate(distance)),reverse=True,key= lambda x:x[1])[1:6]
    recommendations = []

    for i in moviesList:
        recommendations.append(newDf.iloc[i[0]].title)

    return recommendations

# print(recommend("Ratatouille"))