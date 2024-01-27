import os 
location = os.chdir("D:/6610301012Work/BigYukPython/Batch_Rename/Image")
dir_list = os.listdir(location)
counter = 1
print(": WELCOME TO BATCH RENAMING TOOL :")
file_ex = input("please select file extension (.jpg , .png etc) = ")

for file_name in dir_list : 
    new_file_name = "{:03d}.{}".format(counter,file_ex)
    os.rename(file_name , new_file_name)
    counter += 1

# if __name__ == "__main__" :



    