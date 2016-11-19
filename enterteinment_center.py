import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", 
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.title)

avatar = media.Movie("Avatar", 
					 "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.", 
					 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg", 
					 "https://youtu.be/cRdxXPV9GNQ?t=1m53s")
#print(avatar.title)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
						 	 "Using rock music to learn",
						 	 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg",
						 	 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
						  "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
						  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
						  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
							    "While on a trip to Paris with his fiancee's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
							    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
							    "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
						  "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
						  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
						  "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)