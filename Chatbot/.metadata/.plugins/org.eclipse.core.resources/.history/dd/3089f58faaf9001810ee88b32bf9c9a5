# coding: utf-8

import nltk
import warnings
warnings.filterwarnings("ignore")

import random
import string


f=open('chatbot.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# mettre la casse en minuscules
sent_tokens = nltk.sent_tokenize(raw)# conversion en liste de phrases 
word_tokens = nltk.word_tokenize(raw)# conversion en liste de mots


sent_tokens[:2]


word_tokens[:5]


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("bonjour", "salut", "yo", "slt", "hello","hey",)
GREETING_RESPONSES = ["salut !", "hey !", "Baisse les yeux", "Hi there (General Kenobi)", "T'as de la chance, je suis d'humeur", "J'espere que t'as une bonne raison de venir me parler"]



# Checking for greetings
def greeting(sentence):
    """Si l'utilisateur dit bonjour, souhaiter la bienvenue"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='french')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"Je suis desole, je ne comprends pas"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag=True
print("VeganOS: Je m'appelle VeganOS. Si tu es un carniste oppresseur, pas besoin de venir me parler")

while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='merci' or user_response=='merci !' ):
            flag=False
            print("VeganOS: Avec plaisir !")
        else:
            if(greeting(user_response)!=None):
                print("VeganOS: "+greeting(user_response))
            else:
                print("VeganOS: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
print("VeganOS: A plus ! Oublie pas d'acheter des graines de courge pour ce soir :)") 