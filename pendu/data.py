# -*- coding:UTF-8 -*
#Created by SuXes, this 28/10/2018
"""
    The second Project from the same book
    to vaidate the second part of the book.
    It is a game. A claasical words game.
    """
initial_text = "In my teaching both at the University of Washington and at various tech-focused\
conferences and meetups, one of the most common questions I have heard is this: \
“how should I learn Python?” The people asking are generally technically minded \
students, developers, or researchers, often with an already strong background in writing \
code and using computational and numerical tools. Most of these folks don’t want \
to learn Python per se, but want to learn the language with the aim of using it as a \
tool for data-intensive and computational science. While a large patchwork of videos, \
blog posts, and tutorials for this audience is available online, I’ve long been frustrated \
by the lack of a single good answer to this question; that is what inspired this book. \
The book is not meant to be an introduction to Python or to programming in general; \
I assume the reader has familiarity with the Python language, including defining \
functions, assigning variables, calling methods of objects, controlling the flow of a \
program, and other basic tasks. Instead, it is meant to help Python users learn to use \
Python’s data science stack—libraries such as IPython, NumPy, Pandas, Matplotlib, \
Scikit-Learn, and related tools—to effectively store, manipulate, and gain insight \
from data."
words_list = initial_text.split(" ")
words_list = [word.replace(".","").replace(",","").replace("?","").replace(" ","").replace("'","").replace(":","").lower() for word in words_list]
#print(words_list)
word_lenght = 8
words_list = [word for word in words_list if len(word)<=word_lenght]
scores_file_name = "my_scores"
#for word in words_list:
#    print (len(word))
#print(words_list)

