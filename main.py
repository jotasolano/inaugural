import nltk
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
    print(df)
    # df.to_csv(os.path.join(dir_name, str(concept[0]) + "." + suffix))


# the 'seed' tokens for every concept
unityT = ['unity', 'together', 'solidarity', 'confederation']
democracyT = ['democracy', 'people', 'republic', 'state', 'freedom', 'nation']
successT = ['success', 'innovation', 'progress', 'win', 'technology']
immigrationT = ['immigration, migrant', 'foreigner', 'settler', 'invader']
terrorismT = ['terror', 'terrorism', 'fear', 'islam', 'communist', 'attack', 'threat']
warT = ['war', 'battle', 'nuclear', 'invasion', 'gun', 'weapon', 'tyranny']

# the final 'words'  #this isn't working!
unityW = [synset.name().split('.')[0].split('_')[0] for token in unityT for synset in wn.synsets(token, 'n') ]
unityW.insert(0,"unity")

democracyW = [synset.name().split('.')[0].split('_')[0] for token in democracyT for synset in wn.synsets(token, 'n') ]
democracyW.insert(0, 'democracy')

successW = [synset.name().split('.')[0].split('_')[0] for token in successT for synset in wn.synsets(token, 'n') ]
successW.insert(0, 'success')

immigrationW = [synset.name().split('.')[0].split('_')[0] for token in immigrationT for synset in wn.synsets(token, 'n') ]
immigrationW.insert(0, 'immigration')

terrorismW = [synset.name().split('.')[0].split('_')[0] for token in terrorismT for synset in wn.synsets(token, 'n') ]
terrorismW.insert(0, 'terror')

warW = [synset.name().split('.')[0].split('_')[0] for token in warT for synset in wn.synsets(token, 'n') ]
warW.insert(0, 'war')

listOfWords = [immigrationW]

# listOfWords = [unityW, democracyW, successW, immigrationW, terrorismW, warW]


# lets run the function on a loop
for item in listOfWords:
    frequencies(inaugural, item)

