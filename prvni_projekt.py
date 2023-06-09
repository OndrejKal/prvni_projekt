"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Kalvas
email: kalvasondrej@gmail.com
discord: Ondřej K.#0612
"""

'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

usernames = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]
user_password = zip(usernames, passwords)
upper, lower, number, title, sum_of_numbers, graph_for_number = 0, 0, 0, 0, 0, 0

username = input("username:")
password = input("password:")
print("-" * 40)
if username in usernames:
    if dict(user_password).get(username) == password:
        print("Welcome to the app,", username)
        print("We have 3 texts to be analyzed.")
        print("-" * 40)
        text_selection = int(input("Enter a number btw. 1 and 3 to select: "))
        print("-" * 40)
        if text_selection in list(range(len(TEXTS) + 1)):
            text_selection = TEXTS[text_selection - 1]
            print("There are", len(text_selection.split()), "words in the selected text.")
            for words_and_number in text_selection.split():
                if words_and_number.istitle():
                    title += 1
                    continue
                elif words_and_number.isupper():
                    upper += 1
                    continue
                elif words_and_number.islower():
                    lower += 1
                    continue
                elif words_and_number.isdigit():
                    number += 1
                    continue

            print("There are", title, "titlecase words.")
            print("There are", upper, "uppercase words.")
            print("There are", lower, "lowercase words.")
            print("There are", number, "numeric strings.")
            for number_count in text_selection.split():
                if number_count.isdigit():
                    sum_of_numbers += int(number_count)
                    continue
            print("The sum of all the numbers", sum_of_numbers)
            print("-" * 40)

            import re

            text_selection_filter = re.sub("[,.]", "", text_selection)

            dictionary = dict()
            max_len_value = len(max(text_selection_filter.split(), key=len))

            for word in text_selection_filter.split():
                if len(word) not in dictionary:
                    dictionary[len(word)] = []
                dictionary[len(word)].append(word)

            for word_len in sorted(dictionary.keys()):
                graph_for_number = word_len
                words = dictionary[word_len]
                print(str(graph_for_number).rjust(3),
                      "|", len(words) * "*",
                      "|".rjust(max_len_value + 1 - len(words)), len(words))
        else:
            print("wrongly entered value, terminating the program..")
    else:
        print("unregistered user, terminating the program..")
else:
    print("your username is incorrect, terminating the program..")