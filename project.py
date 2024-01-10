from textblob import TextBlob
from textblob import Word
from nltk.stem import WordNetLemmatizer
from collections import Counter
import sys
import pprint
import re

def main():
    while True:
        print('''Dear researcher! Wecome to American poetry corpus!
Here we have three collections of poetry: "The Collosus" by Silvia Plath,
"Harmonium" by Wallace Stevens and "New Hampshire" by Robert Frost.
Which author would you like to study now?''')
        while True:
            poet = input("Please, choose among Silvia Plath, Wallace Stevens and Robert Frost: ")
            print()
            if poet in ['Silvia Plath', 'Wallace Stevens', 'Robert Frost']:
                print(f"Excellent! Let's get aquainted with some statistical parameters of {poet}'s poetry.")
                print()
                break
            else:
                print("Sorry, the input is incorrect. Please, try again")
                continue
        name, surname = poet.split()
        file = f"{surname}.txt"
        text = open(file).read().lower().replace("'s", "")
        blob_object = TextBlob(text)
        tokens = blob_object.words
        num_words = counting(tokens)
        set_words = original(tokens)
        print(f"The total number of words in {poet}'s collection of poetry: {num_words} words")
        print(f"The number of original words in {poet}'s collection of poetry: {set_words} words")
        print()
        while True:
            print(f"What else do you want to know from {poet}'s collection of poetry?")
            choice = input('''Please, choose the number among the proposed variants:
1 - the most frequent words in the text;
2 - the most frequent nouns in the text;
3 - the most frequent adjectives in the text;
4 - the most frequent verbs in the text;
5 - the contexts, in which the chosen word occurs;
6 - to return to the beginning and choose a new author for research;
7 - nothing;
Enter a number here:  ''')
            print()
            if choice == "1":
                while True:
                    number = input("Please, choose the number of the most frequent words: ")
                    try:
                        common = Counter(tokens).most_common(int(number))
                        print(f"These are {number} most common words in {poet}'s collection of poetry:")
                        print()
                        i = 0
                        for common_word in common:
                            i += 1
                            pprint.pprint(f"{i} {common_word}")
                        print()
                        break
                    except ValueError:
                        print("Sorry, the input is incorrect. Please, enter a number.")
            elif choice == "2":
                while True:
                    number1 = input("Please, choose the number of the most frequent nouns: ")
                    try:
                        tagged = blob_object.tags
                        nouns = noun(tagged)
                        common_nouns = Counter(nouns).most_common(int(number1))
                        print(f"These are {number1} most frequet nouns:")
                        print()
                        i = 0
                        for common_noun in common_nouns:
                            i += 1
                            pprint.pprint(f"{i} {common_noun}")
                        print()
                        break
                    except ValueError:
                        print("Sorry, the input is incorrect. Please, enter a number.")
            elif choice == "3":
                while True:
                    number2 = input("Please, choose the number of the most frequent adjectives: ")
                    try:
                        tagged = blob_object.tags
                        adjectives = adjective(tagged)
                        common_adjectives = Counter(adjectives).most_common(int(number2))
                        print(f"These are {number2} most frequet adjectives:")
                        print()
                        i = 0
                        for common_adjective in common_adjectives:
                            i += 1
                            pprint.pprint(f"{i} {common_adjective}")
                        print()
                        break
                    except ValueError:
                        print("Sorry, the input is incorrect. Please, enter a number.")
            elif choice == "4":
                while True:
                    number3 = input("Please, choose the number of the most frequent verbs: ")
                    try:
                        tagged = blob_object.tags
                        verbs = verb(tagged)
                        common_verbs = Counter(verbs).most_common(int(number3))
                        print(f"These are {number3} most frequet verbs:")
                        print()
                        i = 0
                        for common_verb in common_verbs:
                            i += 1
                            pprint.pprint(f"{i} {common_verb}")
                        print()
                        break
                    except ValueError:
                        print("Sorry, the input is incorrect. Please, enter a number.")
            elif choice == "5":
                while True:
                    text = open(file)
                    chosen_word = input("Please, enter a word: ")
                    print()
                    if chosen_word.isalpha():
                        number = 0
                        count = 0
                        lines = []
                        my_regex = r"\b" + re.escape(chosen_word) + r"\b"
                        for line in text:
                            count += 1
                            if re.search(my_regex, line, re.IGNORECASE):
                                number +=1
                                lines.append(count)
                                print(line)
                        if number != 0:
                            print(f"The chosen word appeares {number} times in the text collection in lines {lines}")
                            print()
                            break
                        else:
                            print("There is no such a word in the text collection")
                            print()
                            break
                    else:
                        print("Sorry, the input is incorrect. Please, enter a word.")
            elif choice == "6":
                break
            elif choice == "7":
                sys.exit("Thank you for using this program!")
            else:
                ("Sorry, the input is incorrect.")
                print()

def counting(n):
    return len(n)

def original(n):
    return len(set(n))

def noun(n):
    nouns = []
    for lexem in n:
        if (lexem[1] == "NN" and lexem[0] != "i") or lexem[1] == "NNP":
            nouns.append(lexem[0])
        elif lexem[1] == "NNS" or lexem[1] == "NNPS":
            le = Word(lexem[0])
            nouns.append(le.lemmatize())
    return nouns

def adjective(n):
    adjectives = []
    for lexem in n:
        if lexem[1] == "JJ" and lexem[0] != "i":
            adjectives.append(lexem[0])
        elif lexem[1] == "JJR" or lexem[1] == "JJS":
            le = Word(lexem[0])
            adjectives.append(le.lemmatize())
    return adjectives

def verb(n):
    lemmatizer = WordNetLemmatizer()
    verbs = []
    for lexem in n:
        if (lexem[1] == "VB" or lexem[1] == "VBD" or lexem[1] == "VBG" or lexem[1] == "VBN" or lexem[1] == "VBP" or lexem[1] == "VBZ") and lexem[0] not in ["i", "’", "s", "“", "”"]:
            le = lemmatizer.lemmatize(lexem[0], pos="v")
            verbs.append(le)
    return verbs



if __name__ == "__main__":
    main()
