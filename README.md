# AMERICAN POETRY CORPUS FOR RESEARCHES
#### Video Demo:  <https://youtu.be/o6OFpsjbKts>
#### Description:

Dear developer/user/researcher!

Welcome to American poetry corpus! This project was developed for linguists and literary critics,
who study American poetry of the 20th century. The idea of creating the corpus of poetic texts came
to my mind after the long experience of conductinп researches on the material of different literary
text. My colleagues and I had to search for needed words and expressions in huge text massives and
rewrite them manually. And after such tedious procedure we tried to make some calculations (which, as
you can imagine were not accurate enough) with the obtained material (to define the most frequent
words/nouns/adjectives and etc, to find out what word groups/syntactic expressions are the most
significant in percentage terms and many other calculations).
When I started to get acquainted with the possibilities of programming in python, it became increasingly
clear to me, that the very process of linguistic/literary research could be optimized. As a result, I
managed to make a program, which allow a researcher to save great amount of time and concentrate on
the actual intellectual tasks, on the interpretation of the statistical parameters. The program calculates
the whole number of the words and the number of original (non-repeating) words in a chosen file. Also it has
the functions, which display lists of the most frequent words/nouns/adjectives/verbs (the length of the list -
of the user's choosing). Finally, the program shows all the contexts, where the chosen word occurs with the
accurate number of its occurrences (if the user needs it).
A big advantage of the program, from my point of view, is a possibility to add any other author to the existing
collection (here we have just three collections of poetry: "The Colossus" by Silvia Plath,"Harmonium" by Wallace
Stevens and "New Hampshire" by Robert Frost). If you, as the user of the program and as the developer, do not interested
in American poetry particularly or in literary texts at all, you can replace proposed files with
any English text you like. The software will make all the necessary calculations on a new text material. You just
need to change the name of the files in a code body.
Let us discuss sometechnical peculiarities of the program.
The first and the most complicated task for me was to design a function, which is able to tokenize text. Initially,
I tried to explain to computer, what the word actually is with the help of the RegexTokenizer - the instrument of
the nltk library. My own regular expression for words in poetic text was quite massive and cryptic
(RegexpTokenizer(r'([A-Za-z]+)(\'[A-Za-z]+)?(\-[A-Za-z]+)?(\-[A-Za-z]+)?(\'s)?')).Fortunately, after
a while, I found out the information about textblob lybrary, which has a method called "words" and
tokenized a proposed text relatively correctly, taking Englis hgrammar and punctuation into account.
Also, textblob library gives an opportunity to make part of speech tagging automatically (with the help
of the method called "tags"). Despite the above mentioned advantages of the textblob lybrary method,I had
to turn back to nltk library, because only with the help of its WordNetLematizer class I managed to
get correct verb lemmas (initial forms). In order to find the most frequent words/nouns/adjectives/verbs
I used the class Counter (from collections library) and its method called "most_common()".Before that
I tried to create my own counter, based on dictionaries. It worked as correctly as above mentioned method,
but the code looked too lengthy.
Moreover, it should be mentioned. that I didn't removed so-called "stopwords"
/"grammatical words" from the texts (what specialists in NLP strongly recommend to do), because as
a professional linguist I can say for sure, that pronouns, prepositions, conjunctions and etc. have
meanings and are extremely important parts of the text. If you want to study some author's
style realistically, you should definitely take all the words into consideration.To start working with
the program you need to install textblob, nltk.stem, collections, sys, pprint and re libraries.
I really hope that you will enjoy the process of studying poetry (or any other) texts! I am open
to good advice from more experienced programmers and collaboration!


