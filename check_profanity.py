def read_text():
	quotes = open(r"/Users/mimica/Google Drive/CodeDevelopment/Udacity/ud036 Fundamentos da Programacao com Python/movie_quotes.txt")
	curses = open(r"/Users/mimica/Google Drive/CodeDevelopment/Udacity/ud036 Fundamentos da Programacao com Python/curses.txt")
	
	content_quotes = quotes.read()
	print(content_quotes)
	quotes.close()

	content_curses = curses.read()
	print(content_curses)
	curses.close()
	words = content_curses.split( )

	result = False
	for word in words:
		result = word in content_quotes
		break

	print result

read_text()