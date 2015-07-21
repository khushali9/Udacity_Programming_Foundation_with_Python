import webbrowser
class Movie():
	def __init__(self,movie_t,st,pos,trailer):
		self.title=movie_t
		self.storyline=st
		self.poster_image_url=pos
		self.trailer_youtube_url=trailer
	#init for intializing the space n remember its  var n fun
	#__XX__ means XX is reserved work in python
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
