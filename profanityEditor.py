def read_text():
	quotes=open("/Users/khushali/Coding/Udacity_Programming_Foundation_with_Python/movie_quotes.txt")
	content=quotes.read()
	print(content)
	quotes.close()
read_text()