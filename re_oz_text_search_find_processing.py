import re

# import L. Frank Baum's The Wonderful Wizard of Oz
oz_text = open("the_wizard_of_oz_text.txt",encoding='utf-8').read().lower()

# search oz_text for an occurrence of 'wizard'
found_wizard = re.search("wizard",oz_text)

# find all the occurrences of 'lion' in oz_text
all_lions = re.findall("lion", oz_text)
print(all_lions)

# store and print the length of all_lions
number_lions = len(all_lions)
print(number_lions)
