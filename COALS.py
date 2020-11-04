#You may need to enable these two commandes if your punkt isn't installed
#once dowloaded and installed nltk will work perfectly fine
#import nltk
#nltk.download('punkt')

'''
    Imports:
        - re.sub: function that alllow as to delete portions of text that are or not in the text
        - math library for math computing
        - The nltk tokenizer is used to split the text into words
    ---------
    Variables returned:
        -a Python Dictionnary is stored as a json file in the same path of this code file
    ---------
    Structure of the file:
        -Containes function of cleaning, weight computing and semantic space
'''

from re import sub #https://docs.python.org/3/library/re.html
import math as m 
from nltk.tokenize import word_tokenize
import os
import json

#funct to compute stopwords in a text
def StopWords(Text):
    #opening file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'Stopwords.txt')
    read_file = open(my_file, "r", encoding="utf-8")

    File = read_file.read()
    
    #geting lists of: total input wordslist, stopwords from the file.
    WordsList = word_tokenize(Text)
    StopWords = word_tokenize(File)

    #a variable to store the stowords found
    StopsIn = []


    #looping over each word
    for word in WordsList:
        if word in StopWords:
            #if the word is consider as a stopword, we remove it from the input text
            WordsList.pop(WordsList.index(word))
            if word not in StopsIn:
                #if the word found hasn't being saved yet, we save it in StopsIn list
                StopsIn.append(word)

    #rewriting the text
    newText = ""
    for word in WordsList:
        newText = newText + " " + word

    #returning a dict of the new text and the list of stops
    return {"newText" : newText, "StopsIn" : StopsIn}

#funct to clean data, delet stopwords and other non-text elements
def Clean(Text):
    #first stop words elimination
    NoStop = StopWords(Text)
    Text = NoStop["newText"]
    #numbers and special caracteres 
    Text = sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+',' ', Text)
    Text = sub(r'[0-9?]', ' ',Text)
    Text = word_tokenize(Text)

    #returning new text
    return Text


#funct to compute weights of words pairs
def poid(txt):
    WORDS = txt.split()
    NWORDS = []
    for i in range(len(WORDS)):
      if len(NWORDS) !=20000:
        if WORDS[i] not in NWORDS:
          NWORDS.append(WORDS[i])
      else:
        print(len(NWORDS))
        
    print(NWORDS)
    
    #saving words
    WordsList = ""
    for i in range(len(NWORDS)-1):
        WordsList = WordsList + NWORDS[i]+"\n"	
    


    #Creating a matrix of words
    FREQ = [[0 for j in range(0,len(NWORDS))] for FREQ in range(0,len(NWORDS))]

  
    try:
        #weights processing
      for i in range(len(WORDS)):

        if i < len(WORDS) - 4:
            for f in range(1, 5):
                FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i + f])] += (5 - f)

        elif i < len(WORDS) - 3:
            for f in range(1, 4):
                FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i + f])] += (5 - f)


        elif i < len(WORDS) - 2:
            for f in range(1, 3):
                FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i + f])] += (5 - f)


        elif i < len(WORDS) - 1:
            FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i + 1])] += 4

        if i >= 4:
            for f in range(1, 5):
                FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i - f])] += (5 - f)

        elif i >= 3:
            for f in range(1, 4):
                FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i - f])] += (5 - f)


        elif i >= 2:
            for f in range(1, 3):
                FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i - f])] += (5 - f)

        elif i >= 1:
            FREQ[NWORDS.index(WORDS[i])][NWORDS.index(WORDS[i - 1])] += 4
    except:
       print("no index")


#to print the matrix
# print("la matrice de co-occurence")

#returning frequecy, nwords and the words list
    return FREQ, NWORDS, WordsList


#funct to compute correlation between words
def corr(FREQ,NWORDS):
    som = 0      #sum of matrix elements
    #summing ...
    for i in range(len(NWORDS)):
        for j in range(len(NWORDS)):
            som += FREQ[i][j]

    # vector contains columns summation
    v = [0 for i in range(len(FREQ))]
    for i in range(len(FREQ)):
        for j in range(len(FREQ)):
            v[i] += FREQ[i][j]

    # computing values ..
    for i in range(len(FREQ)):
        for j in range(len(FREQ)):
          try:
            FREQ[i][j] = round(((som * FREQ[i][j])-(v[i] * v[j])) / m.sqrt(v[i] * (som-v[i]) * v[j] * (som-v[j])),3)
          except:
            FREQ[i][j]=0

    for i in range(len(FREQ)):
        for j in range(len(FREQ)):
            if FREQ[i][j] > 0:
                FREQ[i][j] = round(m.sqrt(FREQ[i][j]),3)
            else:
                FREQ[i][j] = 0

    #returning correlated frequecies
    return FREQ

#saving matrix in a dict "words : vector line"
def save(FREQ, Words):
    WordsList = Words.splitlines()
    Lines = []
    for i in range(len(FREQ)):
        Line = ""
        for j in range(len(FREQ)):
            Line = Line + str(FREQ[i][j]) + " "
        Lines.append({WordsList[i] : Line[0:len(Line)-2]})
    return Lines


def fromTxt(Path):
    with open(Path, "r") as Text:
        return Text.read()
        
#general funct to call al the other segmants of the code
def getSemSpace(Text):
    newText = Clean(Text)
    ES,NWORDS,WordsList = poid(newText)
    ES=corr(ES,NWORDS)
    Dict = {}

    #returning a dict containing semantic space and the words list
    Dict = {"Matrix" : save(ES, WordsList), "Words" : word_tokenize(WordsList)}

    #Saving into a json file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER,'COALS.json')

    write_file = open(my_file, "w")
    json.dump(Dict, write_file, indent=2)
    write_file.close()

