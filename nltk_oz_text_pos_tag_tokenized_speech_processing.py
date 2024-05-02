import nltk
from nltk import pos_tag
from word_tokenized_oz import word_tokenized_oz

# save and print the sentence stored at index 100 in word_tokenized_oz
witches_fate = word_tokenized_oz[100]
print(witches_fate)

# create a list to hold part-of-speech tagged sentences
pos_tagged_oz = list()
# create a for loop through each word tokenized
for word in word_tokenized_oz:
  pos_tagged_oz.append(pos_tag(word))
print(pos_tagged_oz)

# store and print the 101st part-of-speech tagged sentence
witches_fate_pos = pos_tagged_oz[100]
print(witches_fate_pos)
