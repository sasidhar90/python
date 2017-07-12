import os

def rename_files():
    file_list = os.listdir(r"/Users/sasidharpedapati/Documents/python/prank")
    print(file_list)

    path=os.getcwd()
    os.chdir(r"/Users/sasidharpedapati/Documents/python/prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(path)
rename_files()    

