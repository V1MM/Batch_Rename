import os 
def Batch_Rename() :
 curret_dir = os.getcwd() #หา directory ปัจจจุบัน
 image = os.path.join(curret_dir, "Image") # ไปยังโฟลเดอร์ ภาพ 
 
 location = os.chdir(image) # เปลี่ยนเป็นตำแหน่ง Image ปัจจุบัน
 dir_list = os.listdir(location) # แสดงข้อมูลภาพใน Image หรือ location ของ Folder Image

 print(": WELCOME TO BATCH RENAMING TOOL :") # หน้าจอแสดงผล ยินดีต้อนรับ
 file_ex = input("please select file extension (.jpg , .png etc) = ") # กำหนดประเภทไฟล์ ที่ต้องการเปลี่ยนชื่อ
 i = 1 # กำหนด I เท่ากับ 1 

 for file_name in dir_list : # ตัวแปร File_name วิ่งเช็คภายในโฟลเดอร์ ว่ามีไฟล์อะไรอยู่บ้าง
   name,ext = os.path.splitext(file_name) # แยก ชื่อและตัว extension ของไฟล์ทั้งหมด
   if ext == file_ex :  # ไฟล์ extension ในโฟลเดอร์ เท่ากับ ค่า extnsion ที่ user ป้อนมา หรือไม่ ?
    new_file_name = "{:03d}{}".format(i , ext) # ชื่อไฟล์ใหม่ เป็นเลข 000 3 digit แทนชื่อ ตามด้วย ประเภทไฟล์ 
    os.rename(file_name , new_file_name) # เปลี่ยนชื่อใหม่
    print("Old File Name >>", name,ext , "New File Name >>" , new_file_name) # พิมพ์ค่าชื่อใหม่่ออกมา
    i += 1 # i   + 1 

if __name__ == "__main__" :
  Batch_Rename() 



        