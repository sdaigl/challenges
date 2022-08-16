#!/usr/bin/python3
import requests, json
'''
Devnet challange activity no 2
#https://icanhazdadjoke.com/api
'''

print('Welcome to dadjokes')
word_to_search = input('Enter a word for specific dadjoke subject - Pressing enter will give you a random joke: ')

if word_to_search == "" :
    ########### GLOBALS ###########
    URL = "https://icanhazdadjoke.com"
    PATH = "/"
    QUERY = ""
    HEADERS = "Accept: application/json"
    ################################
    uri=URL+PATH+QUERY+word_to_search
    #print(uri)
    resp=requests.get(uri,headers={"Accept": "application/json"})
    json_data=resp.json()
    print(json_data['joke'])
    
else :
    ########### GLOBALS ###########
    URL = "https://icanhazdadjoke.com"
    PATH = "/search?"
    QUERY = "term="
    HEADERS = "Accept: application/json"
    ################################
    uri=URL+PATH+QUERY+word_to_search
    #print(uri)
    resp=requests.get(uri,headers={"Accept": "application/json"})
    json_data=resp.json()
    totaljokes=json_data['total_jokes']
    #print ("Total_jokes: ",totaljokes)
    # limit to first page since it's 20 by default

    if totaljokes > 20 : totaljokes = 20
    for n in range (0,totaljokes):
        print(json_data['results'][n]['joke'])

