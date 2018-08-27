'''
This is a simple python application implimenting a
real world dictionary that takes a word as an input and
displays its relevent information
'''
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
		ans = (input("did you mean %s instead (Y/N)? :" % get_close_matches(word,data.keys(),cutoff=0.8)[0])).lower()
		if ans == 'y':
			return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
		if ans == 'n':
			return "please check your input!"
		else:
			return "invalid!"
	else:
		return "please check your input!"

print(search(input("enter a word:").lower()))
