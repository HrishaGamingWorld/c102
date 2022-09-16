from os import access
from turtle import width
import dropbox
import cv2
import time
import random
start_time=time.time()
def snap():
    no=random.randint(0,100)
    videocapture=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videocapture.read()
        image_name="img"+str(no)+".png" #str is used to convert any other data type to string.
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("Snapshot Taken!")
    videocapture.release()
    cv2.destroyAllWindows()

def upload_file(imgname):
    access_token = 'sl.BPasE1P7aQu85qkQ5rncU_V8jree3pQ6cLQpm8MEDLyi40GcggMQiV7HSqC6QsX6nxCBXxIMni00PcrjyoeY91QN2EqXHauHmQ2hSwoRzZ3rA_HKFdOKYXYmxVH9snRuyR7hna6GW-Yl'
    file = imgname
    file_from = file
    file_to = "/cv02/"+(imgname)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED TO DROPBOX!")
while(True):
    if ((time.time()-start_time)>=60):
        name=snap()
        upload_file(name)


