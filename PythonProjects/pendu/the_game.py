# -*- coding:latin-1 -*
#Created by SuXess, this 28/10/2018
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
    new_game(score)

def get_name():
    text_to_print = "Hello ! Welcome ! I am Smart, your new words game\n\
You already know the rules. but I will remind them to you !\n\
I choose a 8_letter word and you have to guess it. You have 8 attempts.\n\
You begin with 8 points and for each wrong attempt you lose 1 point.\n\
Your score at the end of the game will be the points you got.\n\
The game ends when you have 0 point and you loose.\n\
Press the 'Enter' key if you are ready to start.\n"
    print(text_to_print.center(len(text_to_print)))
    #os.system('pause')
    return input_name()

def input_name():
    name = input("What is your name please : ")
    try :
        int(name)
        #if the name is not a string
        print("Please Enter a name !\n")
        input_name()
    except ValueError :
        pass
    return name

def get_score(name):
          score = get_score_from_file()
          return score
    

def print_score(name,score):
    print("{} ! Your previous score is : {}\n".format(name,score))


def new_game(score):
    print("let's play!\n")
    word = choose_random_word()
    interact_with_user(word,score)


def choose_random_word():
    words_list = data.words_list
    index = random.randrange(len(words_list)-1)
    word = words_list[index]
    return word


def interact_with_user(word,score):
    print("The word is a {}-letter word\n".format(len(word)))
    formatted_word = ""
    i = 0
    while i <= len(word):
        formatted_word+=str("*")
        i+=1
    process_input(word,formatted_word)


def process_input(word,formatted_word):
    count = 1
    succes = False
    lose = False
    print("We are processing input now")
    while count <= (data.word_lenght and not succes) or not lose:
        print("The word is {}".format(formatted_word))
        choice = input("Guess a letter : ")
        formatted_word = process(choice,word,formatted_word)
        attempts_left = data.word_lenght-count
        if 1 < count <= data.word_lenght :
            print("Letter {} is not in the word.\n You have {} attempts left".format(choice,attempts_left))
        if count == data.word_lenght :
            print("You have lost, the real word was {}".format(word))
            lose = True
        if formatted_word==word:
            sucess = True
        count+=1
    score = data.word_lenght-count
    print("Your score is : {}".format(score))


def process(choice,word,formatted_word):
    index = word.find(choice)
    if index != -1 :
        print("A right letter chosen\n")
        formatted_word = formatted_word[:index]+choice+formatted_word[index+1:]
    return formatted_word


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



#    splitted_word = [letter for letter in word]
#    for letter in splitted_word :
#       if letter == choice :
#            formatted_word=[:splitted_word.po
        



    
if __name__=="__main__" :
    game()





