import time
import webbrowser

count = 0

print("This program started on "+time.ctime())
while (count < 3):
	# Wait for 2 hours
	time.sleep(10)

	# Open the browser
	webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
	print("   opening the video at "+time.ctime())

	count = count + 1

print("Bye bye. See you ...")