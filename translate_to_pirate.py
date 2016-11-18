import urllib

def translate_to_pirate():
	#content = "How are you doing today my lovely gentleman?"
	content = "your bastard"

	connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+content)
	output = connection.read()
	connection.close()
	print(output)

translate_to_pirate()