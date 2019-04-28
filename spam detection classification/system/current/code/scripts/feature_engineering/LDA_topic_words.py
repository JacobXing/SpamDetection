# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:38:27 2018

@author: 13661
"""

from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
from numpy import array
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

def textPrecessing(text):
    #小写化
    text = text.lower()
    #去除特殊标点
    for c in string.punctuation:
        text = text.replace(c, ' ')
    #分词
    wordLst = nltk.word_tokenize(text)
    #去除停用词
    filtered = [w for w in wordLst if w not in stopwords.words('english')]
    #仅保留名词或特定POS   
    refiltered =nltk.pos_tag(filtered)
    filtered = [w for w, pos in refiltered if pos.startswith('NN')]
    #词干化
    ps = PorterStemmer()
    filtered = [ps.stem(w) for w in filtered]

    return " ".join(filtered)

def print_top_words(model, feature_names, n_top_words):
    #打印每个主题下权重较高的term
    for topic_idx, topic in enumerate(model.components_):
        print ("Topic #%d:" % topic_idx)
        a.extend([feature_names[i]
                for i in topic.argsort()[:-n_top_words - 1:-1]])
    #打印主题-词语分布矩阵
    print(a)
    print(model.components_)
    
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

#构建词汇统计向量并保存
tf_vectorizer = CountVectorizer(max_df=1.0, min_df=0.0,
                                max_features=200,
                                stop_words='english')
score = []

for t in range(0,1000):
    
    df = pd.read_csv("../../../data_sets/honey_pot/preprocessed/Divided/test_{0}.csv".format(t))
    df = df.dropna(subset=['Tweet'])
    cf = df['Tweet']
    cf = list(cf)
    if len(cf):
        try:
            docLst = []
            for desc in cf :
                docLst.append(textPrecessing(desc).encode('utf-8'))

            tf = tf_vectorizer.fit_transform(docLst)
            n_topics = 1
            lda = LatentDirichletAllocation(n_topics=n_topics, 
                                            max_iter=50,
                                            learning_method='batch')
            lda.fit(tf) #tf即为Document_word Sparse Matrix    
            a = []

            n_top_words=10
            tf_feature_names = tf_vectorizer.get_feature_names()
            print_top_words(lda, tf_feature_names, n_top_words)
            o = []
            p = []
            for i in range(len(docLst)):
                o.append(str(docLst[i], encoding = "utf-8"))

            for j in range(len(o)):
                w = o[j]
                w = w.split(' ')    
                retA = [i for i in a if i in w]
                p.append(retA)
                e = []
                
            for i in range(len(p)):
                e.append(len(p[i])/10) 
            score.append(averagenum(e))
        except:
            score.append(0)
    else:
        score.append(0)

        
reader = pd.read_csv('../../../data_sets/honey_pot/preprocessed/dynamic_features_intermediate.csv')
index = []
index = reader['user_id']
import numpy as np
index = np.array(index)
df_empty = pd.DataFrame(columns=['user_id', 'LDA_score'])
for v in range(0,1000):
    df_empty.loc[v] = [index[v], score[v]]
df_empty.to_csv("../../../data_sets/honey_pot/final_features/std.csv",encoding="gbk",index=False )
std = pd.read_csv("../../../data_sets/honey_pot/final_features/std.csv")
reader1 = pd.read_csv("../../../data_sets/honey_pot/final_features/static_features1.csv")
LDA_Score = pd.merge(reader1, std, how='left')
LDA_Score.to_csv("../../../data_sets/honey_pot/final_features/static_features2.csv",encoding="utf-8",index=False )

