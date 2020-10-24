from difflib import get_close_matches
from difflib import SequenceMatcher
import enchant

word = "rainny"
possibility_list = ["rainny1","rainny2","rainny3","rainnny4"]


# get_close_matches : Default value of n  and cutoff is 3 and 0.6.  
# To get the list of closest matches from the input list of words and the user defined search word , it internally
# uses SequenceMatcher

# Suppose if n = 2, cutoff = 0.6 , our list length is huge and out first 2 entries crosses 0.6 then they will be taken as output 
# but the list processing still continues and if we find the entries in the list whiose matching ratio exceeds our result then they 
# become our output.

output = get_close_matches(word,possibility_list)
print(output)


# Sequence matcher : Used to know the closeness of two words.
# To know how close each word in list is to the user defined word. 
for item in possibility_list:
	print(SequenceMatcher(None, word, item).ratio())


# ************ The above 2 modules compares the similarity between the given words or given list of words  

# There is another module names pyenchant which shows the suggestions for a input typo error word from the
# availbale language dictionaries. It is available only for 32 bit version of python 


# Refer https://www.geeksforgeeks.org/get-similar-words-suggestion-using-enchant-in-python/




