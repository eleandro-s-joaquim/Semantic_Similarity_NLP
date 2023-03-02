import spacy
nlp = spacy.load("en_core_web_md")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#The similarity is shown as a floating decimal from 0
#to 1, where 0 indicates ‘most dissimilar’ and the strength of the similarity increases
#all the way up to 1.

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print()

#WORKING WITH VECTORS

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    print("-"*30)
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()
#WORKING WITH SENTENCES
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
