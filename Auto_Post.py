import docx
import random
import tweepy
from API_Keys import API_key, secret_key, access_token, secret_access_token

def first_filter(doc):
    doc1 = docx.Document(doc)
    i = 128
    string = []
    while i < 3646:
        string.append(doc1.paragraphs[i].text)
        i += 1
    while '' in string:
        string.remove('')
    return string

def remove_spaces(ff):
    quote = ""
    quotes_list = []
    for text in ff:
        try:
            text == int(text)
            quotes_list.append(quote)
            # print(quote)
            quote = ""
        except ValueError:
            quote += f"{text} "
    return quotes_list

def tweeter(API_key, secret_key, access_token, secret_access_token):
    auth = tweepy.OAuthHandler(API_key, secret_key)
    auth.set_access_token(access_token, secret_access_token)
    return tweepy.API(auth)


doc = ("Inspirational Quotes.docx")
ff = first_filter(doc)
new_list = remove_spaces(ff)
random.shuffle(new_list)
random_quote = (new_list[0])
access = tweeter(API_key, secret_key, access_token, secret_access_token)
access.update_status(f"{random_quote}")
print("Tweet Successful")

