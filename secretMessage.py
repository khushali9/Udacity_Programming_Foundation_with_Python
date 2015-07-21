import os
#get file names from a folder
#os.getcwd() gets current working dir
#loop through each files but first change dir
def rename_file():
    file_list = os.listdir(r"/Users/khushali/Coding/Udacity_Programming_Foundation_with_Python/prank")
    saved_path = os.getcwd()
    os.chdir(r"/Users/khushali/Coding/Udacity_Programming_Foundation_with_Python/prank")
	
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))#old,new
        #file_name.translate(None,"012334")(table which translates one char to another set of char,list of char to remove)
    os.chdir(saved_path)
             
rename_file()

#python -m tabnanny secretMessage.py
#for indentation error




	