#Cheung Lap Yan 12/07/15, CSCI-UA.0002-005, Assign 10 PART 3

import random

#read data
file_object=open('Thesaurus.txt','r')
#split data by line
all_words=file_object.read()
words=all_words.split('\n')
#create dictionary and make the first word of each line the key
thesaurus={}
#iterate through words and synonym
for w in words:
    #create a list when each line is iterated, dividing word with
    #synoymn
    each_word=w.split(',')
    new_entry=each_word[0]
    #make subsequent words values in list, use len function
    synonym=[]
    for s in range(1,len(each_word)):
        synonym=synonym+[each_word[s]]
    #store synonyms in dictionary
    thesaurus[new_entry]=synonym
#Report total number of words in thesaurus
print('Total words in thesaurus: ',len(thesaurus))
print()

#Ask user for frequency of word substitution
user_chance=float(input('Enter a % chance to change a word (0-0.99): '))
#open lyrics file
bieber_object=open('bieber_baby.txt','r')
ori_lyrics=bieber_object.read()
clean_lyrics=''
#clean up lyrics file
for words in ori_lyrics:
    if words.isalpha() or words.isspace():
        clean_lyrics+=str.lower(words)
#use cleaned lyrics
phrase_user=clean_lyrics
phrase=''
#remove punctuation
for n in phrase_user:
    if n.isalpha() or n.isspace():
        phrase+=n
#check if any word is in thesaurus
#split each word for analysis, store each word in list
words=phrase.split(' ')
new_phrase=''
for w in words:
    #determine chance of modifying word
    chance=1//user_chance
    prob=random.randint(1,chance)
    if prob==1:
        #replace word with synonyms in uppercase
        try:
            if w in thesaurus.keys():
                new_word=thesaurus[w]
                #randomize synonym choice
                choice=random.randint(0,len(new_word))
                #replace word
                replace=new_word[choice-1].upper()
                new_phrase+=(replace+' ')
            else:
                #return original word if no synonym is detected
                new_phrase+=(w+' ')
        except:
            new_phrase+=(w+' ')
    else:
        new_phrase+=(w+' ')

#print updated song
print(new_phrase)       
