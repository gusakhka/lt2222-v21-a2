import sys
import os
import numpy as np
import numpy.random as npr
import pandas as pd
import random

# Module file with functions that you fill in so that they can be
# called by the notebook.  This file should be in the same
# directory/folder as the notebook when you test with the notebook.

# You can modify anything here, add "helper" functions, more imports,
# and so on, as long as the notebook runs and produces a meaningful
# result (though not necessarily a good classifier).  Document your
# code with reasonable comments.

# Function for Part 1
import sys
import os
import numpy as np
import numpy.random as npr
import pandas as pd
import random
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import string
import re



def preprocess(inputfile):
    lemmatizer = WordNetLemmatizer()
    ps = PorterStemmer()
    contents = [x.strip().split("\t") for x in inputfile.readlines()]
    #Filter out remaining items that are not alphabetic.
    c_contents = [l for l in contents if l[2].isalpha()]
    #''.join([i for i in raw_file if not i.isdigit()])

    
    rows = []
    for row in c_contents[1:]:
        row[2] = ps.stem(row[2])
        row[2] = lemmatizer.lemmatize(row[2].lower())
        row[2] = re.sub(r'[^\w\s]','',row[2])
        rows.append(row)
    
    clean_rows = []    
    for line in rows:
        if (line[2] != ""):
            clean_rows.append(line)
            

                 
    col = ['WordN', 'SentN', 'Word', 'Pos', 'Type']
    return pd.DataFrame(clean_rows, columns = col)


# Code for part 2
import re
class Instance:
    def __init__(self, neclass, features):
        self.neclass = neclass
        self.features = features

    def __str__(self):
        return "Class: {} Features: {}".format(self.neclass, self.features)

    def __repr__(self):
        return str(self)



def create_instances(data):
    instances = []
    sent_num = list(data['SentN'])
    word = list(data['Word'])
    type_ent = list(data['Type'])
    tuples_ent = list(zip(sent_num, word, type_ent))
    for index, tup in enumerate(tuples_ent):
        features = []
        last_features = []
        if tup[2].startswith('B'):
            neclass = re.sub('B-', '', tup[2])
            for i in reversed(list(range(1, 6))): #the 5 freatures before the word with a NE
                if index-i > 0:
                    if tuples_ent[index-i][0] == tup[0]:
               
                        features.append(tuples_ent[index-i][1]) #Append the word
                    else:
                        features.append("<s>")
                else:
                    features.append("<s>")
            counter = 1
            while tuples_ent[index+counter][2].startswith('I'):
                counter += 1

            for j in range(1, 6):#the 5 freatures after the word with a NE
                if j+index+counter < len(tuples_ent):
                    if tuples_ent[index+j+counter][0] == tup[0]:
          
                        last_features.append(tuples_ent[index+j+counter][1]) #Append the word
                    else:
                        last_features.append("<e>")

                    
                else:
                    last_features.append("<e>")

            features.extend(last_features) 
            instances.append(Instance(neclass, features))
    return instances
    

# Code for part 3
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

def create_table(instances):
    features_items = []
    for instance in instances:
        for feature in instance.features:
            if feature not in features_items:
                features_items.append(feature)
    data = []
    for instance in instances:
        for feature in instance.features:
            data += [[instance.neclass] + [feature.count(word) for word in features_items]]
    features_items = ["class"] + features_items
    df = pd.DataFrame(data, columns = features_items)
    red_df = reduce(df)
    return red_df

def reduce(matrix, dims=300):
    data= matrix.copy()
    df_x = data.iloc[:,1:] #full matrix without the first column
    df_y = data.iloc[:,0]  # file name column
 
    col_names = df_x.columns.tolist() #here I put the name of column in the df_x
    feature_names = col_names
  
    svd = TruncatedSVD(n_components=dims, n_iter=7, random_state=42)
    svd = svd.fit(df_x)

    mat_r = svd.transform(df_x)
    
  
    return pd.concat([pd.DataFrame(df_y), pd.DataFrame(mat_r)], axis=1)

def ttsplit(bigdf):
    train = bigdf.sample(frac=0.8)
    df_train = train.reset_index()
    df_test = bigdf.drop(train.index).reset_index()
    
    
       
    return df_train.drop('class', axis=1).to_numpy(), df_train['class'], df_test.drop('class', axis=1).to_numpy(), df_test['class'], df_test.drop('class', axis=1).to_numpy(), df_test['class']

# Code for part 5
from sklearn.metrics import confusion_matrix as cm
def confusion_matrix(truth, predictions):
    labels = ['art','eve','geo','gpe','nat','org','per','tim']
    matrix = cm(truth, predictions, labels = labels )
    df = pd.DataFrame(matrix, index = labels, columns = labels)
    return df
    

# Code for bonus part B
def bonusb(filename):
    pass
