# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:54:11 2018

@author: Minh Bach, Tram Ho
Do something"""

"""testing again and again"""

import pandas as pd
import numpy as np

#Set work dir
dir=
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
            page = requests.get(url, timeout=10) #Check the timeout here
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
#with open('html_chunks', 'rb') as f:
#    html_chunks = pickle.load(f)
    

##2.2. Merge chunks


##2.3. Save as pickle    


#3. Preprocess text - Tram
##3.1. Detect language
    
    
##3.2. Translate


##3.3. Basic processing     

#4. Cluster
##4.1. Transform with pretrained TF-IDF


##4.2. Cluster with pretrained model
    
    
#5. Chunk and save chunks
##5.1. Chunk of size 200


##5.2 Save each chunk as .xlsx    