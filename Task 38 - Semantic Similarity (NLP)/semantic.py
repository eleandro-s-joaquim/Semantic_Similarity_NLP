"""
Compulsory Task 1

    ● Create a file called semantic.py and run all the code extracts above.
    ● Write a note about what you found interesting about the similarities
    between cat, monkey and banana and think of an example of your own.
    ● Run the example file with the simpler language model ‘en_core_web_sm’
    and write a note on what you notice is different from the model
    'en_core_web_md'.
    ● Host your solution on a Git host such as GitLab or GitHub.
        ○ Remember to exclude any venv or virtualenv files from your repo.
    ● Add the link for your remote Git repo to a text file named
    semantic_similarity.txt
"""


import spacy
from tabulate import tabulate

# Loads the medium-sized English language model used for NLP capabilities
nlp = spacy.load("en_core_web_md")

# ------------------------------------------------------------------------------------- #
# Code 1
print("-"*70) # Prints border for UI and user readability purposes
print("CODE 1 - SEMANTIC SIMILARITY BETWEEN \'CAT\', \'MONKEY\' AND \'BANANA\':\n")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Declares data and header lists for the Tabulate table, note use of .similarity()
# function to calculate similarity score
headers = ["Word:", "Word:", "Similarity:"]
data = [[word1, word2, word1.similarity(word2)],
        [word3, word2, word3.similarity(word2)],
        [word3, word1, word3.similarity(word1)]
        ]

# Prints results in user readable table
print(tabulate(data, headers=headers, tablefmt="simple_outline"))

# ------------------------------------------------------------------------------------- #
# Code 2
# This code explores the capability of semantic similarity between multiple words [tokens]
# by employing the use of for loops.
print("-"*70)
print("CODE 2 - WORD SIMILARITY FOR MULTIPLE WORDS:\n")
tokens = nlp('cat monkey banana')

# Declares data and header lists for the Tabulate table
headers = ["Word:", "Word:", "Similarity:"]
data = []

# Loops through the tokens and calculates their similarity score
for token1 in tokens:
    for token2 in tokens:
        data.append([token1.text, token2.text, token1.similarity(token2)])

# Prints results in user readable table
print(tabulate(data, headers=headers, tablefmt="simple_outline"))

# ------------------------------------------------------------------------------------- #
# Code 3
# This code explores the capability of semantic similarity between multiple sentences
# by employing the use of foor loops.
print("\n" + "-"*70)
print("CODE 3 - SENTENCE SIMILARITY:\n")
sentence_to_compare = "Why is my cat on the car"

# Declare a list of sentences
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

# Create comparison sentence token
model_sentence = nlp(sentence_to_compare)

# Declares data and header lists for the Tabulate table
headers = ["Sentence:", "Model Sentence:", "Similarity:"]
data = []

# Loops through the tokens and calculates their similarity score
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    data.append([sentence, model_sentence, similarity])

# Prints results in user readable table
print(tabulate(data, headers=headers, tablefmt="simple_outline"))


"""
NOTE 01:

This code checks the semantic similarity between three words: "cat", "monkey" and "banana".

# "cat" and "monkey" bear similarity as both are members of the animal kingdom and are mammals.
# "banana" and "monkey" monkeys usually eat bananas, imagery of monkeys eating bananas is frequently seen in 
popular culture, further strengthening their association.
# "banana" and "gato" have the lowest similarity score due to the lack of identifiable links.
"""

"""
NOTE 02:
Note on difference between 'en_core_web_sm' vs. 'en_core_web_md':

* "en_core_web_sm" returns significantly lower similarity scores with a variable margin.
* "en_core_web_md" includes all features of "en_core_web_sm" and additional features that enhance your word
vector analysis and similarity capabilities as this model is trained on a much larger dataset.
"""

"""
References Used:

Most code was obtained help in some conversations and doubts via APP DISCORD
from the HyperionDev Software Engineering student group.
#---------------------------------------------------------------------------------#
SE T38 - Semantic Similarity (NLP).pdf
SE T38 - Semantic Similarity (NLP) video
https://youtu.be/IB9m-2x88TI
Author : HyperionDev 2023.
#---------------------------------------------------------------------------------#
Reference: Site W3 Schools Python/
https://www.geeksforgeeks.org/
#---------------------------------------------------------------------------------#
Reference: Real Python
https://realpython.com/natural-language-processing-spacy-python/
#---------------------------------------------------------------------------------#
"""