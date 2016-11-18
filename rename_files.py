#
# Rename a bunch of files to find the secret hidden message
#

import os


def rename_files():
	# (1) get filenames from a given folder
	file_list = os.listdir(r"/Users/mimica/Google Drive/CodeDevelopment/Udacity/ud036 Fundamentos da Programacao com Python/prank")
	print(file_list)
	saved_path = os.getcwd();
	os.chdir(r"/Users/mimica/Google Drive/CodeDevelopment/Udacity/ud036 Fundamentos da Programacao com Python/prank")

	# (2) for each file, rename it, removing numbers from the name
	for file_name in file_list:
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

print("Running ...")
rename_files()
print("End.")