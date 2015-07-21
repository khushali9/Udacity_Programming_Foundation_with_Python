# -*- coding: utf-8 -*-
import urllib
def read_text():
	quotes=open("/Users/khushali/Coding/Udacity_Programming_Foundation_with_Python/movie_quotes.txt")
	content=quotes.read()
	print(content)
	quotes.close()
	check_profanity(content)

def check_profanity(word):
	con=urllib.urlopen("http://www.wdyl.com/profanity?q="+word)
	out=con.read()
	#print(out)
	con.close()
	if "true" in out:
		print("you shoul check the file")
	elif "false" in out:
		print("well done")
	else:
		print("could not scan the document")
read_text()