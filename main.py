import nltk
import inspect
import matplotlib as plot
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import inaugural
import numpy as np
import pandas as pd
import os.path


# the 'seed' tokens for every concept
unityT = ['unity', 'together', 'solidarity', 'confederation']
democracyT = ['democracy', 'people', 'republic', 'state', 'freedom', 'nation']
successT = ['success', 'innovation', 'progress', 'win', 'technology']
immigrationT = ['immigration, migrant', 'foreigner', 'settler', 'invader']
terrorismT = ['terror', 'terrorism', 'fear', 'islam', 'communist', 'attack', 'threat']
warT = ['war', 'battle', 'nuclear', 'invasion', 'gun', 'weapon', 'tyranny']


# variables for filename creation
dir_name = '~/Desktop/'
suffix = 'csv'
listy = [unityT, democracyT]

# the frequency finding function
def frequencies(source, concept):
    cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in source.fileids()
        for w in source.words(fileid)
        for target in [synset.name().split('.')[0].split('_')[0] for token in concept for synset in wn.synsets(token, 'n') ]
        if w.lower().startswith(target))
        
    df = pd.DataFrame(cfd)
    df.to_csv(os.path.join(dir_name, str(concept[0]) + "." + suffix))

frequencies(inaugural, unityT)
# frequencies(inaugural, democracyT)


# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in [synset.name().split('.')[0].split('_')[0] for token in unityT for synset in wn.synsets(token, 'n') ]
#     if w.lower().startswith(target))

# # print(cfd.tabulate())

# df = pd.DataFrame(cfd)
# print(df.head())


