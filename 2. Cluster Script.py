# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:54:11 2018

@author: Minh Bach, Tram Ho
"""


import pandas as pd
import numpy as np

#Set work dir
dir =
import os
os.chdir(dir)


#0. Load data
data = 

df = data[['G2 ID', 'G2 Verified URL']]


#1. Crawl
##1.1. Chunk data
def chunker(df, size):
    '''This function chunks dataframe into smaller chunks
       Input: df = dataframe
       Output: generator object'''
       
    return (df[pos:pos + size] for pos in range(0, len(df), size))


size = 500
chunks = [chunk for chunk in chunker(df, size)]


##1.2. Crawl html
import requests
import numpy as np

def get_html(urllist):
    """This function takes in a list of urls and return the html_list
       Input: a list of url
       Output: a tuple of html list and inaccessible url list"""
    
    html = []
    inaccessible_url = []
    i=1
    
    for url in urllist: 
        try:
            page = requests.get(url, timeout=10) 
            content = page.text
            html.append(content)
            print('finish step '+str(i))
            i += 1
        except:
            inaccessible_url.append(url)
            html.append(np.nan)
            print('Exception occur when retrieve:', url)
            i += 1
            
    return (html, inaccessible_url)


html_chunks = [] #This variable stores a list of dataframes, each dataframe is a chunk
i = 1
for chunk in chunks:
    
    html_list, inaccessible_url = get_html(chunk['G2 Verified URL'])
    
    html_chunk = pd.DataFrame({'G2 ID': chunk['G2 ID'],
                               
                            'G2 Verified URL': chunk['G2 Verified URL'],
                            
                            'html':html_list})
    
    html_chunks.append(html_chunk)
    
    print('finish chunk ' + str(i))
    i += 1


##1.3. Save list html_chunks as pickle
import pickle
with open('html_chunks', 'wb') as f:
    pickle.dump(html_chunks, f)
    

#2. Get text - Minh
##2.1. Strip tags


## Only use these if need to reload the data at this step
#with open('html_chunks.pkl', 'rb') as f:
#    html_chunks = pickle.load(f)


from bs4 import BeautifulSoup

def get_text_bs(html):
    '''this function strips all the tags from the html'''
    tree = BeautifulSoup(html, 'lxml')

    body = tree.body
    
    if body is None:
        return None

    for tag in body.select('script'):
        tag.decompose()
        
    for tag in body.select('style'):
        tag.decompose()

    text = body.get_text(separator='\n')
    
    return text    


### Apply the function
i = 1

for chunk in html_chunks:
    
    chunk['text'] = [get_text_bs(i) for i in chunk['html']]
    
    ### Strip all space 
    chunk['text'] = chunk['text'].str.replace(r'\r|\n|\t|(\xa0)',' ').str.lstrip().str.rstrip()
    
    print('finish chunk ' + str(i))
    i += 1

text_chunks = html_chunks


##2.2. Merge chunks
text_df = pd.concat(text_chunks)

##2.3. Save as pickle    
text_df.to_pickle('text_df.pkl')


#3. Preprocess text - Tram


## Only use these if need to reload the data at this step
#with open('text_df.pkl', 'rb') as f:
#    text_df = pickle.load(f)


##3.1. Detect language
    
    
##3.2. Translate


##3.3. Basic processing     


#4. Cluster - Tram
##4.1. Transform with pretrained TF-IDF


##4.2. Cluster with pretrained model
    
    
#5. Chunk and save chunks - Minh
##5.1. Chunk of size 200


##5.2 Save each chunk as .xlsx

    