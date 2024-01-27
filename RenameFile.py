import os 
def Batch_Rename() :
 location = os.chdir("D:/6610301012Work/BigYukPython/Batch_Rename/Image")
 dir_list = os.listdir(location)
 print(": WELCOME TO BATCH RENAMING TOOL :")
 file_ex = input("please select file extension (.jpg , .png etc) = ")
 i = 1

 for file_name in dir_list : 
   name,ext = os.path.splitext(file_name)
   if ext == file_ex :  
    new_file_name = "{:03d}{}".format(i , ext)
    os.rename(file_name , new_file_name)
    print(new_file_name)
    i += 1

if __name__ == "__main__" :
  Batch_Rename() 



        