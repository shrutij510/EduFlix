#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import neattext.functions as nfx
import pickle

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel


# In[6]:


df = pd.read_csv("udemy_courses.csv")


# In[7]:


df.head()


# In[8]:


df['course_title']


# In[9]:


dir(nfx)


# In[10]:


#cleaning text

df['clean_course_title'] = df['course_title'].apply(nfx.remove_stopwords)


# In[11]:


df['clean_course_title'] = df['clean_course_title'].apply(nfx.remove_special_characters)


# In[12]:


df[['course_title','clean_course_title']]


# In[13]:


count_vect = CountVectorizer()
cv_mat = count_vect.fit_transform(df['clean_course_title'])


# In[16]:


#Sparse
cv_mat


# In[15]:


# Dense
cv_mat.todense()


# In[18]:


df_cv_words = pd.DataFrame(cv_mat.todense(),columns=count_vect.get_feature_names_out())


# In[19]:


df_cv_words.head()


# In[20]:


cosine_sim_mat = cosine_similarity(cv_mat)


# In[21]:


cosine_sim_mat


# In[22]:


df.head()


# In[23]:


course_indices = pd.Series(df.index,index=df['course_title']).drop_duplicates()


# In[24]:


course_indices


# In[39]:


def recommend_course(title,num_of_rec=5):
    # ID for title
    idx = course_indices[title]
    scores = list(enumerate(cosine_sim_mat[idx]))
    sorted_scores = sorted(scores,key=lambda x:x[1],reverse=True)
    selected_course_indices = [i[0] for i in sorted_scores[1:]]
    selected_course_scores = [i[1] for i in sorted_scores[1:]]
    result = df['course_title'].iloc[selected_course_indices]
    rec_df = pd.DataFrame(result)
    rec_df['similarity_scores'] = selected_course_scores
    return rec_df.head(num_of_rec)


# In[41]:


recommend_course('Trading Options Basics')


# In[42]:


df.to_csv("udemy_courses_clean.csv")

pickle.dump(regressor, open('model.pkl','wb'))

# In[ ]:




