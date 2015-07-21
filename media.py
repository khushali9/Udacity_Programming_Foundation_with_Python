import webbrowser
class Movie():
	def __init__(self,movie_title,movie_storyline,poster_image_url,trailer_youtube_url):
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image_url
		self.trailer_youtube_url=trailer_youtube_url
	#init for intializing the space n remember its  var n fun
	#__XX__ means XX is reserved work in python
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
