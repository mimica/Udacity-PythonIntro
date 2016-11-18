#
# Rename a bunch of files to find the secret hidden message
#

import os


def rename_files():
	# (1) get filenames from a given folder
	file_list = os.listdir(r"/Users/mimica/Google Drive/CodeDevelopment/Udacity/ud036 Fundamentos da Programacao com Python/prank")
	print(file_list)
	
	# (2) for each file, rename it, removing numbers from the name

print("Running ...")
rename_files()
print("End.")