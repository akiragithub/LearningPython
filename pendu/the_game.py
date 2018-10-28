# -*- coding:latin-1 -*
#Created by SuXes, this 28/10/2018
"""
    The second Project from the same book
    to vaidate the second part of the book.
    It is a game. A claasical words game.
    """
import data
import os
import data
import pickle
import random

def game():
    name = get_name()
    score = get_score(name)
    print_score(name,score)
    new_game()

def get_name():
    text_to_print = "Hello ! Welcome ! I am Smart, your new words game\n\
You already know the rules. but I will remind them to you !\n\
I choose a 8_letter word and you have to guess it. You have 8 attempts.\n\
You begin with 8 points and for each wrong attempt you lose 1 point.\n\
Your score at the end of the game will be the points you got.\n\
The game ends when you have 0 point and you loose.\n\
Press the 'Enter' key if you are ready to start.\n")
    print(text_to_print.center(len(text_to_print))
    os.system('pause')
    return input_name()

def input_name():
    name = input("What is your name please : ")
    try :
        int(name)
    except ValueError :
        print("Please Enter a name !\n")
        input_name()
    return name

def get_score(name):
    return get_score_from_file() 
    

def get_score_from_file():
    scores_file_name_1 = data.scores_file_name
    last_score = 0 #initializing default score
    scores = dict()
    try :
        with open(scores_file_name_1,'rb') as scores_file:
            unpickler = pickle.Unpickler(scores_file)
            scores = unpickler.load()
            if score[name] != None :
                last_score = scores[name]
    except :
        print("There was an error")
    print("Last score : {}".format(last_score))
    return int(last_score)


def print_score(name,score):
    print("{} ! Your previous score is : {}\n".format(name,score))

def new_game(score):
    print("let's play!\n")
    word = choose_random_word()
    interact_with_user(word,score)

def choose_random_word():
    words_list = data.words_list
    index = random.randrange(len(data)-1)
    word = words_list[index]
    return word

def interact_with_user(word,score):
    print("The word is a {}-letter word\n".format(len(word)+1).center())
    formatted_word = ""
    i = 0
    while i <= len(word):
        formatted_word+=str("*")
    process_input(word,formatted_word)

def process_input(word,formatted_word):
    count = 1
    succes = False
    while count <= data.word_lenght and not succes:
        print("The word is {}\n".format(formatted_word).center)
        choice = input("Guess a letter : ")
        formatted_word = process(choice,word,formatted_word)
        count+=1
        if formatted_word==word:
            sucess = True
    score = data.word_lenght-count
    print("Your score is : {}".format(score))

def process(choice,word,formatted_word):
    index = word.find(choice)
    if index != -1 :
        print("A right letter chosen\n")
        formatted_word = formatted_word[:index]+choice+formatted_word[index+1:]
    return formatted_word


#    splitted_word = [letter for letter in word]
#    for letter in splitted_word :
#       if letter == choice :
#            formatted_word=[:splitted_word.po
        



    
if __name__=="__main__" :
    game()





