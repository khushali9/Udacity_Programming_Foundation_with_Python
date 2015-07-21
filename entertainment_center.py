import media
import frsh_tomatoes

toy_story=media.Movie("Toy Story","A story of a boy and his toys that come to life","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
bahubali=media.Movie("Baahubali: The Beginning","A dispute between brothers spans across two generations","https://en.wikipedia.org/wiki/Baahubali:_The_Beginning#/media/File:Baahubali_poster.jpg","https://www.youtube.com/watch?v=sOEg_YZQsTI")
dil_dhadakne_do=media.Movie("Dil Dhadakne Do","The film tells the story of a dysfunctional Punjabi family who invite their family and friends on a cruise trip to celebrate the parents' 30th wedding anniversary.","https://en.wikipedia.org/wiki/Dil_Dhadakne_Do#/media/File:First_Look_Poster_of_Dil_Dhadakne_Do.jpg","https://www.youtube.com/watch?v=ipk1-aQaWyw")
#print(toy_story.storyline)
#bahubali.show_trailer()
movies= ["toy_story","bahubali","dil_dhadakne_do"]
fresh_tomatoes.open_movies_page(movies)
