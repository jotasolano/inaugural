import nltk
# import inspect
# import matplotlib as plot
# from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import inaugural
import numpy as np
import pandas as pd
import os.path

# variables for filename creation
dir_name = '~/Desktop/concepts/'
suffix = 'csv'


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


# the 'seed' tokens for every concept
unityT = ['unity', 'together', 'solidarity', 'confederation']
democracyT = ['democracy', 'people', 'republic', 'state', 'freedom', 'nation']
successT = ['success', 'innovation', 'progress', 'win', 'technology']
immigrationT = ['immigration, migrant', 'foreigner', 'settler', 'invader']
terrorismT = ['terror', 'terrorism', 'fear', 'islam', 'communist', 'attack', 'threat']
warT = ['war', 'battle', 'nuclear', 'invasion', 'gun', 'weapon', 'tyranny']

# the final 'words'  #this isn't working!
unityW = ['unity', [synset.name().split('.')[0].split('_')[0] for token in unityT for synset in wn.synsets(token, 'n') ]]
democracyW = ['democracy', [synset.name().split('.')[0].split('_')[0] for token in democracyT for synset in wn.synsets(token, 'n') ]]
successW = ['success', [synset.name().split('.')[0].split('_')[0] for token in successT for synset in wn.synsets(token, 'n') ]]
immigrationW = ['immigration', [synset.name().split('.')[0].split('_')[0] for token in immigrationT for synset in wn.synsets(token, 'n') ]]
terrorismW = ['terror', [synset.name().split('.')[0].split('_')[0] for token in terrorismT for synset in wn.synsets(token, 'n') ]]
warW = ['war', [synset.name().split('.')[0].split('_')[0] for token in warT for synset in wn.synsets(token, 'n') ]]


listOfWords = [unityW, democracyW, successW, immigrationW, terrorismW, warW]


# lets run the function on a loop
# for item in listOfWords:
#     frequencies(inaugural, item)

