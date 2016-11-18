import urllib

def read_text():
	quotes = open(r"/Users/mimica/Google Drive/CodeDevelopment/Udacity/ud036 Fundamentos da Programacao com Python/movie_quotes.txt")
	
	content_quotes = quotes.read()
	print(content_quotes)
	quotes.close()
	check_profanity(content_quotes)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()

read_text()