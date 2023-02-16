# imports
import spacy

# loading language model
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana ')

#loop to calculate similarities
l, r = 0, 0
for token in tokens:
    while r <= len(tokens) - 1:
        print(tokens[l].text, tokens[r].text, tokens[l].similarity(tokens[r]))
        r += 1
    if r > len(tokens) - 1:
        r = 0
        l += 1
print('\n\n')
# The items which belongs to the same group has got high similarity ex apple - banana
# On the other hand items from the differnt grups has got low similarity

# My example:
# with more complex language model
nlp = spacy.load('en_core_web_md')
tokens =nlp('bear wolf meat human vegetables')
l, r = 0, 0
print('More complex: ')
for token in tokens:
    while r <= len(tokens) - 1:
        print(tokens[l].text, tokens[r].text, tokens[l].similarity(tokens[r]))
        r += 1
    if r > len(tokens) - 1:
        r = 0
        l += 1
print('\n')

# Bear and wolf has got quite significant similarity because their are animals, bear and wolf 
# has got bigger similarity with meat than similarity with vegeatbles because both of those anilmals
# are considered carnivores.

# with less complex language model
nlp = spacy.load('en_core_web_sm')
tokens =nlp('bear wolf meat human vegetables')
l, r = 0, 0
print('Simpler: ')
for token in tokens:
    while r <= len(tokens) - 1:
        print(tokens[l].text, tokens[r].text, tokens[l].similarity(tokens[r]))
        r += 1
    if r > len(tokens) - 1:
        r = 0
        l += 1
print('\n')

# After using the simple language model warning message was printed out, 
# and the similarity results and the result were significantly different from those obtained using a more complex model.

"""ModelsWarning: [W007] The model you're using has no word vectors loaded, so the result of the Token. \
    similarity method will be based on the tagger, parser, and NER, which may not give useful similarity judgments. \
    This may happen if you're using one of the small models, \
    e.g. en_core_web_sm, which don't ship with word vectors and only use context-sensitive tensors.\
      You can always add your own word vectors, or use one of the larger models instead if available"""